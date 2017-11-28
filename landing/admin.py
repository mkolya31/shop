from django.contrib import admin
from .models import *


class SubscriberAdmin(admin.ModelAdmin):
    list_display = ["email"]

    fields = ["email"]
    # exclude = ["email"]

    class Meta:
        model = Subscriber

admin.site.register(Subscriber, SubscriberAdmin)

# Register your models here.
