# Generated by Django 4.1 on 2022-09-16 07:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0008_seller_details_c_email_user_details_c_email_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_details',
            name='email',
            field=models.CharField(max_length=35),
        ),
    ]