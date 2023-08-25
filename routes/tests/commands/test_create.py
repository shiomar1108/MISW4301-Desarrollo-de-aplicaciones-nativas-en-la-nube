
import random
from src.commands.create import CreateRoute
from faker import Faker


# Clase que contiene la logica de las pruebas del servicio de trayectos
class TestCreate():
    flightId_values_provider = DynamicProvider(
        provider_name="flightId_provider",
        elements=["686", "687", "688", "689", "690"],
        )
    
    sourceAirportCode_values_provider = DynamicProvider(
        provider_name="sourceAirportCode_provider",
        elements=["BOG", "MDE", "AXM", "BGA", "LET","PEI","ADZ","SMR"],
        )
    
    sourceCountry_values_provider = DynamicProvider(
        provider_name="sourceCountry_provider",
        elements=["Colombia", "Mexico", "Peru", "Ecuador", "Brasil","EEUU","España","Noruega"],
        )
    
    dataFactory = Faker()
    dataFactory.add_provider(flightId_values_provider)
    dataFactory.add_provider(sourceAirportCode_values_provider)
    dataFactory.add_provider(sourceCountry_values_provider)    
    
    flightId = None
    sourceAirportCode = None
    sourceCountry = None
    destinyAirportCode = None
    destinyCountry = None
    bagCost = None
    plannedStartDate = None
    plannedEndDate = None
    data = {}
    

    # Función que genera datos del la oferta
    def set_up(self): 
        
        self.flightId = self.dataFactory.flightId_provider()
        self.sourceAirportCode = self.dataFactory.sourceAirportCode_provider()
        self.sourceCountry = self.dataFactory.sourceCountry_provider()
        self.destinyAirportCode = self.dataFactory.sourceAirportCode_provider()
        self.destinyCountry = self.dataFactory.sourceCountry_provider()
        self.bagCost = self.dataFactory.pydecimal(left_digits=6, right_digits=0, positive=True)
        self.plannedStartDate = '2022-09-01T21:20:53.214Z'
        self.plannedEndDate = '2022-09-27T21:20:53.214Z'
        
        self.data = {
            "flightId"=f"{self.flightId}",
            "sourceAirportCode"=f"{self.sourceAirportCode}",
            "sourceCountry"=f"{self.sourceCountry}",
            "destinyAirportCode"=f"{self.destinyAirportCode}",
            "destinyCountry"=f"{self.destinyCountry}",
            "bagCost"=f"{self.bagCost}",
            "plannedStartDate"=f"{self.plannedStartDate}",
            "plannedEndDate"=f"{self.plannedEndDate}",
            )
