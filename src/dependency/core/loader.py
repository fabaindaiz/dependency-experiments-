import logging
logger = logging.getLogger("DependencyLoader")

from pprint import pformat
from dependency.core.module import Module
from dependency.core.container import Container
from dependency.core.resolver import resolve_dependency_layers

def resolve_dependency(container: Container, appmodule: Module) -> None:
    logger.info("Resolving dependencies")

    unresolved_layers = appmodule.init_providers()
    resolved_layers = resolve_dependency_layers(unresolved_layers)

    named_layers = pformat(resolved_layers)
    logger.info(f"Layers:\n{named_layers}")

    for resolved_layer in resolved_layers:
        for provider in resolved_layer:
            provider.provider.populate_container(container)
    
    container.check_dependencies()
    container.init_resources()
    appmodule.init_bootstrap()
    logger.info("Dependencies resolved and injected")