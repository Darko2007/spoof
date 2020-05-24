# -*- coding: utf-8 -*-

import pycurl
from StringIO import StringIO
from colorama import Back, Fore, init

init(autoreset=True)

def spoof():
    while True:
        print '''
 #####                             
#     # ####   ####   ####  ###### 
#       #   # #    # #    # #     
 #####  #   # #    # #    # ##### 
      # ####  #    # #    # #     
#     # #     #    # #    # #     
 #####  #      ####   ####  #
Version:1.0
Codigo escrito por: Angelo Mass - Darko.

El autor no se hace responsable por el uso que den a la herramienta.

1) Enviar correo a un solo destinatario.
2) Enviar correo a multiples destinatarios.
3) Salir.
'''
        opcion = raw_input('Darko@Spoof$ ')
        if opcion == '1':
            opcion_uno()
        elif opcion == '2':
            opcion_dos()
        elif opcion == '3':
            exit()
        else:
            print Fore.RED + '[*]Ingrese un argumento valido.'

def opcion_uno():
    print '''
 #####                             
#     # ####   ####   ####  ###### 
#       #   # #    # #    # #     
 #####  #   # #    # #    # ##### 
      # ####  #    # #    # #     
#     # #     #    # #    # #     
 #####  #      ####   ####  #
Version:1.0
Codigo escrito por: Angelo Mass - Darko.

Seccion: Enviar correo a un solo destinatario.
'''
    remitente = raw_input('Remitente: ')
    receptor = raw_input('Receptor: ')
    asunto = raw_input('Asunto: ')
    mensaje = raw_input('Mensaje: ')
    post_vars = {}
    try:
        url = 'https://insessorial-halls.000webhostapp.com/index.php'
        post_vars['desde'] = remitente
        post_vars['asunto'] = asunto
        post_vars['remitente'] = receptor
        post_vars['msj'] = mensaje
        buffer = StringIO()
        c = pycurl.Curl()
        c.setopt(pycurl.URL, url)
        c.setopt(pycurl.POSTFIELDS,urllib.urlencode(post_vars))
        c.setopt(c.WRITEDATA, buffer)
        c.perform()
        c.close()
        print Fore.GREEN +  '[*]Enviando correo a: ' + receptor
        print Fore.GREEN + '[*]Correo enviado con exito.'
    except:
        print Fore.YELLOW + '[*]Al parecer a ocurrido un error. Intentelo de nuevo.'

def opcion_dos():
    print '''
 #####                             
#     # ####   ####   ####  ###### 
#       #   # #    # #    # #     
 #####  #   # #    # #    # ##### 
      # ####  #    # #    # #     
#     # #     #    # #    # #     
 #####  #      ####   ####  #
Version:1.0
Codigo escrito por: Angelo Mass - Darko.

Seccion: Enviar correo a multiples destinatarios.
'''
    remitente = raw_input('Remitente: ')
    archivo = raw_input('Archivo de texto con las direcciones de correo(una direccion por linea): ')
    try:
        abrir = open(archivo, 'r')
    except:
        print '[*]el archivo: ' + archivo + ' no existe.'
    asunto = raw_input('Asunto: ')
    mensaje = raw_input('Mensaje: ')
    post_vars = {}
    try:
        url = 'https://insessorial-halls.000webhostapp.com/index.php'
        for receptor in abrir.readlines():
            post_vars['desde'] = remitente
            post_vars['asunto'] = asunto
            post_vars['remitente'] = receptor
            post_vars['msj'] = mensaje
            buffer = StringIO()
            c = pycurl.Curl()
            c.setopt(pycurl.POSTFIELDS,urllib.urlencode(post_vars))
            c.setopt(pycurl.URL, url)
            c.setopt(c.WRITEDATA, buffer)
            c.perform()
            c.close()
            print Fore.GREEN + 'Enviando correo a: ' + receptor
        print Fore.GREEN + '[*]Los correos fueron enviados correctamente.'
    except:
        print Fore.YELLOW + '[*]Al parecer a ocurrido un error. Intentelo de nuevo.'

spoof()

#Codigo escrito por Angelo Mass - Darko.

#La herramienta fue diseñada para el grupo
#"Auditoria global" y para la pagina
#"black hat"

#Hackea El Planeta.
