print('----------')
global_var = 'creado: '
salto = """ 
dfsdfsfsdfsdfsdfsdf
sdf
sdfsd
fds
f
sdf
sf
sdf
sd
fsd
"""

def Persona(name):
    return global_var + name

def Vehiculo():
    variable_local = 'Hello'
    return global_var + variable_local

def Restaurante():
    variable_local = '--ss'
    def local():
        nonlocal variable_local
        variable_local = '++ss'

    local()

    return global_var + variable_local

def Aqui(a, b, c='Sad'):
    return a + b + c + salto

def Ope():
    return 12.5 // 2 

print(Persona('carlos'))
print(Vehiculo())
print(Restaurante())
print(Aqui('Play', "Game"))
print(Ope())

#Crear una funcion