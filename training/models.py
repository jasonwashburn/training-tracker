from django.conf import settings
from django.db import models


class Employee(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.email


class TrainingRequirement(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    link = models.URLField()

    def __str__(self):
        return self.name


class TrainingAssignment(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    training_requirement = models.ForeignKey(
        TrainingRequirement, on_delete=models.CASCADE
    )
    assigned_date = models.DateField()
    due_date = models.DateField()

    def __str__(self):
        return f"{self.employee} - {self.training_requirement} - {self.due_date}"


class TrainingCompletion(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    training_requirement = models.ForeignKey(
        TrainingRequirement, on_delete=models.CASCADE
    )
    completion_date = models.DateField()
    # TODO: Add the ability to upload a certificate, store in blob storage like s3, then
    # store the url to the certificate in this model

    def __str__(self):
        return f"{self.employee} - {self.training_requirement} - {self.completion_date}"
