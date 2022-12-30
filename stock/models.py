from django.db import models

class Stock(models.Model):
    name = models.CharField('企業名', max_length=50)
    sector = models.CharField('業種', max_length=50,null=True)
    country = models.CharField('国', max_length=50,null=True)
    image = models.ImageField(upload_to='images',verbose_name='企業ロゴ')
    content = models.TextField('本文')
    blog_url = models.URLField('関連記事',max_length=200,null=True)
    buffet_code = models.URLField('バフェットコード',max_length=200,null=True)

    def __str__(self):
        return self.name
