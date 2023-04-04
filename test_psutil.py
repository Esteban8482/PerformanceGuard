import psutil
import time

# Utilidades auxiliares
start_time = time.time()

## Contador de nucleos e hilos del procesador
#logical_cpu_count = psutil.cpu_count()
#fisical_cpu_count = psutil.cpu_count(False)

#"" Averigua la maxima frecuencia del procesador
#freq = psutil.cpu_freq()

## Calcular carga del procesador en los ultimos minutos, en windows debe ser ejecutado de manera ciclica, basado en la cantidad de nucleos
load = [i / psutil.cpu_count() * 100 for i in psutil.getloadavg()]

print(load)