from django.shortcuts import render, get_object_or_404

from .models import UserProfile
from .forms import UserProfileForm

# Modified from Boutique Ado sample project

def profile(request):
    """ Display the user's profile. """
    profile = get_object_or_404(UserProfile, user=request.user)
    form = UserProfileForm(instance=profile)
    orders = profile.orders.all()

    template = 'profiles/profile.html'
    # Check if profile context is used in template and delete context if not.
    context = {
        'form': form,
        'orders': orders,
        'profile': profile,
    }

    return render(request, template, context)
