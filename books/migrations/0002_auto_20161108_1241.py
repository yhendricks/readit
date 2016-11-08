# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(help_text=b'Use pen name, not real name', unique=True, max_length=70)),
            ],
        ),
        migrations.AlterField(
            model_name='book',
            name='author',
            field=models.CharField(help_text=b'Use pen name, not real name', max_length=70),
        ),
        migrations.AlterField(
            model_name='book',
            name='is_favourite',
            field=models.BooleanField(default=False, verbose_name=b'Favourite'),
        ),
    ]
