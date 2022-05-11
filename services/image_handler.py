import os
from pprint import pprint

import ffmpeg

from pathlib import Path
from PIL import Image as PIL_Image
from io import BytesIO
from django.core.files import File

from pics.models import Image


def handle(image: Image) -> None:
    data = ffmpeg.probe(image.file.path)
    pprint(data)
    if "height" in data["streams"][0]:
        image.height = data["streams"][0]["height"]
    if "width" in data["streams"][0]:
        image.width = data["streams"][0]["width"]
    if "codec_long_name" in data["streams"][0]:
        image.codec = data["streams"][0]["codec_long_name"]
    if "display_aspect_ratio" in data["streams"][0]:
        image.ratio = data["streams"][0]["display_aspect_ratio"]
    img = PIL_Image.open(image.file.path)
    image.orig_format = img.format
    image.orig_mode = img.mode
    size = Path(image.file.path).stat().st_size
    re_size = 100
    if size > 524288:
        re_size = 100 * (0.5 / round(size / 1024 / 1024))

    blob = BytesIO()
    img.save(blob, "WEBP", quality=re_size)

    path = image.file.path.split(".")[0]
    image.image.save(f"uploads/images/cropped/{path.split('/')[-1]}.webp", File(blob), save=False)
    image.save()
