from django.db import models

class Books(models.Model):
    title = models.CharField('タイトル', max_length=50)
    image = models.ImageField(upload_to='images', verbose_name='イメージ画像')
    subimage = models.ImageField(upload_to='images', verbose_name='コンテンツ画像')
    content = models.TextField('本文')

    def __str__(self):
        return self.title