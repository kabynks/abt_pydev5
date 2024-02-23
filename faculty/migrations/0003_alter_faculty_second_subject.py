# Generated by Django 4.2.8 on 2024-02-21 11:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('faculty_fields', '0001_initial'),
        ('faculty', '0002_alter_faculty_first_subject'),
    ]

    operations = [
        migrations.AlterField(
            model_name='faculty',
            name='second_subject',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='second_subject', to='faculty_fields.subject', verbose_name='Second subject'),
        ),
    ]