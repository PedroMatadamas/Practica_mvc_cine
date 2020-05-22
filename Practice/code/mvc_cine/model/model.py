from mysql import connector

class Model:
    """
    *****************************************
    * a data model with MySQL for a store DB*
    *****************************************
    """
    def __init__(self, config_db_file='config.txt'):
        self.config_db_file = config_db_file
        self.config_db = self.read_config_db()
        self.connect_to_db()

    def read_config_db(self):
        d={}
        with open(self.config_db_file ) as f_r:
            for line in f_r: 
                (key, val) = line.strip().split(':')
                d[key] = val
        return d
        
    def connect_to_db(self):
        self.cnx = connector.connect(**self.config_db)
        self.cursor = self.cnx.cursor()

    def close_db(self):
        self.cnx.close()

    """
    *****************
    * Genero metodos*
    *****************
    """
    def create_gen(self,genero):
        try:
            print(genero)
            sql = 'INSERT INTO genero (`genero`) VALUES (%s)'
            vals = (genero,)
            self.cursor.execute(sql,vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            print(err)
            self.cnx.rollback()
            return err

    def read_a_genero(self,genero):
        try:
            sql = 'SELECT * FROM genero WHERE id_genero = %s'
            vals = (genero,)
            self.cursor.execute(sql,vals)
            record = self.cursor.fetchone()
            return record
        except connector.Error as err:
            return err


    def read_all_generos(self):
        try:
            sql = 'SELECT * FROM genero'
            self.cursor.execute(sql)
            record = self.cursor.fetchall()
            return record
        except connector.Error as err:
            return err
    
    def update_genero(self,fields,vals):
        try:
            sql = 'UPDATE genero SET '+','.join(fields)+'WHERE id_genero = %s'
            self.cursor.execute(sql,vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err

    def delete_genero(self, id_genero):
        try:
            sql = 'DELETE FROM genero WHERE id_genero = %s'
            vals = (id_genero,)
            self.cursor.execute(sql,vals)
            self.cnx.commit()
            count = self.cursor.rowcount
            return count
        except connector.Error as err:
            self.cnx.rollback()
            return err
    
    """
    *********************
    * Generos Peliculas metodos*
    *********************
    """
    def create_generos_peliculas(self, gp_id_genero, gp_id_pelicula):
        try:
            sql = 'INSERT INTO genpelicula (`gp_id_genero`, `gp_id_pelicula`) VALUES (%s, %s)'
            vals = (gp_id_genero, gp_id_pelicula)
            self.cursor.execute(sql,vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err

    def read_a_genpelicula(self,gp_id_genero):
        try:
            sql = 'SELECT genero.id_genero, genero.genero FROM genpelicula JOIN genero ON genero.id_genero = genpelicula.gp_id_genero WHERE gp_id_genero = %s'
            vals = (gp_id_genero,)
            self.cursor.execute(sql, vals)
            record = self.cursor.fetchall()
            return record
        except connector.Error as err:
            return err

    def read_a_peliculagen(self,gp_id_pelicula):
        try:
            sql = 'SELECT genero.id_genero, genero.genero FROM genpelicula JOIN genero ON genero.id_genero = genpelicula.gp_id_genero WHERE gp_id_pelicula = %s'
            vals = (gp_id_pelicula,)
            self.cursor.execute(sql, vals)
            record = self.cursor.fetchall()
            return record
        except connector.Error as err:
            return err

    def read_all_genpelicula(self):
        try:
            sql = 'SELECT genero.id_genero, genero.genero, peliculas.id_pelicula, peliculas.p_titulo FROM genero JOIN genpelicula ON genero.id_genero = genpelicula.gp_id_genero JOIN peliculas ON peliculas.id_peliculas = genpelicula.gp_id_pelicula'
            self.cursor.execute(sql)
            record = self.cursor.fetchall()
            return record
        except connector.Error as err:
            return err
    
    def update_genpelicula(self, fields, vals):
        try:
            sql = 'UPDATE genpelicula SET '+','.join(fields)+'WHERE gp_id_genero = %s AND gp_id_pelicula = %s'
            self.cursor.execute(sql,vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err
    
    def delete_genero_pelicula(self, gp_id_genero, gp_id_pelicula):
        try:
            sql = 'DELETE FROM genpelicula WHERE gp_id_genero = %s AND gp_id_pelicula = %s'
            vals = (gp_id_genero, gp_id_pelicula)
            self.cursor.execute(sql,vals)
            self.cnx.commit()
            count = self.cursor.rowcount
            return count
        except connector.Error as err:
            self.cnx.rollback()
            return err

    """
    *********************
    * Directores metodos*
    *********************
    """
    def create_director(self,d_nombre,d_apellidoPat,d_apellidoMat,d_nacionalidad,d_fnacimiento,d_educacion):
        try:
            sql = 'INSERT INTO directores (`d_nombre`,`d_apellidoPat`,`d_apellidoMat`,`d_nacionalidad`,`d_fnacimiento`,`d_educacion`) VALUES (%s,%s,%s,%s,%s,%s)'
            vals = (d_nombre,d_apellidoPat,d_apellidoMat,d_nacionalidad,d_fnacimiento,d_educacion)
            self.cursor.execute(sql,vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err

    def read_a_director(self,id_director):
        try:
            sql = 'SELECT * FROM directores WHERE id_director = %s'
            vals = (id_director,)
            self.cursor.execute(sql,vals)
            record = self.cursor.fetchone()
            return record
        except connector.Error as err:
            return err

    def read_a_director_nacionalidad(self,d_nacionalidad):
        try:
            sql = 'SELECT * FROM directores WHERE d_nacionalidad = %s'
            vals = (d_nacionalidad,)
            self.cursor.execute(sql,vals)
            record = self.cursor.fetchall()
            return record
        except connector.Error as err:
            return err


    def read_all_director(self):
        try:
            sql = 'SELECT * FROM directores'
            self.cursor.execute(sql)
            record = self.cursor.fetchall()
            return record
        except connector.Error as err:
            return err
    
    def update_director(self,fields,vals):
        try:
            sql = 'UPDATE directores SET '+','.join(fields)+'WHERE id_director = %s'
            self.cursor.execute(sql,vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err

    def delete_director(self, id_genero):
        try:
            sql = 'DELETE FROM directores WHERE id_director = %s'
            vals = (id_genero,)
            self.cursor.execute(sql,vals)
            self.cnx.commit()
            count = self.cursor.rowcount
            return count
        except connector.Error as err:
            self.cnx.rollback()
            return err

    """
    *********************
    * actores metodos*
    *********************
    """
    def create_actor(self,a_nombre,a_apellidoPat,a_apellidoMat,a_nacionalidad,a_fnacimiento):
        try:
            sql = 'INSERT INTO actores (`a_nombre`,`a_apellidoPat`,`a_apellidoMat`,`a_nacionalidad`,`a_fnacimiento`) VALUES (%s,%s,%s,%s,%s)'
            vals = (a_nombre,a_apellidoPat,a_apellidoMat,a_nacionalidad,a_fnacimiento)
            self.cursor.execute(sql,vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err

    def read_a_actor(self,id_director):
        try:
            sql = 'SELECT * FROM actores WHERE id_actor = %s'
            vals = (id_director,)
            self.cursor.execute(sql,vals)
            record = self.cursor.fetchone()
            return record
        except connector.Error as err:
            return err

    def read_a_actor_nacionalidad(self,d_nacionalidad):
        try:
            sql = 'SELECT * FROM actores WHERE a_nacionalidad = %s'
            vals = (d_nacionalidad,)
            self.cursor.execute(sql,vals)
            record = self.cursor.fetchall()
            return record
        except connector.Error as err:
            return err


    def read_all_actor(self):
        try:
            sql = 'SELECT * FROM actores'
            self.cursor.execute(sql)
            record = self.cursor.fetchall()
            return record
        except connector.Error as err:
            return err
    
    def update_actor(self,fields,vals):
        try:
            sql = 'UPDATE actores SET '+','.join(fields)+'WHERE id_actor = %s'
            self.cursor.execute(sql,vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err

    def delete_actor(self, id_actor):
        try:
            sql = 'DELETE FROM actores WHERE id_actor = %s'
            vals = (id_actor,)
            self.cursor.execute(sql,vals)
            self.cnx.commit()
            count = self.cursor.rowcount
            return count
        except connector.Error as err:
            self.cnx.rollback()
            return err
    """
    *********************
    * peliculas metodos*
    *********************
    """
    def create_movie(self,p_titulo,p_idioma,p_subtitulos):
        try:
            sql = 'INSERT INTO peliculas (`p_titulo`,`p_idioma`,`p_subtitulos`) VALUES (%s,%s,%s)'
            vals = (p_titulo,p_idioma,p_subtitulos)
            self.cursor.execute(sql,vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err

    def read_a_movie(self,id_pelicula):
        try:
            sql = 'SELECT * FROM peliculas WHERE id_pelicula = %s'
            vals = (id_pelicula,)
            self.cursor.execute(sql,vals)
            record = self.cursor.fetchone()
            return record
        except connector.Error as err:
            return err

    def read_a_movies_year(self,p_año):
        try:
            sql = 'SELECT * FROM peliculas WHERE p_año = %s'
            vals = (p_año,)
            self.cursor.execute(sql,vals)
            record = self.cursor.fetchall()
            return record
        except connector.Error as err:
            return err


    def read_all_movies(self):
        try:
            sql = 'SELECT * FROM peliculas'
            self.cursor.execute(sql)
            record = self.cursor.fetchall()
            return record
        except connector.Error as err:
            return err
    
    def update_movie(self,fields,vals):
        try:
            sql = 'UPDATE peliculas SET '+','.join(fields)+'WHERE id_pelicula = %s'
            self.cursor.execute(sql,vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err

    def delete_movie(self, id_actor):
        try:
            sql = 'DELETE FROM peliculas WHERE id_pelicula = %s'
            vals = (id_actor,)
            self.cursor.execute(sql,vals)
            self.cnx.commit()
            count = self.cursor.rowcount
            return count
        except connector.Error as err:
            self.cnx.rollback()
            return err

    """
    ***********************
    * actor_movies metodos*
    ***********************
    """
    def create_ac_mov(self,ap_id_actor,ap_id_pelicula):
        try:
            sql = 'INSERT INTO actorpeliculas (`ap_id_actor`,`ap_id_pelicula`) VALUES (%s,%s)'
            vals = (ap_id_actor,ap_id_pelicula)
            self.cursor.execute(sql,vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err


    def read_a_ac_mov(self, ap_id_actor):
        try:
            sql = 'SELECT peliculas.id_pelicula ,peliculas.p_titulo, peliculas.p_idioma, peliculas.p_subtitulos, peliculas.p_año from actorpeliculas join peliculas on peliculas.id_pelicula = actorpeliculas.ap_id_pelicula where ap_id_actor = %s'
            vals = (ap_id_actor,)
            self.cursor.execute(sql,vals)
            record = self.cursor.fetchall()
            return record
        except connector.Error as err:
            return err

    def read_a_mov_ac(self, ap_id_pelicula):
        try:
            sql = 'SELECT actores.id_actor,actores.a_nombre, actores.a_apellidoPat, actores.a_apellidoMat , actores.a_nacionalidad, actores.a_fnacimiento from actorpeliculas join actores on actores.id_actor = actorpeliculas.ap_id_actor where ap_id_pelicula = %s'
            vals = (ap_id_pelicula,)
            self.cursor.execute(sql,vals)
            record = self.cursor.fetchall()
            return record
        except connector.Error as err:
            return err

    def read_all_ac_mov(self):
        try:
            sql = 'select peliculas.p_titulo, actores.a_nombre from peliculas join actorpeliculas on  actorpeliculas.ap_id_pelicula = peliculas.id_pelicula join actores on actores.id_actor = actorpeliculas.ap_id_actor'
            self.cursor.execute(sql)
            record = self.cursor.fetchall()
            return record
        except connector.Error as err:
            return err
    
    def update_ac_mov(self,fields,vals):
        try:
            sql = 'UPDATE actorpeliculas SET '+','.join(fields)+'WHERE ap_id_actor = %s AND ap_id_pelicula  = %s '
            self.cursor.execute(sql,vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err

    def delete_ac_mov(self, ap_id_actor,ap_id_pelicula):
        try:
            sql = 'DELETE FROM actorpeliculas WHERE ap_id_actor = %s AND ap_id_pelicula  = %s '
            vals = (ap_id_actor,ap_id_pelicula,)
            self.cursor.execute(sql,vals)
            self.cnx.commit()
            count = self.cursor.rowcount
            return count
        except connector.Error as err:
            self.cnx.rollback()
            return err

    """
    ***
    * Detalles
    **
    """

    def create_detalles_pelicula(self, dp_id_pelicula, dp_id_director, descripcion,dp_duracion,dp_año):
        try:
            sql = 'INSERT INTO detalles_peliculas(`dp_id_pelicula`, `dp_id_director`, `descripcion`,`dp_duracion`,`dp_año`) VALUES ( %s, %s, %s, %s,%s)'
            vals = ( dp_id_pelicula, dp_id_director, descripcion,dp_duracion,dp_año)
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            print(err)
            return err

    def read_detalles_pelicula(self, dp_id_pelicula):
        try: 
            sql ='SELECT detalles_peliculas.dp_id_pelicula, peliculas.p_titulo, directores.d_nombre , detalles_peliculas.descripcion, detalles_peliculas.dp_duracion FROM peliculas JOIN detalles_peliculas ON peliculas.id_pelicula =  detalles_peliculas.dp_id_pelicula JOIN directores ON detalles_peliculas.dp_id_director = directores.id_director WHERE dp_id_pelicula = %s'
            vals=(dp_id_pelicula, )
            self.cursor.execute(sql, vals)
            record = self.cursor.fetchall()
            return record
        except connector.Error as err:
            return err


    def read_all_detalles_pelicula(self):
        try: 
            sql ='SELECT detalles_peliculas.dp_id_pelicula, peliculas.p_titulo, directores.d_nombre , detalles_peliculas.descripcion, detalles_peliculas.dp_duracion FROM peliculas JOIN detalles_peliculas ON peliculas.id_pelicula =  detalles_peliculas.dp_id_pelicula JOIN directores ON detalles_peliculas.dp_id_director = directores.id_director'
            self.cursor.execute(sql)
            record = self.cursor.fetchall()
            return record
        except connector.Error as err:
            return err

    
    def update_detalles_pelicula(self, fields, vals):
        try:
            sql = 'UPDATE detalles_peliculas SET '+','.join(fields)+'WHERE id_dp = %s'
            self.cursor.execute(sql,vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err

    def delate_detalles_prlicula(self, dp_id_pelicula):
        try:
            sql = 'DELETE FROM detalles_peliculas WHERE dp_id_pelicula = %s '
            vals = (dp_id_pelicula, )
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            count = self.cursor.rowcount
            return count
        except connector.Error as err:
            self.cnx.rollback()
            return err


    def read_a_dir_mov(self, id_director):
        try:
            sql = 'SELECT peliculas.id_pelicula ,peliculas.p_titulo, peliculas.p_idioma, peliculas.p_subtitulos, peliculas.p_año from detalles_peliculas join peliculas on peliculas.id_pelicula = detalles_peliculas.dp_id_pelicula where dp_id_director = %s'
            vals = (id_director,)
            self.cursor.execute(sql,vals)
            record = self.cursor.fetchall()
            return record
        except connector.Error as err:
            return err

    """
    *************************
    * Administrador metodos *
    *************************
    """

    def create_amdin(self,a_nombre,a_apellidoPat,a_apellidoMat,a_nacionalidad,a_fnacimiento,correo,password):
        try:
            sql = 'INSERT INTO administrador (`a_nombre`,`a_apellidoPat`,`a_apellidoMat`,`a_nacionalidad`,`a_fnacimiento`,`correo`,`contrasena`) VALUES (%s,%s,%s,%s,%s,%s,%s)'
            vals = (a_nombre,a_apellidoPat,a_apellidoMat,a_nacionalidad,a_fnacimiento,correo,password)
            self.cursor.execute(sql,vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err

    def read_a_admin(self,id_administrador):
        try:
            sql = 'SELECT * FROM administrador WHERE correo = %s'
            vals = (id_administrador,)
            self.cursor.execute(sql,vals)
            record = self.cursor.fetchone()
            return record
        except connector.Error as err:
            return err
    def read_all_admin(self):
        try:
            sql = 'SELECT * FROM administrador'
            self.cursor.execute(sql,)
            record = self.cursor.fetchall()
            return record
        except connector.Error as err:
            return err

    def read_all_admin2(self):
        try:
            sql = 'SELECT id_administrador,a_nombre,a_apellidoPat,a_apellidoMat FROM administrador'
            self.cursor.execute(sql,)
            record = self.cursor.fetchall()
            return record
        except connector.Error as err:
            return err           
    

    def update_admin(self,fields,vals):
        try:
            sql = 'UPDATE administrador SET '+','.join(fields)+'WHERE correo = %s'
            self.cursor.execute(sql,vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err

    def delete_admin(self, id_administrador):
        try:
            sql = 'DELETE FROM administrador WHERE WHERE correo = %s'
            vals = (id_administrador,)
            self.cursor.execute(sql,vals)
            self.cnx.commit()
            count = self.cursor.rowcount
            return count
        except connector.Error as err:
            self.cnx.rollback()
            return err


    """
    *******************
    * cliente metodos *
    *******************
    """

    def create_client(self,a_nombre,a_apellidoPat,a_apellidoMat,a_nacionalidad,a_fnacimiento,correo,contrasena):
        try:
            sql = 'INSERT INTO cliente (`a_nombre`,`a_apellidoPat`,`a_apellidoMat`,`a_nacionalidad`,`a_fnacimiento`,`correo`,`contrasena`) VALUES (%s,%s,%s,%s,%s,%s,%s)'
            vals = (a_nombre,a_apellidoPat,a_apellidoMat,a_nacionalidad,a_fnacimiento,correo,contrasena)
            self.cursor.execute(sql,vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err

    def read_a_client(self,id_cliente):
        try:
            sql = 'SELECT * FROM cliente WHERE correo = %s'
            vals = (id_cliente,)
            self.cursor.execute(sql,vals)
            record = self.cursor.fetchone()
            return record
        except connector.Error as err:
            return err

    def read_all_clients(self):
        try:
            sql = 'SELECT * FROM cliente'
            self.cursor.execute(sql,)
            record = self.cursor.fetchall()
            return record
        except connector.Error as err:
            return err
    

    def update_client(self,fields,vals):
        try:
            sql = 'UPDATE cliente SET '+','.join(fields)+'WHERE correo = %s'
            self.cursor.execute(sql,vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err

    def delete_client(self, id_cliente):
        try:
            sql = 'DELETE FROM cliente WHERE WHERE correo = %s'
            vals = (id_cliente,)
            self.cursor.execute(sql,vals)
            self.cnx.commit()
            count = self.cursor.rowcount
            return count
        except connector.Error as err:
            self.cnx.rollback()
            return err
    
    """
    *****************
    * Salas metodos *
    *****************
    """

    
    def create_sala(self,id_sala,filas,columnas,asientos_t):
        try:
            sql = 'INSERT INTO sala (`id_sala`,`filas`,`columnas`,`asientos_t`) VALUES (%s,%s,%s,%s)'
            vals = (id_sala,filas,columnas,asientos_t)
            self.cursor.execute(sql,vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err

    def read_sala(self,id_sala):
        try:
            sql = 'SELECT * FROM sala WHERE id_sala = %s'
            vals = (id_sala,)
            self.cursor.execute(sql,vals)
            record = self.cursor.fetchone()
            return record
        except connector.Error as err:
            return err     

    def read_sala_capacity(self,asientos_t):
        try:
            sql = 'SELECT * FROM sala WHERE asientos_t >= %s'
            vals = (asientos_t,)
            self.cursor.execute(sql,vals)
            record = self.cursor.fetchall()
            return record
        except connector.Error as err:
            return err

    def read_all_salas(self):
        try:
            sql = 'SELECT * FROM sala'
            self.cursor.execute(sql,)
            record = self.cursor.fetchall()
            return record
        except connector.Error as err:
            return err    
   
    def update_sala(self,fields,vals):
        try:
            sql = 'UPDATE sala SET '+','.join(fields)+' WHERE id_sala = %s'
            self.cursor.execute(sql,vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err


    def delete_sala(self, id_sala):
        try:
            sql = 'DELETE FROM sala WHERE id_sala = %s'
            vals = (id_sala,)
            self.cursor.execute(sql,vals)
            self.cnx.commit()
            count = self.cursor.rowcount
            return count
        except connector.Error as err:
            self.cnx.rollback()
            return err

    """
    *********************
    * Cartelera metodos *
    *********************
    """

        
    def create_cartelera(self,c_id_sala,c_id_pelcula,c_hora,date):
        try:
            sql = 'INSERT INTO Cartelera (`c_id_sala`,`c_id_pelicula`,`c_hora`,`o_date`) VALUES (%s,%s,%s,%s)'
            vals = (c_id_sala,c_id_pelcula,c_hora,date)
            self.cursor.execute(sql,vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err

    
    def read_a_cartelera(self,pelicula,date):
        try:
            sql = 'SELECT sala.id_sala, peliculas.p_titulo, Cartelera.c_hora from  peliculas join Cartelera on peliculas.id_pelicula = Cartelera.c_id_pelicula join sala on sala.id_sala = Cartelera.c_id_sala WHERE peliculas.p_titulo = %s AND Cartelera.o_date = %s'
            vals = (pelicula,date)
            self.cursor.execute(sql,vals)
            record = self.cursor.fetchall()
            return record
        except connector.Error as err:
            return err

    def read_all_cartelera(self,date):
        try:
            sql = 'SELECT sala.id_sala, peliculas.p_titulo, Cartelera.c_hora from  peliculas join Cartelera on peliculas.id_pelicula = Cartelera.c_id_pelicula join sala on sala.id_sala = Cartelera.c_id_sala WHERE o_date = %s'
            vals = (date, )
            self.cursor.execute(sql,vals)
            record = self.cursor.fetchall()
            return record
        except connector.Error as err:
            return err

    def read_cartelera(self,id_sala,hora,date):
        try:
            sql = 'SELECT peliculas.p_titulo from  peliculas join Cartelera on peliculas.id_pelicula = Cartelera.c_id_pelicula join sala on sala.id_sala = Cartelera.c_id_sala WHERE sala.id_sala = %s AND Cartelera.c_hora = %s AND o_date = %s'
            vals = (id_sala,hora,date)
            self.cursor.execute(sql,vals)
            record = self.cursor.fetchone()
            return record
        except connector.Error as err:
            return err   

    def read_all_cartelera2(self):
        try:
            sql = 'SELECT sala.id_sala, peliculas.p_titulo, peliculas.id_pelicula, Cartelera.c_hora from  peliculas join Cartelera on peliculas.id_pelicula = Cartelera.c_id_pelicula join sala on sala.id_sala = Cartelera.c_id_sala'
            self.cursor.execute(sql,)
            record = self.cursor.fetchall=()
            return record
        except connector.Error as err:
            return err


    def update_cartelera(self,fields,vals):
        try:
            sql = 'UPDATE Cartelera SET '+','.join(fields)+'WHERE c_id_sala = %s AND c_hora = %s AND o_date = %s'
            self.cursor.execute(sql,vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err
            
    def delete_cartelera(self, c_id_sala,c_hora,fecha):
        try:
            vals = (c_id_sala,c_hora,fecha)
            sql = 'DELETE FROM Cartelera WHERE c_id_sala = %s AND c_hora = %s AND o_date = %s'
            vals = (c_id_sala,c_hora,fecha)
            self.cursor.execute(sql,vals)
            self.cnx.commit()
            count = self.cursor.rowcount
            return count
        except connector.Error as err:
            self.cnx.rollback()
            return err
    

    """
    *********************
    * Asientos metodos *
    *********************
    """

    def create_asiento(self,asiento,id_sala,horario,fecha):
        
        try:
            sql = 'INSERT INTO Asientos (`id_asiento`,`c_id_sala`,`c_hora`,`o_date`) VALUES (%s,%s,%s,%s)'
            vals = (asiento,id_sala,horario,fecha)
            self.cursor.execute(sql,vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err

    def read_asiento(self,asiento,id_sala,horario):
        try:
            sql = 'SELECT * FROM Asientos WHERE id_asiento = %s AND c_id_sala = %s AND c_hora = %s'
            vals = (id_sala,)
            self.cursor.execute(sql,vals)
            record = self.cursor.fetchone()
            return record
        except connector.Error as err:
            return err 

    def read_all_asientso(self,c_id_sala,c_hora):
        try:
            sql = 'SELECT * FROM Asientos WHERE  c_id_sala = %s AND c_hora = %s'
            vals = (c_id_sala,c_hora)
            self.cursor.execute(sql,vals)
            record = self.cursor.fetchall()
            return record
        except connector.Error as err:
            return err 
        
    def delete_asiento(self, asiento,id_sala,horario):
        try:
            sql = 'DELETE FROM Asientos WHERE id_asiento = %s AND c_id_sala = %s AND c_hora = %s'
            vals = (asiento,id_sala,horario,)
            self.cursor.execute(sql,vals)
            self.cnx.commit()
            count = self.cursor.rowcount
            return count
        except connector.Error as err:
            self.cnx.rollback()
            return err


    """
    ******************
    * Boleto Methods *
    ******************
    """
    def create_boleto(self,id_asiento,pelicula,correo,c_id_sala,c_hora,fecha):
        try:
            sql = 'INSERT INTO Boleto (`id_asiento`,`peliula`,`correo`,`c_id_sala`,`c_hora`,`o_date`) VALUES (%s,%s,%s,%s,%s,%s)'
            vals = (id_asiento,pelicula,correo,c_id_sala,c_hora,fecha)
            self.cursor.execute(sql,vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            print(err)
            self.cnx.rollback()
            return err

    def read_boleto(self,id_boleto):
        try:
            sql = 'SELECT * FROM Boleto WHERE id_boleto = %s'
            vals = (id_boleto,)
            self.cursor.execute(sql,vals)
            record = self.cursor.fetchone()
            return record
        except connector.Error as err:
            return err 

    def read_all_boletos(self,sala,hora,fecha):
        try:
            sql = 'SELECT id_asiento FROM Boleto  WHERE c_id_sala = %s AND c_hora = %s AND o_date = %s'
            vals = (sala,hora,fecha)
            self.cursor.execute(sql,vals)
            record = self.cursor.fetchall()
            return record
        except connector.Error as err:
            return err 
        

    def update_boleto(self,fields,vals):
        try:
            sql = 'UPDATE Boleto SET '+','.join(fields)+'WHERE id_boleto = %s'
            self.cursor.execute(sql,vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err

    def delete_boleto(self, id_boleto):
        try:
            sql = 'DELETE FROM Boleto WHERE id_boleto = %s'
            vals = (id_boleto)
            self.cursor.execute(sql,vals)
            self.cnx.commit()
            count = self.cursor.rowcount
            return count
        except connector.Error as err:
            self.cnx.rollback()
            return err

    """
    ******************
    * Ticket Methods *
    ******************
    """
    
    def read_boleto_user(self,correo):
        try:
            sql = 'SELECT * FROM Boleto WHERE correo = %s'
            vals = (correo,)
            self.cursor.execute(sql,vals)
            record = self.cursor.fetchall()
            return record
        except connector.Error as err:
            return err 

    def read_boleto_user_date(self,correo,fecha):
        try:
            sql = 'SELECT * FROM Boleto WHERE correo = %s AND o_date = %s'
            vals = (correo,fecha)
            self.cursor.execute(sql,vals)
            record = self.cursor.fetchall()
            return record
        except connector.Error as err:
            return err 

    def read_boleto_user_date_time(self,correo,fecha,hora):
        try:
            sql = 'SELECT * FROM Boleto WHERE correo = %s AND o_date = %s AND c_hora = %s'
            vals = (correo,fecha,hora)
            self.cursor.execute(sql,vals)
            record = self.cursor.fetchall()
            return record
        except connector.Error as err:
            return err 
