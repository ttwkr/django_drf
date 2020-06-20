from django.db import models


class TodoList(models.Model):
    id = models.AutoField(primary_key=True)
    contents = models.TextField()
    image_list = models.CharField(max_length=300)
    is_use = models.IntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    deleted_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'todolists'


class Bests(models.Model):
    id = models.AutoField(primary_key=True)
    todo = models.ForeignKey(
        TodoList, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'bests'
