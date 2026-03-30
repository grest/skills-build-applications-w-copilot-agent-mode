from django.test import TestCase
from .models import User, Team, Activity, Workout, Leaderboard

class BasicModelTests(TestCase):
    def setUp(self):
        self.team = Team.objects.create(name='Marvel', description='Marvel superheroes')
        self.user = User.objects.create(name='Spider-Man', email='spiderman@marvel.com', team=self.team, is_superhero=True)
        self.workout = Workout.objects.create(name='Web Swing', description='Swinging through the city')
        self.activity = Activity.objects.create(user=self.user, activity_type='Swing', duration_minutes=30, date='2026-03-30')
        self.leaderboard = Leaderboard.objects.create(team=self.team, total_points=100)

    def test_user_team(self):
        self.assertEqual(self.user.team.name, 'Marvel')

    def test_leaderboard_points(self):
        self.assertEqual(self.leaderboard.total_points, 100)

    def test_activity(self):
        self.assertEqual(self.activity.activity_type, 'Swing')

    def test_workout(self):
        self.assertEqual(self.workout.name, 'Web Swing')
