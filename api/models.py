from django.db import models


# Create your models here.
class Boat(models.Model):
    id = models.AutoField(db_column='id', primary_key=True)
    name = models.CharField(db_column='name', max_length=255, null=False)
    boat_class = models.ForeignKey('BoatClass', models.DO_NOTHING,
                                   db_column='boat_class', null=False)
    boat_number = models.IntegerField(db_column='boat_number', null=False)
    tech_inspection = models.BooleanField(db_column='tech_inspection',
                                          default=False)
    max_members = models.IntegerField(db_column='max_members', default=1)

    class Meta:
        db_table = "Boat"


class BoatClass(models.Model):
    id = models.AutoField(db_column='id', primary_key=True)
    name = models.CharField(db_column='name', max_length=255, null=False)

    class Meta:
        db_table = "BoatClass"


class Role(models.Model):
    id = models.AutoField(db_column='id', primary_key=True)
    name = models.CharField(db_column='name', max_length=255, null=False)

    class Meta:
        db_table = "Role"


class Member(models.Model):
    id = models.AutoField(db_column='id', primary_key=True)
    first_name = models.CharField(db_column='first_name', max_length=255,
                                  null=False)
    patronymic = models.CharField(db_column='patronymic', max_length=255,
                                  null=True)
    last_name = models.CharField(db_column='last_name', max_length=255,
                                 null=False)
    email = models.CharField(db_column='email', max_length=255, null=False,
                             unique=True)
    phone_number = models.CharField(db_column='phone_number', max_length=12,
                                    null=False, unique=True)
    passport = models.BinaryField(db_column='passport', null=True)
    take_part_flag = models.BooleanField(db_column='take_part_flag',
                                         default=False)
    swimming_skill = models.BooleanField(db_column='swimming_skill',
                                         default=False)
    role = models.ForeignKey('Role', models.DO_NOTHING, db_column='role',
                             null=False)
    password = models.CharField(db_column='password', max_length=1024,
                                null=False)

    class Meta:
        db_table = "Member"


class Team(models.Model):
    boat = models.ForeignKey('Boat', on_delete=models.CASCADE, db_column='boat',
                             null=False)
    member = models.ForeignKey('Member', models.DO_NOTHING, db_column='member',
                               null=False)

    class Meta:
        db_table = "Team"


class Token(models.Model):
    user = models.ForeignKey('Member', models.CASCADE, db_column='user',
                             primary_key=True, unique=True)  # Field name made lowercase.
    token = models.CharField(db_column='Token', blank=True, null=True, max_length=255)  # Field name made lowercase.
    time = models.DateTimeField(db_column='Time', blank=True, null=True, auto_now=True)  # Field name made lowercase.

    class Meta:
        db_table = "Token"


class Track(models.Model):
    id = models.AutoField(db_column='id', primary_key=True)
    member = models.ForeignKey('Member', models.CASCADE, db_column='member')
    coordinates = models.CharField(db_column='coordinates', max_length=100)

    class Meta:
        db_table = "Track"

