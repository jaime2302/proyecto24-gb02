from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from . import models, crud 
import os 

"""
Autor: Grupo GA01 - ASEE
Versión: 1.0
Descripción: Conexión a la base de datos contenidos.db y creación de sesión

"""

# URL de la base de datos (SQLite en este caso)
SQLALCHEMY_DATABASE_URL = "sqlite:///./contenidos.db"

# Crear el motor para interactuar con la base de datos
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

# Crear una fábrica de sesiones para hacer queries
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base para los modelos de SQLAlchemy
Base = declarative_base()

# Dependencia para obtener una sesión de base de datos
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def initialize_database():
    if not os.path.exists("./contenidos.db"):
        # Crea las tablas si no existen
        Base.metadata.create_all(bind=engine)
        print("Base de datos creada y tablas inicializadas.")

        # Insertar valores iniciales
        db = SessionLocal()
        try:
            subtitulosExistentes = db.query(models.Subtitulo).count()
            if subtitulosExistentes == 0:
                subtitulo_nuevo = models.Subtitulo(idSubtitulo="1", idioma="Inglés")    
                db.add(subtitulo_nuevo)  
                subtitulo_nuevo = models.Subtitulo(idSubtitulo="2", idioma="Español")    
                db.add(subtitulo_nuevo)  
                subtitulo_nuevo = models.Subtitulo(idSubtitulo="3", idioma="Italiano")    
                db.add(subtitulo_nuevo)  
                subtitulo_nuevo = models.Subtitulo(idSubtitulo="4", idioma="Portugués")    
                db.add(subtitulo_nuevo)      
            
            doblajesExistentes = db.query(models.Subtitulo).count()
            if doblajesExistentes == 0:
                doblaje_nuevo = models.Doblaje(idDoblaje="1", idioma="Inglés")    
                db.add(doblaje_nuevo)  
                doblaje_nuevo = models.Doblaje(idDoblaje="2", idioma="Español")    
                db.add(doblaje_nuevo)  
                doblaje_nuevo = models.Doblaje(idDoblaje="3", idioma="Italiano")    
                db.add(doblaje_nuevo)  
                doblaje_nuevo = models.Doblaje(idDoblaje="4", idioma="Portugués")    
                db.add(doblaje_nuevo)

            actoresExistentes = db.query(models.Actor).count()
            if actoresExistentes == 0:
                actor_nuevo = models.Actor(idACtor="1", nombre="Robert Deniro", nacionalidad="EstadoUnidense", fechaNacimiento="1943-08-17")    
                db.add(actor_nuevo)  
                actor_nuevo = models.Actor(idACtor="2", idioma="Tom Cruise", nacionalidad="EstadoUnidense", fechaNacimiento="1962-07-03")    
                db.add(actor_nuevo)  
                actor_nuevo = models.Actor(idACtor="3", idioma="Tom Hardy", nacionalidad="Britanico", fechaNacimiento="1977-09-15")    
                db.add(actor_nuevo)  
                actor_nuevo = models.Actor(idACtor="4", idioma="George Clooney", nacionalidad="EstadoUnidense", fechaNacimiento="1961-05-06")    
                db.add(actor_nuevo)

            directoresExistentes = db.query(models.Director).count()
            if directoresExistentes == 0:
                directorNuevo = models.Director(id="1", nombre="Francis Ford Coppola", nacionalidad="EstadoUnidense", fechaNacimiento="1939-04-07")    
                db.add(directorNuevo)  
                directorNuevo = models.Director(id="2", idioma="Stanley Kubrik", nacionalidad="Estadounidense", fechaNacimiento="1928-07-26")    
                db.add(directorNuevo)  
                directorNuevo = models.Director(id="3", idioma="Jean Luc Godard", nacionalidad="Frances", fechaNacimiento="1930-12-03")    
                db.add(directorNuevo)  
                directorNuevo = models.Director(id="4", idioma="David Lynch", nacionalidad="EstadoUnidense", fechaNacimiento="1946-01-20")    
                db.add(directorNuevo)

            db.commit()
            print("Valores iniciales insertados (Idiomas).")
        finally:
            db.close()