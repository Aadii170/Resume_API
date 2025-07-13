from django.db import models

# Create your models here.
class Resume(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    dob= models.DateField(auto_now=False, auto_now_add=False)
    profile= models.ImageField(upload_to='profiles/', null=True, blank=True)
    resume_file = models.FileField(upload_to='resumes/')
   

    def __str__(self):
        return self.name