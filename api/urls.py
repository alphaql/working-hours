from django.conf.urls import url, include
from rest_framework import routers
from api.views import (
    UserViewSet,
    WorkingHoursViewSet,
    WorkingHoursWeekViewSet,
)


# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'working-hours', WorkingHoursViewSet)
router.register(r'working-hours/week/(?P<week>.+)/year/(?P<year>.+)',
                WorkingHoursWeekViewSet,
                basename='WorkingHour')

urlpatterns = [
    url(r'^', include(router.urls)),
]
