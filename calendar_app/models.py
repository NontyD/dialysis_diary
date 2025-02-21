from django.db import models
from django.conf import settings
from django.utils.timezone import make_aware, now

end = models.DateTimeField(default=now)


class Event(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    start = models.DateTimeField()  
    end = models.DateTimeField()

    def save(self, *args, **kwargs):
        """Ensure datetimes are timezone-aware."""
        if self.start and not self.start.tzinfo:
            self.start = make_aware(self.start)
        if self.end and not self.end.tzinfo:
            self.end = make_aware(self.end)
        super().save(*args, **kwargs)
