from rest_framework import serializers

# ------------------ MODELOS ---------------------------
from Profile.models import ProfileModel

class ProfileModelSerializers(serializers.ModelSerializer):
    class Meta:
        model = ProfileModel
        fields = ('_all_')

