from django.contrib import admin

from .models import (
    Employee,
    TrainingAssignment,
    TrainingCompletion,
    TrainingRequirement,
)

admin.site.register(Employee)
admin.site.register(TrainingRequirement)
admin.site.register(TrainingAssignment)
admin.site.register(TrainingCompletion)
