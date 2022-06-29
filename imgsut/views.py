from rest_framework import viewsets
from rest_framework.response import Response

from .models import imgs
from .serializers import imgsSerializers


class imgsView(viewsets.ModelViewSet):
    queryset = imgs.objects.all()
    serializer_class = imgsSerializers

    def put(self, request, *args, **kwargs):
        imgs_objects = self.get_object()
        data = request.data

        imgs_objects.title = data["title"]
        imgs_objects.imges = data["imges"]

        imgs_objects.save()

        serializer = imgsSerializers(imgs_objects)

        return Response(serializer.data)
