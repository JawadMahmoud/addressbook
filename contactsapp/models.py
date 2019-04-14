from django.db import models
from django.template.defaultfilters import slugify

# Create your models here.


class Organization(models.Model):
    name = models.CharField(max_length=128, unique=True, null=False)
    email = models.CharField(max_length=128, unique=True)
    address = models.CharField(max_length=128, null=True)
    city = models.CharField(max_length=128, null=True)
    country = models.CharField(max_length=128, null=True)
    logo = models.ImageField(upload_to='org_logos/', blank=True)
    slug = models.SlugField(blank=True, unique=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Organization, self).save(*args, **kwargs)


class Contact(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=128, unique=True, null=False)
    address = models.CharField(max_length=128, null=True)
    city = models.CharField(max_length=64, null=True)
    country = models.CharField(max_length=64, null=True)
    phone = models.CharField(max_length=16, null=True)
    email = models.CharField(max_length=128, unique=True, null=True)
    role = models.CharField(max_length=64, null=True)
    company = models.ForeignKey(Organization, on_delete=models.SET_NULL, null=True)
    picture = models.ImageField(upload_to='con_dps/', blank=True)

    def __str__(self):
        return self.name