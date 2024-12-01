from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .forms import UserProfileForm 
from .models import UserProfile
from django.contrib.auth.decorators import login_required

@login_required
def profile(request):
    """ Display the user's profile. """
    # Get the user's profile or return 404 if not found
    profile = get_object_or_404(UserProfile, user=request.user)

    # Use the template directly
    return render(request, 'profiles/profile.html', {'profile': profile})


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
    order = get_object_or_404(Order, order_number=order_number)

    messages.info(request, (
        f'This is a past confirmation for order number {order_number}. '
        'A confirmation email was sent on the order date.'
    ))

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
        'from_profile': True,
    }

    return render(request, template, context)

def checkout_success(request, order_number):
    """
    Handle successful checkouts
    """
    save_info = request.session.get('save_info')
    order = get_object_or_404(Order, order_number=order_number)

    if request.user.is_authenticated:
        profile = UserProfile.objects.get(user=request.user)
        # Attach the user's profile to the order
        order.user_profile = profile
        order.save()

        # Save the user's info
        if save_info:
            profile_data = {
                'default_phone_number': order.phone_number,
                'default_country': order.country,
                'default_postcode': order.postcode,
                'default_town_or_city': order.town_or_city,
                'default_street_address1': order.street_address1,
                'default_street_address2': order.street_address2,
                'default_county': order.county,
            }
            user_profile_form = UserProfileForm(profile_data, instance=profile)
            if user_profile_form.is_valid():
                user_profile_form.save()

    messages.success(request, f'Order successfully processed! \
        Your order number is {order_number}. A confirmation \
        email will be sent to {order.email}.')

    if 'bag' in request.session:
        del request.session['bag']

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
    }

    return render(request, template, context)