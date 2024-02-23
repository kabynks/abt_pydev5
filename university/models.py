from django.db import models

class University(models.Model):
    name = models.CharField('Name of the university',max_length=256)
    address = models.TextField('Address of the university')
    phone_number = models.CharField('Phone number', max_length=13)
    image = models.ImageField('Image of the university',upload_to='university-images')
    def __str__(self):
        return f"{self.name}"
    class Meta:
        verbose_name = "University"
        verbose_name_plural = "Universities"