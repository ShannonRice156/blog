# Generated by Django 4.2 on 2023-04-30 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blogs", "0002_blog_content"),
    ]

    operations = [
        migrations.AlterField(
            model_name="blog",
            name="featured_image",
            field=models.ImageField(blank=True, default="default.jpg", upload_to=""),
        ),
    ]