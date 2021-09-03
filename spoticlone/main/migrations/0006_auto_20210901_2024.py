# Generated by Django 3.1.7 on 2021-09-01 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20210426_1034'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='songs',
            name='cover',
        ),
        migrations.AddField(
            model_name='songs',
            name='duration',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='songs',
            name='path',
            field=models.FilePathField(),
        ),
        migrations.AlterField(
            model_name='songs',
            name='track_num',
            field=models.IntegerField(default=0),
        ),
    ]
