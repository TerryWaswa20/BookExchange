# Generated by Django 4.2.6 on 2023-11-22 21:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Hiring',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('official_name', models.CharField(max_length=100)),
                ('contact', models.CharField(max_length=10)),
                ('location', models.CharField(max_length=80)),
                ('book_image', models.ImageField(blank=True, null=True, upload_to='images/')),
            ],
        ),
        migrations.CreateModel(
            name='Parent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=60)),
                ('last_name', models.CharField(max_length=60)),
                ('email', models.EmailField(max_length=80)),
                ('username', models.CharField(max_length=10)),
                ('password', models.CharField(max_length=16)),
                ('confirm_password', models.CharField(max_length=16)),
            ],
        ),
        migrations.CreateModel(
            name='Purchase',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('official_name', models.CharField(max_length=100)),
                ('contact', models.CharField(max_length=14)),
                ('location', models.CharField(max_length=80)),
            ],
        ),
    ]
