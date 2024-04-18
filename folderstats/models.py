from django.db import models

# Create your models here.
class Folder(models.Model):
    name = models.CharField(max_length=200)
    
    def __str__(self) -> str:
        return self.name

class File(models.Model):
    folder = models.ForeignKey(Folder, on_delete=models.DO_NOTHING)
    filename = models.CharField(max_length=200)
    size = models.IntegerField(default=0)

    def __str__(self) -> str:
        return f'{self.folder} - {self.filename}'


class Line(models.Model):
    rawline = models.TextField()
    processed = models.BooleanField()
    
    def __str__(self) -> str:
        return self.rawline[:10]