from abc import *


class ChessPlayer(ABC):

    @abstractmethod
    def move_piece(self, piece, end_place):
        pass

    @abstractmethod
    def start_match(self):
        pass

    @abstractmethod
    def wait_for_move(self):
        pass
