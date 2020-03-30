# Generated by Django 3.0.3 on 2020-03-30 19:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Automovel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(blank=True, max_length=128, null=True, verbose_name='Nome')),
            ],
            options={
                'verbose_name': 'Automóvel',
                'verbose_name_plural': 'Automóveis',
            },
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(blank=True, max_length=128, null=True, verbose_name='Nome')),
                ('email', models.EmailField(blank=True, max_length=254, null=True, verbose_name='E-mail')),
            ],
            options={
                'verbose_name': 'Usuario',
                'verbose_name_plural': 'Usuarios',
            },
        ),
        migrations.CreateModel(
            name='Solicitar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateField(blank=True, null=True)),
                ('horario', models.TimeField(blank=True, null=True)),
                ('origem', models.CharField(blank=True, max_length=128, null=True, verbose_name='Origem')),
                ('destino', models.CharField(blank=True, max_length=128, null=True, verbose_name='Destino')),
                ('Solicitante', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_solicitacoes.Usuario')),
            ],
            options={
                'verbose_name': 'Solicitar Automóvel',
                'verbose_name_plural': 'Solicitar Automóveis',
            },
        ),
        migrations.CreateModel(
            name='Motorista',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_solicitacoes.Usuario')),
            ],
            options={
                'verbose_name': 'Motorista',
                'verbose_name_plural': 'Motoristas',
            },
        ),
        migrations.CreateModel(
            name='Departamento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(blank=True, max_length=128, null=True, verbose_name='Nome')),
                ('responsavel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_solicitacoes.Usuario')),
            ],
            options={
                'verbose_name': 'Departamento',
                'verbose_name_plural': 'Departamentos',
            },
        ),
        migrations.CreateModel(
            name='AtenderSolicitacao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Motorista', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_solicitacoes.Motorista')),
                ('Solicitante', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_solicitacoes.Solicitar')),
                ('automovel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_solicitacoes.Automovel')),
            ],
            options={
                'verbose_name': 'Atender Solicitação',
                'verbose_name_plural': 'Atender Solicitações',
            },
        ),
    ]