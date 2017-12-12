from django.core.cache import cache
from django.utils.deprecation import MiddlewareMixin
from online_status.conf import online_status_settings as config
from online_status.status import OnlineStatus, refresh_user, refresh_users_list


class OnlineStatusMiddleware(MiddlewareMixin):
    """Cache OnlineStatus instance for an authenticated User"""

    def process_request(self, request):
        if request.user.is_authenticated:
            onlinestatus = cache.get(
                config.CACHE_PREFIX_USER % request.user.pk)
        elif not config.ONLY_LOGGED_USERS:
            onlinestatus = cache.get(
                config.CACHE_PREFIX_ANONYM_USER % request.session.session_key)
        else:
            return
        if not onlinestatus:
            onlinestatus = OnlineStatus(request)
        refresh_user(request)
        refresh_users_list(request, updated=onlinestatus)
        return
