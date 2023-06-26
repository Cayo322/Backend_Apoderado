from django.db import models
#para la tabla parentesco
class TblParentesco(models.Model):
    parentesco_id = models.AutoField(primary_key=True)
    parentesco_nombre = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'tbl_parentesco'
        
    def __str__(self):
        return self.parentesco_nombre
    
#para la tabla apoderado
class TblApoderado(models.Model):
    apoderado_id = models.AutoField(primary_key=True)
    apoderado_nombre = models.CharField(max_length=255)
    apoderado_apellido = models.CharField(max_length=255)
    apoderado_telefono = models.CharField(max_length=255)
    apoderado_documento_identidad = models.CharField(max_length=20, blank=True, null=True)
    parentesco = models.ForeignKey('TblParentesco', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'tbl_apoderado'

    def __str__(self):
        return self.apoderado_nombre
    