def authorize_facebook():
	"""
	Redirects the user to the Facebook login page to authorize the app:
	- response_type=code
	- Scope requests is to post updates on behalf of the user and read the ir stream
	
	:return: Redirects to the Facebook login page
	"""
	
	# Tutorial for this function:
	# http://www.programmableweb.com/news/how-to-build-facebook-hello-world-web-app-python/how-to/2015/10/05?page=2
	
	# Facebook documentation about access tokens:
	# https://developers.facebook.com/docs/facebook-login/access-tokens
	
	# What to do after this function gets us the token:
	# http://facebook-sdk.readthedocs.io/en/latest/api.html
	
	format_str = 'https://www.facebook.com/dialog/oauth?client_id={0}&redirect_uri={1}&scope=publish_actions'
	
	return flsk.redirect(fromat_str.format(FACEBOOK_APP_ID, REDIRECT_URI)
	