# Generated by Django 4.1.4 on 2023-01-16 18:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadastros', '0002_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='sala',
            name='laboratorio',
            field=models.BooleanField(default=False, verbose_name='É laboratório?'),
        ),
    ]
