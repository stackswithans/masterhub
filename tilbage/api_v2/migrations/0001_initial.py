# Generated by Django 3.2.3 on 2021-07-07 23:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='KnowledgeCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='MasterhubUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('U', 'UNKNOWN')], default='U', max_length=100)),
                ('telephone', models.CharField(max_length=100, unique=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Timeslot',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.IntegerField(choices=[(0, 'Mon'), (1, 'Tues'), (2, 'Wed'), (3, 'Thur'), (4, 'Fri'), (5, 'Sat'), (6, 'Sun')])),
                ('time', models.IntegerField(choices=[(6, '6:00'), (7, '7:00'), (8, '8:00'), (9, '9:00'), (10, '10:00'), (11, '11:00'), (12, '12:00'), (13, '13:00'), (14, '14:00'), (15, '15:00'), (16, '16:00'), (17, '17:00'), (18, '18:00')])),
            ],
        ),
        migrations.CreateModel(
            name='Master',
            fields=[
                ('masterhubuser_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='api_v2.masterhubuser')),
                ('occupation', models.CharField(max_length=100)),
                ('academic_degree', models.IntegerField(choices=[(0, 'Licenciatura'), (1, 'Mestrado'), (2, 'Doutoramento'), (3, 'Nenhum')], default=3)),
                ('activated', models.BooleanField(default=False)),
                ('k_categories', models.ManyToManyField(to='api_v2.KnowledgeCategory')),
                ('timeslots', models.ManyToManyField(to='api_v2.Timeslot')),
            ],
            bases=('api_v2.masterhubuser',),
        ),
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('timeslot', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api_v2.timeslot')),
                ('users', models.ManyToManyField(related_name='lesson_users', to='api_v2.MasterhubUser')),
                ('master', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lesson_owner', to='api_v2.master')),
            ],
            options={
                'unique_together': {('title', 'master')},
            },
        ),
    ]
