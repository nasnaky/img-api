# Generated by Django 4.0.3 on 2022-05-30 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='imgs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('imges', models.ImageField(upload_to='', verbose_name='img/')),
            ],
        ),
    ]
