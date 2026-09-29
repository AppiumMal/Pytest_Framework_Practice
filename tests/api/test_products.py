from xmlrpc import client

from core.api_client import ApiClient
from core.api_actions import ApiActions
from config.config import config

def test_get_products():

  client = ApiClient(config.BASE_URL)
  api = ApiActions(client)
  products = api.get_products()
  assert len(products) > 0, "No products returned"