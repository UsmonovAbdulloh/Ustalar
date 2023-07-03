# Generated by Django 4.2.2 on 2023-07-03 04:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClientModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client_name', models.CharField(default='', max_length=50)),
                ('client_phonenumber', models.CharField(default='', max_length=15)),
                ('client_location', models.CharField(default='', max_length=100)),
            ],
            options={
                'db_table': 'client',
            },
        ),
        migrations.RemoveField(
            model_name='ordermodel',
            name='client_location',
        ),
        migrations.RemoveField(
            model_name='ordermodel',
            name='client_name',
        ),
        migrations.RemoveField(
            model_name='ordermodel',
            name='client_phonenumber',
        ),
        migrations.RemoveField(
            model_name='ustamodel',
            name='price',
        ),
        migrations.AddField(
            model_name='ordermodel',
            name='price',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='ordermodel',
            name='order',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='order.clientmodel'),
        ),
    ]