# Generated by Django 4.0.4 on 2022-09-04 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Games',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=1111111)),
                ('imageB', models.ImageField(upload_to='pics')),
                ('imageA', models.ImageField(upload_to='pics')),
                ('image1', models.ImageField(upload_to='pics')),
                ('image2', models.ImageField(upload_to='pics')),
                ('image3', models.ImageField(upload_to='pics')),
                ('image4', models.ImageField(upload_to='pics')),
                ('image5', models.ImageField(upload_to='pics')),
                ('image6', models.ImageField(upload_to='pics')),
                ('price', models.IntegerField()),
                ('desc', models.TextField(max_length=100000)),
                ('typea', models.CharField(max_length=111111111)),
                ('action', models.BooleanField(default=False)),
                ('adventure', models.BooleanField(default=False)),
                ('roleplay', models.BooleanField(default=False)),
                ('Simulation', models.BooleanField(default=False)),
                ('Sports', models.BooleanField(default=False)),
                ('Strategy', models.BooleanField(default=False)),
                ('free', models.BooleanField(default=False)),
                ('top', models.BooleanField(default=False)),
                ('logo', models.ImageField(upload_to='pics')),
            ],
            options={
                'verbose_name_plural': 'games',
            },
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=1111)),
                ('image1', models.ImageField(upload_to='pics')),
                ('image2', models.ImageField(upload_to='pics')),
                ('desc', models.TextField(max_length=100000)),
            ],
            options={
                'verbose_name_plural': 'news',
            },
        ),
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=111)),
                ('email', models.CharField(max_length=111)),
                ('message', models.TextField(max_length=11111)),
                ('phone', models.IntegerField()),
                ('games', models.CharField(max_length=111)),
                ('price', models.IntegerField()),
            ],
            options={
                'verbose_name_plural': 'orders',
            },
        ),
        migrations.CreateModel(
            name='Tranding',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image1', models.ImageField(upload_to='pics')),
                ('image2', models.ImageField(upload_to='pics')),
                ('image3', models.ImageField(upload_to='pics')),
                ('image4', models.ImageField(upload_to='pics')),
                ('image5', models.ImageField(upload_to='pics')),
                ('name1', models.CharField(max_length=1111)),
                ('name2', models.CharField(max_length=1111)),
                ('name3', models.CharField(max_length=1111)),
                ('name4', models.CharField(max_length=1111)),
                ('name5', models.CharField(max_length=1111)),
            ],
            options={
                'verbose_name_plural': 'tranding',
            },
        ),
    ]
