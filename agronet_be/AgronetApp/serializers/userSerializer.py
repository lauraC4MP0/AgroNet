from AgronetApp.models.user import User
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"

        def create(self, validated_data):
            userInstance = User.objects.create(**validated_data)
            return userInstance

        def to_representation(self, obj):
            user = User.objects.get(id=obj.id)
            return {
                "usermane" : user.usersname,
                "name_user" : user.name_user,
                "lastname_user" : user.lastname_user,
                "email" : user.email,
                "address_user" : user.address_user,
                "id_city" : user.id_city,
                "id_department" : user.id_department,
                "num_phone" : user.num_phone,
                "Type_sex" : user.Type_sex,
                "Type_rol" : user.Type_rol,
                "sex_user" : user.sex_user,
                "rol_user" : user.rol_user,
            }



