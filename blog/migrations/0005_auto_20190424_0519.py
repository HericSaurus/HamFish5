# Generated by Django 2.2 on 2019-04-24 05:19

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20190423_0153'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='feature_img',
            field=ckeditor_uploader.fields.RichTextUploadingField(),
        ),
    ]
