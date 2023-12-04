# Generated by Django 4.2.7 on 2023-11-30 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0037_happy_image_alter_happy_text1_alter_happy_text2_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Testimony',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text1', models.TextField(default='text1', max_length=500)),
                ('text2', models.TextField(default='text2', max_length=500)),
                ('text3', models.TextField(default='text3', max_length=500)),
                ('image', models.ImageField(default='testimony.jpg', upload_to='testimony')),
            ],
        ),
    ]