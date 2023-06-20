from django.db import models

# Create your models here.
# class referenceM(models.Model):
#     author = models.CharField(max_length=255)
#     title = models.CharField(max_length=255)
#     volume = models.CharField(max_length=255)
#     Doi = models.CharField(max_length=255)
#     date = models.CharField(max_length=255)
#     page = models.CharField(max_length=255)

#     def __str__(self):
#         return self.title
    
class titleM(models.Model):
    title = models.CharField(max_length=255)
    Doi = models.CharField(max_length=255)
    
    def __str__(self):
        return self.title
    

