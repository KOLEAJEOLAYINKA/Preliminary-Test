from django.urls import path
from bincom_test import views

urlpatterns = [
    path('', views.indexView, name='index'),
    path('polling-unit-result/$', views.puResultsView,  name='unit-results'),
	path('results/polling-unit-summary/$', views.lgaSummaryView,  name='unit-summary'),
	path('lga-summary/$', views.addNewScoreView,  name='add-new-result'),
]
