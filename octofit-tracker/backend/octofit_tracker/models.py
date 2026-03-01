from djongo import models
from bson import ObjectId

class Team(models.Model):
    _id = models.ObjectIdField(primary_key=True, default=ObjectId, editable=False)
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)
    def __str__(self):
        return self.name

class User(models.Model):
    _id = models.ObjectIdField(primary_key=True, default=ObjectId, editable=False)
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=100)
    team = models.CharField(max_length=100)
    is_superhero = models.BooleanField(default=False)
    def __str__(self):
        return self.email

class Workout(models.Model):
    _id = models.ObjectIdField(primary_key=True, default=ObjectId, editable=False)
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    difficulty = models.CharField(max_length=50)
    def __str__(self):
        return self.name

class Activity(models.Model):
    _id = models.ObjectIdField(primary_key=True, default=ObjectId, editable=False)
    user_id = models.CharField(max_length=100)  # Store User's ObjectId as string
    type = models.CharField(max_length=100)
    duration = models.IntegerField()  # in minutes
    date = models.DateField()
    def __str__(self):
        return f"{self.user_id} - {self.type}"

class Leaderboard(models.Model):
    _id = models.ObjectIdField(primary_key=True, default=ObjectId, editable=False)
    user_id = models.CharField(max_length=100)  # Store User's ObjectId as string
    score = models.IntegerField()
    rank = models.IntegerField()
    def __str__(self):
        return f"{self.user_id} - {self.rank}"