from django.db import models
from django.conf import settings
from djangotoolbox.fields import ListField
from django_mongodb_engine.fields import GridFSField
from django_mongodb_engine.storage import GridFSStorage
from utils.helper import current_site_url

gridfs = GridFSStorage(database='damncms_media', collection='media', base_url='%s/media/' % getattr(settings, 'SITE_URL', 'http://localhost:8080'))

import logging

logger = logging.getLogger('apps')

class ProductType(models.Model):
	name = models.CharField(max_length=100)
	order = models.IntegerField(unique=True, default=0)

	def save(self, *args, **kwargs):
		# autogenerate order id if none is provided
		if self.order == 0:
			query_result = ProductType.objects.all()
			if query_result:
				self.order = query_result.aggregate(max_value=models.Max('order'))['max_value'] + 1
			else:
				self.order = 1
		super(ProductType, self).save(*args, **kwargs)

	def __unicode__(self):
		return u'%d-%s' % (self.order, self.name)

	class Meta:
		# order ascending by order
		ordering = ['order']
		# add view permission (GET)
		permissions = (
			("view_productype", "Can view avaliable product types"),
			)

class Product(models.Model):
	product_type = models.ForeignKey('ProductType', related_name='products')
	productimage = models.FileField(storage=gridfs, upload_to='simpleapp')
	name = models.CharField(max_length=100)
	description = models.CharField(max_length=4096)
	releasedate = models.DateTimeField()

	def __unicode__(self):
		return u'Type: %s Name: %s' % (self.product_type, self.name)

	class Meta:
		# order by product_type and releasedate (desc)
		ordering = ['product_type', '-releasedate']
		# add view permission (GET)
		permissions = (
			("view_pproduct", "Can view avaliable products"),
			)
