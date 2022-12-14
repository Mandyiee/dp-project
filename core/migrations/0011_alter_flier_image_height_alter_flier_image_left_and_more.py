# Generated by Django 4.1.1 on 2022-10-25 09:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_flier_htmlfile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flier',
            name='image_height',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='flier',
            name='image_left',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='flier',
            name='image_top',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='flier',
            name='image_width',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.CreateModel(
            name='UserFlier',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=100)),
                ('image', models.ImageField(default='r.jpg', upload_to='user_fliers')),
                ('flier', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='userfliers', to='core.flier')),
            ],
        ),
    ]
