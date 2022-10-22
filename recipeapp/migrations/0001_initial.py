# Generated by Django 4.0.5 on 2022-09-23 05:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.IntegerField(default='0', primary_key=True, serialize=False)),
                ('title', models.CharField(default='title', max_length=200)),
                ('items', models.CharField(default='ingredient', max_length=200)),
                ('recipe_category', models.CharField(default='recipe', max_length=200)),
                ('image', models.CharField(default='image', max_length=400)),
            ],
        ),
    ]