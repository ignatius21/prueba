# Generated by Django 4.0.1 on 2022-01-23 23:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AppEntrega', '0005_alter_libros_autor_alter_libros_genero'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Nosotros',
            new_name='Usuarios',
        ),
    ]
