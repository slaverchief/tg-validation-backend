from django.db import models

class TGuser(models.Model):
    tgid = models.CharField(max_length=100, unique=True, db_index=True)

    class Meta:
        verbose_name_plural = "Кто власть имеет"
        verbose_name = verbose_name_plural

class Chat(models.Model):
    name = models.CharField(max_length=100, unique=True)
    chatid = models.CharField(max_length=100, db_index=True)
    topic_id = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Чаты"
        verbose_name = "Чат"
        constraints = [models.UniqueConstraint(fields=['chatid', 'topic_id'], name='unique_chat')]

class Group(models.Model):
    name = models.CharField(max_length=100, unique=True)
    chats = models.ManyToManyField(Chat)

    def __str__(self):
        return self.name


    class Meta:
        verbose_name_plural = "Группы"
        verbose_name = "Группа"