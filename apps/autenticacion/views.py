from django.shortcuts import redirect, render
from django.core.mail import send_mail 
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from apps.usuarios.models import Usuario
from django.db.models import Q
from django.conf import settings # Import necesario para acceder a EMAIL_HOST_USER

# Create your views here.


def login_view(request):
    if request.method == 'GET':
        return render(request, 'autenticacion/login.html', {
            'error': None
        })
    else:
        user = authenticate(
            request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'autenticacion/login.html', {
                'error': 'Usuario o contraseña incorrectos'
            })
        else:
            login(request, user)
            return redirect('inicio')


def logout_view(request):
    logout(request)
    return redirect('login')


def password_reset_request(request):
    """Maneja la solicitud de recuperación de contraseña, buscando el email en la DB."""
    
    context = {}
    
    if request.method == 'POST':
        user_email = request.POST.get('email', '').strip().lower()
        
        if not user_email:
            context['error'] = "Por favor, ingresa un correo electrónico."
            return render(request, 'autenticacion/password_reset_form.html', context)
        
        # 1. BÚSQUEDA EN LA BASE DE DATOS (Interacción con la DB)
        try:
            # Buscamos el usuario por el campo 'email' en el modelo User
            user = User.objects.get(email=user_email) 
            
            # --- Criterio 1: Usuario Encontrado (Éxito) ---
            
            # 2. ENVÍO DE CORREO REAL
            send_mail(
                subject='Recuperación de Contraseña - FETM',
                # NOTA: Este mensaje NO es un enlace real de Django, es un placeholder.
                message=f'Hola {user.first_name}, hemos recibido una solicitud para restablecer tu contraseña. Haz clic en el siguiente enlace simulado para continuar: http://127.0.0.1:8000/autenticacion/password/done/',
                # ✅ Remitente seguro leído desde settings (EMAIL_HOST_USER)
                from_email=settings.EMAIL_HOST_USER, 
                recipient_list=[user_email],
                fail_silently=False, 
            )
            
            # Criterio de Aceptación: Mostrar mensaje de éxito en la interfaz
            context['message'] = "Su contraseña generada ha sido enviada al email ingresado."
            
        except User.DoesNotExist:
            # --- Criterio 2: Usuario No Encontrado (Fallo) ---
            
            # Criterio de Aceptación: Mostrar mensaje de error en la interfaz
            context['error'] = "El correo electrónico ingresado no se encuentra registrado."
            
        return render(request, 'autenticacion/password_reset_form.html', context)
    
    return render(request, 'autenticacion/password_reset_form.html', context)


def password_reset_confirm(request):
    """Simula la interfaz a la que llega el usuario para ingresar la clave temporal/nueva."""
    return render(request, 'autenticacion/password_reset_confirm.html', {})