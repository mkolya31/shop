from django.db import models
from products.models import Product


class Customer(models.Model):
    customer_login = models.CharField(max_length=64, blank=True, null=True, default=None)
    customer_password = models.CharField(max_length=64, blank=True, null=True, default=None)
    customer_firstname = models.CharField(max_length=64, blank=True, null=True, default=None)
    customer_secondname = models.CharField(max_length=64, blank=True, null=True, default=None)
    customer_email = models.EmailField(max_length=64, blank=True, null=True, default=None)
    customer_phone = models.CharField(max_length=48, blank=True, null=True, default=None)
    customer_address = models.CharField(max_length=128, blank=True, null=True, default=None)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return "Покупатель %s %s" % (self.customer_secondname, self.id)

    class Meta:
        verbose_name = 'Покупатель'
        verbose_name_plural = 'Покупатели'


class DeliveryMethod(models.Model):
    name = models.CharField(max_length=24, blank=True, null=True, default=None)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return "Метод доставки: %s" % self.name

    class Meta:
        verbose_name = 'Метод доставки'
        verbose_name_plural = 'Методы доставки'


class PaymentMethod(models.Model):
    name = models.CharField(max_length=48, blank=True, null=True, default=None)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return "Метод оплаты: %s" % self.name

    class Meta:
        verbose_name = 'Метод оплаты'
        verbose_name_plural = 'Методы оплаты'


class Status(models.Model):
    name = models.CharField(max_length=24, blank=True, null=True, default=None)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return "Статус заказа: %s" % self.name

    class Meta:
        verbose_name = 'Статус'
        verbose_name_plural = 'Статусы'


class Order(models.Model):
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)  # total price for all products
    customer_id = models.ForeignKey(Customer, blank=True, null=True, default=None)
    delivery_method = models.ForeignKey(DeliveryMethod, blank=True, null=True, default=None)
    payment_method = models.ForeignKey(PaymentMethod, blank=True, null=True, default=None)
    comments = models.TextField(blank=True, null=True, default=None)
    status = models.ForeignKey(Status, blank=True, null=True, default=None)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return "Заказ %s %s" % (self.id, self.status.name)

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'


class ProductInOrder(models.Model):
    order = models.ForeignKey(Order, blank=True, null=True, default=None)
    product = models.ForeignKey(Product, blank=True, null=True, default=None)
    number = models.IntegerField(default=1)
    price_per_item = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0) #price*nmb*discount
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return "%s %s" % (self.product.name, self.product.id)

    class Meta:
        verbose_name = 'Товар в заказе'
        verbose_name_plural = 'Товары в заказах'


# Create your models here.
