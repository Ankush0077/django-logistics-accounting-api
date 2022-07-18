from django.contrib import admin
from django.urls import path, include
from requests import post, request
# from rest_framework_jwt.views import TokenObtainPairView,TokenRefreshView,TokenVerifyView
from rest_framework.routers import DefaultRouter
from khatadata import views as khataviews
from users import views as usersviews

# PartyRouter = DefaultRouter()
# PartyRouter.register('',khataviews.PartyModelViewSet)

# DriverRouter = DefaultRouter()
# DriverRouter.register('',khataviews.DriverModelViewSet)

# SupplierRouter = DefaultRouter()
# SupplierRouter.register('',khataviews.SupplierModelViewSet)

# PartyTransactionRouter = DefaultRouter()
# PartyTransactionRouter.register('',khataviews.PartyTransactionModelViewSet)

# DriverTransactionRouter = DefaultRouter()
# DriverTransactionRouter.register('',khataviews.DriverTransactionModelViewSet)

# SupplierTransactionRouter = DefaultRouter()
# SupplierTransactionRouter.register('',khataviews.SupplierTransactionModelViewSet)

# UserDetailsRouter = DefaultRouter()
# UserDetailsRouter.register('',usersviews.UserDetailsModelViewSet)

action1 = {'get': 'list', 
           'post' : 'create',
           'put' : 'update',
           'patch' : 'partial_update',
           'delete' : 'destroy'}

action2 = {'get': 'retrieve', 
           'post' : 'create',
           'put' : 'update',
           'patch' : 'partial_update',
           'delete' : 'destroy'}

UserRouter = DefaultRouter()
UserDetailsRouter = DefaultRouter()

UserRouter.register('',usersviews.USerReadOnlyModelViewSet,basename='user')
UserDetailsRouter.register('',usersviews.UserDetailsModelViewSet,basename='userdetails')

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('api/khatadata/party/',khataviews.PartyModelViewSet.as_view(action1)),
    path('api/khatadata/party/<str:user_phone_number>/',khataviews.PartyModelViewSet.as_view(action2)),
    path('api/khatadata/supplier/',khataviews.SupplierModelViewSet.as_view(action1)),
    path('api/khatadata/supplier/<str:user_phone_number>/',khataviews.SupplierModelViewSet.as_view(action2)),
    path('api/khatadata/driver/',khataviews.DriverModelViewSet.as_view(action1)),
    path('api/khatadata/driver/<str:user_phone_number>/',khataviews.DriverModelViewSet.as_view(action2)),
    path('api/khatadata/party/party_transaction/',khataviews.PartyTransactionModelViewSet.as_view(action1)),
    path('api/khatadata/party/party_transaction/<str:party_phone_number>/',khataviews.PartyTransactionModelViewSet.as_view(action2)),
    path('api/khatadata/supplier/supplier_transaction/',khataviews.SupplierTransactionModelViewSet.as_view(action1)),
    path('api/khatadata/supplier/supplier_transaction/<str:supplier_phone_number>/',khataviews.SupplierTransactionModelViewSet.as_view(action2)),
    path('api/khatadata/driver/driver_transaction/',khataviews.DriverTransactionModelViewSet.as_view(action1)),
    path('api/khatadata/driver/driver_transaction/<str:driver_phone_number>/',khataviews.DriverTransactionModelViewSet.as_view(action2)),
    path('api/user/',usersviews.OtpAPI),
    path('api/user/otp/',include(UserRouter.urls)),
    path('api/user/userdetails/',include(UserDetailsRouter.urls)),
    # path('api/user/userdetails/',usersviews.UserDetailsModelViewSet.as_view(action1)),
    # path('api/user/userdetails/<str:user_phone_number>/',usersviews.UserDetailsModelViewSet.as_view(action2)),
]