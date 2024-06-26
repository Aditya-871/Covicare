# Generated by Django 3.2.9 on 2021-11-10 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coviapp', '0002_auto_20211109_1316'),
    ]

    operations = [
        migrations.RenameField(
            model_name='hospital',
            old_name='city',
            new_name='Address',
        ),
        migrations.RenameField(
            model_name='oxygen',
            old_name='hospital_id',
            new_name='hospital',
        ),
        migrations.RenameField(
            model_name='vaccine',
            old_name='hospital_id',
            new_name='hospital',
        ),
        migrations.RemoveField(
            model_name='vaccine',
            name='amount',
        ),
        migrations.RemoveField(
            model_name='vaccine',
            name='cost',
        ),
        migrations.AddField(
            model_name='vaccine',
            name='amount_dose_1',
            field=models.IntegerField(help_text='available amount of Dose 1', null=True),
        ),
        migrations.AddField(
            model_name='vaccine',
            name='amount_dose_2',
            field=models.IntegerField(help_text='available amount of Dose 2', null=True),
        ),
        migrations.AddField(
            model_name='vaccine',
            name='cost_dose_1',
            field=models.IntegerField(help_text='cost of dose 1 per dose', null=True),
        ),
        migrations.AddField(
            model_name='vaccine',
            name='cost_dose_2',
            field=models.IntegerField(help_text='cost of dose 2 per dose', null=True),
        ),
        migrations.AddField(
            model_name='vaccine',
            name='vaccine_name',
            field=models.CharField(help_text='name of vaccine', max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='hospital',
            name='hospital_id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='hospital',
            name='pincode',
            field=models.CharField(help_text='6-digits pincode of city', max_length=10),
        ),
        migrations.AlterField(
            model_name='oxygen',
            name='cost',
            field=models.IntegerField(help_text='cost per cylinder'),
        ),
    ]
