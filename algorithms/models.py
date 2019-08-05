from django.db import models

# Create your models here.
class JobInfo(models.Model):
    post = models.OneToOneField("social_app.Post", on_delete=models.CASCADE)
    status = models.CharField(
        choices = [('Finished', 'Finshed'), ('Failed', 'Failed'), 
                    ('Processing', 'Processing'),('Started','Started')]
    )
    created_at = models.DateField()
    modified_at = models.DateField()