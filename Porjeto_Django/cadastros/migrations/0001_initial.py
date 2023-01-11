# Generated by Django 4.1.4 on 2023-01-11 18:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Laboratorio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('descricao', models.TextField(max_length=200, verbose_name='Descrição')),
                ('tipo', models.CharField(choices=[('INFORMATICA', 'Informática'), ('APICULTURA', 'Apicultura'), ('QUIMICA', 'Quimica'), ('ALIMENTOS', 'Alimentos')], max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='Reserva',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('capacidade', models.IntegerField()),
                ('bloco', models.IntegerField()),
                ('descricao', models.TextField(max_length=100, verbose_name='Descrição')),
                ('data', models.DateField(blank='False', null='False')),
                ('horario', models.CharField(choices=[('07:00 - 07:45', '07:00 - 07:45'), ('07:45 - 08:30', '07:45 - 08:30'), ('08:50 - 09:35', '08:50 - 09:35'), ('09:35 - 10:20', '09:35 - 10:20'), ('10:30 - 11:15', '10:30 - 11:15'), ('11:15 - 12:00', '11:15 - 12:00'), ('13:00 - 13:45', '13:00 - 13:45'), ('13:45 - 14:30', '13:45 - 14:30'), ('14:50 - 15:35', '14:50 - 15:35'), ('15:35 - 16:20', '15:35 - 16:20'), ('16:30 - 17:15', '16:30 - 17:15'), ('17:15 - 18:00', '17:15 - 18:00'), ('19:00 - 19:45', '19:00 - 19:45'), ('19:45 - 20:30', '19:45 - 20:30'), ('20:40 - 21:25', '20:40 - 21:25'), ('21:25 - 22:10', '21:25 - 22:10')], max_length=15)),
                ('salas', models.CharField(choices=[('56 - LABORATÓRIO DE INFORMÁTICA I', '56 - LABORATÓRIO DE INFORMÁTICA I'), ('57 - LABORATÓRIO DE INFORMÁTICA II', '57 - LABORATÓRIO DE INFORMÁTICA II'), ('58 - LABORATÓRIO DE INFORMÁTICA III', '57 - LABORATÓRIO DE INFORMÁTICA III')], max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Sala',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=30)),
                ('numero', models.IntegerField(verbose_name='Número')),
                ('bloco', models.CharField(max_length=10, verbose_name='Bloco')),
                ('descricao', models.TextField(max_length=100, verbose_name='Descrição')),
                ('capacidade', models.IntegerField(verbose_name='Capacidade')),
                ('laboratorio', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, to='cadastros.laboratorio')),
            ],
        ),
    ]
