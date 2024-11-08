#Análisis de datos con pandas (Análisis descriptivo)
#1. Para analizar datos con pandas necesitamos instalar
# e importar la herramienta

import pandas as pd

#2. Se obtiene la fuente de datos
#lista de datos
datos= [
     {'Nombre': 'Carlos Mendoza', 'Ciudad': 'Cali', 'Edad': 29},
    {'Nombre': 'Ana Velasquez', 'Ciudad': 'Cartagena', 'Edad': 34},
    {'Nombre': 'Miguel Pardo', 'Ciudad': 'Bogotá', 'Edad': 42},
    {'Nombre': 'Sofia Londoño', 'Ciudad': 'Medellín', 'Edad': 23},
    {'Nombre': 'Lucia Rojas', 'Ciudad': 'Cúcuta', 'Edad': 37},
    {'Nombre': 'Manuel Díaz', 'Ciudad': 'Barranquilla', 'Edad': 28},
    {'Nombre': 'Felipe Torres', 'Ciudad': 'Pereira', 'Edad': 31},
    {'Nombre': 'Laura Gutierrez', 'Ciudad': 'Ibagué', 'Edad': 26},
    {'Nombre': 'Julian Mejia', 'Ciudad': 'Manizales', 'Edad': 39},
    {'Nombre': 'Paula Vargas', 'Ciudad': 'Bucaramanga', 'Edad': 33},
    {'Nombre': 'Oscar Herrera', 'Ciudad': 'Cali', 'Edad': 48},
    {'Nombre': 'Diana Muñoz', 'Ciudad': 'Cartagena', 'Edad': 22},
    {'Nombre': 'Gabriel Morales', 'Ciudad': 'Bogotá', 'Edad': 36},
    {'Nombre': 'Andrea Pérez', 'Ciudad': 'Medellín', 'Edad': 27},
    {'Nombre': 'Javier Ortiz', 'Ciudad': 'Cúcuta', 'Edad': 40},
    {'Nombre': 'Carolina Sánchez', 'Ciudad': 'Barranquilla', 'Edad': 32},
    {'Nombre': 'Raúl Castro', 'Ciudad': 'Pereira', 'Edad': 45},
    {'Nombre': 'Natalia Flores', 'Ciudad': 'Ibagué', 'Edad': 30},
    {'Nombre': 'David Marín', 'Ciudad': 'Manizales', 'Edad': 50},
    {'Nombre': 'Marcela Espinosa', 'Ciudad': 'Bucaramanga', 'Edad': 28},
    {'Nombre': 'Ricardo Lozano', 'Ciudad': 'Cali', 'Edad': 44},
    {'Nombre': 'Sandra León', 'Ciudad': 'Cartagena', 'Edad': 38},
    {'Nombre': 'Fernando Ríos', 'Ciudad': 'Bogotá', 'Edad': 41},
    {'Nombre': 'Luisa Castillo', 'Ciudad': 'Medellín', 'Edad': 35},
    {'Nombre': 'Pedro Pardo', 'Ciudad': 'Cúcuta', 'Edad': 29},
    {'Nombre': 'Camila Suárez', 'Ciudad': 'Barranquilla', 'Edad': 33},
    {'Nombre': 'Mario Cortés', 'Ciudad': 'Pereira', 'Edad': 24},
    {'Nombre': 'Paola Ramírez', 'Ciudad': 'Ibagué', 'Edad': 37},
    {'Nombre': 'Diego López', 'Ciudad': 'Manizales', 'Edad': 43},
    {'Nombre': 'Alejandra Ruiz', 'Ciudad': 'Bucaramanga', 'Edad': 26},
    {'Nombre': 'Edgar Niño', 'Ciudad': 'Cali', 'Edad': 52},
    {'Nombre': 'Elena Bernal', 'Ciudad': 'Cartagena', 'Edad': 21},
    {'Nombre': 'Tomás Fuentes', 'Ciudad': 'Bogotá', 'Edad': 46},
    {'Nombre': 'Isabel Sánchez', 'Ciudad': 'Medellín', 'Edad': 34},
    {'Nombre': 'Sebastián Duarte', 'Ciudad': 'Cúcuta', 'Edad': 32},
    {'Nombre': 'Daniela Cruz', 'Ciudad': 'Barranquilla', 'Edad': 39},
    {'Nombre': 'Alberto Vega', 'Ciudad': 'Pereira', 'Edad': 42},
    {'Nombre': 'Rosa Aguilar', 'Ciudad': 'Ibagué', 'Edad': 25},
    {'Nombre': 'Luis Navarro', 'Ciudad': 'Manizales', 'Edad': 47},
    {'Nombre': 'Andrea Cardona', 'Ciudad': 'Bucaramanga', 'Edad': 31}
]

#3. Se capturan los datos 
#Pandas utiliza una tabla tabulada que se llama Dataframe 

datosOrdenados=pd.DataFrame(datos)

#print (datosOrdenados)

#utilizando el tail
#print(datosOrdenados.tail())

#utilizando el info
#print(datosOrdenados.info())

#utilizando el describe
#print(datosOrdenados.describe())

#utilizando corchetes
#print(datosOrdenados[datosOrdenados['Edad']>=18])
#print(datosOrdenados['Nombre'])

#Elimina registros

#datosOrdenados.drop(0)
#print(datosOrdenados)

print(datosOrdenados.groupby('Ciudad').size())