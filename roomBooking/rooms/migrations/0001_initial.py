# Generated by Django 4.0.10 on 2023-06-22 06:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('roomName', models.CharField(max_length=50)),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
