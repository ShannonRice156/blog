# Generated by Django 4.2 on 2023-04-30 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blogs", "0004_alter_blog_featured_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="blog",
            name="featured_image",
            field=models.ImageField(default="default.png", upload_to=""),
        ),
    ]
