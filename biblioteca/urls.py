from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_view, name="autores"),
    path('autor/<int:autor_id>/', views.autor_view, name="autor"),
    path('livro/<int:livro_id>/', views.livro_view, name="livro"),
    path('generos/', views.generos_view, name="generos"),
    path('genero/<str:genero>', views.genero_view, name="genero"),
    path('autor/novo', views.novo_autor_view,name="novo_autor"),
    path('autor/<int:autor_id>/edita', views.edita_autor_view,name="edita_autor"),
    path('autor/<int:autor_id>/apaga', views.apaga_autor_view,name="apaga_autor"),
    path('autor/<int:autor_id>/novo-livro/', views.novo_livro_view,name="novo_livro"),

    path('registo/', views.registo_view, name="registo"),
    path('login/', views.login_view, name="login"),
    path('logout/', views.logout_view, name="logout"),
]
  
from django.contrib.auth import views as auth_views 

urlpatterns += [
#    path('reset_password/', auth_views.PasswordResetView.as_view(), name='reset_password'),
    path('reset_password/', auth_views.PasswordResetView.as_view(template_name='registration/custom_password_reset_form.html'), name='reset_password'),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name='registration/custom_password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='registration/custom_password_reset_confirm.html'), name='password_reset_confirm'),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name='registration/custom_password_reset_complete.html'), name='password_reset_complete'),
]