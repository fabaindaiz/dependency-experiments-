from dependency_injector import containers, providers
from src.service2 import Service2

class Service2Container(containers.DeclarativeContainer):
    service = providers.Singleton(Service2)