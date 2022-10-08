from django.db import models

class AtulModel(models.Model):
    id=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=5)

    def __str__(self):
        return self.name
    






