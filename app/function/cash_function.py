import logging

import azure.functions as func
from dependency_injector.wiring import Provide, inject
from app.container.container import Container
from app.services.cash_service import CashService

cash_function = func.Blueprint() 
@inject
def get_container(global_container : Container = Provide[Container.global_container]) :
    return global_container
@cash_function.route(route="cashfunction")
@cash_function.http_type("GET")
def runcashtrigger(
    req: func.HttpRequest) -> func.HttpResponse: 
    logging.info('Python HTTP trigger function processed a request.') 
    global_container : Container = get_container()
    service: CashService = global_container.cash_service()
    service.get_cash()
    return func.HttpResponse( 
        body=service.test(),
        status_code= 200)