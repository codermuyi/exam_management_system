# Generated by Django 5.0.2 on 2024-02-15 19:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='examvenue',
            name='code',
            field=models.CharField(max_length=20, null=True),
        ),
    ]