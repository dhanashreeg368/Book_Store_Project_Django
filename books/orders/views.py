import stripe
from django.views.generic.base import TemplateView
from django.conf import settings
from django.shortcuts import render
from django.contrib.auth.models import Permission

stripe.api_key = settings.STRIPE_TEST_SECRET_KEY


class OrdersPageView(TemplateView):
    template_name = 'orders/purchase.html'

    # return public key in html page
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['stripe_key'] = settings.STRIPE_TEST_PUBLISHABLE_KEY
        return context


# Function based views
def charge(request):
    #Giving access this user to custom permission to see books list
    permission = Permission.objects.get(codename='special_status')
    #get user
    u = request.user
    #add to users permission set
    u.user_permissions.add(permission)


    if request.method == 'POST':
        charge = str
        charge = stripe.Charge.create(
             amount=39000,
            currency='usd',
            description='Purchase all books',
            source=request.POST['stripeToken']
        )
    return render(request, 'orders/charge.html')
