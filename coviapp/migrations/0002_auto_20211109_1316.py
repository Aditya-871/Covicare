# Generated by Django 3.2.9 on 2021-11-09 07:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('coviapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bed',
            name='hospital_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='coviapp.hospital', unique=True),
        ),
        migrations.AlterField(
            model_name='oxygen',
            name='hospital_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='coviapp.hospital', unique=True),
        ),
        migrations.AlterField(
            model_name='vaccine',
            name='hospital_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='coviapp.hospital', unique=True),
        ),
    ]
