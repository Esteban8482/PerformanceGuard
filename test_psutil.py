import psutil

## Codigo Auxiliar para las pruebas
# Funcion que convierte arrays con bytes a gigabytes
def bToB (memory, save = None, convert_indexes = []):
    
    memoryGB = []
    
    for i, val in enumerate(memory):
        if i in convert_indexes:
            memoryGB.append(val / (1000 ** 3))
        else:
            memoryGB.append(val)
    
    memoryGB = [round(i, 2) for i in memoryGB]
    
    if save is not None:
        return memoryGB
    else:
        print(memoryGB)

## Contador de nucleos e hilos del procesador
#logical_cpu_count = psutil.cpu_count()
#fisical_cpu_count = psutil.cpu_count(False)

## Averigua la maxima frecuencia del procesador
#freq = psutil.cpu_freq()

## Determina distintos valores sobre la memoria RAM del sistema: Total, disponible, y cantidad siendo usada
#mem = psutil.virtual_memory()
#bToB(mem, convert_indexes=[0, 1, 3, 4])
#print(mem)

## Memoria SWAP
swapsito = psutil.swap_memory()
bToB(swapsito, convert_indexes=[0, 1, 2])
print(swapsito)

#print(memoryGB)