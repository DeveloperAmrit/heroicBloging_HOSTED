# Generated by Django 4.0 on 2022-09-05 22:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('heroicBlog', '0003_alter_blog_bottomimage_alter_blog_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='bottomimage',
            field=models.ImageField(default='imgBOTTOM', upload_to=''),
        ),
        migrations.AlterField(
            model_name='blog',
            name='image',
            field=models.ImageField(default='imgTOP', upload_to=''),
        ),
        migrations.AlterField(
            model_name='blog',
            name='middleimage',
            field=models.ImageField(default='imgMIDDLE', upload_to=''),
        ),
    ]