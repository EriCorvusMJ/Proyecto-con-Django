# Generated by Django 5.1.7 on 2025-06-10 18:26

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0004_bitacora_user_profile_estatus_profile_user_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50, verbose_name='Nombre de la tarea')),
                ('descripcion', models.CharField(max_length=100, verbose_name='Descripción')),
                ('estatus', models.BooleanField(default=False, verbose_name='¿Terminada?')),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tasks', to='dashboard.profile')),
            ],
            options={
                'db_table': 'tasks',
            },
        ),
    ]
