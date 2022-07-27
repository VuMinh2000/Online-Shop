# Generated by Django 4.0.6 on 2022-07-27 01:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=75)),
                ('metaTitle', models.CharField(default='', max_length=100)),
                ('slug', models.CharField(default='', max_length=100)),
                ('content', models.TextField(default='')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=75)),
                ('mataTitle', models.CharField(default='', max_length=100)),
                ('slug', models.CharField(default='', max_length=100)),
                ('summary', models.TextField(default='')),
                ('Type', models.IntegerField(max_length=6)),
                ('sku', models.CharField(default='', max_length=100)),
                ('content', models.TextField(default='')),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=75)),
                ('metaTitle', models.CharField(default='', max_length=100)),
                ('slug', models.CharField(default='', max_length=100)),
                ('content', models.TextField(default='')),
            ],
        ),
        migrations.CreateModel(
            name='product_tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.product')),
                ('tag', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.tag')),
            ],
        ),
        migrations.CreateModel(
            name='product_review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=100)),
                ('rating', models.IntegerField(max_length=6)),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
                ('publishedAt', models.DateTimeField(auto_now=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.product')),
            ],
        ),
        migrations.CreateModel(
            name='product_meta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.CharField(default='', max_length=50)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.product')),
            ],
        ),
        migrations.CreateModel(
            name='product_category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.category')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.product')),
            ],
        ),
    ]