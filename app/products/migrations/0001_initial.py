# Generated by Django 3.2.5 on 2021-07-03 19:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProductModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_product', models.CharField(blank=True, max_length=255, null=True, verbose_name='Name Product')),
                ('plataform', models.CharField(max_length=255, verbose_name='Plataform')),
                ('price', models.FloatField(blank=True, default=0, null=True, verbose_name='Price')),
                ('restaurant', models.CharField(blank=True, max_length=255, null=True, verbose_name='Restaurant')),
                ('category', models.CharField(blank=True, max_length=255, null=True, verbose_name='Category')),
            ],
        ),
    ]