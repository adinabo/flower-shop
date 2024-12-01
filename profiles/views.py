from django.shortcuts import render, get_object_or_404, redirect
from .forms import UserProfileForm 
from .models import UserProfile
from django.contrib.auth.decorators import login_required

@login_required
def profile(request):
    """ Display the user's profile. """
    # Try to get the user's profile, and redirect to a profile creation view if not found
    try:
        profile = UserProfile.objects.get(user=request.user)
    except UserProfile.DoesNotExist:
        return redirect('create_profile')  # Ensure you have a create_profile view for profile creation

    template = 'profiles/profile.html'
    context = {
        'profile': profile,
    }

    return render(request, template, context)


def create_profile(request):
    """
    Create a user profile if it does not exist.
    """
    if request.method == 'POST':
        form = UserProfileForm(request.POST)
        if form.is_valid():
            user_profile = form.save(commit=False)
            user_profile.user = request.user  # Associate the profile with the logged-in user
            user_profile.save()
            return redirect('profile')  # Redirect to the profile page after saving
    else:
        form = UserProfileForm()

    return render(request, 'profiles/create_profile.html', {'form': form})
    """
    Create a user profile if it does not exist.
    """
    if request.method == 'POST':
        form = UserProfileForm(request.POST)
        if form.is_valid():
            user_profile = form.save(commit=False)
            user_profile.user = request.user  # Associate the profile with the logged-in user
            user_profile.save()
            return redirect('profile')  # Redirect to the profile page after saving
    else:
        form = UserProfileForm()

    return render(request, 'profiles/create_profile.html', {'form': form})
    if request.method == 'POST':
        form = UserProfileForm(request.POST)
        if form.is_valid():
            user_profile = form.save(commit=False)
            user_profile.user = request.user
            user_profile.save()
            return redirect('profile')  # Redirect to the profile page after creation
    else:
        form = UserProfileForm()

    return render(request, 'profiles/create_profile.html', {'form': form})