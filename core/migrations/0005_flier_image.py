# Generated by Django 4.1.1 on 2022-10-18 11:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_alter_flier_hashtag1_alter_flier_hashtag2_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='flier',
            name='image',
            field=models.ImageField(default='r.jpg', upload_to='dp_fliers'),
        ),
    ]
