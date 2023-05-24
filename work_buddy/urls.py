
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('projects', include('projects.urls')),
    path('', include('users.urls')),

    path('api', include('api.urls')),

    # USER SEND EMAIL FOR RESET
    path('reset_passsword/', auth_views.PasswordResetView.as_view(template_name="reset_password.html"),
         name="reset_password"),
    
    # EMAIL SENT MESSAGE
    path('reset_passsword_sent/', auth_views.PasswordResetDoneView.as_view(template_name="reset_password_sent.html"),
         name="password_reset_done"),
    
    #EMAIL WITH LINK AND RESET INSTRUCTIONS
    path('reset/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(template_name="password_reset_confirm.html"),
         name="password_reset_confirm"),
    
    # PASSWORD SUCCESSFULLY RESET MESSAGE
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name="reset_password_complete.html"),
         name="password_reset_complete"),
    
    
    


]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
