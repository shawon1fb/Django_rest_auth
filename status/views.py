from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics, mixins
from status.models import Status
from status.serializers import StatusSerializer
from rest_framework import serializers


class StatusList(mixins.CreateModelMixin, generics.GenericAPIView):
    serializer_class = StatusSerializer
    queryset = Status.objects.all()
    permission_classes = [permissions.AllowAny]

    def get(self, request, *args, **kwargs):
        qs = Status.objects.all()
        ser = StatusSerializer(qs, many=True)
        return Response(ser.data)

    def post(self, request, *args, **kwargs):
        # return mixins.ListModelMixin.list(self=self, request=request, *args, **kwargs)
        return mixins.CreateModelMixin.create(self, request=request, *args, **kwargs)
