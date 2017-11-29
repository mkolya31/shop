from django.db import models


class ProductCategory(models.Model):
    name = models.CharField(max_length=48, blank=True, null=True, default=None)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return "%s %s" % (self.id, self.name)

    class Meta:
        verbose_name = 'Категория товара'
        verbose_name_plural = 'Категории товара'


class Product(models.Model):
    name = models.CharField(max_length=64, blank=True, null=True, default=None)
    product_category = models.ForeignKey(ProductCategory, blank=True, null=True, default=None)
    description = models.TextField(blank=True, null=True, default=None)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return "%s %s" % (self.name, self.id)

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'


class ProductImage(models.Model):
    product = models.ForeignKey(Product, blank=True, null=True, default=None)
    image = models.ImageField(upload_to='products_images/')
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return "Фотография %s" % self.id

    class Meta:
        verbose_name = 'Фотография'
        verbose_name_plural = 'Фотографии'

# # Create your models here.
