import json
import os

from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from api.v1.serializers.general import GeneralSerializer


class GeneralViewSet(ModelViewSet):
    http_method_names = ['get']
    serializer_class = GeneralSerializer
    permission_classes = (IsAuthenticated,)
    data = None

    def set_file_path(self, data_file_path):
        if not os.path.exists(data_file_path):
            return
        with open(data_file_path) as json_file:
            self.data = json.load(json_file)

    def set_data_from_str(self, data):
        self.data = json.loads(data)

    def list(self, request, *args, **kwargs):
        if self.data:
            return Response(self.data)
