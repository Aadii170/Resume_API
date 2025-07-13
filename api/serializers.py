from pyexpat import model
from rest_framework import serializers
from api.models import Resume

class ProfileSerializer(serializers.ModelSerializer):
  class Meta:
    model=Resume
    fields = ['name', 'email', 'dob', 'profile', 'resume_file']