# Generated by Django 4.2.3 on 2024-05-15 20:29

import account.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserCourse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('nom', models.CharField(blank=True, max_length=50)),
                ('prenom', models.CharField(blank=True, max_length=50)),
                ('phone', models.CharField(max_length=15, unique=True)),
                ('nni', models.CharField(max_length=15, unique=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('address', models.CharField(max_length=200)),
                ('image', models.ImageField(blank=True, null=True, upload_to=account.models.image_upload_profile_agent)),
                ('number_attempt', models.IntegerField(default=0)),
                ('is_blocked', models.BooleanField(default=False)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('role', models.CharField(choices=[('Admin', 'Admin'), ('Etudiante', 'Etudiante'), ('Enseignant', 'Enseignant')], default='Admin', max_length=30, null=True)),
                ('transaction_authorization', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Matiere',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titre', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Enseignant',
            fields=[
                ('usercourse_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('niveau_educatif', models.CharField(choices=[('Fondemental', 'Fondemental'), ('Breve', 'Breve')], default='Fondemental', max_length=30, null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('account.usercourse',),
        ),
        migrations.CreateModel(
            name='Bacalorea',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('niveau', models.CharField(choices=[('C', 'C'), ('D', 'D'), ('A', 'A'), ('O', 'O')], default='C', max_length=30, null=True)),
                ('matieres', models.ManyToManyField(to='account.matiere')),
            ],
        ),
        migrations.CreateModel(
            name='Etudiante',
            fields=[
                ('usercourse_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('niveau_etude', models.CharField(choices=[('Fondemental', 'Fondemental'), ('Breve', 'Breve')], default='Fondemental', max_length=30, null=True)),
                ('bac', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='account.bacalorea')),
            ],
            options={
                'abstract': False,
            },
            bases=('account.usercourse',),
        ),
        migrations.CreateModel(
            name='Cour',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titre', models.CharField(max_length=100, null=True)),
                ('date_commence_cour', models.DateTimeField()),
                ('date_fin_cour', models.DateTimeField()),
                ('prof', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='account.enseignant')),
            ],
        ),
    ]
