# Generated by Django 5.0.2 on 2024-02-15 19:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0006_alter_course_course_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='course_code',
            field=models.CharField(max_length=7),
        ),
    ]
