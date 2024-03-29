# Generated by Django 4.1.5 on 2023-01-11 12:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("experiences", "0003_remove_perk_category_experience_category"),
        ("rooms", "0004_room_category"),
        ("medias", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="photo",
            name="experience",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="experiences.experience",
            ),
        ),
        migrations.AlterField(
            model_name="photo",
            name="room",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="rooms.room",
            ),
        ),
        migrations.AlterField(
            model_name="video",
            name="file",
            field=models.FileField(upload_to=""),
        ),
    ]
