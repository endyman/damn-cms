from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin
from tastypie.api import Api
admin.autodiscover()

from simpleapp.api import TypeResource, ProductResource

# create the naespaces for the applications
simpleapp_api = Api(api_name='simpleapp')
simpleapp_api.register(TypeResource())
simpleapp_api.register(ProductResource())

urlpatterns = patterns('',
	# Examples:
	# url(r'^$', 'restapi.views.home', name='home'),
	# url(r'^restapi/', include('restapi.foo.urls')),

	# Uncomment the next line to enable the admin:
	url(r'^admin/', include(admin.site.urls)),
	url(r'^api/v1/', include(simpleapp_api.urls)),
)
