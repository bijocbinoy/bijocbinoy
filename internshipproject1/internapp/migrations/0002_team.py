# Generated by Django 3.2.16 on 2022-11-13 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('internapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('namE', models.CharField(max_length=200)),
                ('imge', models.ImageField(upload_to='pic')),
                ('descp', models.TextField()),
            ],
        ),
    ]