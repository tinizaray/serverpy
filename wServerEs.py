import socket 
import datetime 
    
# función utilizada para iniciar el servidor del reloj
def initiateClockServer(): 
  
    s = socket.socket() 
    print("Socket creado correctamente")
        
    # Puerto de servicio
    port = 8000
  
    s.bind(('', port)) 
       
    # Comience a escuchar solicitudes
    s.listen(5)       
    print("Socket está escuchando...")
        
    # Servidor de reloj funcionando definido
    while True:  
        
       # Establecer conexión con el cliente
       connection, address = s.accept()       
       print('Servidor conectado a ', address)
        
       # Responder al cliente con la hora del reloj del servidor
       connection.send(str( 
                    datetime.datetime.now()).encode()) 
        
       # Cerrar la conexión con el proceso del cliente.
       connection.close() 
  
  
# funcion principal
if __name__ == '__main__': 
  
    # Activar el servidor del reloj
    initiateClockServer() 