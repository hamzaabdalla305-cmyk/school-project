from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from schools import views as school_views  # استيراد دوال الواجهات

urlpatterns = [
    # --- واجهات المستخدم (UI) ---
    path('', school_views.student_list, name='student_list'),
    path('login/', school_views.login_view, name='login'),
    path('logout/', school_views.logout_view, name='logout'),
    path('students/add/', school_views.student_create, name='student_create'),
    path('students/<int:pk>/edit/', school_views.student_update, name='student_update'),
    path('students/<int:pk>/delete/', school_views.student_delete, name='student_delete'),
    path('signup/', school_views.signup_view, name='signup'),
    # --- لوحة الإدارة ---
    path('admin/', admin.site.urls),

    # --- واجهات API (REST) ---
    path('api/', include('schools.urls')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]