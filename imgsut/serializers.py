from rest_framework import serializers
from .models import imgs


class imgsSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = imgs
        fields = ('title', 'imges')

