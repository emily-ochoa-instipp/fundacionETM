from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from apps.usuarios.models import Usuario
from django.contrib.auth.models import User, Group
from django.db.models import Q

from django.contrib import messages

# Create your views here.

@login_required
def tabla_usuarios(request):
    usuarios = Usuario.objects.all()
    return render(request, 'usuarios/tabla_usuarios.html', {
        'usuarios': usuarios
    })

def registrar_usuario(request):
    if request.method == 'POST':
            first_name_ = request.POST.get('txtNombres')
            last_name_ = request.POST.get('txtApellidos')
            email_ = request.POST.get('txtEmail')
            num_doc_ = request.POST.get('txtNumDoc')
            username_ = request.POST.get('txtUsername')
            password_ = request.POST.get('txtPassword')
            rol_ = request.POST.get('txtRol')
            telefono_ = request.POST.get('txtTelefono')

            # Verificar duplicados
            users = User.objects.filter(Q(username__iexact=username_) | Q(email__iexact=email_))
            usuarios = Usuario.objects.filter(Q(num_doc__iexact=num_doc_))

            if users.exists() or usuarios.exists():
                return render(request, 'usuarios/tabla_usuarios.html', {
                    'error': 'Ya existe un usuario con ese nombre de usuario, email o cédula',
                })

            # Crear el usuario base
            userCreate = User.objects.create_user(
                first_name=first_name_,
                last_name=last_name_,
                email=email_,
                username=username_,
                password=password_
            )

            userCreate.is_active = True   # Activo por defecto
            userCreate.save()

            #perfil Usuario se crea automáticamente por signals.py
            usuario = userCreate.usuario
            usuario.rol = rol_
            usuario.telefono = telefono_
            usuario.num_doc = num_doc_
            usuario.save()

            return redirect('tabla_usuarios')
    
    return render(request, 'usuarios/tabla_usuarios.html')

@login_required
def editar_usuario(request, usuario_id):
    usuario = get_object_or_404(Usuario, id=usuario_id)
    if request.method == 'POST':
        user = usuario.user
        usuario.user.first_name = request.POST.get('txtNombres')
        usuario.user.last_name = request.POST.get('txtApellidos')
        usuario.user.email = request.POST.get('txtEmail')
        usuario.user.username = request.POST.get('txtUsername')
        if 'estado' in request.POST:
            user.is_active = True
        else:
            user.is_active = False

        # password = request.POST.get('txtPassword')
        # if password:
        #     usuario.user.set_password(password)

        usuario.rol = request.POST.get('txtRol')
        usuario.num_doc = request.POST.get('txtNumDoc')
        usuario.telefono = request.POST.get('txtTelefono')

        usuario.user.save()
        usuario.save()
        
        return redirect('tabla_usuarios')
    return render(request, 'usuarios/editar_usuario.html', {'usuario': usuario})

@login_required
def eliminar_usuario(request, usuario_id):
    usuario = get_object_or_404(Usuario, id=usuario_id)
    user = usuario.user
    user.delete()
    return redirect('tabla_usuarios')

@login_required
def profile(request):
    usuario = Usuario.objects.get(user=request.user)
    if request.method == 'POST':
        # actualizar campos user
        user = request.user
        user.first_name = request.POST.get('txtNombres')
        user.last_name = request.POST.get('txtApellidos')
        user.email = request.POST.get('txtEmail')
        user.save()

        # actualizar usuario
        usuario.telefono = request.POST.get('txtTelefono')
        usuario.num_doc = request.POST.get('txtNumDoc')

        if 'foto' in request.FILES:
            usuario.foto = request.FILES['foto']

        usuario.save()
        messages.success(request, 'Los datos del perfil se actualizaron correctamente.')
        return redirect('profile')
    return render(request, 'usuarios/profile.html', {'usuario': usuario})
