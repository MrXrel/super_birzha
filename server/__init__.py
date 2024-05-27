from flask import Flask
from flask_login import LoginManager
from db import database
from parser import parser
import os
from server.config import TOKEN, METAL_KEY, EXCHANGE_RATE_KEY

DATABASE = "db/superbirzha.db"
SECRET_KEY = "KETUNREAL"  # Запилить конфиг-файл надо будет
CURRENCIES = {
    "XAU": ["GLDRUB_TOM", "Золото", 4],
    "USD": ["USD000000TOD", "Доллар США", 1],
    "CNY": ["CNYRUB_TMS", "Китайский юань", 3],
    "EUR": ["EUR_RUB__TOM", "Eвро", 2],
}
# token = "t.IEa99GPRoD0m0Z3MH_M2BUMIAVsqYMCpcmJhQFIKDw8rg3tk7CpENgicqyVpOMSTK1ubCt1ZB7SQCXTcEy0Dcw"
# metal_key = "5f266da4bdd540557f1d6c8707360cc8"
# exchange_rate_key = "752cb5b3134f445168799121"

app = Flask(__name__)
app.config.from_object(__name__)
app.config.update(dict(DATABASE=os.path.join(app.root_path, "superbirzha.db")))

login_manager = LoginManager(app)
login_manager.login_message = ""
login_manager.login_view = "get_user_authorization"


dbase = database.Database()
parser_API = parser.CurrencyInfo(TOKEN, METAL_KEY, EXCHANGE_RATE_KEY)

from server import models
from server import views
