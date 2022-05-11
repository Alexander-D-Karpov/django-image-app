from django.urls import path

from pics.views import upload, list_groups, group, image

urlpatterns = [
    path("", list_groups, name="image_groups"),
    path("group/<str:slug>", group, name="image_group"),
    path("image/<str:slug>", image, name="image"),
    path("upload/", upload, name="image_upload")
]
