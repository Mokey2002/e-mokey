# Generated by Django 4.2.16 on 2024-10-22 20:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='user_data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(max_length=150)),
                ('email', models.CharField(max_length=500)),
                ('name', models.CharField(max_length=150)),
                ('lname', models.CharField(max_length=150)),
                ('address', models.CharField(max_length=150)),
            ],
        ),
    ]
