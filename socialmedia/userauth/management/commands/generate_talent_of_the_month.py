from django.core.management.base import BaseCommand
from django.utils import timezone
from userauth.models import TalentOfTheMonth, Post

class Command(BaseCommand):
    help = 'Generate Talent of the Month'

    def handle(*args, **kwargs):
        current_month = timezone.now().month
        current_year = timezone.now().year

        # Get the most rated post of the current month
        most_rated_post = Post.objects.filter(
            created_at__year=current_year,
            created_at__month=current_month,
            status="ALLOWED"
        ).order_by('-no_of_likes').first()
        most_rated_post.talent = True
        most_rated_post.update() 
        if most_rated_post:
            # Create or update the Talent of the Month
            talent, created = TalentOfTheMonth.objects.update_or_create(
                month=current_month,
                year=current_year,
                defaults={'user': most_rated_post.user, 'post': most_rated_post}
            )
            print(f"Talent of the Month: {talent.user} for post {talent.post.id}")
        else:
            print("No posts found for the current month.")