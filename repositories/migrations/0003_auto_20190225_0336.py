# Generated by Django 2.1.7 on 2019-02-25 03:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('repositories', '0002_auto_20190219_0204'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commit',
            name='message',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='repository',
            name='description',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
