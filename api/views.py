from urllib import request

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.status import *

from university.models import University
from .serializers import Tuition_LanguageSerializer, EducationFormSerializer, SubjectSerializer, FacultySerializer, \
    UniversitySerializer
from faculty_fields.models import Tuition_language, Education_form, Subject
from faculty.models import Faculty


class TuitionLanguageList(APIView):

    def get(self, request, format=None):
        queryset = Tuition_language.objects.all()
        serializer = Tuition_LanguageSerializer(queryset, many=True)
        return Response(serializer.data, status=HTTP_200_OK)
    def post(self, request, format=None):
        serializer = Tuition_LanguageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_201_CREATED)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

class TuitionLanguageDetail(APIView):
    def get_object(self, pk):
        try:
            return Tuition_language.objects.get(pk=pk)
        except Tuition_language.DoesNotExist:
            return Response(status=HTTP_404_NOT_FOUND)

    def get(self, request, pk, format=None):
        queryset = self.get_object(pk)
        serializer = Tuition_LanguageSerializer(queryset)
        return Response(serializer.data, status=HTTP_200_OK)
    def put(self, request, pk, format=None):
        queryset = self.get_object(pk)
        serializer = Tuition_LanguageSerializer(queryset, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=HTTP_406_NOT_ACCEPTABLE)
    def patch(self, request, pk, format=None):
        queryset = self.get_object(pk)
        serializer = Tuition_LanguageSerializer(queryset, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=HTTP_406_NOT_ACCEPTABLE)
    def delete(self, request, pk, format=None):
        queryset = self.get_object(pk)
        queryset.delete()
        return Response(status=HTTP_204_NO_CONTENT)



class EducationFormList(APIView):
    def get(self, request, format=None):
        queryset = Education_form.objects.all()
        serializer = EducationFormSerializer(queryset, many=True)
        return Response(serializer.data, status=HTTP_200_OK)
    def post(self, request, format=None):
        serializer = EducationFormSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_201_CREATED)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
class EducationFormDetail(APIView):
    def get_object(self, pk):
        try:
            return Education_form.objects.get(pk=pk)
        except Education_form.DoesNotExist:
            return Response(status=HTTP_404_NOT_FOUND)
    def get(self, request, pk, format=None):
        queryset = self.get_object(pk)
        serializer = EducationFormSerializer(queryset)
        return Response(serializer.data, status=HTTP_200_OK)
    def put(self, pk, request, format=None):
        queryset = self.get_object(pk)
        serializer = EducationFormSerializer(queryset, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=HTTP_406_NOT_ACCEPTABLE)
    def patch(self, request, pk, format=None):
        queryset = self.get_object(pk)
        serializer = EducationFormSerializer(queryset, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=HTTP_406_NOT_ACCEPTABLE)
    def delete(self, request, pk, format=None):
        queryset = self.get_object(pk)
        queryset.delete()
        return Response(status=HTTP_204_NO_CONTENT)

class Subject_List(APIView):
    def get(self, request, format=None):
        queryset = Subject.objects.all()
        serializer = SubjectSerializer(queryset, many=True)
        return Response(serializer.data, status=HTTP_200_OK)
    def post(self, request, format=None):
        serializer = SubjectSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_201_CREATED)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

class Subject_Detail(APIView):
    def get_object(self, pk):
        try:
            return Subject.objects.get(pk=pk)
        except Subject.DoesNotExist:
            return Response(status=HTTP_404_NOT_FOUND)
    def get(self, request, pk, format=None):
        queryset = self.get_object(pk)
        serializer = SubjectSerializer(queryset)
        return Response(serializer.data, status=HTTP_200_OK)
    def put(self, request, pk, format=None):
        queryset = self.get_object(pk)
        serializer = SubjectSerializer(queryset, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=HTTP_406_NOT_ACCEPTABLE)
    def patch(self, request, pk, format=None):
        queryset = self.get_object(pk)
        serializer = SubjectSerializer(queryset, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=HTTP_406_NOT_ACCEPTABLE)
    def delete(self, pk):
        queryset = self.get_object(pk)
        queryset.delete()
        return Response(status=HTTP_204_NO_CONTENT)

class Faculty_List(APIView):
    def get(self, request, format=None):
        queryset = Faculty.objects.all()
        serializer = FacultySerializer(queryset, many=True)
        return Response(serializer.data, status=HTTP_200_OK)
    def post(self, request, format=None):
        serializer = FacultySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_201_CREATED)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

class Faculty_Detail(APIView):
    def get_object(self, pk):
        try:
            return Faculty.objects.get(pk=pk)
        except Faculty.DoesNotExist:
            return Response(status=HTTP_404_NOT_FOUND)
    def get(self, request, pk, format=None):
        queryset = self.get_object(pk)
        serializer = FacultySerializer(queryset)
        return Response(serializer.data, status=HTTP_200_OK)
    def put(self, request, pk, format=None):
        queryset = self.get_object(pk=pk)
        serializer = FacultySerializer(queryset, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_201_CREATED)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
    def patch(self, request, pk, format=None):
        queryset = self.get_object(pk=pk)
        serializer = FacultySerializer(queryset, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_201_CREATED)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
    def delete(self, pk):
        queryset = Faculty.objects.get(pk=pk)
        queryset.delete()
        return Response(status=HTTP_204_NO_CONTENT)
class UniversityList(APIView):
    def get(self, request, format=None):
        queryset = University.objects.all()
        serializer = UniversitySerializer(queryset, many=True, context={'request': request})
        return Response(serializer.data, status=HTTP_200_OK)
    def post(self, request, format=None):
        serializer = UniversitySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_201_CREATED)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
class UniversityDetail(APIView):
    def get_object(self, pk):
        try:
            return University.objects.get(pk=pk)
        except Faculty.DoesNotExist:
            return Response(status=HTTP_404_NOT_FOUND)
    def get(self, request, pk, format=None):
        queryset = self.get_object(pk)
        serializer = UniversitySerializer(queryset)
        return Response(serializer.data, status=HTTP_200_OK)
    def put(self, request, pk, format=None):
        queryset = self.get_object(pk=pk)
        serializer = UniversitySerializer(queryset, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_201_CREATED)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
    def patch(self, request, pk, format=None):
        queryset = self.get_object(pk=pk)
        serializer = UniversitySerializer(queryset, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_201_CREATED)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
    def delete(self, pk):
        queryset = University.objects.get(pk=pk)
        queryset.delete()
        return Response(status=HTTP_204_NO_CONTENT)