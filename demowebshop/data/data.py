import os

from dotenv import load_dotenv


load_dotenv()


class Data:
    BASE_URL = os.getenv("BASE_URL")
    CART_URL = BASE_URL + "/cart"

    LOGIN = os.getenv("LOGIN")
    PASSWORD = os.getenv("PASSWORD")