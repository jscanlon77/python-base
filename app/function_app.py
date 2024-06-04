from .container.container import Container
import azure.functions as func

from app.function.cash_function import cash_function

app = func.FunctionApp() 

# don't forget to register your blueprint too.
app.register_functions(cash_function)

# init dependencies for Resource type.
container = Container()
container.init_resources()
container.wire(packages=["cash_package"])