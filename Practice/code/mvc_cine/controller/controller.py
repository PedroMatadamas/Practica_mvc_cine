from model.model import Model
from view.view import View
from datetime import date
from datetime import datetime

 
class Controller:
    """
    *******************************
    * A controller for a store DB *
    *******************************
    """
    def __init__(self):
        self.model = Model()
        self.view = View()
    
    def start(self):
        self.view.start()
        self.user_menu()

    """
    ***********************
    * General controllers *
    ***********************
    """  
    def user_menu(self):
        o = '0'
        while o != '5':
            self.view.user_menu()
            self.view.option('5')
            o = input()
            if o == '1':
                self.client_menu()
            elif o == '2':
                self.anonimo_menu()
            elif o == '3':
                self.main_menu()
            elif o == '4':
                self.tipe_user_menu()
            elif o == '5':
                self.view.end()
            else:
                self.view.not_valid_option()
        return

    def ask_session(self):
        self.view.ask('Ingrese Correo: ')
        id_usr = input()
        self.view.ask('Ingrese Contraseña: ')
        Pass = input()
        return [id_usr,Pass]

    def ask_session_client(self):
        self.view.ask('Ingrese Correo: ')
        correo = input()
        self.view.ask('Ingrese Contraseña: ')
        Pass = input()
        return [correo,Pass]

    def gerent_session(self):
        gerentes = self.model.read_all_admin()
        correo, Pass = self.ask_session_client()

        com = 0
        for gerente in gerentes:
            if ( str(gerente[6]) == str(correo) and str(gerente[7]) == str(Pass)):
               com =1
        if com == 1:
            return True
        else:
            return False

    def main_menu(self):

        admin = self.gerent_session()
        if admin == True:
            o = '0'
            while o != '9':
                self.view.main_menu()
                self.view.option('10')
                o = input()
                if o == '1':
                    self.movies_menu()
                elif o == '2':
                    self.actors_menu()
                elif o == '3':
                    self.director_menu()
                elif o == '4':
                    self.genero_menu()
                elif o == '5':
                    self.client_account_menu()
                elif o == '6':
                    self.admin_account_menu()
                elif o == '7':
                    self.salas_menu()
                elif o == '8':
                    self.cartelera_menu()
                elif o == '9':
                    self.comprar_boleto()
                elif o == '10':
                    self.Registro_menu()
                    pass
                elif o == '11':
                    self.view.end()
                    o = '9'
                    return
                else:
                    self.view.not_valid_option()
            return
        else:
            self.view.error('Error de inicio de sesion de administrador')
            return

    def Registro_menu(self):
        o = '0'
        while o != '4':
            self.view.Registro_menu()
            self.view.option('4')
            o = input()
            if o == '1':
                self.read_all_boletos()
            elif o == '2':
                self.read_all_boletos_date()
            elif o == '3':
                self.reimprimir_boleto()
            elif o == '4':
                return
            else:
                self.view.not_valid_option()
        return

    def client_session(self):
        correo, Pass = self.ask_session_client()
        cliente = self.model.read_all_clients()
        band =0
        for client in cliente:
            if ( str(client[5]) == str(correo) and str(client[6]) == str(Pass)):
               band =1
        if band == 1:
            return True
        else:
            return False

    def client_menu(self):
        client = self.client_session()
        today = date.today()

        if client == True:
            o = '0'
            while o != '6':
                self.view.main_menu_client()
                self.view.option('6')
                o = input()
                if o == '1':
                    self.read_carteleras(today,0) 
                elif o == '2':
                    self.horario_pelicula()
                elif o == '3':
                    self.comprar_boleto()                
                elif o == '4':
                    self.Registro_menu()
                elif o == '5':
                    self.extra_menu()
                elif o == '6':
                    return
                else:
                    self.view.not_valid_option()
            return
        else:
            self.view.error('Error de inicio de sesion')
            return

    def anonimo_menu(self):
        o = '0'
        today = date.today()

        while o != '5':
            self.view.main_menu_anonimo()
            self.view.option('5')
            o = input()
            if o == '1':
                self.read_carteleras(today,0) 
            elif o == '2':
                self.horario_pelicula()
            elif o == '3':
                self.comprar_boleto()                #si son 3 formas de sesion cada una lo llama ahorita trabajamos con el cliente sin cuenta 
            elif o == '4':
                self.extra_menu()
            elif o == '5':
                return
            else:
                self.view.not_valid_option()
        return


    def extra_menu(self):
        self.view.extra_menu()
        self.view.option('5')
        o = input()
        if o == '1':
            self.movies_menu_client()
        elif o == '2':
            self.actors_menu_client()
        elif o == '3':
            self.director_menu_client()
        elif o == '4':
            self.genero_menu_client()
        elif o == '5':
            return
        else:
            self.view.not_valid_option()

    def update_lists(self, fs , vs):
        fields = []
        vals = []
        for f,v in zip(fs,vs):
            if v != '':
                fields.append(f+' = %s')
                vals.append(v)
        return fields, vals


    """
    ********************
    * Users for movies *
    ********************
    """


    def tipe_user_menu(self):
        user = '0'
        while user != '3':
            self.view.user_type_menu()
            user = input()
            if user == '1':
                self.create_a_client()
            if user == '2':
                self.create_a_admin()
            elif user == '3':
                return
            else:
                self.view.not_valid_option()
        return


    


  
    

    """
    **********************
    * General for movies *
    **********************
    """


    def movies_menu_client(self):
        o = '0'
        while o != '5':
            self.view.movies_menu_client()
            self.view.option('5')
            o = input()
            if o == '1':
                self.read_a_movie()
            elif o == '2':
                self.read_all_movies()
            elif o == '3':
                self.read_all_details()
            elif o == '4':
                self.read_details()
            elif o == '5':
                return
            else:
                self.view.not_valid_option()
        return

    def movies_menu(self):
        o = '0'
        while o != '12':
            self.view.movies_menu()
            self.view.option('12')
            o = input()
            if o == '1':
                self.create_a_movie()
            elif o == '2':
                self.read_a_movie()
            elif o == '3':
                self.read_all_movies()
            elif o == '4':
                self.read_all_details()
            elif o == '5':
                self.read_details()
            elif o == '6':
                self.add_details()
            elif o == '7':
                self.edit_details()
            elif o == '8':
                self.update_pelicula()
            elif o == '9':
                self.delete_detail()
            elif o == '10':
                self.delete_movie()
            elif o == '11':
                return
            else:
                self.view.not_valid_option()
        return

    def ask_movie(self):
        self.view.ask('Titulo: ')
        Titulo = input()
        self.view.ask('Idioma: ')
        Idioma = input()
        self.view.ask('Subtitulo: ')
        Subtitulo = input()
        return [Titulo,Idioma,Subtitulo]

    def ask_detail(self):
        self.view.ask('id Titutlo: ')
        id_pelicula= input()
        self.view.ask('Id Director: ')
        id_director = input()
        self.view.ask('Descripcion: ')
        descripcion = input()
        self.view.ask('Duracion: ')
        duracion = input()
        self.view.ask('Año: ')
        año = input()
        return [id_pelicula,id_director, descripcion,duracion,año]
    
    def create_a_movie(self):
        Titulo,Idioma,Subtitulo = self.ask_movie()
        out = self.model.create_movie(Titulo,Idioma,Subtitulo)
        if out == True:
            self.view.ok(Titulo, 'agrego')
        else:
            self.view.error('No se pudo agregar la pelicula')
        return

    def read_a_movie(self):
        self.view.ask('ID de pelicula: ')
        i_movie = input()
        movie = self.model.read_a_movie(i_movie)
        if type(movie) == tuple:
            self.view.show_movie_header('Datos de la pelicula  '+i_movie+' ')
            self.view.show_a_movie(movie)
            self.view.show_movie_midder()
            self.view.show_movie_footer()
        else:
            if movie == None:
                self.view.error('La pelicula no existe')
            else:
                self.view.error(' Hay un problema al leer la pelicula ')
        return
    
    def read_all_movies(self):
        movies = self.model.read_all_movies()
        if type(movies) ==  list:
            self.view.show_movie_header(' Todos las peliculas ')
            for movie in movies:
                self.view.show_a_movie(movie)
            self.view.show_movie_midder()
            self.view.show_movie_footer()
        else:
            self.view.error('Hay un problema todas las peliculas ')

    def read_movie_year(self):
        self.view.ask('año de la pelicula: ')
        year = input()
        movies = self.model.read_a_movies_year(year)
        if type(movies) == list:
            self.view.show_movie_header('Peliculas del año  '+year+' ')
            for movie in movies:
                self.view.show_a_movie(movie)
            self.view.show_movie_footer()
        else:
            if movies == []:
                self.view.error('No hay pelicula del año '+year)
            else:
                self.view.error(' Hay un problema al leer las peliculas del año '+year)
        return

    def add_details(self):
        self.read_all_movies()
        self.read_all_directors()
        dp_id_pelicula, dp_id_director, descripcion,dp_duracion,año = self.ask_detail()
        out = self.model.create_detalles_pelicula(dp_id_pelicula, dp_id_director, descripcion,dp_duracion,año)
        if out == True:
            self.view.ok(dp_id_pelicula, 'agrego')
        else:
            if out == 1062:
                self.view.error('ya existe una descripcion')
            else:
                self.view.error('No se pudo agregar la pelicula')
        return

    def read_details(self):
        self.read_all_movies()
        self.view.ask('ID de pelicula: ')
        i_movie = input()
        details = self.model.read_detalles_pelicula(i_movie)
        if type(details) == list:
            if details == []:
                self.view.error('La pelicula no cuenta con una descripcion ')
                return
            self.view.show_detail_header('Description de la pelicula  '+details[0][1]+' ')
            for detail in details:
                self.view.show_a_detail(detail)
            self.view.show_detail_midder()
            self.view.show_detail_footer()
        actors = self.model.read_a_mov_ac(i_movie)
        if type(actors) ==  list:
            self.view.show_actor_header(' Actores de la pelicula ')
            for actor in actors:
                self.view.show_a_actor(actor)
            self.view.show_actor_midder()
            self.view.show_actor_footer()
        else:
            self.view.error('Hay un problema todas los actores ')
        generos = self.model.read_a_peliculagen(i_movie )
        if generos == []:
            self.view.error('No existe el genero')
            return
        else:
            if type(generos) == list:
                self.view.show_genero_header('Generos de la pelicula ')
                for genero in generos:
                    self.view.show_a_genero(genero)
                self.view.show_genero_footer()
            else:
                if generos == []:
                    self.view.error('La pelicula no contiene generos')
                else:
                    self.view.error(' Hay un problema al leer los generos de la pelicula')



    def read_all_details(self):
        movies = self.model.read_all_detalles_pelicula()
        if type(movies) ==  list:
            self.view.show_detail_header(' Todos las descripciones ')
            for movie in movies:
                self.view.show_a_detail(movie)
            self.view.show_detail_midder()
            self.view.show_detail_footer()
        else:
            self.view.error('Hay un problema al leer todas las decripciones ')       

    def edit_details(self):
        self.view.ask(' ID de descripcion de pelicula: ')
        i_desc = input()
        details = self.model.read_detalles_pelicula(i_desc)
        if type(details) == list:
            self.view.show_detail_header('Description de la pelicula  '+details[0][1]+' ')
            for detail in details:
                self.view.show_a_detail(detail)
            self.view.show_detail_midder()
            self.view.show_detail_footer()
        else:
            if details == None:
                self.view.error('No existe la descricion')
            else:
                self.view.error('Problema al leer la descripcion')
            return

        self.view.msg('Ingresa los valores a modificar ( vacio para dejarlo igual ):')
        whole_vals = self.ask_detail()
        fields, vals = self.update_lists(['dp_id_pelicula', 'dp_id_director', 'descripcion','dp_duracion'],whole_vals)
        vals.append(i_desc)
        vals = tuple(vals)
        out = self.model.update_detalles_pelicula(fields,vals)
        if out == True:
            self.view.ok(i_desc, 'atualizo')
        else:
            self.view.error('No se pudo actualizar')
        return        

    def delete_detail(self):
        self.view.ask('ID de detalle a borrar: ')
        dp_id_pelicula = input()
        count = self.model.delate_detalles_prlicula(dp_id_pelicula)
        if count != 0:
            self.view.ok(dp_id_pelicula, 'Borro')
        else:
            if count == 0:
                self.view.error('La pelicula no exite')
            else:
                self.view.error('Prblema al borrar la pelicula')
        return

    def update_pelicula(self):
        self.view.ask(' ID de pelicula a modificar: ')
        id_pelicula = input()
        movie = self.model.read_a_movie(id_pelicula)
        if type(movie) == tuple:
            self.view.show_movie_header('Datos de la pelicula  '+id_pelicula+' ')
            self.view.show_a_movie(movie)
            self.view.show_movie_midder()
            self.view.show_movie_footer()
        else:
            if movie == None:
                self.view.error('La pelicula no existe')
            else:
                self.view.error('Problema al leer la pelicula')
            return
        self.view.msg('Ingresa los valores a modificar ( vacio para dejarlo igual ):')
        whole_vals = self.ask_movie()
        fields, vals = self.update_lists(['p_titulo','p_idioma','p_subtitulos','p_año'],whole_vals)
        vals.append(id_pelicula)
        vals = tuple(vals)
        out = self.model.update_movie(fields,vals)
        if out == True:
            self.view.ok(id_pelicula, 'atualizo')
        else:
            self.view.error('No se pudo actualizar')
        return

    def delete_movie(self):
        self.view.ask('ID de pelicula a borrar: ')
        id_pelicula = input()
        count = self.model.delete_movie(id_pelicula)
        if count != 0:
            self.view.ok(id_pelicula, 'Borro')
        else:
            if count == 0:
                self.view.error('La pelicula no exite')
            else:
                self.view.error('Prblema al borrar la pelicula')
        return


    """
    **********************
    * General for actors *
    **********************
    """

    def actors_menu_client(self):
        o = '0'
        while o != '5':
            self.view.actors_menu_client()
            self.view.option('5')
            o = input()
            if o == '1':
                self.read_a_actor()
            elif o == '2':
                self.read_all_actor()
            elif o == '3':
                self.read_movie_actor()
            elif o == '4':
                self.read_a_actor_nacionality()                
            elif o == '5':
                return
            else:
                self.view.not_valid_option()
        return

    def actors_menu(self):
        o = '0'
        while o != '10':
            self.view.actors_menu()
            self.view.option('10')
            o = input()
            if o == '1':
                self.create_a_actor()
            elif o == '2':
                self.read_a_actor()
            elif o == '3':
                self.read_all_actor()
            elif o == '4':
                self.read_movie_actor()
            elif o == '5':
                self.read_a_actor_nacionality()                
            elif o == '6':
                self.update_actor()
            elif o == '7':
                self.add_movie()
            elif o == '8':
                self.del_movie()
            elif o == '9':
                self.delete_actor()
            elif o == '10':
                return
            else:
                self.view.not_valid_option()
        return

    def ask_actor(self):
        self.view.ask('Nombre: ')
        Nombre = input()
        self.view.ask('Apellido Paterno: ')
        ApellidoPat = input()
        self.view.ask('Apellido Materno: ')
        ApellidoMat = input()
        self.view.ask('Nacionalidad: ')
        Nacionalidad = input()
        self.view.ask('Fecha de nacimiento: ')
        Año = input()        
        return [Nombre,ApellidoPat,ApellidoMat,Nacionalidad,Año]
    
    def create_a_actor(self):
        Nombre,ApellidoPat,ApellidoMat,Nacionalidad,Año = self.ask_actor()
        out = self.model.create_actor(Nombre,ApellidoPat,ApellidoMat,Nacionalidad,Año)
        if out == True:
            self.view.ok(Nombre+' '+ApellidoPat, ' se agrego')
        else:
            self.view.error('No se pudo agregar el actor')
        return

    def read_a_actor(self):
        self.view.ask('ID de Actor: ')
        i_actor = input()
        actor = self.model.read_a_actor(i_actor)
        if type(actor) == tuple:
            self.view.show_movie_header('Datos del actor  '+i_actor+' ')
            self.view.show_a_actor(actor)
            self.view.show_actor_midder()
            self.view.show_actor_footer()
        else:
            if actor == None:
                self.view.error('El actor no existe')
            else:
                self.view.error(' Hay un problema al leer el actor ')
        return

    def read_a_actor_nacionality(self):
        self.view.ask('Nacionalidad: ')
        nacionality = input()
        actors = self.model.read_a_actor_nacionalidad(nacionality)
        if type(actors) == list:
            self.view.show_actor_header('Peliculas del año  '+nacionality+' ')
            for actor in actors:
                self.view.show_a_actor(actor)
            self.view.show_actor_footer()
        else:
            if actors == []:
                self.view.error('No hay actores de la nacionalidad '+nacionality)
            else:
                self.view.error(' Hay un problema al leer las nacionalidades '+nacionality)
        return
    
    def read_all_actor(self):
        actors = self.model.read_all_actor()
        if type(actors) ==  list:
            self.view.show_actor_header(' Todos los actores ')
            for actor in actors:
                self.view.show_a_actor(actor)
            self.view.show_actor_midder()
            self.view.show_actor_footer()
        else:
            self.view.error('Hay un problema todas los actores ')

    def read_movie_actor(self):
        self.view.ask('ID del actor: ')
        i_actor = input()
        movies = self.model.read_a_ac_mov(i_actor)
        if type(movies) == list:
            self.view.show_movie_header('Peliculas del actor ')
            for movie in movies:
                self.view.show_a_movie(movie)
            self.view.show_movie_footer()
        else:
            if movies == []:
                self.view.error('No hay pelicula del actor')
            else:
                self.view.error(' Hay un problema al leer las peliculas del actor')
        return
    
    def update_actor(self):
        self.view.ask(' ID de ator a modificar: ')
        id_actor = input()
        actor = self.model.read_a_actor(id_actor)
        if type(actor) == tuple:
            self.view.show_movie_header('Datos del actor  '+actor[1]+' ')
            self.view.show_a_actor(actor)
            self.view.show_actor_midder()
            self.view.show_actor_footer()
        else:
            if actor == None:
                self.view.error('El actor no existe')
            else:
                self.view.error('Problema al leer el actor')
            return
        self.view.msg('Ingresa los valores a modificar ( vacio para dejarlo igual ):')
        whole_vals = self.ask_actor()
        fields, vals = self.update_lists(['a_nombre','a_apellidoPat','a_apellidoMat','a_nacionalidad','a_fnacimiento'],whole_vals)
        vals.append(id_actor)
        vals = tuple(vals)
        out = self.model.update_actor(fields,vals)
        if out == True:
            self.view.ok(id_actor, 'atualizo')
        else:
            self.view.error('No se pudo actualizar')
        return

    def add_movie(self):
        movies = self.model.read_all_movies()
        if type(movies) ==  list:
            self.view.show_movie_header(' Todos las peliculas ')
            for movie in movies:
                self.view.show_a_movie(movie)
            self.view.show_movie_midder()
            self.view.show_movie_footer()
        else:
            self.view.error('Hay un problema todas las peliculas ')
        self.view.ask('ID de actor: ')
        id_actor= input()
        self.view.ask('ID de pelicula: ')
        id_movie = input()
        out = self.model.create_ac_mov(id_actor,id_movie)
        if out == True:
            self.view.ok(id_movie , 'Se agrego la pelicula al actor')
        else:
            self.view.error('No se pudo agregar')
        return        

    def del_movie(self):
        self.view.ask('ID de actor a borrar: ')
        id_actor = input()
        self.view.ask('ID de pelicula a borrar: ')
        id_movie = input()
        count = self.model.delete_ac_mov(id_actor,id_movie)
        if count != 0:
            self.view.ok(id_actor, 'Borro')
        else:
            if count == 0:
                self.view.error('El actor no exite')
            else:
                self.view.error('Prblema al borrar la pelicula del actor')
        return

    def delete_actor(self):
        self.view.ask('ID de actor a borrar: ')
        id_actor = input()
        count = self.model.delete_actor(id_actor)
        if count != 0:
            self.view.ok(id_actor, 'Borro')
        else:
            if count == 0:
                self.view.error('El actor no exite')
            else:
                self.view.error('Prblema al borrar el actor')
        return
    """
    ************************
    * General for director *
    ************************
    """

    def director_menu_client(self):
        o = '0'
        while o != '8':
            self.view.directors_menu_client()
            self.view.option('8')
            o = input()
            if o == '1':
                self.read_a_director()
            elif o == '2':
                self.read_all_directors()
            elif o == '3':
                self.read_a_director_nacionality()                
            elif o == '4':
                self.read_director_movies()
            elif o == '5':
                return
            else:
                self.view.not_valid_option()
        return

    def director_menu(self):
        o = '0'
        while o != '8':
            self.view.directors_menu()
            self.view.option('8')
            o = input()
            if o == '1':
                self.create_a_director()
            elif o == '2':
                self.read_a_director()
            elif o == '3':
                self.read_all_directors()
            elif o == '4':
                self.read_a_director_nacionality()                
            elif o == '5':
                self.read_director_movies()
            elif o == '6':
                self.edit_director()
            elif o == '7':
                self.del_director()
            elif o == '8':
                return
            else:
                self.view.not_valid_option()
        return

    def ask_director(self):
        self.view.ask('Nombre: ')
        Nombre = input()
        self.view.ask('Apellido Paterno: ')
        ApellidoPat = input()
        self.view.ask('Apellido Materno: ')
        ApellidoMat = input()
        self.view.ask('Nacionalidad: ')
        Nacionalidad = input()      
        self.view.ask('Fecha de nacimiento: ')
        año = input()       
        self.view.ask('Estudios: ')
        Estudios = input() 
        return [Nombre,ApellidoPat,ApellidoMat,Nacionalidad,año,Estudios]
    
    def create_a_director(self):
        Nombre,ApellidoPat,ApellidoMat,Nacionalidad,año,Estudios = self.ask_director()
        out = self.model.create_director(Nombre,ApellidoPat,ApellidoMat,Nacionalidad,año,Estudios)
        if out == True:
            self.view.ok(Nombre+' '+ApellidoPat, ' se agrego')
        else:
            self.view.error('No se pudo agregar el actor')
        return

    def read_a_director(self):
        self.view.ask('ID de Director: ')
        i_director = input()
        director = self.model.read_a_director(i_director)
        if type(director) == tuple:
            self.view.show_director_header('Datos del director  '+i_director+' ')
            self.view.show_a_director(director)
            self.view.show_director_midder()
            self.view.show_director_footer()
        else:
            if director == None:
                self.view.error('El director no existe')
            else:
                self.view.error(' Hay un problema al leer el director ')
        return

    def read_a_director_nacionality(self):
        self.view.ask('Nacionalidad: ')
        nacionality = input()
        directors = self.model.read_a_director_nacionalidad(nacionality)
        if type(directors) == list:
            self.view.show_director_header('Directores de la nacionalidad: '+nacionality+' ')
            for actor in directors:
                self.view.show_a_actor(actor)
            self.view.show_actor_footer()
        else:
            if directors == []:
                self.view.error('No hay directores de la nacionalidad '+nacionality)
            else:
                self.view.error(' Hay un problema al leer las nacionalidades '+nacionality)
        return
    
    def read_all_directors(self):
        directors = self.model.read_all_director()
        if type(directors) ==  list:
            self.view.show_director_header(' Todos los directores ')
            for director in directors:
                self.view.show_a_director(director)
            self.view.show_director_midder()
            self.view.show_director_footer()
        else:
            self.view.error('Hay un problema todas los actores ')

    def read_director_movies(self):
        self.view.ask('ID del director: ')
        id_director = input()
        movies = self.model.read_a_dir_mov(id_director)
        if movies == []:
            self.view.error('No existe el director')
            return
        else:
            if type(movies) == list:
                self.view.show_movie_header('Peliculas del director ')
                for movie in movies:
                    self.view.show_a_movie(movie)
                self.view.show_movie_footer()
            else:
                if movies == []:
                    self.view.error('No hay pelicula del director')
                else:
                    self.view.error(' Hay un problema al leer las peliculas del director')
            return
    
    def edit_director(self):
        self.view.ask(' ID de director a modificar: ')
        id_director = input()
        director = self.model.read_a_director(id_director)
        if type(director) == tuple:
            self.view.show_director_header('Datos del director  '+id_director+' ')
            self.view.show_a_director(director)
            self.view.show_director_midder()
            self.view.show_director_footer()
        else:
            if director == None:
                self.view.error('El director no existe')
            else:
                self.view.error(' Hay un problema al leer el director ')
            return
        self.view.msg('Ingresa los valores a modificar ( vacio para dejarlo igual ):')
        whole_vals = self.ask_director()
        fields, vals = self.update_lists(['d_nombre','d_apellidoPat','d_apellidoMat','d_nacionalidad','d_fnacimiento','d_educacion'],whole_vals)
        vals.append(id_director)
        vals = tuple(vals)
        out = self.model.update_director(fields,vals)
        if out == True:
            self.view.ok(id_director, 'atualizo')
        else:
            self.view.error('No se pudo actualizar')
        return


    def del_director(self):
        self.view.ask('ID de director a borrar: ')
        id_director = input()
        count = self.model.delete_director(id_director)
        if count != 0:
            self.view.ok(id_director, 'Borro')
        else:
            if count == 0:
                self.view.error('El director no exite')
            else:
                self.view.error('Prblema al borrar el director')
        return

    """
    ************************
    * General for genero *
    ************************
    """

    def genero_menu_client(self):
        o = '0'
        while o != '3':
            self.view.generos_menu_client()
            self.view.option('3')
            o = input()
            if o == '1':
                self.read_all_generos() 
            elif o == '2':
                self.read_all_generos_pelicula()                 
            elif o == '3':
                return
            else:
                self.view.not_valid_option()
        return

    def genero_menu(self):
        o = '0'
        while o != '10':
            self.view.generos_menu()
            self.view.option('10')
            o = input()
            if o == '1':
                self.create_a_genero()
            elif o == '2':
                self.add_genero_pelicula()
            elif o == '3':
                self.read_a_genero()
            elif o == '4':
                self.read_all_generos() 
            elif o == '5':
                self.update_genero()
            elif o == '6':
                self.update_genero_pelicula()
            elif o == '7':
                self.read_all_generos_pelicula()                 
            elif o == '8':
                self.delete_genero()
            elif o == '9':
                self.delete_genero_pelicula()
            elif o == '10':
                return
            else:
                self.view.not_valid_option()
        return

    def ask_genpelicula(self):
        self.view.ask('Genero: ')
        Genero = input()
        self.view.ask('Pelicula: ')
        Pelicula = input()
        return[Genero, Pelicula]

    def ask_genero(self):
        self.view.ask('Genero: ')
        Genero = input()
        return(Genero)
    
    def ask_genero2(self):
        self.view.ask('Genero: ')
        Genero = input()
        return[Genero]

    def create_a_genero(self):
        Genero = self.ask_genero()
        out = self.model.create_gen(Genero)
        if out == True:
            self.view.ok(Genero, ' se agrego')
        else:
            self.view.error('No se pudo agregar el genero')
        return

    def add_genero_pelicula(self):
        self.read_all_movies()
        self.read_all_generos()
        Genero, Pelicula = self.ask_genpelicula()
        out = self.model.create_generos_peliculas(Genero, Pelicula)
        if out == True:
            self.view.ok(Genero+' '+Pelicula, ' se agrego')
        else:    
            self.view.error('No se pudo agregar el genero a la pelicula')
        return

    def read_a_genero(self):
        self.view.ask('ID de Genero: ')
        i_genero = input()
        genero = self.model.read_a_genero(i_genero)
        if type(genero) == tuple:
            self.view.show_genero_header('Genero  '+i_genero+' ')
            self.view.show_a_genero(genero)
            self.view.show_genero_midder()
            self.view.show_genero_footer()
        else:
            if genero == None:
                self.view.error('El genero no existe')
            else:
                self.view.error(' Hay un problema al leer el genero ')
        return
    
    def read_all_generos(self):
        generos = self.model.read_all_generos()
        if type(generos) ==  list:
            self.view.show_genero_header(' Todos los generos ')
            for genero in generos:
                self.view.show_a_genero(genero)
            self.view.show_genero_midder()
            self.view.show_genero_footer()
        else:
            self.view.error('Hay un problema con todos los generos ')
        return

    def read_all_generos_pelicula(self):
        self.read_all_movies()
        self.view.ask('ID de la pelicula: ')
        id_pelicula = input()
        generos = self.model.read_a_peliculagen(id_pelicula)
        if generos == []:
            self.view.error('No existe el genero')
            return
        else:
            if type(generos) == list:
                self.view.show_genero_header('Generos de la pelicula ')
                for genero in generos:
                    self.view.show_a_genero(genero)
                self.view.show_genero_footer()
            else:
                if generos == []:
                    self.view.error('La pelicula no contiene generos')
                else:
                    self.view.error(' Hay un problema al leer los generos de la pelicula')
            return

        
    def update_genero_pelicula(self):
        self.read_all_movies()
        self.view.ask(' ID de la pelicula a modificar: ')
        id_pelicula = input()
        generos = self.model.read_a_peliculagen(id_pelicula)
        if type(generos) ==  list:
            self.view.show_genero_header(' Todos los generos de la pelicula ')
            for genero in generos:
                self.view.show_a_genero(genero)
            self.view.show_genero_midder()
            self.view.show_genero_footer()
        else:
            self.view.error('Hay un problema con todos los generos ')
        self.view.ask(' ID de genero a modificar: ')
        id_genero = input()
        self.view.msg('Ingresa los valores a modificar ( vacio para dejarlo igual ):')
        whole_vals = self.ask_genpelicula()
        fields, vals = self.update_lists(['gp_id_genero', 'gp_id_pelicula'],whole_vals)
        vals.append(id_genero)
        vals.append(id_pelicula)
        vals = tuple(vals)
        out = self.model.update_genpelicula(fields,vals)
        if out == True:
            self.view.ok(id_genero, 'atualizo')
        else:
            self.view.error('No se pudo actualizar')
        return
        
    def update_genero(self):
        self.read_all_generos()
        self.view.ask(' ID de genero a modificar: ')
        id_genero = input()
        self.view.msg('Ingresa los valores a modificar ( vacio para dejarlo igual ):')
        whole_vals = self.ask_genero2()
        fields, vals = self.update_lists(['genero'],whole_vals)
        vals.append(id_genero)
        vals = tuple(vals)
        out = self.model.update_genero(fields,vals)
        
        if out == True:
            self.view.ok(id_genero, 'atualizo')
        else:
            self.view.error('No se pudo actualizar')
        return
    
    def delete_genero(self):
        self.view.ask('ID del genero a borrar: ')
        id_genero = input()
        count = self.model.delete_genero(id_genero)
        if count != 0:
            self.view.ok(id_genero, 'Borro')
        else:
            if count == 0:
                self.view.error('El genero no exite')
            else:
                self.view.error('Problema al borrar el genero')
        return

    def delete_genero_pelicula(self):
        self.read_all_movies()
        self.view.ask('ID de la pelicula para borrar genero: ')
        id_pelicula = input()




        generos = self.model.read_a_peliculagen(id_pelicula)
        if generos == []:
            self.view.error('No existe el genero')
            return
        else:
            if type(generos) == list:
                self.view.show_genero_header('Generos de la pelicula ')
                for genero in generos:
                    self.view.show_a_genero(genero)
                self.view.show_genero_footer()
            else:
                if generos == []:
                    self.view.error('La pelicula no contiene generos')
                else:
                    self.view.error(' Hay un problema al leer los generos de la pelicula')

        self.view.ask('ID del genero a borrar: ')
        id_genero = input()
        count = self.model.delete_genero_pelicula(id_genero, id_pelicula)
        if count != 0:
            self.view.ok(id_genero + ' ' +id_pelicula, 'Borro')
        else:
            if count == 0:
                self.view.error('La pelicula no contiene ese genero')
            else:
                self.view.error('Problema al borrar el genero de la pelicula')
        return

    """
    *******************
    * Clients mehtods *
    *******************
    """

    def ask_user(self):
        self.view.ask('Nombre: ')
        Nombre = input()
        self.view.ask('Apellido Paterno: ')
        ApellidoPat = input()
        self.view.ask('Apellido Materno: ')
        ApellidoMat = input()
        self.view.ask('Nacionalidad: ')
        Nacionalidad = input()
        self.view.ask('Fecha de nacimiento: ')
        Año = input()
        self.view.ask('Correo electronico: ')
        correo = input() 
        self.view.ask('Password: ')
        Pass = input()         
        return [Nombre,ApellidoPat,ApellidoMat,Nacionalidad,Año,correo,Pass]

    def create_a_client(self):
        Nombre,ApellidoPat,ApellidoMat,Nacionalidad,Año,correo,Pass = self.ask_user()
        out = self.model.create_client(Nombre,ApellidoPat,ApellidoMat,Nacionalidad,Año,correo,Pass)
        if out == True:
            self.view.ok(Nombre + ' '+ ApellidoPat+ ' ' +ApellidoMat, 'creo cunenta de cliente')
            self.start()
        else:
            self.view.error('No se pudo agregar el cliente')
        return

    def client_account_menu(self):
        o = '0'
        while o != '6':
            self.view.client_menu()
            self.view.option('6')
            o = input()
            if o == '1':
                self.create_a_client()
            elif o == '2':
                self.read_a_client()
            elif o == '3':
                self.read_all_clients()
            elif o == '4':
                self.edit_client()
            elif o == '5':
                self.delete_client()                
            elif o == '6':
                self.Registro_menu()
            elif o == '7':
                return
            else:
                self.view.not_valid_option()
        return

    def admin_account_menu(self):
        o = '0'
        while o != '6':
            self.view.admin_a_menu()
            self.view.option('6')
            o = input()
            if o == '1':
                self.create_a_admin()
            elif o == '2':
                self.read_a_admin()
            elif o == '3':
                self.read_all_admins()
            elif o == '4':
                self.edit_admin()
            elif o == '5':
                self.delete_admin()          
            elif o == '6':
                self.Registro_menu()         
            elif o == '7':
                return
            else:
                self.view.not_valid_option()
        return


    def read_a_client(self):
        self.view.ask('Correo de Cliente: ')
        id_client = input()
        client = self.model.read_a_client(id_client)
        if type(client) == tuple:
            self.view.show_client_header('Cliente  '+id_client+' ')
            self.view.show_a_client(client)
            self.view.show_client_midder()
            self.view.show_client_footer()
        else:
            if client == None:
                self.view.error('El cliente no existe')
            else:
                self.view.error(' Hay un problema al leer el cliente ')
        return


    def read_all_clients(self):
        clients = self.model.read_all_clients()
        if type(clients) ==  list:
            self.view.show_client_header(' Todos los clientes ')
            for client in clients:
                self.view.show_a_client(client)
            self.view.show_client_midder()
            self.view.show_client_footer()
        else:
            self.view.error('Hay un problema con todos los generos ')
        return

    def edit_client(self):
        self.model.read_all_clients()
        self.view.ask(' Correo de cliente a modificar: ')
        id_cliente = input()
        cliente = self.model.read_a_client(id_cliente)
        if type(cliente) == tuple:
            self.view.show_client_header('Datos del cliente  '+id_cliente+' ')
            self.view.show_a_client(cliente)
            self.view.show_client_midder()
            self.view.show_client_footer()
        else:
            if cliente == None:
                self.view.error('El cliente no existe')
            else:
                self.view.error(' Hay un problema al leer el cliente ')
            return
        self.view.msg('Ingresa los valores a modificar ( vacio para dejarlo igual ):')
        whole_vals = self.ask_user()
        fields, vals = self.update_lists(['a_nombre','a_apellidoPat','a_apellidoMat','a_nacionalidad','a_fnacimiento','correo','contrasena'],whole_vals)
        vals.append(id_cliente)
        vals = tuple(vals)
        out = self.model.update_client(fields,vals)
        if out == True:
            self.view.ok(id_cliente, 'atualizo')
        else:
            self.view.error('No se pudo actualizar')
        return
    
    def delete_client(self):
        self.read_all_clients()
        self.view.ask('ID del cliente a borrar: ')
        id_cliente = input()
        count = self.model.delete_client(id_cliente)
        if count != 0:
            self.view.ok(id_cliente, 'Se borro')
        else:
            if count == 0:
                self.view.error('El cliente no exite')
            else:
                self.view.error('Problema al borrar el cliente')
        return



    # ******************
    # * Admins mehtods *
    # ******************

    def create_a_admin(self):
        self.view.admin_ask()
        clave = input()
        if clave == 'UserGeneral':
            Nombre,ApellidoPat,ApellidoMat,Nacionalidad,Año,correo,Pass = self.ask_user()
            out = self.model.create_amdin(Nombre,ApellidoPat,ApellidoMat,Nacionalidad,Año,correo,Pass)
            if out == True:
                self.view.ok(Nombre + ' '+ ApellidoPat+ ' ' +ApellidoMat, 'creo cunenta de administrador')
                op = 0
                while op == 0:
                    self.view.ask_return()
                    op = input()
                    if op == 1:
                        self.start()
                    else:
                        self.main_menu()
            else:
                self.view.error('No se pudo agregar el administrador')
            return
        else:
            self.view.error('Necesitas la clave de administrador') 
            return 


    def read_a_admin(self):
        self.view.ask('Correo de administrador: ')
        id_client = input()
        client = self.model.read_a_admin(id_client)
        if type(client) == tuple:
            self.view.show_admin_header('Administrador '+id_client+' ')
            self.view.show_a_admin(client)
            self.view.show_admin_midder()
            self.view.show_admin_footer()
        else:
            if client == None:
                self.view.error('El administrador no existe')
            else:
                self.view.error(' Hay un problema al leer el administrador ')
        return


    def read_all_admins(self):
        clients = self.model.read_all_admin()
        if type(clients) ==  list:
            self.view.show_admin_header(' Todos los clientes ')
            for client in clients:
                self.view.show_a_admin(client)
            self.view.show_admin_midder()
            self.view.show_admin_footer()
        else:
            self.view.error('Hay un problema con todos los generos ')
        return

    def edit_admin(self):
        self.model.read_all_clients()
        self.view.ask(' Correo de cliente a modificar: ')
        id_cliente = input()
        cliente = self.model.read_a_admin(id_cliente)
        if type(cliente) == tuple:
            self.view.show_admin_header('Datos del cliente  '+id_cliente+' ')
            self.view.show_a_admin(cliente)
            self.view.show_admin_midder()
            self.view.show_admin_footer()
        else:
            if cliente == None:
                self.view.error('El admin no existe')
            else:
                self.view.error(' Hay un problema al leer el admin ')
            return
        self.view.msg('Ingresa los valores a modificar ( vacio para dejarlo igual ):')
        whole_vals = self.ask_user()
        fields, vals = self.update_lists(['a_nombre','a_apellidoPat','a_apellidoMat','a_nacionalidad','a_fnacimiento','correo','contrasena'],whole_vals)
        vals.append(id_cliente)
        vals = tuple(vals)
        out = self.model.update_admin(fields,vals)
        if out == True:
            self.view.ok(id_cliente, 'atualizo')
        else:
            self.view.error('No se pudo actualizar')
        return
    
    def delete_admin(self):
        self.read_all_admins()
        self.view.ask('Correo de administrador a borrar: ')
        id_cliente = input()
        count = self.model.delete_admin(id_cliente)
        if count != 0:
            self.view.ok(id_cliente, 'Se borro')
        else:
            if count == 0:
                self.view.error('El administrador no exite')
            else:
                self.view.error('Problema al borrar el administrador')
        return
    

    #********************
    #* Metodos de Salas *
    #*********************


    def salas_menu(self):
        o = '0'
        while o != '7':
            self.view.Sala_menu()
            self.view.option('7')
            o = input()
            if o == '1':
                self.create_sala()
            elif o == '2':
                self.read_a_sala()
            elif o == '3':
                self.read_all_salas()
            elif o == '4':
                self.read_sala_capacity()
            elif o == '5':
                self.edit_sala()       
            elif o == '6':
                self.delete_sala()           
            elif o == '7':
                return
            else:
                self.view.not_valid_option()
        return

    def ask_sala(self):
        self.view.ask('Numero de sala: ')
        id_sala = input()
        self.view.ask('Filas de sala: ')
        filas = input()
        self.view.ask('Columnas de sala: ')
        columnas = input()
        capacidad = int(filas)*int(columnas)       
        return [int(id_sala),int(filas),int(columnas),int(capacidad)]

    def create_sala(self):
        id_sala,filas,columnas,capacidad = self.ask_sala()
        out = self.model.create_sala(id_sala,filas,columnas,capacidad)
        print(out)
        if out == True:
            self.view.ok('Sala', ' creada')
        else:
            self.view.error('la sala ya exite o no se pudo agregar la sala')
        return

    def read_a_sala(self):
        self.view.ask('ID de sala: ')
        id_sala = input()
        sala = self.model.read_sala(id_sala)
        if type(sala) == tuple:
            self.view.show_sala_header('Datos de la sala  '+id_sala+' ')
            self.view.show_a_sala(sala)
            self.view.show_sala_midder()
            self.view.show_sala_footer()
        else:
            if sala == None:
                self.view.error('La sala no existe')
            else:
                self.view.error(' Hay un problema al leer la sala ')
        return

    def read_all_salas(self):
        salas = self.model.read_all_salas()
        if type(salas) ==  list:
            self.view.show_sala_header(' Todos las salas ')
            for sala in salas:
                self.view.show_a_sala(sala)
            self.view.show_sala_midder()
            self.view.show_sala_footer()
        else:
            self.view.error('Hay un problema con todos los generos ')
        return

    def read_sala_capacity(self):
        self.view.capacity()
        capacity = input()
        salas = self.model.read_sala_capacity(int(capacity))
        if type(salas) ==  list:
            self.view.show_sala_header(' Todos las salas ')
            for sala in salas:
                self.view.show_a_sala(sala)
            self.view.show_sala_midder()
            self.view.show_sala_footer()
        else:
            self.view.error('Hay un problema al buscar salas')
        return


    def edit_sala(self):
        self.read_all_salas()
        self.view.ask(' ID de sala a modificar: ')
        id_sala = input()
        sala = self.model.read_sala(id_sala)
        if type(sala) == tuple:
            self.view.show_sala_header_e('Datos de la sala  '+id_sala+' ')
            self.view.show_a_sala_e(sala)
            self.view.show_sala_midder_e()
            self.view.show_sala_footer_e()
        else:
            if sala == None:
                self.view.error('La sala no existe')
            else:
                self.view.error(' Hay un problema al leer la sala ')
            return

        self.view.msg('Ingresa los valores a modificar y los valores a conservar( No dejes nigun valor vacio ):')
        whole_vals = self.ask_sala()
        fields, vals = self.update_lists(['id_sala','filas','columnas','asientos_t'],whole_vals)
        vals.append(id_sala)
        vals = tuple(vals)
        out = self.model.update_sala(fields,vals)
        if out == True:
            self.view.ok(id_sala, 'Se atualizo la sala')
        else:
            self.view.error('No se pudo actualizar la sala')
        return

    def delete_sala(self):
        self.read_all_salas()
        self.view.ask('ID de sala a borrar: ')
        id_sala = input()
        count = self.model.delete_sala(id_sala)
        if count != 0:
            self.view.ok(id_sala, 'Se borro')
        else:
            if count == 0:
                self.view.error('La sala no exite')
            else:
                self.view.error('Problema al borrar la sala')
        return

    # """
    #     ************************
    #     * Metodos de Cartelera *
    #     ************************
    # """
    
    def cartelera_menu(self):
        o = '0'
        today = date.today()
        bandera =0
        while o != '6':
            self.view.cartelera_menu()
            self.view.option('6')
            o = input()
            if o == '1':
                self.add_movie_cartelera() 
            elif o == '2':
                self.read_carteleras(today,bandera)                 
            elif o == '3':
                self.horario_pelicula()
            elif o == '4':
                self.edit_carteleras() 
            elif o == '5':
                self.delete_cartelera()
            elif o == '6':
                return
            else:
                self.view.not_valid_option()
        return

    def ask_cartelera(self):
        self.view.ask('Sala: ')
        sala = input()
        self.view.ask('ID de Pelicula: ')
        pelicula = input()
        self.view.ask('Hora de la pelicula: ')
        hora = input()
        self.view.ask('Dia de la pelicula: ')
        date = input()
        return [sala,pelicula,hora,date]
        
    def add_movie_cartelera(self):
        self.read_all_salas()
        self.read_all_movies()
        sala,pelicula,hora,date = self.ask_cartelera()
        out = self.model.create_cartelera(sala,pelicula,hora,date)
        if out == True:
            self.view.ok('Horario ', 'agrego a cartelera')
        else:
            self.view.error('No se pudo agregar la cartelera')
        return
            

    def read_carteleras(self,fecha,bandera):
        salas = self.model.read_all_cartelera(fecha)
        if type(salas) != list:
            self.view.error('El horario no existe')
            return False
        Horario=[]
        car =[]
        sala = salas[0][0]
        titu = salas[0][1]
        car.append(sala)
        car.append(titu)
        car.append(salas[0][2])
        for i in range(1,len(salas)):
            if salas[i][0] != sala:
                Horario.append(car)
                car = []
                sala = salas[i][0]
                titu = salas[i][1]
                car.append(sala)
                car.append(titu)
            if (i+1) == len(salas):
                car.append(salas[i][2])
                Horario.append(car)
            if (i+1) != len(salas):
                car.append(salas[i][2])
        self.view.show_cartelera_header(' Cartelera ')
        for sala in Horario:
            self.view.show_a_cartelera(sala)
        self.view.show_cartelera_midder()
        self.view.show_cartelera_footer()

        if bandera == 0:
            self.view.msg('Ingrese fecha para otra consulta o de enter para continuar')
            opcion=input()
            if opcion =='':
                return
            else:
                self.read_carteleras(opcion,0)
        else:
            return


    def horario_pelicula(self):
        self.view.ask('Pelicula: ')
        nombre = input()
        self.view.ask('Fecha: ')
        date = input()
        salas = self.model.read_a_cartelera(nombre,date)
        if type(salas) != list or salas == []:
            self.view.error(' No hay horario para esa pelicula o esta mal escrita ')
            return
        Horario=[]
        car =[]
        sala = salas[0][0]
        titu = salas[0][1]
        car.append(sala)
        car.append(titu)
        car.append(salas[0][2])
        for i in range(1,len(salas)):
            if salas[i][0] != sala:
                Horario.append(car)
                car = []
                sala = salas[i][0]
                titu = salas[i][1]
                car.append(sala)
                car.append(titu)
            if (i+1) == len(salas):
                car.append(salas[i][2])
                Horario.append(car)
            if (i+1) != len(salas):
                car.append(salas[i][2])
        self.view.show_cartelera_header(' Cartelera ')
        for sala in Horario:
            self.view.show_a_cartelera(sala)
        self.view.show_cartelera_midder()
        self.view.show_cartelera_footer()
        return
    
    def edit_carteleras(self):
        self.view.ask(' Fecha a modificar: ')
        date = input()
        self.read_carteleras(date,1)
        self.view.ask(' ID de la sala a modificar: ')
        c_id_sala = input()
        self.view.ask(' Hora a modificar: ')
        c_hora = input()

        self.view.msg('Ingresa los valores a modificar ( vacio para dejarlo igual ):')

        whole_vals = self.ask_cartelera()
        fields, vals = self.update_lists(['c_id_sala','c_id_pelicula','c_hora','o_date'],whole_vals)
        vals.append(c_id_sala)
        vals.append(c_hora)
        vals.append(date)
        vals = tuple(vals)
        out = self.model.update_cartelera(fields,vals)
        if out == True:
            self.view.ok('Cartelera', 'atualizo')
        else:
            self.view.error('No se pudo actualizar')
        return

    def delete_cartelera(self):
        self.view.ask('Fecha: ')
        date = input()
        self.read_carteleras(date,1)
        self.view.ask('ID de sala: ')
        sala = input()
        self.view.ask('Horario: ')
        horario = input()

        count = self.model.delete_cartelera(sala,horario,date)
        if count != 0:
            self.view.ok(horario, 'Se borro')
        else:
            if count == 0:
                self.view.error('El horario no existe')
            else:
                self.view.error('Problema al leer la cartelera')
        return

# ******************************
# * Metodo para comprar boleto *
# ******************************

    def boleto_impreso(self,sala,pelicula,hora,asiento,fecha):
        self.view.show_boleto_header(' Boleto ')
        self.view.show_boleto_sala_header(str(sala))
        self.view.show_boleto_pelicula_header(str(pelicula))
        self.view.show_boleto_hora_header(str(hora))
        self.view.show_boleto_asiento_header(str(asiento))
        self.view.show_boleto_fecha_header(str(fecha))
        self.view.show_boleto_footer()
        return


    def vie_of_sala(self,sala):
        salita = self.model.read_sala(sala) #llamada a modelo aqui retorna las columnas y filas de una sala para armar la vista de la sala 
        if type(salita) != tuple:
            return False
        filas = salita[1]
        columnas = salita[2]
        asientos=[]
        for i in range(filas):
            asiento=[]
            for j in range(columnas):
                silla=[]
                silla.append(chr(int(i+65)))
                silla.append(str(j))
                StrA = "".join(silla)
                asiento.append(StrA)
            asientos.append(asiento)
        return asientos


    def aks_usuario(self):
        self.view.msg('Si eres cliente ingresa tu correo si no solo presiona enter')
        usuario = input()
        if usuario == '':
            return None
        else:
            exist = self.model.read_a_client(usuario)
            if exist == None:
                self.view.error('El usuario no existe')
                return 0
            else:
                return usuario



    def ask_boleto(self):
        self.view.ask('Ingresa la sala de la pelicula: ')
        sala = input()
        self.view.ask('Ingresa la hora de la pelicula: ')
        hora = input()
        self.view.ask('numero de asientos a reservar: ')
        numero = input()
        return[sala,hora,numero]

    def ask_boleto_fechas(self):
        self.view.ask('ingresa fecha de la reservacion si es para hoy da enter: ')
        fecha = input()
        if fecha == '':
            fecha = date.today()
        return fecha

    def comprar_boleto(self):
        usuario = self.aks_usuario() # preguntamos al usuario si tiene cuenta
        if usuario == 0: # si el usuario ingreso una cuenta inexistente el programa regresara al menu anterior
            return
        fecha = self.ask_boleto_fechas()# preguntar fecha de reservacion
        car = self.read_carteleras(fecha,1) # llamada a vista de carteleras
        if car == False: #en caso de solicitar la vista de una cartelera que no existe el programa retornara al menu anterior
            return
        sala,hora,numero = self.ask_boleto() #peticion de informacion como sala de la funcion , hora de la funcion y el numero de asientos a reservar

        if sala == '' or numero == '' or hora == '': # si los datos son ingresados vacios mostrara un menaje de error y volvera al menu anterior
            self.view.error('Error no al ingresar la reserva')
            return

        pelicula = self.model.read_cartelera(sala,hora,fecha) # en esta seccion de obtendra la pelicula que el usuario desea ver
        if( pelicula == None): # en caso de que no exista una pelicula en el horario deseado despliega un mensaje de error
            self.view.error('No existe pelicula en ese horario intenta de nuevo')
            self.comprar_boleto() # nos solicitara una ves mas todos los datos

        asientos = self.vie_of_sala(sala) # aqui optendremos la vista de la sala en la que veremos la funcion
        # mostrara las numeraciones de los asientos A1 A2 .... A30

        if asientos == False: # en caso de que no exista una sala nos desplegara una alerte
            self.view.error('No existe la sala intenta de nuevo') 
            self.comprar_boleto() # nos solicitara una ves mas todos los datos

        comprados=[] # almanecara todos los numeros de asientos que compre el usuario

        reserv = self.model.read_all_boletos(sala,hora,fecha)  # obtendremos todos los boletos que estan reservados en la sala
        if type(reserv) != list:
            self.view.error('Error en la consulta')
            return


        # esta seccion agregara a la vista de la sala todos los boletos que ya han sido reservados
        for j in range(len(reserv)):
            if(len(reserv[j][0])) >2:
                num=[reserv[j][0][1],reserv[j][0][2]]
                StrA = "".join(num)
                StrA = int(StrA)
                asientos[int(ord(reserv[j][0][0]))-65][StrA] =' X '
            else:
                # marcara con una X el asiento reservado
                asientos[int(ord(reserv[j][0][0]))-65][int(reserv[j][0][1])] =' X '

        contador =0 # llevara el control de cuntos boletos han sido comprados
    
        while contador != int(numero): # repetira la operacion de la reservacion de asientos hasta que el controlador lo detenga
            self.view.contador_boleto(contador+1,numero) #muestra en pantalla el numero de reservacion que se esta haciendo 
            self.view.show_asientos(asientos) # muetra los asientos de la sala
            self.view.numero_asientos()  # solicitara el asiento a reservar

            bande = 1
            while bande == 1:   #comprueba que el asiento no sea mayo a 3 digitos por que no existe o menor a 1 por que no existe por ejemplo A, A222
                reserva = input()  # introduce el numero del asiento el usuario
                if reserva == '0':  # de esta manera en caso de que el usuario ingrese 0 se cancelara la compra de boleto
                    return
                if len(reserva) <= 1: # comprueba que el asiento consita minimo en dos caracterer para ser un asiento valido
                    self.view.asiento_no_valido()
                if len(reserva) >= 2 and len(reserva) <= 3:
                    bande = 2
            StrA = 0

            if len(reserva) > 2: # conviere en un numero el asiento ingresado
                num=[reserva[1],reserva[2]]
                StrA = "".join(num)
                StrA = int(StrA)
            else:
                StrA = int(reserva[1])

            asientos_existentes = self.model.read_sala(sala) #recibe el numero de asiento de una sala filas y columnas

            # comprueba que el asiento ingresado este dentro del rango de los asientos de la sala
            if int(ord(reserva[0]))-65 > asientos_existentes[1] or  StrA > asientos_existentes[2]: 
                self.view.error(' No existe ese asiento intenta de nuevo ')
                self.comprar_boleto()
            # comprueba que el asiento de la sala no este reservado en caso de no estarlo este sera serevado
            if asientos[int(ord(reserva[0]))-65][StrA] != ' X ':
                asientos[int(ord(reserva[0]))-65][StrA] =' X '
                contador +=1
                self.model.create_boleto(reserva,pelicula[0],usuario,sala,hora,fecha)
                # se insertara el boleto en el registro de compra para el control del usuario y de la sala
                comprados.append(reserva)
            else:
                self.view.error_asiento()
           
        #se encarga de la impresion de boletos echos en el momento de la compra
        for k in range(len(comprados)):
            self.boleto_impreso(sala,pelicula[0],hora,comprados[k],fecha)
        return



    def read_all_boletos(self):
        self.view.ask('Ingrese su correo electronico: ')
        correo = input()
        boletos = self.model.read_boleto_user(correo)
        if type(boletos) == list:
            self.view.show_Registro_header(' Todos las compras ')
            for boleto in boletos:
                self.view.show_a_Registro(boleto)
            self.view.show_Registro_midder()
            self.view.show_Registro_footer()
        else:
            self.view.error('No existen compras del usuario')

        return


    def ask_read_boleto(self):
        self.view.ask('Ingrese su correo electronico: ')
        correo = input()
        self.view.ask('Ingrse fecha de la funcion: ')
        fecha = input()
        return [correo,fecha]

    def read_all_boletos_date(self):
        correo,fecha = self.ask_read_boleto()
        boletos = self.model.read_boleto_user_date(correo,fecha)
        if type(boletos) == list:
            self.view.show_Registro_header(' Comprados en'+fecha)
            for boleto in boletos:
                self.view.show_a_Registro(boleto)
            self.view.show_Registro_midder()
            self.view.show_Registro_footer()
        else:
            self.view.error('No existen compras del usuario')
        return

    def ask_boleto_reimpimir(self):
        self.view.ask('Ingrese su correo electronico: ')
        correo = input()
        self.view.ask('Ingrse fecha de compra: ')
        fecha = input()
        self.view.ask('Ingrse hora de la funcion: ')
        hora = input()
        return [correo,fecha,hora]


    def reimprimir_boleto(self):
        correo,fecha,hora = self.ask_boleto_reimpimir()
        boletos = self.model.read_boleto_user_date_time(correo,fecha,hora)
        if type(boletos) == list:
            for j in range(len(boletos)):
                self.boleto_impreso(boletos[j][4],boletos[j][2],boletos[j][5],boletos[j][1],boletos[j][6])
        else:
            self.view.error('No existen compras del usuario')
        return
