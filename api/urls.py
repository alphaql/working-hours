from django.conf.urls import url, include
from rest_framework import routers
from api.v0.views.users import UserViewSet
from api.v1.views.games import GameViewSet
from api.v0.views.working_hours import (
    WorkingHoursViewSet,
    WorkingHoursWeekViewSet,
)


# Routers provide an easy way of automatically determining the URL conf.
router_v0 = routers.DefaultRouter()
router_v1 = routers.DefaultRouter()

router_v0.register(r'users', UserViewSet)
router_v0.register(r'working-hours', WorkingHoursViewSet)
router_v0.register(r'working-hours/week/(?P<week>.+)/year/(?P<year>.+)/user/('
                r'?P<username>.+)',
                WorkingHoursWeekViewSet,
                basename='workinghours')

router_v1.register(r'games', GameViewSet, basename='games')


urlpatterns = [
    url(r'v0/', include(router_v0.urls)),
    url(r'v1/', include(router_v1.urls)),
]
