from django.db import models

AUTHOR=[('Endika', 'Endika'),('Rai','Rai')]
PROJECT=[('PanTCK','PanTCK'), ('ZAP','ZAP')]

class structure(models.Model):
    code=models.CharField(max_length=200)
    smiles=models.CharField(max_length=200)
    author_name=models.CharField(max_length=10, choices=AUTHOR, default='name')
    project_name=models.CharField(max_length=10,choices=PROJECT, default='project')
    def __str__(self):
        return self.code


# Create your models here.
