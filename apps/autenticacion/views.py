from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.core.cache import cache

# Create your views here.

def login_view(request):
    if request.method == 'GET':
        return render(request, 'autenticacion/login.html', {'error': ''})
    
    else:
        username = request.POST['username'].strip().lower()
        password = request.POST['password']

        cache_key = f"login_attempts_{username}"
        blocked_key = f"login_blocked_{username}"

        attempts = cache.get(cache_key, 0)
        is_blocked = cache.get(blocked_key, False)

        if is_blocked:
            return render(request, 'autenticacion/login.html', {
                'error': 'Demasiados intentos. Intente nuevamente en 5 minutos.'
            })

        user = authenticate(request, username=username, password=password)

        if user is None:
            attempts += 1
            cache.set(cache_key, attempts, timeout=300)  # persiste 5 min

            if attempts >= 3:
                cache.set(blocked_key, True, timeout=300)  # bloquea 5 min
                cache.delete(cache_key)  # reinicia el contador
                return render(request, 'autenticacion/login.html', {
                    'error': 'Demasiados intentos. Intente nuevamente en 5 minutos.'
                })

            return render(request, 'autenticacion/login.html', {
                'error': f'Usuario o contraseña incorrecta. Intento {attempts}/3'
            })

        else:
            login(request, user)
            cache.delete(cache_key)  # resetea intentos al loguearse
            return render(request, 'inicio/index.html')











    #if request.method == 'GET':
        #return render(request, 'autenticacion/login.html', {
         #   'error':''
       # })
    #else:
       # print (request.POST)
        #user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
       # print (user)
        #if user is None:
           # return render (request, 'autenticacion/login.html', {
             #   'error':'Usuario o contraseña incorrecta'
              #  })
       # else:
            #login(request, user)
           # return render (request, 'inicio/index.html')

def logout_view(request):
    logout(request)
    return redirect('login')
            
