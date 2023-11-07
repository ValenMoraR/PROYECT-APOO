class Cancion:
    def __init__(self, nombre, archivo):
        self.nombre = nombre
        self.archivo = archivo
        self.es_favorita = False
    
    def to_dict(self):
        """Convierte una instancia de Cancion en un diccionario serializable en JSON."""
        return {
            "nombre": self.nombre,
            "archivo": self.archivo,
            "es_favorita": self.es_favorita
        }
