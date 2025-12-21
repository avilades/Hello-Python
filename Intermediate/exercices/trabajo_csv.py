import csv

def procesar_csv(archivo_entrada, archivo_salida):
    try:
        with open(archivo_entrada, mode='r', encoding='utf-8') as f_in, \
             open(archivo_salida, mode='w', encoding='utf-8') as f_out:
            
            lector = csv.reader(f_in)
            
            for i, linea in enumerate(lector, 1):
                # Unimos los elementos de la fila por si el CSV tiene varias columnas
                contenido = ",".join(linea)
                
                # Construimos la base de la línea: ("contenido"),
                nueva_linea = f'("{contenido}"'
                
                # Lógica para cada 1000 líneas
                if i % 20 == 0:
                    f_out.write(nueva_linea + ");\n\nINSERT INTO tabla (columna)\nVALUES\n")
                else:
                    f_out.write(nueva_linea + "),\n")
                    
        print(f"Procesamiento completado. Archivo guardado como: {archivo_salida}")

    except FileNotFoundError:
        print("Error: No se encontró el archivo de entrada.")
    except Exception as e:
        print(f"Ocurrió un error: {e}")

# Configuración de nombres de archivo
procesar_csv('Intermediate/exercices/datos.csv', 'Intermediate/exercices/resultado.txt')