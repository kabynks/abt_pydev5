from django.db import models
from university.models import University
from faculty_fields.models import *
class Faculty(models.Model):
    university = models.ForeignKey(University, verbose_name='University', on_delete=models.CASCADE)
    name = models.CharField('Faculty Name', max_length=256)
    tuition_language = models.ManyToManyField(
        Tuition_language,
        verbose_name="Tuition language",

    )
    education_form = ManyToManyField(Education_form, verbose_name="Education form")
    acceptance = models.PositiveSmallIntegerField(verbose_name="Acceptance")
    grant = models.DecimalField(
        'Grant score',
        decimal_places=1,
        max_digits=4,
        blank=True, null=True
    )
    contract = models.DecimalField(
        'Contract score',
        decimal_places=1,
        max_digits=4,
        blank=True, null=True
    )
    first_subject = models.ForeignKey(Subject, verbose_name='First subject', on_delete=CASCADE, related_name='first_subject')
    second_subject = models.ForeignKey(Subject, verbose_name="Second subject", on_delete=CASCADE, related_name="second_subject")
    class Meta:
        verbose_name = "Faculty"
        verbose_name_plural = "Faculties"