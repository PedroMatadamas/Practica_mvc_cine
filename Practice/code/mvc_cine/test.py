# from model.model import Model

# m = Model()
# data = m.read_detalles_pelicula(1)
# print(data)


# m.create_gen('Accion')
# m.create_gen('Comedia')
# m.create_gen('Romance')

# m.create_director('Pedro','Matadamas','Marin','Mexicano','1995-05-26','Ingeniero')
# m.create_director('Fabiola','Sierra','','Mexicano','1995-12-28','Ingeniero')

# m.create_actor('Levi','Alvarez','Quijano','Mexicano','1995-10-22')
# m.create_actor('Alondra','Arredondo','Martinez','Mexicano','1996-05-08')

# m.create_movie('Cloud Atlas','Español','Ingles','2017', 2 ,'Una historia de algo','120 min')
# m.create_movie('Batman','Ingles','Español','2017', 2 ,'Una historia de algo','140 min')
# m.create_movie('Avatar','Español',None,'2017', 2 ,'Una historia ','120 min')

# m.create_ac_mov(2,1)
# m.create_ac_mov(1,2)
# m.create_ac_mov(2,3)

# m.create_amdin('Pedro','Matadamas','Marin','Mexicana','1995-05-26','pedro_matadamas@gmail.com','Nosfer17')
# m.create_sala(1,10,20,200)
# m.create_sala(2,10,20,200)
# m.create_sala(3,15,22,200)

# m.create_cartelera(1,1,'13:30','2020-05-29')
# m.create_cartelera(1,1,'15:30','2020-05-29') 
# m.create_cartelera(1,1,'17:30','2020-05-29')
# m.create_cartelera(2,2,'15:30','2020-05-29') 
# m.create_cartelera(2,2,'17:30','2020-05-29')
# m.create_cartelera(2,2,'18:30','2020-05-29') 
# m.create_cartelera(3,3,'15:30','2020-05-29') 
# m.create_cartelera(3,3,'17:30','2020-05-29')
# m.create_cartelera(3,3,'18:30','2020-05-29') 

# m.create_cartelera(1,1,'13:30','2020-05-30')
# m.create_cartelera(1,1,'15:30','2020-05-30') 
# m.create_cartelera(1,1,'17:30','2020-05-30')
# m.create_cartelera(2,2,'15:30','2020-05-30') 
# m.create_cartelera(2,2,'17:30','2020-05-30')
# m.create_cartelera(2,2,'18:30','2020-05-30') 
# m.create_cartelera(3,3,'15:30','2020-05-30') 
# m.create_cartelera(3,3,'17:30','2020-05-30')
# m.create_cartelera(3,3,'18:30','2020-05-30') 

# m.create_cartelera(1,1,'13:30','2020-05-31')
# m.create_cartelera(1,1,'15:30','2020-05-31') 
# m.create_cartelera(1,1,'17:30','2020-05-31')
# m.create_cartelera(2,2,'15:30','2020-05-31') 
# m.create_cartelera(2,2,'17:30','2020-05-31')
# m.create_cartelera(2,2,'18:30','2020-05-31') 
# m.create_cartelera(3,3,'15:30','2020-05-31') 
# m.create_cartelera(3,3,'17:30','2020-05-31')
# m.create_cartelera(3,3,'18:30','2020-05-31') 

# m.create_cartelera(1,1,'13:30','2020-06-01')
# m.create_cartelera(1,1,'15:30','2020-06-01') 
# m.create_cartelera(1,1,'17:30','2020-06-01')
# m.create_cartelera(2,2,'15:30','2020-06-01') 
# m.create_cartelera(2,2,'17:30','2020-06-01')
# m.create_cartelera(2,2,'18:30','2020-06-01') 
# m.create_cartelera(3,3,'15:30','2020-06-01') 
# m.create_cartelera(3,3,'17:30','2020-06-01')
# m.create_cartelera(3,3,'18:30','2020-06-01') 

# m.create_generos_peliculas(1,1)
# m.create_generos_peliculas(1,2)
# m.create_generos_peliculas(3,3)
# m.create_generos_peliculas(2,2)
# m.create_generos_peliculas(2,1)



# m.create_client('Ximena','Oros','Cardenaz','Mexicana','1995-05-26','ximena.oros@gmail.com','Nosfer17')
# m.create_client('Sofia','Matadamas','Marin','Mexicana','1993-03-26','sofia.matadamass@gmail.com','Nosfer17')



from controller.controller import Controller

c = Controller()

c.start()