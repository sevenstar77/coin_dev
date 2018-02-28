from django.conf.urls import url, include


urlpatterns = [
    url(r'^account/', include('account.urls', namespace='account')),
    url(r'^order/', include('order.urls', namespace='order')),
    url(r'^schedules/', include('schedules.urls', namespace='schedules')),
    url(r'^users/', include('users.urls', namespace='users'))

    #url(r'^transaction/', include('transaction.urls', namespace='transaction')),
    #url(r'^public/', include('public.urls', namespace='public')),
]