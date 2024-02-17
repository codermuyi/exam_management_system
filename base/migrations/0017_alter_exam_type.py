# Generated by Django 5.0.2 on 2024-02-17 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0016_exam_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exam',
            name='type',
            field=models.CharField(choices=[('paper', 'Paper Exam'), ('cbt', 'CBT Exam')], default='paper', max_length=20),
        ),
    ]