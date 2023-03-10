# Generated by Django 4.1.4 on 2022-12-19 12:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SubCategory',
            fields=[
                ('subcategoryID', models.AutoField(db_column='subcategoryID', primary_key=True, serialize=False)),
                ('subCategoryName', models.CharField(db_column='subCategoryName', max_length=100, unique=True)),
                ('categoryID', models.ForeignKey(db_column='categoryID', on_delete=django.db.models.deletion.CASCADE, to='mainapp.category')),
            ],
        ),
    ]
