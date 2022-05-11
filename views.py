from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
from pics.forms import UploadFileForm
from pics.models import Image, Group, ImageInGroup
from pics.services.image_handler import handle


def upload(request):
    message = ""
    if request.POST:
        form = UploadFileForm(request.POST, request.FILES)
        group = get_object_or_404(Group, slug=request.POST["group"])
        if form.is_valid():
            for f in request.FILES.getlist("images"):
                img = Image.objects.create(file=f, creator=request.user)
                ImageInGroup.objects.create(group=group, image=img)
                handle(img)
        else:
            message = form.errors
    return redirect("image_group", slug=group.slug)


def list_groups(request):
    return render(request, "pics/index.html", context={"groups": Group.objects.all()})


def group(request, slug):
    group = get_object_or_404(Group, slug=slug)
    return render(request, "pics/image_list.html", context={"group": group})


def image(request, slug):
    image = get_object_or_404(Image, slug=slug)
    return render(request, "pics/image.html", context={"image": image})
