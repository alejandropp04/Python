def validarEmail(email):
    errores = []
    caracterA = False
    punto = False
    empiezaA = False
    termina_Punto = False
    arroba = 0
    empiezaPunto = False

    if email.startswith("@"):
        empiezaA = True
    if email.endswith("."):
        termina_Punto = True
    if email.startswith("."):
        empiezaPunto = True

    for letra in email:
        if letra == "@" and empiezaA == False:
            arroba += 1
            caracterA = True
        if arroba >= 1 and letra == ".":
            punto = True

    if punto == False:
       errores.append("El email debe contener un '.' en el dominio")
    if termina_Punto == True:
        errores.append("El email no puede terminar en '.'")
    if empiezaA == True:
        errores.append("El email no puede empezar por @")
    if caracterA == False:
        errores.append("El email debe contener un '@'")
    if empiezaPunto == True:
        errores.append("El email no puede empezar por un '.'")

    if not errores:
        return "valido"
    else:
        return errores
    
print(validarEmail("alex@gmail.com"))
print(validarEmail("@carlos.com"))
#Da error tambien en el dominio conforme el @ no esta en la posicion adecuada
print(validarEmail("alex@gmail."))
print(validarEmail("ale.x@gmail"))
print(validarEmail(".alex@gmail.com"))
print(validarEmail("alejandro.pacheco@educa.madrid.org"))