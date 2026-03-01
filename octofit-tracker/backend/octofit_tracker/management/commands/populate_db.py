from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Workout, Leaderboard
from django.utils import timezone

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        # Clear existing data
        Leaderboard.objects.all().delete()
        Activity.objects.all().delete()
        Workout.objects.all().delete()
        User.objects.all().delete()
        Team.objects.all().delete()

        # Create Teams
        marvel = Team.objects.create(name='Marvel', description='Marvel superheroes')
        dc = Team.objects.create(name='DC', description='DC superheroes')

        # Create Users

        tony = User.objects.create(email='tony@stark.com', name='Tony Stark', team='Marvel', is_superhero=True)
        steve = User.objects.create(email='steve@rogers.com', name='Steve Rogers', team='Marvel', is_superhero=True)
        bruce = User.objects.create(email='bruce@wayne.com', name='Bruce Wayne', team='DC', is_superhero=True)
        clark = User.objects.create(email='clark@kent.com', name='Clark Kent', team='DC', is_superhero=True)

        # Create Workouts
        pushups = Workout.objects.create(name='Pushups', description='Upper body', difficulty='Easy')
        running = Workout.objects.create(name='Running', description='Cardio', difficulty='Medium')
        swimming = Workout.objects.create(name='Swimming', description='Full body', difficulty='Hard')

        # Create Activities (use user_id as string)
        Activity.objects.create(user_id=str(tony._id), type='Running', duration=30, date=timezone.now().date())
        Activity.objects.create(user_id=str(steve._id), type='Swimming', duration=45, date=timezone.now().date())
        Activity.objects.create(user_id=str(bruce._id), type='Pushups', duration=20, date=timezone.now().date())
        Activity.objects.create(user_id=str(clark._id), type='Running', duration=60, date=timezone.now().date())

        # Create Leaderboard (use user_id as string)
        Leaderboard.objects.create(user_id=str(tony._id), score=120, rank=1)
        Leaderboard.objects.create(user_id=str(steve._id), score=110, rank=2)
        Leaderboard.objects.create(user_id=str(clark._id), score=100, rank=3)
        Leaderboard.objects.create(user_id=str(bruce._id), score=90, rank=4)

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data.'))
