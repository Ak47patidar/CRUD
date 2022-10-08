from django.db import models


class ImageModel(models.Model):
    id=models.CharField(max_length=10,primary_key=True)
    Profile_pic=models.ImageField(upload_to='images')  

    def __str__(self):
        return self.Name
    