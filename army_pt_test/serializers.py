from rest_framework import serializers
from .models import Cadet


class CadetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cadet
        fields = ('id', 'lastname', 'firstname', 'middleinitial', 'gender', 'unit', 'date',
                  'mos', 'grade', 'age', 'heightininches', 'weightinpounds', 'bodyfatpercentage')
