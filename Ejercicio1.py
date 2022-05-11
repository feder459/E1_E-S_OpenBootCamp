file=open('C:/Users/Fede Franco/Documents/CAPACITACIONES 2022/OpenBootcamp/Python/Entrada y Salida/MiPrimerFichero.txt', 'w')
file.write("Primera linea del fichero\n")
file.close()

file=open('C:/Users/Fede Franco/Documents/CAPACITACIONES 2022/OpenBootcamp/Python/Entrada y Salida/MiPrimerFichero.txt', 'r+')
file.readline()
file.write("Es la segunda linea del fichero\n")

#seek parece que da la posición del byte donde comienza a leerse el fichero 

file.seek(0)
print(file.read())
file.close()