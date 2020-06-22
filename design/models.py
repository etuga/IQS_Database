from django.db import models

AUTHOR=[('ENDIKA', 'Endika')]
TAGS=[('DOCKING', 'Docking'), ('MD', 'Molecular Dynamics')]

class script(models.Model):
    author_name=models.CharField(max_length=10, choices=AUTHOR, default='name')
    description=models.CharField(max_length=200)
    tag=models.CharField(max_length=100, choices=TAGS, default='tag')
    code=models.TextField(max_length=None, default='Script Code Goes Here')
    

# Create your models here.
