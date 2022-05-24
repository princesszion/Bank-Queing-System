# from datetime import datetime
from django.db import models


# Create your models here.
class Mybooking(models.Model):
    branch = models.IntegerField()
    service = models.CharField(max_length=100)
    shift = models.IntegerField()
    assignedTeller = models.IntegerField(null=True)
    estimatedTime = models.IntegerField(default=20)

    def __str__(self):
        return self.branch, self.service, self.shift


class Teller(models.Model):
    branchId = models.IntegerField()
    status = models.BooleanField(null=True)


class Shift(models.Model):
    # branchId = models.IntegerField()
    startTime = models.TimeField()
    endTime = models.TimeField()
    duration = models.IntegerField()


class Branch(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)


# # from datetime import datetime
# from django.db import models


# # Create your models here.



# class Teller(models.Model):
#     branchId = models.IntegerField()
#     status = models.BooleanField(null=True)


# class Shift(models.Model):
#     name = models.CharField(max_length=100, null=True, choices=SHIFT)
#     # branchId = models.IntegerField()
#     startTime = models.TimeField()
#     endTime = models.TimeField()
#     duration = models.IntegerField()

#     def __str__(self):
#         return self.name or ''


# class Branch(models.Model):
#     name = models.CharField(max_length=100, null = True, choices=BRANCH)
#     location = models.CharField(max_length=100)

#     def __str__(self):
#         return self.name

# class Mybooking(models.Model):
#     # branch = models.IntegerField()
#     branch = models.ForeignKey(
#         Branch, on_delete=models.SET_NULL, null=True, blank=True)
#     service = models.CharField(max_length=100, null = True, choices=SERVICES)
#     # shift = models.IntegerField()
#     shift = models.ForeignKey(
#         Shift, on_delete=models.SET_NULL, null=True, blank=True)

#     assignedTeller = models.IntegerField(null=True, blank=True)
#     estimatedTime = models.IntegerField(default=20)

#     def __str__(self):
#         return self.branch, self.service, self.shift

