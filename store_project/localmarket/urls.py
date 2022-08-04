from django.urls import path
from . import views

app_name = "localmarket"

urlpatterns = [
    path("add/", views.add_market, name="add_market"),
    path("all/", views.get_markets, name="all_markets"),
    path("update/<market_id>", views.update_market, name="update_market"),
    path("delete/<market_id>", views.delete_market, name="delete_market"),
]