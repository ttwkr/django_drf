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
        db_table = "todolists"


class Bests(models.Model):
    id = models.AutoField(primary_key=True)
    todo = models.ForeignKey(TodoList, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = "bests"


class Shop(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=45)
    phone = models.CharField(max_length=11)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    deleted_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = "shops"


class Item(models.Model):
    id = models.AutoField(primary_key=True)
    shop = models.ForeignKey(Shop, models.DO_NOTHING, related_name="item")
    name = models.CharField(max_length=45)
    qty = models.IntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    deleted_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = "item"


class ShopImage(models.Model):
    id = models.AutoField(primary_key=True)
    shop = models.ForeignKey(Shop, models.DO_NOTHING)
    image = models.CharField(max_length=45)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    deleted_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = "shop_images"


class Likes(models.Model):
    id = models.AutoField(primary_key=True)
    shop = models.ForeignKey(Shop, models.DO_NOTHING)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    deleted_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = "likes"
