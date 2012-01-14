def current_site_url():
	"""Returns fully qualified URL (no trailing slash) for the current site."""
	from django.conf import settings
	from django.contrib.sites.models import Site
	current_site = Site.objects.get_current()
	protocol = getattr(settings, 'MY_SITE_PROTOCOL', 'http')
	port = getattr(settings, 'MY_SITE_PORT', '')
	url = '%s://%s' % (protocol, current_site.domain)
	if port:
		url += ':%s' % port
	return url
