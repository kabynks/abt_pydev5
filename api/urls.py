from django.urls import path
from .views import *

urlpatterns = [
    path("tuition_language/", TuitionLanguageList.as_view(), name="tuition_language"),
    path("tuition_language/<int:pk>/", TuitionLanguageDetail.as_view(), name="tuition_language_detail"),
    path("education_form/", EducationFormList.as_view(), name="education_form"),
    path("education_form/<int:pk>/", EducationFormDetail.as_view(), name="education_form_detail"),
    path("subjects/", Subject_List.as_view(), name="subjects_list"),
    path("subjects/<int:pk>/", Subject_Detail.as_view(), name="subject_detail"),
    path("faculties", Faculty_List.as_view(), name="faculties_list"),
    path("faculties/<int:pk>/", Faculty_Detail.as_view(), name="faculty_detail"),
    path("universities/", UniversityList.as_view(), name="universities"),
    path("universities/<int:pk>/", UniversityDetail.as_view(), name="universities_detail")

]
