# Crear un Diccionario
informacion_personal = {
    "nombre": "Juan",
    "edad": 30,
    "ciudad": "Quito",
    "profesion": "Ingeniero"
}

# Acceder y Modificar Valores
informacion_personal["ciudad"] = "Guayaquil"  # Cambiar la ciudad
informacion_personal["profesion"] = "Doctor"  # Agregar una nueva profesión

# Verificar Existencia de Claves
if "telefono" not in informacion_personal:
    informacion_personal["telefono"] = "1234567890"  # Agregar un número de teléfono ficticio

# Eliminar una Clave
del informacion_personal["edad"]  # Eliminar la edad

# Imprimir el Diccionario Final
print(informacion_personal)