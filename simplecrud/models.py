from django.db import models

class Crudsimple(models.Model):
    id = models.IntegerField()
    id = models.AutoField(primary_key=True)
    nama = models.CharField(max_length=50)
    nim = models.IntegerField()
    fakultas = models.CharField(max_length=50)
    jurusan = models.CharField(max_length=50)

    class Meta:
        db_table = "simplecrud"


