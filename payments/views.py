import stripe
from django.conf import settings
from django.http import JsonResponse
from django.views.generic import DetailView, View, TemplateView

from .models import Item


stripe.api_key = settings.STRIPE_SECRET_KEY


class SuccessView(TemplateView):
    template_name = 'payments/success.html'


class CancelView(TemplateView):
    template_name = 'payments/cancel.html'


class ItemView(DetailView):
    '''GET /item/{id}'''
    model = Item
    context_object_name = 'item'
    template_name = 'payments/item-detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['STRIPE_PUBLISHABLE_KEY'] = settings.STRIPE_PUBLISHABLE_KEY
        return context


class BuyView(View):
    '''GET /buy/{id}'''
    def get(self, request, *args, **kwargs):
        item_id = self.kwargs['pk']
        item = Item.objects.get(pk=item_id)
        url = 'http://localhost:8000'
        session = stripe.checkout.Session.create(
            line_items=[{
                'price_data': {
                    'currency': item.currency,
                    'product_data': {
                        'name': item.name,
                    },
                    'unit_amount': item.price * 100, # Цена в центах (например, $10.00)
                },
                'quantity': 1,
            }],
            mode='payment',
            success_url=url + '/success/',
            cancel_url=url + '/cancel/',
        )

        return JsonResponse({'sessionId': session.id})
