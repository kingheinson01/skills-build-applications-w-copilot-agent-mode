from django.test import TestCase
from .models import User, Team, Activity, Workout, Leaderboard

class ModelTests(TestCase):
    def setUp(self):
        self.team = Team.objects.create(name='Marvel', description='Marvel superheroes')
        self.user = User.objects.create(email='tony@stark.com', name='Tony Stark', team='Marvel', is_superhero=True)
        self.workout = Workout.objects.create(name='Pushups', description='Upper body', difficulty='Easy')
        self.activity = Activity.objects.create(user=self.user, type='Running', duration=30, date='2023-01-01')
        self.leaderboard = Leaderboard.objects.create(user=self.user, score=100, rank=1)

    def test_user(self):
        self.assertEqual(self.user.email, 'tony@stark.com')

    def test_team(self):
        self.assertEqual(self.team.name, 'Marvel')

    def test_workout(self):
        self.assertEqual(self.workout.name, 'Pushups')

    def test_activity(self):
        self.assertEqual(self.activity.type, 'Running')

    def test_leaderboard(self):
        self.assertEqual(self.leaderboard.rank, 1)
