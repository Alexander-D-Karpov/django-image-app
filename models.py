from django.db import models

# Create your models here.
from django.urls import reverse
from django.utils.text import slugify

from common.generator import gen_slug
from user.models import Person


class Image(models.Model):
    file = models.ImageField(upload_to="uploads/images/")
    slug = models.SlugField(blank=True, null=True, max_length=10)
    orig_format = models.CharField(max_length=20, blank=True)
    orig_mode = models.CharField(max_length=20, blank=True)
    codec = models.CharField(max_length=20, blank=True)
    ratio = models.CharField(max_length=10, blank=True)
    image = models.ImageField(upload_to="images/", blank=True)
    uploaded = models.DateTimeField(auto_now_add=True)
    hash = models.CharField(max_length=32, blank=True)
    height = models.IntegerField(blank=True, null=True)
    width = models.IntegerField(blank=True, null=True)
    creator = models.ForeignKey(Person, null=True, blank=True, on_delete=models.SET_NULL, related_name="creator")

    def __str__(self):
        return self.file.name

    def get_absolute_url(self):
        return reverse("image", kwargs={"slug": self.slug})

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        slug = gen_slug(8)
        while Image.objects.filter(slug=slug).exists():
            slug = gen_slug(8)
        self.slug = slug
        super(Image, self).save()

    def get_group(self):
        el = ImageInGroup.objects.filter(image=self)
        if el.exists():
            group = el[0].group
            if not group.private:
                return group
        return False

    class Meta:
        ordering = ("uploaded",)


class Group(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.CharField(blank=True, null=True, max_length=50)
    creator = models.ForeignKey(Person, blank=True, null=True, on_delete=models.SET_NULL)
    private = models.BooleanField(default=True)

    def get_images(self):
        return [x.image for x in ImageInGroup.objects.filter(group=self)]

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        if self.private:
            slug = gen_slug(8)
            while Group.objects.filter(slug=slug).exists():
                slug = gen_slug(8)
            self.slug = slug
        else:
            self.slug = slugify(self.name)
        super(Group, self).save()

    def get_absolute_url(self):
        return reverse("image_group", kwargs={"slug": self.slug})

    def __str__(self):
        return self.name


class ImageInGroup(models.Model):
    image = models.ForeignKey(Image, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)

    class Meta:
        ordering = ("-image__uploaded",)
