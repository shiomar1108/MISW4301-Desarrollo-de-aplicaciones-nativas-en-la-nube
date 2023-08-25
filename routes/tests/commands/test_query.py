import random
from src.commands.query import QueryRoute
from faker import Faker
from faker.providers import DynamicProvider

# Clase que contiene la logica de las pruebas del servicio de consulta de trayectos
class TestCreate():
    
    flightId_values_provider = DynamicProvider(
        provider_name="flightId_provider",
        elements=["686", "687", "688", "689", "690"],
        )
        
    flightId = None
    
    
    # Función que genera datos del la oferta
    def set_up(self): 
        self.flightId = self.dataFactory.flightId_provider()
        
        
    def test_create_get_route(self):
        # Creación oferta
        self.set_up()
        result = QueryRoute(flight).execute()
        assert result != None