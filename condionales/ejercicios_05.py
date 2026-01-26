user = 'admin'
password = 'qwerty'

usuario = input('ingresa tu usuario: ')
contra = input('ingresa tu contraseña: ')

if user == usuario and password == contra:
	print('has entrado al sistema')
else:
	print('error de acceso')