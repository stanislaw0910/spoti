# Generated by Django 3.1.7 on 2022-05-15 19:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_auto_20220515_2245'),
    ]

    operations = [
        migrations.AlterField(
            model_name='albums',
            name='album_art',
            field=models.ImageField(blank=True, null=True, upload_to='None/<django.db.models.fields.CharField>'),
        ),
        migrations.AlterField(
            model_name='songs',
            name='file',
            field=models.FileField(upload_to=''),
        ),
    ]