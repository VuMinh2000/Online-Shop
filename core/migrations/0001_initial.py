# Generated by Django 4.0.6 on 2022-08-12 06:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=200)),
                ('email', models.EmailField(max_length=200)),
                ('phone', models.CharField(default='', max_length=200)),
                ('message', models.TextField()),
                ('create_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
