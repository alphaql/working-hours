from rest_framework import (
    viewsets,
)
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import generics

from api.serializers.user import UserSerializer
from api.serializers.working_hours import (
    WorkingHourSerializer,
    WorkingHourWeekSerializer,
)
from users.models import User
from working_hours.models import WorkingHour


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    http_method_names = ['options', 'patch', 'put', 'get', 'post']
    resource_name = 'customers'
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated,)


class WorkingHoursViewSet(viewsets.ModelViewSet):
    http_method_names = ['options', 'patch', 'put', 'get', 'post']
    resource_name = 'working_hours'
    serializer_class = WorkingHourSerializer
    permission_classes = (IsAuthenticated,)
    queryset = WorkingHour.objects.all().order_by("-date")


class WorkingHoursWeekViewSet(viewsets.ModelViewSet):
    http_method_names = ['options', 'get', ]
    resource_name = 'working_hours_week'
    serializer_class = WorkingHourWeekSerializer
    permission_classes = (IsAuthenticated,)
    week = None

    def list(self, request, *args, **kwargs):
        total_worked_hours_in_week = round(
            WorkingHour.total_worked_hours_in_week(kwargs["week"]))
        total_extra_hours_in_week = round(
            WorkingHour.total_extra_hours_in_week(kwargs["week"]), 2)
        total_mandatory_hours_in_week = round(
            WorkingHour.total_mandatory_hours_in_week(kwargs["week"]), 2)

        data = {
            'total_worked_hours_in_week': total_worked_hours_in_week,
            'total_extra_hours_in_week': total_extra_hours_in_week,
            'total_mandatory_hours_in_week': total_mandatory_hours_in_week,
        }

        serializer = WorkingHourWeekSerializer(data=data)
        if serializer.is_valid():
            return Response(serializer.data)
