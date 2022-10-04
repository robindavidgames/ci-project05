from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.conf import settings

from .forms import OrderForm
from .models import OrderLineItem
from bag.contexts import bag_contents
from products.models import Product

import stripe


# Modified from Boutique Ado sample project
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
            order = order_form.save()
            for item_id, item_data in bag.items():
                try:
                    product = Product.objects.get(id=item_id)

                    if product.has_variants:
                        order_line_item = OrderLineItem(
                            order=order,
                            product=product,
                            quantity=item_data,
                            variant=product_variant,
                        )
                        order_line_item.save()
                    else:
                        order_line_item = OrderLineItem(
                            order=order,
                            product=product,
                            quantity=item_data,
                        )
                        order_line_item.save()

                    # If integer, then doesn't have variants.
                    # if isinstance(item_data, int):
                    #     order_line_item = OrderLineItem(
                    #         order=order,
                    #         product=product,
                    #         quantity=item_data,
                    #     )
                    #     order_line_item.save()
                    # else:
                    #     for size, quantity in item_data['items_by_size'].items():
                    #         order_line_item = OrderLineItem(
                    #             order=order,
                    #             product=product,
                    #             quantity=quantity,
                    #             product_size=size,
                    #         )
                    #         order_line_item.save()

                except Product.DoesNotExist:
                    messages.error(request, (
                        "One of the products in your bag wasn't found in our database. "
                        "Please call us for assistance!")
                    )
                    order.delete()
                    return redirect(reverse('view_bag'))

            # If the user wants to save their info, redirect them to a new page.
            request.session['save_info'] = 'save-info' in request.POST
            return redirect(reverse('checkout_success', args=[order.order_number]))
        else:
            messages.error(request, 'There was an error with your form. \
                Please double check your information.')
    
    else:
        bag = request.session.get('bag', {})
        # To prevent a user typing the checkout URL.
        if not bag:
            messages.error(request, "There's nothing in your bag at the moment")
            return redirect(reverse('products'))

        current_bag = bag_contents(request)
        total = current_bag['grand_total']
        stripe_total = round(total * 100)
        stripe.api_key = stripe_secret_key
        intent = stripe.PaymentIntent.create(
            amount=stripe_total,
            currency=settings.STRIPE_CURRENCY,
        )

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
