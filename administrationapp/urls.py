from django.urls import path, include
from . import views
urlpatterns=[
    path('', views.projecthomepage2, name='projecthomepage2'),
    path('UserRegisterPageCall/', views.UserRegisterPageCall, name='UserRegisterPageCall'),
    path('UserRegisterLogic/', views.UserRegisterLogic, name='UserRegisterLogic'),
    path('UserLoginPageCall/', views.UserLoginPageCall, name='UserLoginPageCall'),
    path('UserLoginLogic/', views.UserLoginLogic, name='UserLoginLogic'),
    path('logout/', views.logout, name='logout'),
    path('add_patient', views.add_patient, name='add_patient'),
    path('patient_list', views.patient_list, name='patient_list'),
    path('patient_list2', views.patient_list2, name='patient_list2'),
    path('patients/delete/<int:id>/', views.delete_patient, name='delete_patient'),
    path('appointment/', views.appointment, name='appointment'),
    path('FAQs/',views.FAQs,name='FAQs'),
    path('medicine/',views.medicine,name='medicine'),
    path('doctor/',views.doctor,name='doctor'),
    path('medicine_avail/',views.medicine_avail,name='medicine_avail'),
    path('book_appointment/', views.book_appointment, name='book_appointment'),
    path('chatbot_view/', views.chatbot_view, name='chatbot_view'),
]