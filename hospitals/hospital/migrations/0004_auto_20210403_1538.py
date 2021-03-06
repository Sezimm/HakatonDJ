# Generated by Django 3.1.7 on 2021-04-03 15:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0003_hospital_person'),
    ]

    operations = [
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('napravlenie', models.CharField(choices=[('ter', 'Terapeft'), ('hit', 'Hirurg')], default='Terapeft', max_length=100)),
                ('full_name', models.CharField(max_length=255)),
                ('pin_id', models.IntegerField()),
                ('age', models.IntegerField()),
                ('staj', models.IntegerField()),
                ('phone', models.IntegerField()),
                ('work', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hospital.hospital')),
            ],
        ),
        migrations.CreateModel(
            name='GL_Doctor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=255)),
                ('pin_id', models.IntegerField()),
                ('age', models.IntegerField()),
                ('staj', models.IntegerField()),
                ('phone', models.IntegerField()),
                ('work', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hospital.hospital')),
            ],
        ),
        migrations.CreateModel(
            name='Nurse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=255)),
                ('pin_id', models.IntegerField()),
                ('age', models.IntegerField()),
                ('phone', models.IntegerField()),
                ('work', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hospital.hospital')),
                ('work_doc', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='hospital.doctor')),
                ('work_gl', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hospital.gl_doctor')),
            ],
        ),
        migrations.CreateModel(
            name='Pacient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=255)),
                ('pin_id', models.IntegerField()),
                ('age', models.IntegerField()),
                ('phone', models.IntegerField()),
                ('story', models.CharField(max_length=255)),
                ('doc', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hospital.doctor')),
                ('hos', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hospital.hospital')),
                ('nur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hospital.nurse')),
            ],
        ),
        migrations.AddField(
            model_name='doctor',
            name='work_gl',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hospital.gl_doctor'),
        ),
    ]
