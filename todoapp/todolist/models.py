from django.db import models
from django.utils import timezone
# Create your models here.


class ToDo(models.Model):
    title = models.CharField("Name task", max_length=200)
    is_complete = models.BooleanField("Complete", default=False)

    class Meta:
        verbose_name = "Task"
        verbose_name_plural = "Tasks"


    def __str__(self) -> str:
        return self.title   
    