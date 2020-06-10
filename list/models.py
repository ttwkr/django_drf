from django.db import models


class List(models.Model):
    id = models.AutoField(primary_key=True)
    contents = models.TextField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    deleted_at = models.DateTimeField()

    class Meta:
        db_tables = 'list'
