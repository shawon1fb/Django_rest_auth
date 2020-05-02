from django.db import models
from django.contrib.auth.models import User


def upload_status_image(instance, filename):
    return f"updates/{instance.user}/{filename}"


class Status(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to=upload_status_image, null=True, blank=True, )
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.content)[:10]

    def delete(self, *args, **kwargs):
        # first, delete the file
        self.image.delete(save=False)
        super(Status, self).delete(*args, **kwargs)
