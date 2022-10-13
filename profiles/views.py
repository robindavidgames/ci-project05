from django.shortcuts import render, get_object_or_404

from .models import UserProfile

# Modified from Boutique Ado sample project

def profile(request):
    """ Display the user's profile. """
    profile = get_object_or_404(UserProfile, user=request.user)

    template = 'profiles/profile.html'
    context = {
        'profile': profile,
    }

    return render(request, template, context)
