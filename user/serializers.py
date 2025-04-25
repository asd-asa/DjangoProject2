from rest_framework import serializers

from user.models import SysUser


class SysUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = SysUser
        fields = "__all__"
