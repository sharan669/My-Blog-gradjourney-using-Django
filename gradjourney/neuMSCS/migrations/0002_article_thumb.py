# Generated by Django 2.2.4 on 2019-08-31 01:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('neuMSCS', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='thumb',
            field=models.ImageField(blank=True, default='default.png', upload_to=''),
        ),
    ]
