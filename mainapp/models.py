from django.db import models

# Create your models here.


class Category(models.Model):
    categoryID = models.AutoField(primary_key=True,null=False , db_column='categoryID')
    categoryName = models.CharField(max_length=100,null=False,db_column='categoryName',unique=True)
    categoryDiscription = models.CharField(max_length=200,null=False , db_column='categoryDiscription')

    def __str__(self):
        return f'Category : id - {self.categoryID}, categoryname - {self.categoryName}, discription - {self.categoryDiscription}'


class SubCategory(models.Model):
    subcategoryID = models.AutoField(primary_key=True,null=False , db_column='subcategoryID')
    subCategoryName = models.CharField(max_length=100,null=False,db_column='subCategoryName')
    categoryID = models.ForeignKey(Category,null=False , db_column='categoryID',on_delete=models.CASCADE)
    
    def __str__(self):
        return f'Sub Category : id - {self.subcategoryID}, subcategoryname - {self.subCategoryName},category -  {self.categoryID}'