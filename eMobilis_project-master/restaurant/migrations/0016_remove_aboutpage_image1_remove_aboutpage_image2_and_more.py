# Generated by Django 4.2.7 on 2023-11-29 08:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0015_desserts_dinner_drinks_lunch_winecard'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='aboutpage',
            name='image1',
        ),
        migrations.RemoveField(
            model_name='aboutpage',
            name='image2',
        ),
        migrations.RemoveField(
            model_name='aboutpage',
            name='image3',
        ),
        migrations.RemoveField(
            model_name='desserts',
            name='image10',
        ),
        migrations.RemoveField(
            model_name='desserts',
            name='image11',
        ),
        migrations.RemoveField(
            model_name='desserts',
            name='image12',
        ),
        migrations.RemoveField(
            model_name='dinner',
            name='image7',
        ),
        migrations.RemoveField(
            model_name='dinner',
            name='image8',
        ),
        migrations.RemoveField(
            model_name='dinner',
            name='image9',
        ),
        migrations.RemoveField(
            model_name='drinks',
            name='image19',
        ),
        migrations.RemoveField(
            model_name='drinks',
            name='image20',
        ),
        migrations.RemoveField(
            model_name='drinks',
            name='image21',
        ),
        migrations.RemoveField(
            model_name='lunch',
            name='image4',
        ),
        migrations.RemoveField(
            model_name='lunch',
            name='image5',
        ),
        migrations.RemoveField(
            model_name='lunch',
            name='image6',
        ),
        migrations.RemoveField(
            model_name='menu',
            name='image1',
        ),
        migrations.RemoveField(
            model_name='menu',
            name='image2',
        ),
        migrations.RemoveField(
            model_name='menu',
            name='image3',
        ),
        migrations.RemoveField(
            model_name='stories',
            name='image1',
        ),
        migrations.RemoveField(
            model_name='stories',
            name='image2',
        ),
        migrations.RemoveField(
            model_name='stories',
            name='image3',
        ),
        migrations.RemoveField(
            model_name='stories',
            name='image4',
        ),
        migrations.RemoveField(
            model_name='stories',
            name='image5',
        ),
        migrations.RemoveField(
            model_name='winecard',
            name='image16',
        ),
        migrations.RemoveField(
            model_name='winecard',
            name='image17',
        ),
        migrations.RemoveField(
            model_name='winecard',
            name='image18',
        ),
    ]
