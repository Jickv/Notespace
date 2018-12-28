from django.db import models

class Note(models.Model):
    content = models.CharField(max_length=1000)
    def __str__(self):
        return '%s' % self.content
    class Meta:
        db_table = "noteinfo"

    


