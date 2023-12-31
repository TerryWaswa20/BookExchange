# Generated by Django 4.2.6 on 2023-11-24 23:42

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ThienryBooks', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('phone_number', models.CharField(max_length=10)),
                ('your_book', models.CharField(max_length=50)),
                ('book_needed', models.CharField(max_length=50)),
                ('upload_book', models.ImageField(blank=True, null=True, upload_to='images/')),
            ],
        ),
        migrations.CreateModel(
            name='Login',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=10)),
                ('password', models.CharField(max_length=16)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_number', models.CharField(default='', max_length=10)),
                ('datetime', models.DateField(default=datetime.datetime.today)),
                ('status', models.BooleanField(default=False)),
                ('address', models.CharField(default='', max_length=100)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ThienryBooks.client')),
            ],
        ),
        migrations.DeleteModel(
            name='Parent',
        ),
        migrations.AddField(
            model_name='hiring',
            name='description',
            field=models.CharField(blank=True, default='', max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='hiring',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=6),
        ),
    ]
