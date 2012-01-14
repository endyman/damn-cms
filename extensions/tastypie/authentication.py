from tastypie.authentication import ApiKeyAuthentication
from django.contrib.auth.models import User

class CustomApiKeyAuthentication(ApiKeyAuthentication):
	def is_authenticated(self, request, **kwargs):

		username =	request.META.get('HTTP_X_RESTCMS_USERNAME')	or request.GET.get('username')
		api_key =	request.META.get('HTTP_X_RESTCMS_APIKEY') or request.GET.get('api_key')

		if not username or not api_key:
			return self._unauthorized()
		try:
			user = User.objects.get(username=username)
		except (User.DoesNotExist, User.MultipleObjectsReturned):
			return self._unauthorized()
		request.user = user
		return self.get_key(user, api_key)
