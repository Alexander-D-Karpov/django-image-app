# Generated by Django 4.0.2 on 2022-05-11 10:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pics', '0012_alter_imageingroup_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='imageingroup',
            options={'ordering': ('-image__uploaded',)},
        ),
    ]
