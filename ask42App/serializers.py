from rest_framework.serializers import ModelSerializer

from ask42App.models import Input


class InputSerializer(ModelSerializer):
    class Meta:
        model = Input
        fields = ['id', 'data']
