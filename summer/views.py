from django.shortcuts import render,get_object_or_404
from rest_framework.response import Response 
from rest_framework.decorators import api_view

from .models import Movie,Comment
from .serializers import *



@api_view(['GET','POST'])
def movie_list_create(request):

    if request.method == 'GET':
        movies = Movie.objects.all()
        serializers = MovieListSerializer(movies,many=True)

        return Response(data=serializers.data)

    if request.method == 'POST' :

        serializer = MovieListSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(data=serializer.data) 


 
@api_view(['GET','PATCH','DELETE'])
def movie_detail_update_delete(request,movie_pk):

    movie = get_object_or_404(Movie, pk=movie_pk)

    if request.method=='GET':
        serializer = MovieListSerializer(movie)
        return Response(serializer.data)

    elif request.method == 'PATCH' :
        serializer = MovieListSerializer(instance=movie, data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)

    elif request.method == 'DELETE' : 
        movie.delete()
        data={
            'movie':movie_pk
        }   
        return Response(data)


@api_view(['GET'])
def comment_list(request) :
    comments = get_list_or_404(Comment)
    serializer = CommentSerializer(comments, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def comment_detail(request, comment_pk) :
    comments = get_list_or_404(Comment, pk = comment_pk)
    serializer = CommentSerializer(comments)
    return Response(serializer.data)

@api_view(['POST'])
def comment_create(request, movie_pk) :
    movie = get_list_or_404(Movie, pk = movie_pk)
    serializer = CommentSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True) :
        serializer.save(movie=movie) 
        return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET', 'DELETE', 'PUT'])
def comment_detail(request, comment_pk) :
    comment = get_list_or_404(Comment, pk = comment_pk)
    if request.method == 'GET' :
        serializer = CommentSerializer(comment)
        return Response(serializer.data)
    elif request.method == "DELETE" :
        comment.delete()
        data= {
            'delete' :f'댓글 {comment_pk}번이 삭제 되었습니다.'
        }
        return Response(data, status=status.HTTP_204_NO_CONTENT)
    elif request.method == "PUT" :
        serializer = CommentSerializer(instance=comment, data=request.data)
        if serializer.is_valid(raise_exception=True) :
            serializer.save()
            return Response(serializer.data)