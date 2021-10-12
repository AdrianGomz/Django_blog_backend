from django.http.response import Http404
from rest_framework.response import Response
from .models import Profile
from .serializers import ProfileSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class ProfileList(APIView):
    def get(self,request):
        profileList = Profile.objects.all()
        serializer = ProfileSerializer(profileList,many=True)
        return Response(serializer.data)
    def post(self,request):
        serializer = ProfileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

class ProfileDetail(APIView):
    def get_profile(self,id):
        try:
            return Profile.objects.get(id=id)
        except Profile.DoesNotExist:
            raise Http404

    def get(self, request,id):
        profile = self.get_profile(id)
        serializer = ProfileSerializer(profile)
        return Response(serializer.data)

    def put(self, request, id):
        profile = self.get_profile(id)
        serializer = ProfileSerializer(Profile, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    def delete(self, request, id):
        article = self.get_profile(id)
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)