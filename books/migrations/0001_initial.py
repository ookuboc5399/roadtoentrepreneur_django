# Generated by Django 3.1.13 on 2021-09-12 16:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='タイトル')),
                ('image', models.ImageField(upload_to='images', verbose_name='イメージ画像')),
                ('content', models.TextField(verbose_name='本文')),
            ],
        ),
    ]
