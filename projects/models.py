from django.db import models


# Create your models here.

class Status(models.TextChoices):
    UNSTARTED = 'u', "Not started yet"
    ONGOING = 'o', "Ongoing"
    FINISHED = 'f', "Finished"

class Course(models.TextChoices):
    UNSTARTED = 'a', "Course A"
    ONGOING = 'b', "Course B"
    FINISHED = 'c', "Course C"


class Project(models.Model):
    name = models.CharField(verbose_name="Enter your name", max_length=65, unique=True)
    status = models.CharField(verbose_name="Project status", max_length=1, choices=Status.choices)
    course = models.CharField(verbose_name="Course name", max_length=1, choices=Course.choices)
    timePreferences = models.CharField(verbose_name="I'd like to finish by", max_length=65)

    def __str__(self):
        return self.name
