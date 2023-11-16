from django.db import models

# Create your models here.
class Person(models.Model):
    p_id = models.AutoField(primary_key=True)
    p_firstname = models.CharField(max_length=50,null=True)
    p_lastname = models.CharField(max_length=50,null=True)
    p_workyear = models.DateField(null=True)
    p_contract = models.DateField(null=True)
    p_email = models.CharField(max_length=100,null=True)
    p_facebook = models.TextField(null=True)
    p_line = models.TextField(null=True)
    p_telephone = models.IntegerField(null=True)
    p_picture = models.ImageField(upload_to='proflie_pictures/',null=True)

    def __str__(self):
        return f'{self.p_firstname} {self.p_lastname}'