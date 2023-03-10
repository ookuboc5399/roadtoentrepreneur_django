# Generated by Django 3.2.9 on 2022-06-23 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0002_stock_sector'),
    ]

    operations = [
        migrations.AddField(
            model_name='stock',
            name='blog_url',
            field=models.URLField(null=True, verbose_name='関連記事'),
        ),
        migrations.AddField(
            model_name='stock',
            name='buffet_code',
            field=models.URLField(null=True, verbose_name='バフェットコード'),
        ),
    ]
