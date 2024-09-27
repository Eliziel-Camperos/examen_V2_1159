class Comics:
    def crear_diccionario_comics(self):
        datos_comics = {
            "ID": 764,
            "Serie": "Caos + Order",
            "Genero": "Acción, superheroes, Ciencia Ficción, Fantasía, Comedia, Drama, aventura",
            "Comics_Vendidos": 1500,
            "Autor": "Eliziel",
            "Color": "Blanco y negro",
            "Precio": 25.99
        }
        return datos_comics

    def crear_diccionario_empleados(self):
        datos_empleados = {
            "ID": 1,
            "Salario": 3000,
            "Nombre": "Eliziel",
            "Apellido": "Camperos",
            "Celular": "656 459 7502",
            "Sexo": "Masculino",
            "Puesto": "Gerente"
        }
        return datos_empleados

    def crear_diccionario_mercancia(self):
        datos_mercancia = {
            "ID": 535,
            "Cantidad_Figuras": 100,
            "Cantidad_Posters": 50,
            "Cantidad_Peluches": 25,
            "Cantidad_Marcadores": 75,
            "Serie": "Caos + Order",
            "Precio": "7 usd"
        }
        return datos_mercancia

    def crear_diccionario_ventas(self):
        datos_ventas = {
            "ID": 642,
            "Comic": "Caos + Order",
            "Numero_Ventas": 200,
            "Generos": "Acción, superheroes, Ciencia Ficción, Fantasía, Comedia, Drama, aventura",
            "Direccion": "Paseos de las alondras 8031 28B",
            "Calificacion_Comic": 4.5
        }
        return datos_ventas

comics_obj = Comics()

datos_comics = comics_obj.crear_diccionario_comics()
datos_empleados = comics_obj.crear_diccionario_empleados()
datos_mercancia = comics_obj.crear_diccionario_mercancia()
datos_ventas = comics_obj.crear_diccionario_ventas()

for clave, valor in datos_comics.items():
    print(clave, valor)
for clave, valor in datos_empleados.items():
    print(clave, valor)
for clave, valor in datos_mercancia.items():
    print(clave, valor)
for clave, valor in datos_ventas.items():
    print(clave, valor)
