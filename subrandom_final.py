import ipaddress
import random 

print("Clase A, B , C: ")
clase = input("Ingrese la clase: ")
if clase == "A" or clase == "a":
    ip1 = str(random.randint(1,126))
    ip2 = "0"
    ip3 = "0"
    ip4 = "0"
    ipv4 = ipaddress.ip_address(f"{ip1}.{ip2}.{ip3}.{ip4}")
    print(ipv4)
elif clase == "B" or clase == "b":
    ip1 = str(random.randint(128,191))
    ip2 = str(random.randint(0,255))
    ip3 = "0"
    ip4 = "0"
    ipv4 = ipaddress.ip_address(f"{ip1}.{ip2}.{ip3}.{ip4}")
    print(ipv4)
elif clase == "C" or clase =="c":
    ip1 = str(random.randint(192,223))
    ip2 = str(random.randint(0,255))
    ip3 = str(random.randint(1,254))
    ip4 = "0"
    ipv4 = ipaddress.ip_address(f"{ip1}.{ip2}.{ip3}.{ip4}")
    print(ipv4)

#CONDICION PARA NO SOBREPASAR CANTIDAD DE SUBREDES PERMITIDAS POR LOS BITS
if clase == "C" or clase == "c":
    cant_sredes = int(input("Cantidad de subredes 1-64: "))
    if cant_sredes >= 1 and cant_sredes <= 64: #si esta dentro del rango
        cant_sredes = cant_sredes
    elif cant_sredes < 1 or cant_sredes > 64: #si esta fuera del rango
        while cant_sredes < 1 or cant_sredes > 64: #bucle de rango 
            cant_sredes = int(input("Cantidad de subredes 1-64: "))
elif clase == "B" or clase == "b":
    cant_sredes = int(input(f"Cantidad de subredes 1-16,384: "))
    if cant_sredes >= 1 and cant_sredes <= 16384: #si esta dentro del rango
        cant_sredes = cant_sredes
    elif cant_sredes < 1 or cant_sredes > 16384: #si esta fuera del rango
        while cant_sredes < 1 or cant_sredes > 16384: #bucle de rango
            cant_sredes = int(input(f"Cantidad de subredes 1-16,384: "))
elif clase == "A" or clase =="a":
    cant_sredes = int(input(f"Cantidad de subredes 1-4,194,304: "))
    if cant_sredes >= 1 and cant_sredes <= 4194304: #si esta dentro del rango
        cant_sredes = cant_sredes
    elif cant_sredes < 1 or cant_sredes > 4194304: #si esta fuera del rango
        while cant_sredes < 1 or cant_sredes >4194304: #bucle de rango
            cant_sredes = int(input(f"Cantidad de subredes 1-4,194,304: "))
#bits
for num in range(0,99):
    calculo_sredes = 2**num #iteracion
    if calculo_sredes >= cant_sredes: #si el calculo es mayor o igual a las sr pedidas
        bits = num
        break #se asigna y rompe el ciclo 

#calculo de hosts por subred
if clase == "A" or clase == "a":
    hosts = 2**(24-num)-2
elif clase == "B" or clase == "b":
    hosts = 2**(16-num)-2
elif clase == "C" or clase == "c":
    hosts = 2**(8-num)-2

#CONDICION PARA NO SOBREPASAR REDES ADMITIDAS POR LOS BITS
pcs = int(input(f"Cantidad de Hosts con rango de 1-{hosts}: "))
#limite clase C
if clase == "C" or clase == "c": 
    if pcs == 1 or pcs <= hosts:
        pcs = pcs
    elif pcs < 1 or pcs > hosts: #si esta fuera del rango permitido
        while pcs < 1 or pcs > hosts: #bucle de rango
            pcs = int(input(f"Cantidad de Hosts con rango de 1-{hosts}: "))
#limite clase B
elif clase == "B" or clase == "b":
    if pcs == 1 or pcs <= hosts:
        pcs == pcs
    elif pcs < 1 or pcs > hosts: #si esta fuera del rango permitido
        while pcs < 1 or pcs > hosts: #bucle de rango
            pcs = int(input(f"Cantidad de Hosts con rango de 1-{hosts}: "))
#limite clase A
elif clase == "A" or clase == "a":
    if pcs == 1 or pcs <= hosts:
        pcs == pcs
    elif pcs < 1 or pcs > hosts: #si esta fuera de rango permitido
        while pcs < 1 or pcs > hosts: #bucle de rango
            pcs = int(input(f"Cantidad de Hosts con rango de 1-{hosts}: "))

#impresion de cada subred y ip utilizable
print(f"\nIP: {ipv4}") #ip principal generada
sred = ipv4 + 1 #primer subred que termina en .1
for num in range(1, cant_sredes + 1):
    print(f"\nSubred {num}: {sred}") 
    pc = sred
    for num in range(1, pcs + 1):
        pc = pc + 1 #iterador para asignacion de ips consecutivas 
        print(f"PC {num}: {pc}")
    sred = sred + hosts + 2 #calculo de cada subred despues de los host y el broadcast
    broadcast = sred - 1 #calculo de broadcast que es antes de la sig subred
    print(f"Broadcast: {broadcast}")