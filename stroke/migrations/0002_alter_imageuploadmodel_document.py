# Generated by Django 3.2.4 on 2021-08-09 09:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stroke', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imageuploadmodel',
            name='document',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
