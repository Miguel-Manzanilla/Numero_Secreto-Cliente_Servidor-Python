import socket

HOST="127.0.0.1"
PORT=2000

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((HOST,PORT))
print("Concetado con el server")
i=0
ganar=True
while i!=4 and ganar:
    print("DAME UN NUMERO")
    numero=(input())
    s.send(numero.encode())
    data=s.recv(1024)
    if data.decode()=="BIEN":
        print(f"BIEN ACERTASTE EL NUMERO ERA: {numero} CON {i+1} INTENTOS")
        ganar=False
    else:
        print(f"RECIBO: {data.decode()}")
    i=i+1
s.close