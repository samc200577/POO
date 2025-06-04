#creacion e inincio de sesion

#descomposición
#- pedir nombre de ususario creado 
#- pedir contraseña creada
#- "iniciar sesion" {pedir nombre de usuario}
#- pedir contraseña
#- rectificar si nombre de usuario y contraseña coinciden con las ceradas
#- determinar acción

from apoyo import ingresar_texto, mostrar_mensaje

def main():
    usuario_creado = ingresar_texto("Ingrese su nombre de usuario a cerear = ")
    contraseña_creada = ingresar_texto("Ingrese su contraseña de única a cerear = ")
    print("Bienvenido al programa, por favor incie sesión")
    usuario = ingresar_texto("Digite su nombre de ususario = ")
    contraseña = ingresar_texto("Digite su contraseña = ")
    rectificacion = rectificar_perfil(usuario_creado,contraseña_creada,usuario,contraseña)
    mensaje = generar_mensaje(rectificacion,usuario)
    mostrar_mensaje(mensaje)

def rectificar_perfil(usuario_creado,contraseña_creada,usuario,contraseña):
    if usuario_creado == usuario and contraseña_creada == contraseña:
        rectificacion = True
    else:
        rectificacion = False
    return rectificacion

def generar_mensaje(rectificacion,usuario):
    if rectificacion == True:
        mensaje = f"Bienvenido {usuario}. "
    else:
        mensaje = "Nombre de usuario o contraseña incorrectos"
    return mensaje
        
main()
        

    