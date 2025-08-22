from typing import Type

from dependency_injector import containers
from fastapi import Depends

from app.src.shared.infrastructure.containers.main_container import MainContainer

def get_main_container():
    container = MainContainer()
    return container

def container_manager(
    container_use_case: Type[containers.DeclarativeContainer],
):
    async def container_use_case_factory(
        main_container: MainContainer = Depends(get_main_container),
    ):
        container = container_use_case()
        container.main_container.override(main_container)
        await container.init_resources()
        return container

    return container_use_case_factory
