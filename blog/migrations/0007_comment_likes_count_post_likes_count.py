# Generated by Django 5.0 on 2023-12-04 14:48

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("blog", "0006_post_comments_count_post_views_count"),
    ]

    operations = [
        migrations.AddField(
            model_name="comment",
            name="likes_count",
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name="post",
            name="likes_count",
            field=models.IntegerField(default=0),
        ),
    ]
