#programa que codifique un texto y lo descodifica

#preguntar si quiere codificar o descodificar
#ingresar  numero
#ingresar texto
#codificar
#descodificar
#generar mensaje
#mostrar mensje

from apoyo import mostrar_mensaje,ingresar_texto, ingresar_lista_numeros

usuario = "samuel1234"
contraseña = "samuel4321"


def iniciar_sesion(usuario,contraseña):
    usuario_ingresado = input("Ingrese su usuario = ")
    contraseña_ingresado = input("Ingrese su contraseña = ")
    
    while usuario_ingresado != usuario or  contraseña_ingresado != contraseña:
        print("usuario o contraseña incorrectos")
        iniciar_sesion(usuario,contraseña)
    
iniciar_sesion(usuario,contraseña)


def codificacion():
    codificar_o_descodificar = preguntar_co_des()
    accion = decidir_trabajo(codificar_o_descodificar)
    resultado = hacer_trabajo(codificar_o_descodificar,accion)
    generar_mensaje(codificar_o_descodificar,resultado)
  

def preguntar_co_des():
    codificar_o_descodificar = input("¿Desesea coodificar o descodificar? = ")
    return codificar_o_descodificar

def decidir_trabajo(codificar_o_desccodificar):
    if codificar_o_desccodificar == "codificar":
        accion = ingresar_texto("Ingrese el mensaje que desea codificar = ")
    
    elif codificar_o_desccodificar == "descodificar":
        accion = ingresar_lista_numeros("Ingrese el mensaje que desea descodificar = ")
    return accion

def hacer_trabajo(codificar_o_descodificar,accion):
    if codificar_o_descodificar == "codificar":
        resultado = []
        for letra  in accion:
            resultado.append(ord(letra))
    
    elif codificar_o_descodificar == "descodificar":
        resultado = ""
        for numero in accion:
            resultado += chr(numero)
    
    return resultado
    
def generar_mensaje(codificar_o_descodificar,resultado):
    
    if codificar_o_descodificar == "descodificar":
        mensaje = resultado
        mostrar_mensaje(mensaje)
    elif codificar_o_descodificar == "codificar":
        mensaje = f"Su mensaje codificado es = {resultado}"
        mostrar_mensaje(mensaje)
        
codificacion()
