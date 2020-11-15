from django.db import models

# Create your models here.
# 产品名字和评论
class Shampoo(models.Model):
    # id 自动创建
    date = models.DateField()
    product_name = models.CharField(max_length=255)
    product_comment = models.CharField(max_length=1024)
    sentiment = models.DecimalField(max_digits=8, decimal_places=5)