# Generated by Django 3.2.16 on 2023-02-20 07:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Izdelie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('age', models.IntegerField(max_length=50)),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='polls.group')),
            ],
        ),
        migrations.CreateModel(
            name='Detal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('opisanie', models.TextField(max_length=100)),
                ('kolichestvo', models.IntegerField(max_length=50)),
                ('tcena', models.IntegerField(max_length=50)),
                ('proizvoditel', models.TextField(max_length=50)),
                ('izdelie', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='polls.izdelie')),
            ],
        ),
    ]