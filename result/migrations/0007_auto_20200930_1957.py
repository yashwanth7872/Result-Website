# Generated by Django 3.0.8 on 2020-09-30 14:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('result', '0006_auto_20200930_1138'),
    ]

    operations = [
        migrations.AlterField(
            model_name='marks',
            name='sub_code',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='result.subject'),
        ),
        migrations.AlterField(
            model_name='marks',
            name='theory',
            field=models.IntegerField(blank=True),
        ),
    ]
