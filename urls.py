import os
import logging

from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin
from django.conf import settings

logger = logging.getLogger('apps')
admin.autodiscover()

APP_DIRS = os.path.abspath(os.path.join(settings.SITE_ROOT, 'apps'))
urlpatterns = patterns('',
	url(r'^admin/', include(admin.site.urls)),
)

## dynamically load tastypie apps
for app_name in os.listdir(APP_DIRS):
	try:
		if not app_name.endswith(".py") and not app_name.endswith(".pyc"):
			logger.debug("found app: %s", app_name)
			import_string = "apps.%s.api" % (app_name)
			api_module = __import__(import_string, globals(), locals(), [])
			app_obj = getattr(api_module,app_name)
			app_url_configs = app_obj.api.get_api()
			for key in app_url_configs:
				urlpatterns += patterns("", url(r'^%s/api/' % app_name, include(app_url_configs[key].urls)))
	except Exception, e:
		logger.debug("couldn't import %s %s %s", app_name, Exception, e)
