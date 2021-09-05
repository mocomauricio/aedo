from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import SignupForm
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .tokens import account_activation_token

from django.contrib.auth.models import Group
from django.contrib.auth import get_user_model


from django.core.mail import EmailMessage

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView

from django.utils import timezone

from apps.aedo.models import Delivery, UserCompany

User = get_user_model()

@method_decorator(login_required, name='dispatch')
class IndexView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        if self.request.user.groups.filter(name='Gestores'):
            context['pending_deliveries'] = Delivery.objects.filter(employee=self.request.user).exclude(state=3).order_by('-id')

        elif self.request.user.groups.filter(name='Clientes'):
            context['pending_deliveries'] = Delivery.objects.filter(company__in=[i.company for i in UserCompany.objects.filter(user=self.request.user)]).exclude(state=3).order_by('-id')
        
        return context

@method_decorator(login_required, name='dispatch')
class CalendarView(TemplateView):
    template_name = "calendar.html"

@method_decorator(login_required, name='dispatch')
class PriceView(TemplateView):
    template_name = "price.html"

@method_decorator(login_required, name='dispatch')
class DeliveryView(TemplateView):
    template_name = "delivery_list.html"

"""
def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            current_site = get_current_site(request)
            mail_subject = 'Activacion de cuenta.'
            message = render_to_string('registro/acc_active_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid':urlsafe_base64_encode(force_bytes(user.pk)),
                #'uid':urlsafe_base64_encode(force_bytes(user.pk)).decode(),
                'token':account_activation_token.make_token(user),
            })
            to_email = form.cleaned_data.get('email')
            email = EmailMessage(
                        mail_subject, message, to=[to_email]
            )
            email.send()
            return HttpResponse('Por favor revise su correo electronico para confirmar el registro')
    else:
        form = SignupForm()
    return render(request, 'registro/signup.html', {'form': form})
"""

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            #login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            group = Group.objects.get(name='Clientes') 
            group.user_set.add(user)

            return redirect('index')
    else:
        form = SignupForm()
    return render(request, 'registro/signup.html', {'form': form})

def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)
        return redirect('/')
        #return HttpResponse('Thank you for your email confirmation. Now you can login your account.')
    else:
        return HttpResponse('Enlace de activacion invalido!')

