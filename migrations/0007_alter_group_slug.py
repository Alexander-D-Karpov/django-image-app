# Generated by Django 4.0.2 on 2022-05-11 08:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pics', '0006_alter_group_name_alter_group_slug_alter_image_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='slug',
            field=models.CharField(blank=True, default='wtmVNMaP', max_length=50),
        ),
    ]