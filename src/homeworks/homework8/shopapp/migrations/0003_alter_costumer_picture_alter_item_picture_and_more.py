# Generated by Django 4.1.7 on 2023-02-24 20:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopapp', '0002_alter_item_picture_alter_storeowner_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='costumer',
            name='picture',
            field=models.ImageField(default='', upload_to='uploads'),
        ),
        migrations.AlterField(
            model_name='item',
            name='picture',
            field=models.ImageField(default='', upload_to='uploads'),
        ),
        migrations.AlterField(
            model_name='itemcategory',
            name='picture',
            field=models.ImageField(default='', upload_to='uploads'),
        ),
        migrations.AlterField(
            model_name='storecategory',
            name='picture',
            field=models.ImageField(default='', upload_to='uploads'),
        ),
        migrations.AlterField(
            model_name='storeowner',
            name='picture',
            field=models.ImageField(default='', upload_to='uploads'),
        ),
    ]