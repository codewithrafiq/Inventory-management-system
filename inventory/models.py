from django.db import models


class BaseModel(models.Model):
    """
        BaseModel is a base model that other models will inherit from.
    """

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    is_deleted = models.BooleanField(default=False)

    class Meta:
        abstract = True


class Inventory(BaseModel):
    """
        Inventory is a model that stores the inventory of a product.
    """

    name = models.CharField(max_length=255)
    description = models.TextField()
    note = models.TextField()
    stock = models.IntegerField()
    availability = models.BooleanField(default=True)
    supplier = models.ForeignKey('Supplier', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Supplier(BaseModel):
    """
        Supplier is a model that stores the supplier of a product.
    """

    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
