# Generated by Django 3.1.7 on 2021-04-26 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_remove_songs_cover'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='songs',
            options={'verbose_name': 'Song', 'verbose_name_plural': 'Songs'},
        ),
        migrations.AddField(
            model_name='songs',
            name='cover',
            field=models.TextField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='songs',
            name='path',
            field=models.TextField(max_length=255),
        ),
    ]