from __future__ import unicode_literals

from django.db import models

from django.db import models


class credentials(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    department = models.CharField(max_length=50)
    hostel = models.CharField(max_length=50)

    def __str__(self):
        return self.username


class checkbox(models.Model):
    name = models.ForeignKey(credentials, on_delete=models.CASCADE)
    caretaker = models.IntegerField(default=0)
    warden = models.IntegerField(default=0)
    gym_vp = models.IntegerField(default=0)
    asst_reg = models.IntegerField(default=0)
    sub_thesis = models.IntegerField(default=0)
    librarian = models.IntegerField(default=0)
    online_cc = models.IntegerField(default=0)
    cc_in = models.IntegerField(default=0)
    faculty = models.IntegerField(default=0)
    dept_workshop = models.IntegerField(default=0)
    hod = models.IntegerField(default=0)
    accounts_head = models.IntegerField(default=0)

    def __str__(self):
        return self.name.username



# Create your models here.
