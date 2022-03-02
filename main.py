from src.security.security import securityKEY
from src.instance.server import server
from src.controllers.routers import *

securityKEY()
server.run()