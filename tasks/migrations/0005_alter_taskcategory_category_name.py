# Generated by Django 3.2 on 2021-05-08 07:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0004_taskcategory_created_by'),
    ]

    operations = [
        migrations.AlterField(
            model_name='taskcategory',
            name='category_name',
            field=models.CharField(max_length=50),
        ),
    ]
