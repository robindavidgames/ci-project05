import json

from django.shortcuts import (
    render, redirect, reverse,
    get_object_or_404, HttpResponse
    )
from django.views.decorators.http import require_POST
from django.contrib import messages
from django.conf import settings

import stripe

from products.models import Product
from profiles.forms import UserProfileForm
from profiles.models import UserProfile
from bag.contexts import bag_contents

from .forms import OrderForm
from .models import Order, OrderLineItem


# Modified from Boutique Ado sample project
@require_POST
def cache_checkout_data(request):
    try:
        pid = request.POST.get('client_secret').split('_secret')[0]
        stripe.api_key = settings.STRIPE_SECRET_KEY
        stripe.PaymentIntent.modify(pid, metadata={
            'bag': json.dumps(request.session.get('bag', {})),
            'save_info': request.POST.get('save_info'),
            'username': request.user,
        })
        return HttpResponse(status=200)
    except Exception as e:
        messages.error(request, 'Sorry, your payment cannot be \
            processed right now. Please try again later.')
        return HttpResponse(content=e, status=400)


def checkout(request):
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    if request.method == 'POST':
        bag = request.session.get('bag', {})

        form_data = {
            'full_name': request.POST['full_name'],
            'email': request.POST['email'],
            'phone': request.POST['phone'],
            'country': request.POST['country'],
            'postcode': request.POST['postcode'],
            'town_city': request.POST['town_city'],
            'street_address_1': request.POST['street_address_1'],
            'street_address_2': request.POST['street_address_2'],
            'county': request.POST['county'],
        }

        order_form = OrderForm(form_data)
        if order_form.is_valid():
            # order = order_form.save()
            order = order_form.save(commit=False)
            pid = request.POST.get('client_secret').split('_secret')[0]
            order.stripe_pid = pid
            order.original_bag = json.dumps(bag)
            order.save()

            for item_id, item_data in bag.items():
                try:
                    product = Product.objects.get(id=item_id)

                    # If integer, then doesn't have variants.
                    if isinstance(item_data, int):
                        order_line_item = OrderLineItem(
                            order=order,
                            product=product,
                            order_quantity=item_data,
                        )
                        order_line_item.save()

                    else:
                        for variant, quantity in item_data[
                            'items_by_variant'
                        ].items():
                            order_line_item = OrderLineItem(
                                order=order,
                                product=product,
                                order_quantity=quantity,
                                product_variant=variant,
                            )
                            order_line_item.save()

                except Product.DoesNotExist:
                    messages.error(request, (
                        "One of the products in your bag wasn't found. "
                        "Please call us for assistance!")
                    )
                    order.delete()
                    return redirect(reverse('view_bag'))

            # If the user wants to save their info,
            # redirect them to a new page.
            request.session['save_info'] = 'save-info' in request.POST
            return redirect(reverse(
                'checkout_success',
                args=[order.order_number]
                ))
        else:
            messages.error(request, 'There was an error with your form. \
                Please double check your information.')

    else:
        bag = request.session.get('bag', {})
        # To prevent a user typing the checkout URL.
        if not bag:
            messages.error(
                request,
                "There's nothing in your bag at the moment")
            return redirect(reverse('products'))

        current_bag = bag_contents(request)
        total = current_bag['grand_total']
        stripe_total = round(total * 100)
        stripe.api_key = stripe_secret_key
        intent = stripe.PaymentIntent.create(
            amount=stripe_total,
            currency=settings.STRIPE_CURRENCY,
        )

        # Prefill form with user info.
        if request.user.is_authenticated:
            try:
                profile = UserProfile.objects.get(user=request.user)
                order_form = OrderForm(initial={
                    'full_name': profile.user.get_full_name(),
                    'email': profile.user.email,
                    'phone': profile.default_phone,
                    'country': profile.default_country,
                    'postcode': profile.default_postcode,
                    'town_city': profile.default_town_city,
                    'street_address_1': profile.default_street_address_1,
                    'street_address_2': profile.default_street_address_2,
                    'county': profile.default_county,
                })
            except UserProfile.DoesNotExist:
                order_form = OrderForm()
        else:
            order_form = OrderForm()

    if not stripe_public_key:
        messages.warning(request, 'Stripe public key is missing.')

    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
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

        # Iterate through the chosen products to reduce stock quantity.
        lineitems = order.lineitems.all()
        for item in lineitems:
            # For variant products
            if item.product.has_variants:
                current_variant = item.product_variant
                if item.product.variant_one == current_variant:
                    item.product.variant_one_stock_quantity -= (
                        item.order_quantity)
                elif item.product.variant_two == current_variant:
                    item.product.variant_two_stock_quantity -= (
                        item.order_quantity)
                elif item.product.variant_three == current_variant:
                    item.product.variant_three_stock_quantity -= (
                        item.order_quantity)
                item.product.save()
            # For non-variant products.
            else:
                item.product.stock_quantity -= item.order_quantity
                item.product.save()

        # Save the user's info
        if save_info:
            profile_data = {
                'default_phone': order.phone,
                'default_country': order.country,
                'default_postcode': order.postcode,
                'default_town_city': order.town_city,
                'default_street_address_1': order.street_address_1,
                'default_street_address_2': order.street_address_2,
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
