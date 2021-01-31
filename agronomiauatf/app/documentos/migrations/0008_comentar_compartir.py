# Generated by Django 3.0.3 on 2021-01-23 00:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('documentos', '0007_auto_20210120_1524'),
    ]

    operations = [
        migrations.CreateModel(
            name='Compartir',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Asunto', models.CharField(max_length=150, verbose_name='Asunto')),
                ('Descripcion', models.TextField(help_text='Describa de que trata el documento', max_length=200)),
                ('Fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('Fecha_mod', models.DateTimeField(auto_now=True)),
                ('Correo_origen', models.EmailField(max_length=200, verbose_name='Origen')),
                ('Correo_Destino', models.EmailField(max_length=200, verbose_name='Origen')),
                ('estado', models.BooleanField(default=True)),
                ('Usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('documento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='documentos.Documento')),
            ],
            options={
                'verbose_name': 'Compartir',
                'verbose_name_plural': 'Compartirs',
            },
        ),
        migrations.CreateModel(
            name='Comentar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Descripcion', models.TextField(help_text='Describa de que trata el documento', max_length=200)),
                ('Fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('Fecha_mod', models.DateTimeField(auto_now=True)),
                ('estado', models.BooleanField(default=True)),
                ('Usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('documento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='documentos.Documento')),
            ],
            options={
                'verbose_name': 'Comentar',
                'verbose_name_plural': 'Comentars',
            },
        ),
    ]