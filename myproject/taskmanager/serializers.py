from rest_framework import serializers
from .models import Tasks

class TasksSerializer(serializers.ModelSerializer):
    title = serializers.CharField(max_length=100, required=True)
    description = serializers.CharField()
    due_date = serializers.DateTimeField(required=True)
    completed = serializers.BooleanField(default=False)
    priority = serializers.CharField(required=True)

    def create(self, validated_data):  
        """ 
        Create and return a new `Students` instance, given the validated data. 
        """  
        return Tasks.objects.create(**validated_data)  
    
    def update(self, instance, validated_data):  
        """ 
        Update and return an existing `Students` instance, given the validated data. 
        """  
        instance.title = validated_data.get('title', instance.title)  
        instance.description = validated_data.get('description', instance.description)  
        instance.due_date = validated_data.get('due_date', instance.due_date)  
        instance.completed = validated_data.get('completed', instance.completed)  
        instance.priority = validated_data.get('priority', instance.priority)  
  
        instance.save()  
        return instance  

    class Meta:
        model = Tasks
        fields = '__all__'