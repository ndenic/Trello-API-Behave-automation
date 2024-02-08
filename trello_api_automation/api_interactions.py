import requests
from .data_class import TrelloBoard
from .config import Config

class TrelloAPI:
    def __init__(self, api_key, token):
        #redudancy of code, pogledaj kasnije 
        self.api_key = Config.API_KEY
        self.token = Config.TOKEN
        self.base_url = Config.BASE_URL

    def create_trello_board(self, board_name, board_desc=""):
        url = f"{self.base_url}boards/"
        params = {
            'key': self.api_key,
            'token': self.token,
            'name': board_name,
            'desc': board_desc
        }

        response = requests.post(url, params=params)

        if response.status_code == 200:
            board_data = response.json()
            return TrelloBoard(id=board_data['id'], name=board_data['name'], desc=board_data['desc'])
        else:
            print(f"Error: {response.status_code}")
            return None
