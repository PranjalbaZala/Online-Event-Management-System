# Generated by Django 4.0 on 2022-02-25 08:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BeEventful', '0007_booking'),
    ]

    operations = [
        migrations.AddField(
            model_name='feedbackdetails',
            name='Status',
            field=models.CharField(default='pending', max_length=10),
        ),
    ]
