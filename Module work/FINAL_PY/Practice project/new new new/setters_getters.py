class game_class:
    def __init__(self, release_month, publisher_name, game_title):
        self.__release_month = release_month
        self.__publisher_name = publisher_name
        self.__game_title = game_title

    def set_release_month(self,release_month):
        self.__release_month = release_month
    def get_release_month(self):
        return self.__release_month

    def set_publisher_name(self,publisher_name):
        self.__publisher_name = publisher_name
    def get_publisher_name(self):
        return self.__publisher_name

    def set_game_title(self,game_title):
        self.__game_title = game_title
    def get_game_title(self):
        return self.__game_title
    
