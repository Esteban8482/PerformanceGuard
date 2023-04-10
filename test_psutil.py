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

# Funcion que estiliza las conexiones de la network (No todos los posibles datos han sido agregados aun)
def filt_IO_net (connections):
    aux_net = []
    for i in connections:
        if i.status == psutil.CONN_ESTABLISHED:
            protocol = i.type
            local_address = f"{i.laddr.ip}{i.laddr.port}"
            remote_adress = f"{i.raddr.ip}{i.raddr.port}"
            pid = i.pid
            aux_net.append(f"{protocol} | {local_address} -> {remote_adress} | PID: {pid}")
            
    for connection in aux_net:
        print(connection)

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
#swapsito = psutil.swap_memory()
#bToB(swapsito, convert_indexes=[0, 1, 2])
#print(swapsito)

## Disco duro datos generales, informacion como el tipo de sistema de archivos
#disks = psutil.disk_partitions(all = False)
#print(disks)

## Espacio usado por el disco
#usageD = psutil.disk_usage('D://')
#usageC = psutil.disk_usage('/')
#bToB(usageD, convert_indexes = [0, 1, 2])
#bToB(usageC, convert_indexes = [0, 1, 2])
#print(usageD, usageC)

## Performance de IO del disco
#performance = psutil.disk_io_counters(perdisk = True)
#performanceC = bToB(performance.get("PhysicalDrive0"), save = True, convert_indexes = [2, 3])
#performanceD = bToB(performance.get("PhysicalDrive1"), save = True, convert_indexes = [2, 3])
#print(performanceC, performanceD)

## Entradas y salidas hacia la network desde distintas interfaces
#netIO = psutil.net_io_counters()
#bToB(netIO, convert_indexes = [0, 1])
#print(netIO)

## Detectar conexiones en la network
conIO = psutil.net_connections()
filt_IO_net(conIO)

#print(memoryGB)