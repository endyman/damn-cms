import copy

from tastypie import fields
from tastypie.resources import ModelResource
from tastypie.api import Api

#internal imports
from extensions.tastypie.authentication import CustomApiKeyAuthentication
from extensions.tastypie.authorization import CustomDjangoAuthorization

from simpleapp.models import ProductType, Product

def get_api():
	# create the naespaces for the applications
	api = Api(api_name='simpleapp')
	api.register(TypeResource())
	api.register(ProductResource())
	
	base_path_regex = r'^api/v1/'
	return base_path_regex,api

class TypeResource(ModelResource):
	products = fields.ToManyField('simpleapp.api.ProductResource', 'products', full=False)
	class Meta:
		queryset = ProductType.objects.all()
		include_resource_uri = False
		resource_name = 'types'
#		authentication = CustomApiKeyAuthentication()
#		authorization = CustomDjangoAuthorization()

	def alter_list_data_to_serialize(self, request, data_dict):
		# remove meta key from response
		if isinstance(data_dict, dict):
			if 'meta' in data_dict:
				# Get rid of the "meta".
				del(data_dict['meta'])
				# Rename the objects.
				data_dict['types'] = copy.copy(data_dict['objects'])
				del(data_dict['objects'])
		return data_dict

class ProductResource(ModelResource):
	class Meta:
		queryset = Product.objects.all()
		include_resource_uri = True
		resource_name = 'products'
#		authentication = CustomApiKeyAuthentication()
#		authorization = CustomDjangoAuthorization()

	def alter_list_data_to_serialize(self, request, data_dict):
		# remove meta key from response
		if isinstance(data_dict, dict):
			if 'meta' in data_dict:
				# Get rid of the "meta".
				del(data_dict['meta'])
				# Rename the objects.
				data_dict['products'] = copy.copy(data_dict['objects'])
				del(data_dict['objects'])
		return data_dict
