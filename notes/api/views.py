from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import noteserial
from .models import Note


@api_view(['GET'])
def getroutes(request):
    routes = [
        {
            'Endpoint': '/notes/',
            'method': 'GET',
            'body': None,
            'description': 'Returns an array of notes'
        },
        {
            'Endpoint': '/notes/id',
            'method': 'GET',
            'body': None,
            'description': 'Returns a single note object'
        },
        {
            'Endpoint': '/notes/create/',
            'method': 'POST',
            'body': {'body': ""},
            'description': 'Creates new note with data sent in post request'
        },
        {
            'Endpoint': '/notes/id/update/',
            'method': 'PUT',
            'body': {'body': ""},
            'description': 'Creates an existing note with data sent in post request'
        },
        {
            'Endpoint': '/notes/id/delete/',
            'method': 'DELETE',
            'body': None,
            'description': 'Deletes and exiting note'
        },
    ]

    return Response(routes)

@api_view(['GET'])
def getnotes(request):
    notes=Note.objects.all()
    serializer=noteserial(notes, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getnote(request, pk):
    notes=Note.objects.get(id=pk)
    serializer=noteserial(notes, many=False)
    return Response(serializer.data)


@api_view(['PUT'])
def updateNote(request, pk):
    data=request.data
    note=Note.objects.get(id=pk)
    serializer=noteserial(instance=note, data=data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['DELETE'])
def deleteNote(request, pk):
    note=Note.objects.get(id=pk)
    note.delete()
    return Response('Note was deleted')

@api_view(['POST'])
def createNote(request):
    data=request.data
    note=Note.objects.create(
        body=data['body']
    )
    serializer=noteserial(note, many=False)
    return Response(serializer.data)