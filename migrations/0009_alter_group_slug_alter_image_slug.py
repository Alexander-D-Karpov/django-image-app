# Generated by Django 4.0.2 on 2022-05-11 08:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pics', '0008_alter_group_slug_alter_image_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='slug',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='image',
            name='slug',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]
