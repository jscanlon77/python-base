import logging.config
import sqlite3
from dependency_injector import containers, providers

from app.services import cash_service
from app.repositories import cash_repository


class Container(containers.DeclarativeContainer):

    config = providers.Configuration(ini_files=["config.ini"])

    logging = providers.Resource(
        logging.config.fileConfig,
        fname="logging.ini",
    )

    # Services

    cash_service = providers.Factory(
        cash_service,
        cash_repository = cash_repository,
    )
    
    # Repositories
    cash_repository = providers.Factory(cash_repository)
    
    
