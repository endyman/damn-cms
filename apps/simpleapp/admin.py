from django.contrib import admin
from tastypie.models import ApiKey
from simpleapp.models import ProductType, Product

admin.site.register(ProductType)
admin.site.register(Product)
admin.site.register(ApiKey)

