# Generated by Django 3.0.8 on 2021-01-01 17:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_coment'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='coment',
            options={'ordering': ['-created_at'], 'verbose_name': 'Comentario', 'verbose_name_plural': 'Comentarios'},
        ),
    ]