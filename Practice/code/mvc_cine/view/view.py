class View:
    """
    **************************
    * A view for a movies DB *
    **************************
    """
    def start(self):
        print('==============')
        print('= Bienvenido =')
        print('==============')

    def end(self):
        print('================================')
        print('=        Hasta la vista!       =')
        print('================================')


    def user_menu(self):
        print('==========================================')
        print('=        Ingresa  tipo de usuario        =')
        print('==========================================')
        print('1. Cliente con cuenta')
        print('2. Cliente sin cuenta')
        print('3. Administrador')
        print('4. Crear cuenta')
        print('5. Salir')


    def user_type_menu(self):
        print('=========================================')
        print('=        Ingresa  tipo de cuenta        =')
        print('=========================================')
        print('1. Cliente')
        print('2. Administrador')
        print('3. Regresar a inicio de sesion')


    def main_menu(self):
        print('======================================')
        print('=        Menu de administrador       =')
        print('======================================')
        print('1. Películas')
        print('2. Actores')
        print('3. Directores')
        print('4. Generos')
        print('5. Cuentas clientes')
        print('6. Cuentas Administradores')
        print('7. Salas')
        print('8. Cartelera')
        print('9. Comprar boletos')
        print('10. Registro de compras')
        print('11. Salir')

    def main_menu_client(self):
        print('================================')
        print('=        Menu de cliente       =')
        print('================================')
        print('1. Cartelera')
        print('2  Mostrar horario de pelicula')
        print('3. Comprar boletos')
        print('4. Registro de compras')
        print('5. Opciones extras')
        print('6. Regresar')

    def main_menu_anonimo(self):
        print('================================')
        print('=        Menu de cliente       =')
        print('================================')
        print('1. Cartelera')
        print('2  Mostrar horario de pelicula')
        print('3. Comprar boletos')
        print('4. Opciones extras')
        print('5. Regresar')

    def extra_menu(self):
        print('================================')
        print('=        Opciones extras       =')
        print('================================')
        print('1. Películas')
        print('2. Actores')
        print('3. Directores')
        print('4. Generos')
        print('5. Regresar')

    def option(self,last):
        print('Selecciona un opcion (1-'+last+'): ', end = '')

    def not_valid_option(self):
        print('Opcion no valida!\nIntenta de nuevo')
    
    def ask(self, output):
        print(output, end = '' )
    
    def msg(self, output):
        print(output)
    
    def admin_ask(self):
        print('Ingrese clave de administrador: ')

    def capacity(self):
        print('Capacidad de sala: ')



    def ask_return(self):
        print('Regresar a menu principal ingrese 1: ')
        print('Ir a menu de administrador ingrese 2: ')

    def ok(self, id, op):
        print('+'*(len(str(id))+len(op)+24))
        print('+'+str(id)+' se '+op+' correctamente! +')
        print('+'*(len(str(id))+len(op)+24))
    
    def error(self, err):
        print(' Error! '.center(len(err)+4,'-'))
        print('-'+err+'-')
        print('-'*(len(err)+4))
    

    """
    *********************
    * A view for movies *
    *********************
    """

    def movies_menu_client(self):
        print('************************')
        print('* -- Submenu Movies -- *')
        print('************************')
        print('1.  Mostrar Pelicula')
        print('2.  Mostrar todas las Peliculas')
        print('3.  Mostrar Descripciones')
        print('4.  Ver detalles de pelicula')
        print('5.  Regresar')


    def movies_menu(self):
        print('************************')
        print('* -- Submenu Movies -- *')
        print('************************')
        print('1.  Agregar Pelicula')
        print('2.  Mostrar Pelicula')
        print('3.  Mostrar todas las Peliculas')
        print('4.  Mostrar Descripciones')
        print('5   Ver detalles de pelicula')
        print('6   Agregar detalles')
        print('7   Editar detalles')
        print('8.  Actualizar Pelicula')
        print('9.  Borrar Detalles')
        print('10. Borrar Pelicula')
        print('11. Regresar')
    
    def show_a_movie(self, record):
        if record[3] == None:
            print(f'{record[0]:<3}|{record[1]:<30}|{record[2]:<20}|')
        else:
            print(f'{record[0]:<3}|{record[1]:<30}|{record[2]:<20}|{record[3]:<20}')
    
    def show_movie_header(self, header):
        print(header.center(77,'*'))
        print('ID'.ljust(3)+'|'+'Pelicula'.ljust(30)+'|'+'Idioma'.ljust(20)+'|'+'Subtitulo'.ljust(20))
        print('-'*77)

    def show_movie_midder(self):
        print('-'*77)
    
    def show_movie_footer(self):
        print('-'*77)

    def show_a_detail(self, record):
        print(f'{record[0]:<3}|{record[1]:<20}|{record[2]:<20}|{record[3]:<100}|{record[4]:<8}')
    
    def show_detail_header(self, header):
        print(header.center(92,'*'))
        print('ID'.ljust(3)+'|'+'Pelicula'.ljust(20)+'|'+'Director'.ljust(20)+'|'+'Descripcion'.ljust(100)+'|'+'Duracion'.ljust(8))
        print('-'*156)

    def show_detail_midder(self):
        print('-'*156)
    
    def show_detail_footer(self):
        print('-'*156)


    """
    *********************
    * A view for Actors *
    *********************
    """

    def actors_menu_client(self):
        print('************************')
        print('* -- Submenu Actors -- *')
        print('************************')
        print('1. Mostrar Actor')
        print('2. Mostrar todas los Actores')
        print('3. Mostrar Peliculas de actor')
        print('4  Ver Actor por nacionalidad')
        print('5  Regresar')

    def actors_menu(self):
        print('************************')
        print('* -- Submenu Actors -- *')
        print('************************')
        print('1. Agregar Actor')
        print('2. Mostrar Actor')
        print('3. Mostrar todas los Actores')
        print('4. Mostrar Peliculas de actor')
        print('5  Ver Actor por nacionalidad')
        print('6  Editar Actor')
        print('7  Agregar pelicula del actor')
        print('8  Eliminar pelicula del actor ')
        print('9  Eliminar actor ')
        print('10 Regresar')
 
    
    def show_a_actor(self, record):
        print(f'{record[0]:<3}|{record[1]:<30}|{record[2]:<15} {record[3]:<15}|{record[4]:<20}|{record[5]}')
    
    def show_actor_header(self, header):
        print(header.center(105,'*'))
        print('ID'.ljust(3)+'|'+'Nombre'.ljust(30)+'|'+'Apellido'.ljust(31)+'|'+'Nacionalidad'.ljust(20)+'|'+'Año de nacimeinto'.ljust(5))
        print('-'*105)

    def show_actor_midder(self):
        print('-'*105)
    
    def show_actor_footer(self):
        print('-'*105)

    """
    ************************
    * A view for Directors *
    ************************
    """

    def directors_menu_client(self):
        print('***************************')
        print('* -- Submenu Directors -- *')
        print('***************************')
        print('1. Mostrar Director')
        print('2. Mostrar todas los Directores')
        print('3  Motrar Director por nacionalidad')
        print('4  Mostras peliculas del director ')
        print('5  Regresar')

    def directors_menu(self):
        print('***************************')
        print('* -- Submenu Directors -- *')
        print('***************************')
        print('1. Agregar Director')
        print('2. Mostrar Director')
        print('3. Mostrar todas los Directores')
        print('4  Motrar Director por nacionalidad')
        print('5  Mostras peliculas del director ')
        print('6  Actualizar Director ')
        print('7  Eliminar Director ')
        print('8  Regresar')
    
    def show_a_director(self, record):
        if record[3] == None:
            print(f'{record[0]:<3}|{record[1]:<30}|{record[2]:<30}|{record[4]:<20}|{record[5]}'+'      'f'|{record[6]:<20}')
        else:      
            print(f'{record[0]:<3}|{record[1]:<30}|{record[2]:<15} {record[3]:<15}|{record[4]:<20}|{record[5]}'+'      'f'|{record[6]:<20}')
    
    def show_director_header(self, header):
        print(header.center(105,'*'))
        print('ID'.ljust(3)+'|'+'Nombre'.ljust(30)+'|'+'Apellido'.ljust(31)+'|'+'Nacionalidad'.ljust(20)+'|'+'nacimiento'.ljust(16)+'|'+'Estudios'.ljust(20))
        print('-'*105)

    def show_director_midder(self):
        print('-'*105)
    
    def show_director_footer(self):
        print('-'*105)

    """
    ************************
    * A view for Generos *
    ************************
    """

    def generos_menu_client(self):
        print('***************************')
        print('* -- Submenu Generos -- *')
        print('***************************')
        print('1. Mostrar todos los generos')
        print('2  Mostrar generos de una pelicula')
        print('3  Salir ')

    def generos_menu(self):
        print('***************************')
        print('* -- Submenu Generos -- *')
        print('***************************')
        print('1. Agregar Genero')
        print('2. Agregar Genero a pelicula')
        print('3. Mostrar Genero')
        print('4. Mostrar todos los generos')
        print('5  Actualizar Genero')
        print('6  Actualizar Genero a pelicula')
        print('7  Mostrar generos de una pelicula')
        print('8  Eliminar Genero')
        print('9  Eliminar Genero a pelicula')
        print('10  Salir ')

    def show_a_genero(self, record):
        print(f'{record[0]:<3}|{record[1]:<15}')

    def show_genpelicula(self, record):
        print(f'{record[0]:<3}|{record[1]:<15}|{record[2]:<3}|{record[3]:<15}')
    
    def show_genero_header(self, header):
        print(header.center(20,'*'))
        print('ID'.ljust(3)+'|'+'Genero'.ljust(15))
        print('-'*20)

    def show_genpelicula_header(self, header):
        print(header.center(38,'*'))
        print('ID'.ljust(3)+'|'+'Genero'.ljust(15)+'|'+'ID'.ljust(3)+'|'+'Pelicula'.ljust(15))
        print('-'*38)

    def show_genero_midder(self):
        print('-'*20)
    
    def show_genero_footer(self):
        print('-'*20)

    def show_genpelicula_midder(self):
        print('-'*38)
    
    def show_genpelicula_footer(self):
        print('-'*38)



   #*****************
   #* Clients Menus *
   #*****************

    def client_menu(self):
        print('*************************')
        print('* -- Submenu Clients -- *')
        print('*************************')
        print('1. Agregar Cliente')
        print('2. Mostrar Cliente')
        print('3. Mostrar todas los Clientes')
        print('4. Editar Cliente')
        print('5. Eliminar Cliente')
        print('6 Registro de compras de Cliente')
        print('7. Regresar')
 
    
    def show_a_client(self, record):
        print(f'{record[0]:<3}|{record[1]:<30}|{record[2]:<15} {record[3]:<15}|{record[4]:<20}|{record[6]:<40}|{record[5]}')
    
    def show_client_header(self, header):
        print(header.center(150,'*'))
        print('ID'.ljust(3)+'|'+'Nombre'.ljust(30)+'|'+'Apellido'.ljust(31)+'|'+'Nacionalidad'.ljust(20)+'|'+'Correo'.ljust(40)+'|'+'Año de nacimeinto'.ljust(9))
        print('-'*150)

    def show_client_midder(self):
        print('-'*150)
    
    def show_client_footer(self):
        print('-'*150) 

    """
    ********************
    * A view for Salas *
    ********************
    """

    def Sala_menu(self):
        print('***********************')
        print('* -- Submenu Salas -- *')
        print('***********************')
        print('1. Agregar Sala')
        print('2. Mostrar Sala')
        print('3. Mostrar todas las salas')
        print('4  Motrar sala por capacidad')
        print('5  Actualizar sala ')
        print('6  Eliminar sala ')
        print('7  Regresar')
    
    def show_a_sala(self, record):
        print(f'{record[0]:<5}|{record[3]:<9}')
    
    def show_sala_header(self, header):
        print(header.center(15,'*'))
        print('Sala'.ljust(5)+'|'+'Asientos'.ljust(9))
        print('-'*15)

    def show_sala_midder(self):
        print('-'*15)
    
    def show_sala_footer(self):
        print('-'*15)

    
    def show_sala_header_e(self, header):
        print(header.center(25,'*'))
        print('Sala'.ljust(5)+'|'+'Filas'.ljust(9)+'|'+'Columnas'.ljust(9))
        print('-'*25)

    def show_a_sala_e(self, record):
        print(f'{record[0]:<5}|{record[1]:<9}|{record[2]:<9}')
    def show_sala_midder_e(self):
        print('-'*25)
    
    def show_sala_footer_e(self):
        print('-'*25)


    """
    *********************
    * A view for Admins *
    *********************
    """

    
    def admin_a_menu(self):
        print('*************************')
        print('* -- Submenu Admins -- *')
        print('*************************')
        print('1. Agregar Administrador')
        print('2. Mostrar Administrador')
        print('3. Mostrar todas los Administradores')
        print('4. Editar Administrador')
        print('5. Eliminar Administrador')
        print('6. Registro de compra de administrador')
        print('7. Regresar')

    def show_a_admin(self, record):
        print(f'{record[0]:<3}|{record[1]:<30}|{record[2]:<15} {record[3]:<15}|{record[4]:<20}|{record[6]:<40}|{record[5]}')
    
    def show_admin_header(self, header):
        print(header.center(150,'*'))
        print('ID'.ljust(3)+'|'+'Nombre'.ljust(30)+'|'+'Apellido'.ljust(31)+'|'+'Nacionalidad'.ljust(20)+'|'+'Correo'.ljust(40)+'|'+'Año de nacimeinto'.ljust(9))
        print('-'*150)

    def show_admin_midder(self):
        print('-'*150)
    
    def show_admin_footer(self):
        print('-'*150)

    """
    **********************
    * Vista de cartelera *
    **********************
    """

    def cartelera_menu(self):
        print('***************************')
        print('* -- Submenu Cartelera -- *')
        print('***************************')
        print('1. Agregar Pelicula a cartelera')
        print('2. Mostrar Cartelera')
        print('3. Mostrar Horario de pelicula')
        print('4. Editar cartelera')
        print('5  Eliminar pelicula de cartelera ')
        print('6  Regresar')
    

    def show_a_cartelera(self, record):
        if len(record) ==3:
            print(f'{record[0]:<4}|{record[1]:<20}|{record[2]}')
        if len(record) ==4:
            print(f'{record[0]:<4}|{record[1]:<20}|{record[2]}|{record[3]}')
        if len(record) ==5:
            print(f'{record[0]:<4}|{record[1]:<20}|{record[2]}|{record[3]}|{record[4]}')
        if len(record) ==6:
            print(f'{record[0]:<4}|{record[1]:<20}|{record[2]}|{record[3]}|{record[4]}|{record[5]}')
        if len(record) ==7:
            print(f'{record[0]:<4}|{record[1]:<20}|{record[2]}|{record[3]}|{record[4]}|{record[5]}|{record[6]}')
        if len(record) ==8:
            print(f'{record[0]:<4}|{record[1]:<20}|{record[2]}|{record[3]}|{record[4]}|{record[5]}|{record[6]}|{record[7]}')
        if len(record) ==9:
            print(f'{record[0]:<4}|{record[1]:<20}|{record[2]}|{record[3]}|{record[4]}|{record[5]}|{record[6]}|{record[7]}|{record[8]}')
        if len(record) ==10:
            print(f'{record[0]:<4}|{record[1]:<20}|{record[2]}|{record[3]}|{record[4]}|{record[5]}|{record[6]}|{record[7]}|{record[8]}|{record[9]}')
    
    def show_cartelera_header(self, header):
        print(header.center(65,'*'))
        print('Sala'.ljust(3)+'|'+'Pelicula'.ljust(20)+'|'+'Hoario'.ljust(6))
        print('-'*65)

    def show_cartelera_midder(self):
        print('-'*65)
    
    def show_cartelera_footer(self):
        print('-'*65)

    
    ###################################
    def show_a_cartelera2(self, record):
        if len(record) ==3:
            print(f'{record[0]:<4}|{record[1]:<20}|{record[2]:<5}  |{record[3]}')
        if len(record) ==4:
            print(f'{record[0]:<4}|{record[1]:<20}|{record[2]:<5}  |{record[3]}|{record[4]}')
        if len(record) ==5:
            print(f'{record[0]:<4}|{record[1]:<20}|{record[2]:<5}  |{record[3]}|{record[4]}|{record[5]}')
        if len(record) ==6:
            print(f'{record[0]:<4}|{record[1]:<20}|{record[2]:<5}  |{record[3]}|{record[4]}|{record[5]}|{record[6]}')
        if len(record) ==7:
            print(f'{record[0]:<4}|{record[1]:<20}|{record[2]:<5}  |{record[3]}|{record[4]}|{record[5]}|{record[6]}|{record[7]}')
        if len(record) ==8:
            print(f'{record[0]:<4}|{record[1]:<20}|{record[2]:<5}  |{record[3]}|{record[4]}|{record[5]}|{record[6]}|{record[7]}|{record[8]}')
        if len(record) ==9:
            print(f'{record[0]:<4}|{record[1]:<20}|{record[2]:<5}  |{record[3]}|{record[4]}|{record[5]}|{record[6]}|{record[7]}|{record[8]}|{record[9]}')
        if len(record) ==10:
            print(f'{record[0]:<4}|{record[1]:<20}|{record[2]:<5}  |{record[3]}|{record[4]}|{record[5]}|{record[6]}|{record[7]}|{record[8]}|{record[9]}|{record[10]}')

    
    def show_cartelera2_header(self, header):
        print(header.center(68,'*'))
        print('Sala'.ljust(3)+'|'+'Pelicula'.ljust(20)+'|'+'ID'.ljust(3)+'|'+'Hoario'.ljust(6))
        print('-'*68)

    def show_cartelera2_midder(self):
        print('-'*68)
    
    def show_cartelera2_footer(self):
        print('-'*68)


    def show_asientos(self,asientos):

        k = len(asientos[0])

        print(' Pantalla '.center((k*7)-6,'-'))
        for i in range(len(asientos)):
            print(asientos[i])
    
    def error_asiento(self):
        print('Asiento ocupado, ingrese otro')
    
    def asiento_no_valido(self):
        print('Ingresa un asiento valido o ingresa 0 para cancelar')

    def numero_asientos(self):
        print('Ingrese asiento a reservar o 0 para regresar')

    def contador_boleto(self,contador,numero):
        print('Boleto ',contador,' de ',numero)

    def show_boleto_header(self, header):
        print(header.center(20,'-'))

    def show_boleto_sala_header(self, header):
        print('Sala')
        print(header.center(20,' '))

    def show_boleto_pelicula_header(self, header):
        print('Pelicula')
        print(header.center(20,' '))

    def show_boleto_hora_header(self, header):
        print('Hora')
        print(header.center(20,' '))

    def show_boleto_asiento_header(self, header):
        print('Asiento')
        print(header.center(20,' '))
    def show_boleto_fecha_header(self, header):
        print('Fecha')
        print(header.center(20,' '))
    
    def show_boleto_footer(self):
        print('-'*20)


    def Registro_menu(self):
        print('**************************')
        print('* -- Submenu Registro -- *')
        print('**************************')
        print('1. Todos los boletos comprados')
        print('2. Boletos comprados por fecha')
        print('3. Reimprimir boleto')
        print('4  Regresar')
    
    def show_a_Registro(self, record):
        print(f'{record[4]:<4}|{record[2]:<20}|{record[5]}  |{record[1]:<8}|{record[6]}')

    def show_Registro_header(self, header):
        print(header.center(68,'*'))
        print('Sala'.ljust(3)+'|'+'Pelicula'.ljust(20)+'|'+'Hora'.ljust(10)+'|'+'Asiento'.ljust(8)+'|'+'Fecha'.ljust(6))
        print('-'*68)

    def show_Registro_midder(self):
        print('-'*68)
    
    def show_Registro_footer(self):
        print('-'*68)
