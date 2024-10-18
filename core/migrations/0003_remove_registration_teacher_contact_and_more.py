# Generated by Django 4.1.7 on 2024-10-18 08:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0002_remove_registration_details_json_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="registration",
            name="teacher_contact",
        ),
        migrations.AddField(
            model_name="registration",
            name="teacher_email",
            field=models.EmailField(
                default="", max_length=100, verbose_name="Teacher Email"
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="registration",
            name="teacher_mobile",
            field=models.CharField(
                default="", max_length=10, verbose_name="Teacher Mobile"
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="registration",
            name="teacher_name",
            field=models.CharField(
                default="", max_length=100, verbose_name="Teacher Name"
            ),
            preserve_default=False,
        ),
    ]