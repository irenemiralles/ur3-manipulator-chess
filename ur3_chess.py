import socket
import time
import random

# Dirección IP del robot UR
HOST = "10.10.73.238"

# Puerto del servidor en el robot
PORT = 30002

# Conexión via socket a la controladora del robot
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((HOST, PORT))

# Scripts para abrir y cerrar la pinza
Abrir_pinza = 'pinza40UR3.py'
Cerrar_pinza = 'pinza10UR3.py'

# Función para enviar una trayectoria en espacio de configuraciones a la controladora del robot en período de tiempo corto (máx. 5seg)
def send_joint_path1(path, sock):
    for joint_config in path:
        print(joint_config)
        sock.send(f"movej({joint_config}, a=0.5, v=0.5)".encode() + "\n".encode())
        time.sleep(5)

# Función para enviar una trayectoria en espacio de configuraciones a la controladora del robot en período de tiempo largo (máx. 10seg)
def send_joint_path2(path, sock):
    for joint_config in path:
        print(joint_config)
        sock.send(f"movej({joint_config}, a=0.5, v=0.5)".encode() + "\n".encode())
        time.sleep(9)



#------------------------------------------------------------------------------------------

#Obre pinça
with open(Abrir_pinza, 'rb') as f: sock.sendall(f.read())
time.sleep(1)

rei = False
#elegir pieza (bucle hasta que la pieza sea rey)
while not rei:
    path_inicial = [[0.0344, -3.0629, 1.4657, -1.4601, 1.5753, 0.0024]] #posición inicial
    send_joint_path1(path_inicial, sock)

    peça = random.randint(1,3) #pieza aleatorio (1, 2, 3)
    if peça ==1:
        path1 = [[-0.4182, -2.0235, -2.1696, 0.2194, 1.8185, -0.3072]] #coger pieza 1       
        send_joint_path2(path1, sock)
        
    if peça ==2:
        path2 = [[-0.1172, -1.8904, -2.4666, 0.4158, 1.6137, -0.0867]] #coger pieza 2             
        send_joint_path2(path2, sock)
        
    if peça ==3:
        path3 = [[0.2627, -1.8261, -2.6847, 0.5445, 1.3510, 0.1896]] #coger pieza 3
        send_joint_path2(path3, sock)
           
    with open(Cerrar_pinza, 'rb') as f: sock.sendall(f.read()) #cerrar pinza
    time.sleep(1)
    
    path_mostrar = [[0.1955, -2.7270, 1.4249, -1.8330, 1.2937, 0.00214]] #mostrar la pieza
    send_joint_path1(path_mostrar, sock)

    # preguntar si la pieza es rey o no
    rei = input("La pieza elegida es rey? (si/no)") == 'si'

     #si la pieza elegida es rey (mover la pieza rey a la posición final |+5 puntos intermedios|) 
    if rei:
        path_final = [
            [0.0546, -2.7420, 1.3724, -1.7656, 1.4334, 0.0052], #punto intermedio 1
            [-0.0774, -2.7537, 1.3057, -1.6875, 1.5656, 0.0038], #punto intermedio 2
            [-0.1966, -2.7612, 1.2264, -1.5999, 1.6850, 0.0072], #punto intermedio 3
            [-0.3020, -2.7585, 1.1293, -1.5067, 1.7897, 0.0072], #punto intermedio 4
            [-0.3955, -2.7486, 1.0169, -1.4036, 1.8822, 0.0076], #punto intermedio 5
            [-0.4814, -2.7235, 0.8748, -1.2871, 1.9697, 0.0073], #punto final
            ]
        send_joint_path1(path_final, sock)
        #mostrar que el código ha finalizado
        print("Trayectoria finalizada")

    #si la pieza no es rey (devolver la pieza elegida a su posición de inicio)
    else:
        if peça==1:
            path1 = [[-0.4182, -2.0235, -2.1696, 0.2194, 1.8185, -0.3072]] #dejar pieza 1
            send_joint_path2(path1, sock)
        
        if peça==2:
            path2 = [[-0.1172, -1.8904, -2.4666, 0.4158, 1.6137, -0.0867]] #dejar pieza 2
            send_joint_path2(path2, sock)
    
        if peça==3:
            path3 = [[0.2627, -1.8261, -2.6847, 0.5445, 1.3510, 0.1896]] #dejar pieza 3
            send_joint_path2(path3, sock)

        with open(Abrir_pinza, 'rb') as f: sock.sendall(f.read()) #abrir pinza
        time.sleep(1)

#------------------------------------------------------------------------------------------