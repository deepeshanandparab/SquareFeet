# Generated by Django 2.2.4 on 2019-09-19 15:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0004_auto_20190919_2036'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
