# Generated by Django 3.1.2 on 2020-10-27 03:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Dashboard', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='chatincidencemodel',
            name='incidence',
        ),
        migrations.RemoveField(
            model_name='chatincidencemodel',
            name='user',
        ),
        migrations.RemoveField(
            model_name='economicallymodel',
            name='user',
        ),
        migrations.RemoveField(
            model_name='eventsmodel',
            name='user',
        ),
        migrations.RemoveField(
            model_name='filesmodel',
            name='incidence',
        ),
        migrations.RemoveField(
            model_name='filesmodel',
            name='user',
        ),
        migrations.RemoveField(
            model_name='groupcode',
            name='user',
        ),
        migrations.RemoveField(
            model_name='groupsmodel',
            name='SchoolCycle',
        ),
        migrations.RemoveField(
            model_name='groupsmodel',
            name='user',
        ),
        migrations.RemoveField(
            model_name='incidencemodel',
            name='student',
        ),
        migrations.RemoveField(
            model_name='incidencemodel',
            name='typeEvent',
        ),
        migrations.RemoveField(
            model_name='incidencemodel',
            name='user',
        ),
        migrations.RemoveField(
            model_name='profilemodel',
            name='user',
        ),
        migrations.RemoveField(
            model_name='registermodel',
            name='carrera',
        ),
        migrations.RemoveField(
            model_name='studentmodel',
            name='user',
        ),
        migrations.DeleteModel(
            name='CarreraModel',
        ),
        migrations.DeleteModel(
            name='ChatIncidenceModel',
        ),
        migrations.DeleteModel(
            name='EconomicallyModel',
        ),
        migrations.DeleteModel(
            name='EventsModel',
        ),
        migrations.DeleteModel(
            name='FilesModel',
        ),
        migrations.DeleteModel(
            name='GroupCode',
        ),
        migrations.DeleteModel(
            name='GroupsModel',
        ),
        migrations.DeleteModel(
            name='IncidenceModel',
        ),
        migrations.DeleteModel(
            name='ProfileModel',
        ),
        migrations.DeleteModel(
            name='RegisterModel',
        ),
        migrations.DeleteModel(
            name='SchoolCycleModel',
        ),
        migrations.DeleteModel(
            name='StudentModel',
        ),
    ]
