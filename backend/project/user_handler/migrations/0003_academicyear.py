# Generated by Django 4.2.2 on 2023-08-22 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_handler', '0002_rename_credit_course_credit_rename_dept_course_dept_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='AcademicYear',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, unique=True)),
                ('is_odd_semester', models.BooleanField(default=False)),
            ],
        ),
    ]
