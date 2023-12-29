from django.db import models

# Create your models here.

JOB_TYPE = [
    ("FT","Full Time"),
    ("PT","Part Time")
]

class Category(models.Model):
    name = models.CharField(max_length=25)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name

class Job(models.Model): 
    title = models.CharField(max_length=100)
    job_type = models.CharField(max_length=30, choices=JOB_TYPE)
    description = models.TextField(max_length=500)
    responsibilites = models.TextField(max_length=500)
    qualifications = models.TextField(max_length=500)
    benefits = models.TextField(max_length=500)
    published_at = models.DateTimeField(auto_now=True)
    Vacancy = models.IntegerField(default=1)
    salary = models.IntegerField(default=0)
    experience = models.IntegerField(default=1)
    job_category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
