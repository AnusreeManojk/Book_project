# Generated by Django 5.1.3 on 2024-12-01 05:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book_PP', '0002_book_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='quantity',
            field=models.IntegerField(default=1234),
            preserve_default=False,
        ),
    ]
