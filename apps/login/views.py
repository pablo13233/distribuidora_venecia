from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import login as auth_login,logout,authenticate #Atenticacion Django

# Create your views here.

#Vista para el login con sus validaciones
def login(request):
	mensaje = ''
	if request.method == 'POST':
		username = request.POST.get('username')
		contrasenia = request.POST.get('pass')
		user = authenticate(username=username,password=contrasenia)
		#Consulta si el usuario tiene una cuenta 
		if user is not None:
			
			if user.is_active:#Si el usuario esta activo
				auth_login(request,user)
				#return render(request,'dashboard/dashboard_index.html')
				return redirect('home:dashboard_index')
			else:
				mensaje = 'USUARIO INACTIVO'
				ctx = {'mensaje':mensaje}
				return render(request,'login/login.html',ctx)
		else:
			mensaje = 'USUARIO O CONTRASEÑA INCORRECTO'
			ctx = {'mensaje':mensaje,'username':username}
			return render(request,'login/login.html',ctx)


	return render(request,'login/login.html')




#vista para cerrar sesion
def cerrar_sesion(request):
	logout(request)
	return redirect('login:login')
