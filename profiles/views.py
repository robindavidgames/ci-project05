from django.shortcuts import render

# Modified from Boutique Ado sample project

def profile(request):
    """ Display the user's profile. """

    template = 'profiles/profile.html'
    context = {}

    return render(request, template, context)
