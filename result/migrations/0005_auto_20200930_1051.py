# Generated by Django 3.0.8 on 2020-09-30 05:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('result', '0004_auto_20200929_1949'),
    ]

    operations = [
        migrations.AlterField(
            model_name='marks',
            name='internal',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='marks',
            name='theory',
            field=models.IntegerField(null=True),
        ),
    ]
