from django.db import models

# Create your models here.


class Category(models.Model):
    categoryID = models.AutoField(primary_key=True,null=False , db_column='categoryID')
    categoryName = models.CharField(max_length=100,null=False,db_column='categoryName',unique=True)
    categoryDiscription = models.CharField(max_length=200,null=False , db_column='categoryDiscription')
    