from rest_framework import serializers
from .models import *

class CommentSerializer(serializers.ModelSerializer) :
    class Meta :
        model = Comment
        fields ='__all__'
        read_only_fields= ('movie', )

class MovieListSerializer(serializers.ModelSerializer):
    comment_set = CommentSerializer(many=True, read_only=True) 
    comment_count = serializers.IntegerField(source='comment_set.count', read_only=True) 
    comment_first = CommentSerializer(source='comment_set.first', read_only=True)
    comment_filter = serializers.SerializerMethodField('less_7')
    
    def less_7(self, movie) :
        qs = Comment.objects.filter(pk__lte=7, movie=movie)
        serializers= CommentSerializer(instance=qs, many=True)
        return serializers.data
    class Meta:
        model = Movie
        fields = '__all__'


