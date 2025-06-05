# Clase de configuración para la aplicación Flask
class Config:
    # URI de conexión a la base de datos PostgreSQL
    # Formato: 'postgresql://usuario:contraseña@host:puerto/nombre_base_datos'
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:Andriw4452@localhost:5432/tareasdb'

    # Desactiva el seguimiento de modificaciones de objetos por parte de SQLAlchemy
    # Esto mejora el rendimiento y evita advertencias innecesarias
    SQLALCHEMY_TRACK_MODIFICATIONS = False
