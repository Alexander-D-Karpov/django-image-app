# Generated by Django 4.0.2 on 2022-04-19 07:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pics', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='height',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='image',
            name='width',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]