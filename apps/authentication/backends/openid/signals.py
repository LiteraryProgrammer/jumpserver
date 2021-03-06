from django.dispatch import Signal


post_create_or_update_openid_user = Signal(providing_args=('user',))
post_openid_login_success = Signal(providing_args=('user', 'request'))
