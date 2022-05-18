from django.urls import path

from core.views.clients_view import ClientsView, ClientRequestView
from core.views.goods_view import GoodsView
from core.views.login_view import LoginUserView, logout_user
from core.views.main_view import MainView
from core.views.partners_view import PartnersView, PartnerRequestView
from core.views.user_view import UserView

urlpatterns = [
    path('', MainView.as_view(), name='home'),
    path('profile/', UserView.as_view(), name='profile'),
    path('login/', LoginUserView.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
    path('clients/', ClientsView.as_view(), name='clients'),
    path('partners/', PartnersView.as_view(), name='partners'),
    path('client-request/', ClientRequestView.as_view(), name='client-request'),
    path('partner-request/', PartnerRequestView.as_view(), name='partner-request'),
    path('food/', GoodsView.as_view(), name='food')
]
