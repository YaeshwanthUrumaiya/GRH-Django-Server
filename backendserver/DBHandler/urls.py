from django.urls import path
from DBHandler.views import AddData, GetData, DBTest, GetUserData

urlpatterns = [
    path('db-test/', DBTest, name='db_test'),
    path('add-data/', AddData, name='add_data'),
    path('get-data/', GetData, name='get_data'),
    path('get-user-data/', GetUserData, name='get_user_data')
]
