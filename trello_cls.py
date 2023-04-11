from trello import TrelloApi


class Trello:
    trello = None
    board_id = None

    def __init__(self, app_key, user_token, board_id):
        self.trello = TrelloApi(app_key)
        self.board_id = board_id
        self.trello.set_token(user_token)
        self.trello.boards.get(self.board_id)

    def get_lists(self):
        return self.trello.boards.get_list(self.board_id)

    def get_cards(self, list_id):
        return self.trello.lists.get(list_id)

    def get_card(self, card_id):
        return self.trello.cards.get(card_id)
