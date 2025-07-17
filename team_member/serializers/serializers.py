from rest_framework import serializers
from team_member.models import TeamMember

class TeamMemberListSerializer(serializers.ModelSerializer):
    class Meta:
        model=TeamMember
        fields='__all__'

class TeamMemberRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model=TeamMember
        fields='__all__'

class TeamMemberWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model=TeamMember
        fields='__all__'
        