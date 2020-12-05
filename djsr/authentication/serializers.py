
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import serializers
from .models import Accounts,Employee

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):

    @classmethod
    def get_token(cls, user):
        token = super(MyTokenObtainPairSerializer, cls).get_token(user)

        # Add custom claims
        return token

class AccountsSerializer(serializers.ModelSerializer):
    """
    Currently unused in preference of the below.
    """
    email = serializers.EmailField(
        required=True
    )
    username = serializers.CharField()
    password = serializers.CharField(min_length=8, write_only=True)
    DateOfBirth = serializers.DateField(required=True)
    CNIC = serializers.CharField(max_length=13, required=True)
    Address = serializers.CharField(max_length=100, required=True)
    Phone_No = serializers.CharField(max_length=11, required=True)

    class Meta:
        model = Accounts
        fields = ('email', 'username', 'password', 'DateOfBirth', 'CNIC', 'Address', 'Phone_No')
        extra_kwargs = {'password': {'write_only': True}}

    
    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)  # as long as the fields are the same, we can just use this
        if password is not None:
            instance.set_password(password)
        instance.save()
        
        return instance



class EmployeeSerializer(serializers.ModelSerializer):
    
    #Employee_ID = models.AutoField(primary_key=True)
    Account_ID = serializers.IntegerField()
    
    class Meta:
        model = Employee
        fields = ('Account_ID',)
    

    def create(self, validated_data):
        instance = self.Meta.model(**validated_data)  # as long as the fields are the same, we can just use this
        instance.save()
        return instance