from django.test import TestCase

# Create your tests here.
@api_view(['GET'])
def API(request):
    return Response("test")