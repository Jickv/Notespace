from django.db import models

class Note(models.Model):
    mod = models.CharField(max_length=1000)

    def __str__(self):
        return self.mod
    """class Meta:
        db_table = "noteinfo"""

    


