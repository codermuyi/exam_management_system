# Generated by Django 5.0.2 on 2024-02-15 19:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0005_remove_examvenue_no_of_seats_examroom_no_of_seats'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='course_code',
            field=models.CharField(max_length=20),
        ),
    ]