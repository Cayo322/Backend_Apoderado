# Generated by Django 4.1.7 on 2023-06-25 22:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apoderado', '0003_tblalumno_tblapoderado_tblcolegio_tblgrado_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='TblAlumno',
        ),
        migrations.DeleteModel(
            name='TblColegio',
        ),
        migrations.DeleteModel(
            name='TblGrado',
        ),
        migrations.DeleteModel(
            name='TblMovilidad',
        ),
        migrations.DeleteModel(
            name='TblVehiculo',
        ),
    ]
