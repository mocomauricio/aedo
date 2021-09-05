from django.urls import path, re_path
from django.contrib.auth import views as auth_views
from .views import IndexView, signup, activate, CalendarView, PriceView, DeliveryView


urlpatterns = [
    # Todo el sistema de autenticación con las vistas genéricas que ya provee Django
    # para más información: https://docs.djangoproject.com/en/3.1/topics/auth/default/
    path('login/', auth_views.LoginView.as_view(template_name='registro/login.html', redirect_authenticated_user=True), name="login"),
    path('logout/', auth_views.LogoutView.as_view(), name="logout"),
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(template_name='registro/password_change_done.html'), name='password_change_done'),
    path('password_change/', auth_views.PasswordChangeView.as_view(template_name='registro/password_change.html'), name='password_change'),
    re_path(r'^reset/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$', auth_views.PasswordResetConfirmView.as_view(template_name='registro/password_reset_confirm.html'), name='password_reset_confirm'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='registro/password_reset_done.html'), name='password_reset_done'),
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='registro/password_reset.html'), name='password_reset'),    
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='registro/password_reset_complete.html'), name='password_reset_complete'),


    re_path(r'^signup/$', signup, name='signup'),
    re_path(r'^activate/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$', activate, name='activate'),

    #templates de ejemplo
    #path('cards/', CardsView.as_view(), name="cards"),
    #path('charts/', ChartsView.as_view(), name="charts"),
    #path('tables/', TablesView.as_view(), name="tables"),
    #path('navbar/', NavbarView.as_view(), name="navbar"),

    # La template del Dashboard 
    path('', IndexView.as_view(), name="index"),

    path('calendar/', CalendarView.as_view(), name="calendar"),
    path('price/', PriceView.as_view(), name="price"),
    path('delivery/', DeliveryView.as_view(), name="delivery"),
]
