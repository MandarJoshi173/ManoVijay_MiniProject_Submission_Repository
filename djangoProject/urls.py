"""
URL configuration for djangoProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from django.contrib import admin
from django.urls import path
from manovijay import views

urlpatterns = [
    #    path('admin/', admin.site.urls),
    path('', views.loadWelcomePage, name="WelcomePage"),
    path('LoginPageLink', views.loadLoginPage),
    path('LogoutLink', views.loadLogoutActionCode),
    path('SignupLink', views.loadSignupPage),
    path('SignupCodeAction',  views.loadSignupActionCode),
    path('LoginCodeAction', views.loadLoginActionCode),
    path('UserProfileLink', views.loadUserProfilePage),
    path('UserViewLink', views.loadUserViewsPage),
    path('UserViewsBlogLink',views.loadUserViewsBlogLink),
    path('UserViewsPomodoroLink', views.loadUserViewsPomodoroLink),
    path('UserUpdateProfileLink', views.loadUserUpdateProfilePage),
    path('UserDeleteProfileLink', views.loadUserDeleteProfilePage),
    path('UpdateUserProfileActionCode', views.loadUpdateUserProfileActionCode),
    path('UserProfileDeletionRequestActionCode', views.loadUserProfileDeletionReqActionCode),
    path('FeedbackLink', views.loadFeedbackPage),
    path('NotificationsLink', views.loadNotificationsPage),
    path('UserAppointmentLink', views.loadAppointmentPage),
    path('BookAppointmentActionCode', views.loadBookAppointmentActionCode,name="BookAppointmentActionCode"),
    path('FeedbackActionCode', views.loadTherapistFeedbackActionCode,name="FeedbackActionCode"),
    path('FeedbackActionCode2', views.loadAdminFeedbackActionCode,name="FeedbackActionCode2"),
    path('UserDashboardReturnLink', views.loadUserDashboardReturnActionCode),
    path('UserProfileReturnLink', views.loadUserProfileReturnActionCode),

    #Therapist Dashboard Requests
    path('TherapistLoginPageLink', views.loadTherapistLoginPage),
    path('TherapistSignupLink', views.loadTherapistSignupPage),
    path('TherapistSignupActionCode', views.loadTherapistSignupActionCode),
    path('TherapistLoginActionCode', views.loadTherapistLoginActionCode),
    path('TherapistProfileLink', views.loadTherapistProfilePage),
    path('TherapistBlogsLink', views.loadTherapistBlogLink),
    path('TherapistBlogCreationActionCode',views.loadTherapistBlogCreationActionCode),
    path('TherapistUpdateProfileLink', views.loadTherapistUpdateProfileLink),
    path('UpdateTherapistProfileActionCode', views.loadUpdateTherapistProfileActionCode),
    path('TherapistDeleteProfileLink', views.loadTherapistDeleteProfileLink),
    path('TherapistProfileDeletionRequestActionCode', views.loadTherapistProfileDeletionRequestActionCode),
    path('TherapistFeedbackLink', views.loadTherapistFeedbackLink),
    path('TherapistFeedbackActionCode', views.loadTherapistFeedbackActionCode,name="TherapistFeedbackActionCode"),
    path('TherapistAppointmentLink', views.loadTherapistAppointmentLink),
    path('TherapistAppointmentActionCode', views.loadTherapistAppointmentActionCode),
    path('TherapistNotificationsLink', views.loadTherapistNotificationsLink),
    path('TherapistNotificationsActionCode', views.loadTherapistNotificationsActionCode),
    path('TherapistLogoutLink', views.loadTherapistLogoutActionCode),
    path('TherapistDashboardReturnLink', views.loadTherapistDashboardReturnActionCode),
    path('TherapistProfileReturnLink', views.loadTherapistProfileActionCode),

    #Admin Dashboard Requests
    path('AdminLoginLink', views.loadAdminLoginLink),
    path('AdminLoginActionCode', views.loadAdminLoginActionCode),
    path('AdminLogoutLink', views.loadAdminLogoutLink),
    path('AdminBlogsLink', views.loadAdminBlogsLink),
    path('AdminRequestsLink', views.loadAdminRequestsLink),
    path('AdminUserRequestLink', views.loadAdminUserRequestLink),
    path('AdminTherapistRequestLink', views.loadAdminTherapistRequestLink),
    path('AdminProfilesLink', views.loadAdminProfilesLink),
    path('AdminUserProfileLink', views.loadAdminUserProfilesLink),
    path('AdminUserProfileDeletionActionCode', views.loadAdminUserProfileDeletionActionCode),
    path('AdminTherapistProfileLink', views.loadAdminTherapistProfilesLink),
    path('AdminTherapistProfileDeletionActionCode', views.loadAdminTherapistProfileDeletionActionCode),
    path('AdminNotificationsLink', views.loadAdminNotificationsLink),
    path('AdminNotificationsActionCode', views.loadAdminNotificationsActionCode),
    path('AdminFeedbacksLink', views.loadAdminFeedbacksLink),
    path('AdminFeedbackActionCode', views.loadAdminFeedbackActionCode),
    path('AdminDashboardReturnLink', views.loadAdminDashboardReturnLink),
    path('AdminRequestsReturnLink', views.loadAdminRequestsReturnLink),
    path('AdminProfileReturnLink', views.loadAdminProfileReturnLink),
]
