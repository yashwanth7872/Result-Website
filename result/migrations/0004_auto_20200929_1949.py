# Generated by Django 3.0.8 on 2020-09-29 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('result', '0003_marks_sub_code'),
    ]

    operations = [
        migrations.AddField(
            model_name='marks',
            name='sem',
            field=models.IntegerField(default='1'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='marks',
            name='internal',
            field=models.IntegerField(null=True),
        ),
    ]
