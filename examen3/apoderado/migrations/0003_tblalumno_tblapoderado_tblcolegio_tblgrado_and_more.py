# Generated by Django 4.1.7 on 2023-06-25 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apoderado', '0002_remove_apoderado_parentesco_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='TblAlumno',
            fields=[
                ('alumno_id', models.AutoField(primary_key=True, serialize=False)),
                ('alumno_nombre', models.CharField(max_length=255)),
                ('alumno_apellido', models.CharField(max_length=255)),
                ('alumno_fecha_nacimiento', models.DateField(blank=True, null=True)),
                ('alumno_foto', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'db_table': 'tbl_alumno',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TblApoderado',
            fields=[
                ('apoderado_id', models.AutoField(primary_key=True, serialize=False)),
                ('apoderado_nombre', models.CharField(max_length=255)),
                ('apoderado_apellido', models.CharField(max_length=255)),
                ('apoderado_telefono', models.CharField(max_length=255)),
                ('apoderado_documento_identidad', models.CharField(blank=True, max_length=20, null=True)),
            ],
            options={
                'db_table': 'tbl_apoderado',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TblColegio',
            fields=[
                ('colegio_id', models.AutoField(primary_key=True, serialize=False)),
                ('colegio_nombre', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'tbl_colegio',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TblGrado',
            fields=[
                ('grado_id', models.AutoField(primary_key=True, serialize=False)),
                ('grado_nombre', models.CharField(max_length=50)),
                ('grado_nivel', models.CharField(blank=True, max_length=45, null=True)),
            ],
            options={
                'db_table': 'tbl_grado',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TblMovilidad',
            fields=[
                ('movilidad_id', models.AutoField(primary_key=True, serialize=False)),
                ('movilidad_tipo_servicio', models.CharField(max_length=45)),
                ('movilidad_turno', models.CharField(max_length=45)),
                ('movilidad_seccion', models.CharField(max_length=45)),
                ('movilidad_docente', models.CharField(max_length=255)),
                ('movilidad_pago', models.FloatField()),
            ],
            options={
                'db_table': 'tbl_movilidad',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TblParentesco',
            fields=[
                ('parentesco_id', models.AutoField(primary_key=True, serialize=False)),
                ('parentesco_nombre', models.CharField(max_length=45)),
            ],
            options={
                'db_table': 'tbl_parentesco',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TblVehiculo',
            fields=[
                ('vehiculo_id', models.AutoField(primary_key=True, serialize=False)),
                ('vehiculo_placa', models.CharField(max_length=20)),
                ('vehiculo_conductor', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'db_table': 'tbl_vehiculo',
                'managed': False,
            },
        ),
        migrations.DeleteModel(
            name='Apoderado',
        ),
    ]
