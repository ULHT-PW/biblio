# Generated by Django 4.0.6 on 2024-04-15 00:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('biblioteca', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='livro',
            name='autor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='livros', to='biblioteca.autor'),
        ),
    ]
