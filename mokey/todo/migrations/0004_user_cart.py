# Generated by Django 4.2.16 on 2024-11-13 00:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0003_product_data'),
    ]

    operations = [
        migrations.CreateModel(
            name='user_cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(max_length=150)),
                ('product_id', models.CharField(max_length=150)),
                ('quantity', models.CharField(max_length=150)),
            ],
        ),
    ]