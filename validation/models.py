from django.db import models

class TGuser(models.Model):
    tgid = models.CharField(max_length=100, unique=True, db_index=True)

    class Meta:
        verbose_name_plural = "Кто власть имеет"
        verbose_name = verbose_name_plural
