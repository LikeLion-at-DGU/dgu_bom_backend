# Generated by Django 4.2.1 on 2023-05-18 06:45

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("booth", "0007_alter_comment_password_alter_commentreply_password_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="comment",
            name="password",
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name="commentreply",
            name="password",
            field=models.CharField(max_length=10),
        ),
    ]