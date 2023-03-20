from django.shortcuts import render

from django.http.response import JsonResponse
from rest_framework import status
 
from Content.models import *
from Content.serializer import *
from rest_framework.decorators import api_view


@api_view(['GET', 'POST', 'DELETE'])
def contentList(request):
    if request.method == 'GET':
        allcontent = Content.objects.all()
        
        tutorials_serializer = ContentSerializer(allcontent, many=True)
        return JsonResponse(tutorials_serializer.data, safe=False)
        # 'safe=False' for objects serialization
 
    elif request.method == 'POST':
        # content_data = JSONParser().parse(request)
        content_serializer = ContentSerializer(data=request.data)
        if content_serializer.is_valid():
            content_serializer.save()
            return JsonResponse(content_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(content_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        count = Content.objects.all().delete()
        return JsonResponse({'message': '{} Contents were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)
 
 
@api_view(['GET', 'PUT', 'DELETE'])
def contentdetail(request, pk):
    try: 
        content = Content.objects.get(pk=pk) 
    except Content.DoesNotExist: 
        return JsonResponse({'message': 'The Content does not exist'}, status=status.HTTP_404_NOT_FOUND) 
 
    if request.method == 'GET': 
        tutorial_serializer = ContentSerializer(content) 
        return JsonResponse(tutorial_serializer.data) 
 
    elif request.method == 'PUT': 
        print(request.data )

        field_to_update = request.data.get('field')
        new_value = request.data.get('value')

        if not field_to_update or not new_value:
            return JsonResponse({'error': 'field and new_value fields are required'}, status=status.HTTP_400_BAD_REQUEST)

        # Update the specified field
        setattr(content, field_to_update, new_value)
        content.save()

        content_serializer = ContentSerializer(content)
 
        return JsonResponse(content_serializer.data) 
 
    elif request.method == 'DELETE': 
        content.delete() 
        return JsonResponse({'message': 'Tutorial was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
    
        

