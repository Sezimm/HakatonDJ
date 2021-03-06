# Generated by Django 3.1.7 on 2021-04-03 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='hospital',
            old_name='title',
            new_name='name',
        ),
        migrations.AlterField(
            model_name='hospital',
            name='region',
            field=models.CharField(choices=[('O', 'OSH'), ('T', 'TALAS'), ('C', 'CHUI'), ('B', 'BATKEN'), ('I', 'ISSYK-KUL'), ('N', 'NARYN'), ('J', 'JALAL-ABAD')], max_length=100),
        ),
        migrations.AlterField(
            model_name='hospital',
            name='slug',
            field=models.SlugField(max_length=100, unique=True, verbose_name='ОКПО'),
        ),
    ]
