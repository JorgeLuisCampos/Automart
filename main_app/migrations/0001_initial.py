# Generated by Django 2.2.5 on 2019-09-28 00:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Auto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('precio', models.DecimalField(decimal_places=2, max_digits=10)),
                ('color', models.CharField(max_length=100)),
                ('modelo', models.DecimalField(decimal_places=0, max_digits=4)),
                ('img_url', models.TextField()),
            ],
        ),
    ]
