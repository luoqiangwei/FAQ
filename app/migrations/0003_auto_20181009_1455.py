# Generated by Django 2.1.2 on 2018-10-09 06:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20181009_1429'),
    ]

    operations = [
        migrations.AlterField(
            model_name='puzzleinfo',
            name='ptitle',
            field=models.CharField(max_length=1000),
        ),
    ]
