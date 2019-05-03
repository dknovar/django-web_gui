from django.db import models

# Create your models here.
class info(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    waktu = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "{} {}".format(self.id, self.title)