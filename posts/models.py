from django.db import models

# Create your models here.
# 创建模型
class Article(models.Model):
    title = models.CharField(max_length=20)
    content = models.TextField()