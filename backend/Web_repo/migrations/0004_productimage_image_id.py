# Generated by Django 5.1.6 on 2025-03-29 22:46

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Web_repo', '0003_images_remove_productimage_image_url_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='productimage',
            name='image_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='Image', to='Web_repo.images'),
        ),
    ]
