# Generated by Django 2.2.6 on 2019-10-26 06:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('campesinos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Oferta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_entrega', models.CharField(max_length=200)),
                ('ubicacion_entrega', models.CharField(max_length=200)),
                ('estado', models.CharField(max_length=20)),
                ('campesino', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='campesinos.Campesino')),
            ],
        ),
    ]