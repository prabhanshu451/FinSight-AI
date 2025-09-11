from django.db import models
from django.contrib.auth.models import User

class Forecast(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    horizon_months = models.IntegerField(default=3)
    generated_at = models.DateTimeField(auto_now_add=True)
    data_json = models.JSONField()
    def __str__(self):
        return f"Forecast {self.user.username} @ {self.generated_at}"
