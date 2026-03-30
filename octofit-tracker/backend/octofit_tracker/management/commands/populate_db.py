from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Workout, Leaderboard
from django.utils import timezone

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Clear existing data
        Activity.objects.all().delete()
        Workout.objects.all().delete()
        Leaderboard.objects.all().delete()
        User.objects.all().delete()
        Team.objects.all().delete()

        # Create Teams
        marvel = Team.objects.create(name='Marvel', description='Marvel superheroes')
        dc = Team.objects.create(name='DC', description='DC superheroes')

        # Create Users
        users = [
            User.objects.create(name='Spider-Man', email='spiderman@marvel.com', team=marvel, is_superhero=True),
            User.objects.create(name='Iron Man', email='ironman@marvel.com', team=marvel, is_superhero=True),
            User.objects.create(name='Wonder Woman', email='wonderwoman@dc.com', team=dc, is_superhero=True),
            User.objects.create(name='Batman', email='batman@dc.com', team=dc, is_superhero=True),
        ]

        # Create Workouts
        workout1 = Workout.objects.create(name='Web Swing', description='Swinging through the city')
        workout2 = Workout.objects.create(name='Flight', description='Flying workout')
        workout1.suggested_for.set([users[0]])
        workout2.suggested_for.set([users[1], users[2]])

        # Create Activities
        Activity.objects.create(user=users[0], activity_type='Swing', duration_minutes=30, date=timezone.now().date())
        Activity.objects.create(user=users[1], activity_type='Fly', duration_minutes=45, date=timezone.now().date())
        Activity.objects.create(user=users[2], activity_type='Fight', duration_minutes=60, date=timezone.now().date())
        Activity.objects.create(user=users[3], activity_type='Detective Work', duration_minutes=90, date=timezone.now().date())

        # Create Leaderboards
        Leaderboard.objects.create(team=marvel, total_points=150)
        Leaderboard.objects.create(team=dc, total_points=200)

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data.'))
