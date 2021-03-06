# Generated by Django 3.0.6 on 2020-09-12 14:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20200912_1709'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Category'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='tag',
            field=models.ManyToManyField(to='blog.Tag'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='text',
            field=models.TextField(max_length=5000, verbose_name='text'),
        ),
        migrations.AlterField(
            model_name='category',
            name='title',
            field=models.CharField(max_length=50, verbose_name='title'),
        ),
        migrations.AlterField(
            model_name='tag',
            name='title',
            field=models.CharField(max_length=50, verbose_name='title'),
        ),
    ]
