# Generated by Django 4.0.4 on 2022-06-02 00:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Login', '0001_initial'),
        ('Integrante', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='archivo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.FileField(blank=True, null=True, upload_to='archivos/')),
                ('tarea', models.CharField(max_length=60)),
                ('tipo', models.CharField(max_length=60)),
                ('estado', models.BooleanField(default=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now_add=True)),
                ('autor', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='Integrante.integrante')),
                ('equipo', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='Login.equipo')),
            ],
            options={
                'verbose_name': 'archivos',
                'verbose_name_plural': 'archivo',
            },
        ),
    ]
