from rest_framework import serializers

from materials.models import Course, Lesson, Subscription
from materials.validators import ValidateYoutubeUrl


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'


class SubSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        fields = '__all__'


class CourseListSerializer(serializers.ModelSerializer):
    lesson_count = serializers.SerializerMethodField()
    lesson = LessonSerializer(many=True, source='lesson_set')
    sub = serializers.SerializerMethodField()


    class Meta:
        validators = [ValidateYoutubeUrl(fields='link')]
        model = Course
        fields = '__all__'

    def get_lesson_count(self, obj):
        return obj.lesson_set.count()

    def get_sub(self, instance):
        sub = Subscription.objects.all().filter(course=instance.pk).filter(user=self.context.get('request').user.pk)
        if sub:
            return True
        else:
            return False



class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'
