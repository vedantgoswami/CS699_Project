# Generated by Django 4.2.5 on 2023-10-07 10:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('description', '0004_item_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='item',
            old_name='image',
            new_name='image1',
        ),
        migrations.AddField(
            model_name='item',
            name='image2',
            field=models.TextField(default='NULL'),
            preserve_default=False,
        ),
    ]
