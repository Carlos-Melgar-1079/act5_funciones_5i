print("Manejo de funciones V1")
def hola_mundo():
    print("hola aqui estoy dentro de la funcion")
    
def Mensa(msg):
        print(msg)
def EscribeNC(Nombre,Apellido):
    print(Nombre,Apellido)
    print(f"tu nombre completo es {Nombre} {Apellido}")
def suma2numeros(n1,n2):
    s=n1 +n2
    print(f"la suma de {n1} y de {n2} es de:"),s
    return s
#llamando a la funcion
hola_mundo()
Mensa("hola wattsap") #llama a mensa con 1 parametro
Mensa("el profe me sorprendio enviando mensajes")#llama a mensa
EscribeNC("eliseo","Nava")
print("Funciones que regresan valores")
print(suma2numeros(7,3))
print(suma2numeros(15,45))