# Generated by Django 5.0.2 on 2024-02-15 19:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_examvenue_code'),
    ]

    operations = [
        migrations.AddField(
            model_name='examvenue',
            name='room_no',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
