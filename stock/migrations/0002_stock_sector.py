# Generated by Django 3.2.9 on 2022-06-23 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='stock',
            name='sector',
            field=models.CharField(max_length=50, null=True, verbose_name='業種'),
        ),
    ]
