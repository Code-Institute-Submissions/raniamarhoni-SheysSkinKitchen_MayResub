# Generated by Django 3.1.8 on 2021-05-04 18:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='star',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]