# Generated by Django 3.0.5 on 2020-04-04 18:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_book_added_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='added_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
