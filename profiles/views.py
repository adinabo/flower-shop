from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .forms import UserProfileForm 
from .models import UserProfile
from checkout.models import Order
from django.contrib.auth.decorators import login_required

def profile(request):
    """ Display the user's profile, including order history. """
    profile = UserProfile.objects.get(user=request.user)
    orders = profile.orders.all()  # Related name from the Order model

    context = {
        'profile': profile,
        'orders': orders,
    }
    return render(request, 'profiles/profile.html', context)


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


def order_history(request, order_number):
    """ Display the details of a specific order for a user """
    profile = get_object_or_404(UserProfile, user=request.user)
    order = get_object_or_404(Order, order_number=order_number, user_profile=profile)

    context = {
        'order': order,
        'from_profile': True,  # Flag to show the "Back to Profile" button
    }
    return render(request, 'checkout/checkout_success.html', context)
