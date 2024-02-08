from behave import given, when, then
from trello_api_automation.api_interactions import TrelloAPI
from trello_api_automation.data_class import TrelloBoard
from trello_api_automation.config import Config

trello_api = TrelloAPI(api_key=Config.API_KEY, token=Config.TOKEN)

@given('a Trello API key {api_key}')
def step_given_api_key(context, api_key):
    context.api_key = api_key

@given('a Trello API token {token}')
def step_given_api_token(context, token):
    context.token = token

@when('I create a new Trello board with name {board_name} and description {board_desc}')
def step_when_create_new_board(context, board_name, board_desc):
    context.created_board = trello_api.create_trello_board(board_name, board_desc)

@then('the API returns the new board details')
def step_then_check_new_board_details(context):
    assert context.created_board is not None
    assert isinstance(context.created_board, TrelloBoard)

@then('I print or save the new board details to {file_path}')
def step_then_print_save_new_board_details(context, file_path):
    with open(file_path, 'w') as file:
        file.write(f"Board ID: {context.created_board.id}\n")
        file.write(f"Board Name: {context.created_board.name}\n")
        file.write(f"Board Description: {context.created_board.desc}\n")
