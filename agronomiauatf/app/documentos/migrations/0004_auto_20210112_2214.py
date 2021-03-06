# Generated by Django 3.0.3 on 2021-01-13 02:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('documentos', '0003_documento'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='documento',
            options={'ordering': ('-id',), 'verbose_name': 'Documento', 'verbose_name_plural': 'Documentos'},
        ),
        migrations.AddField(
            model_name='documento',
            name='Privado',
            field=models.BooleanField(default=False, help_text='Documento privado', verbose_name='Privado'),
        ),
        migrations.AddField(
            model_name='documento',
            name='público',
            field=models.BooleanField(default=False, help_text='Documento Público', verbose_name='Público'),
        ),
    ]
