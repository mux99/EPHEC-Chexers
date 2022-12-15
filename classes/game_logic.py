# checkers on hexagonal grid
#	for details see readme.md
#
# Dourov Maxime   
# Cruquenaire Achille   
# Gendbeien Jonas
#

from re import findall

import bin.fcts as fcts
from classes.piece import Piece


class GameLogic:
    """
            DO NOT USE ALONE, will not work
            extension of App class
    """
    def is_piece(self, coord: tuple) -> bool:
        """
        :coords: (x,y,z) valid coordinates of the board

        :return: True if a piece is in that place, False otherwise
        """
        for piece in self._pieces:
            if coord == piece.coord:
                return True
        return False

    def get_piece(self, coord: tuple) -> Piece:
        """
        :coords: (x,y,z) valid coordinates of the board

        :return: the piece at the given coordinates, None if empty tile
        """
        for piece in self._pieces:
            if piece.coord == coord:
                return piece

    def take_piece(self, coord: tuple) -> None:
        """ take piece at given coords if any

        :coords: (x,y,z) valid coordinates of the board

        a taken piece is removed from the board
        """
        board = self._pieces
        for i in range(len(board)):
            if board[i].coord == coord:
                board[i].delete()
                del board[i]
                break

    def get_takes(self, coord, coord_2, player):
        """ list all takes for given moves

        :coords: (x,y,z) valid coordinates of the board, the current position
        :coords_2: (x,y,z) valid coordinates of the board, the new position
        :player: 'white' or 'black' is the current player

        :return: a list of the coords of the pieces that can be taken
        """
        out = []
        valid_takes = {(2, -1, -1): [(1, 0, -1), (1, -1, 0)],
                        (1, -2, 1): [(1, -1, 0), (0, -1, 1)],
                        (-1, -1, 2): [(0, -1, 1), (-1, 0, 1)],
                        (-2, 1, 1): [(-1, 1, 0), (-1, 0, 1)],
                        (-1, 2, -1): [(-1, 1, 0), (0, 1, -1)],
                        (1, 1, -2): [(1, 0, -1), (0, 1, -1)]}

        move = fcts.vector_sub(coord_2, coord)
        # find parallel vector
        base_move = None
        for i in valid_takes.keys():
            if fcts.vector_cross_product(move, i) == (0, 0, 0) and fcts.is_the_right_parallel(move, i):
                base_move = i
                break

        # list takes
        candidate = coord
        while True:  # do while candidate2 != move
            if candidate == coord_2:
                break
            if base_move is None:
                break
            for i in valid_takes[base_move]:
                take_coord = fcts.warp(fcts.vector_add(candidate, i))
                if self.is_piece(take_coord) and self.get_piece(take_coord).player == fcts.other_player(player):
                    out.append(take_coord)
            candidate = fcts.vector_add(base_move, candidate)
        return out

    def get_moves(self, coord, player):
        """ all coords of valid move from given coord
        
        :coords: (x,y,z) valid coordinates of the board
        :player: 'white' or 'black' is the current player

        :return: a list of the coords of new coords to move to, empty if none
        """
        out = []
        valid_moves = {"white": [(2, -1, -1), (1, -2, 1), (1, 1, -2)],
                       "black": [(-2, 1, 1), (-1, 2, -1), (-1, -1, 2)]}
        valid_back_moves = {"white": [(-1, 2, -1), (-1, -1, 2)],
                            "black": [(1, 1, -2), (1, -2, 1)]}
        valid_queen_moves = [(2, -1, -1), (1, -2, 1), (1, 1, -2),
                       (-1, 2, -1), (-2, 1, 1), (-1, -1, 2)]

        # move a queen
        if self.get_piece(coord).promotion:
            for i in valid_queen_moves:
                candidate = fcts.vector_add(coord, i)
                while not self.is_piece(fcts.warp(candidate)) and fcts.validate_coords(candidate):
                    out.append((candidate,len(self.get_takes(coord,candidate,player))))
                    candidate = fcts.vector_add(candidate, i)

        # move a standard piece
        else:
            # forward moves
            for i in valid_moves[player]:
                candidate = fcts.vector_add(coord, i)
                if not self.is_piece(fcts.warp(candidate)) and fcts.validate_coords(candidate):
                    out.append((candidate,len(self.get_takes(coord,candidate,player))))

            # back takes
            for i in valid_back_moves[player]:
                candidate = fcts.vector_add(coord, i)
                n = len(self.get_takes(coord,candidate,player))
                if not self.is_piece(fcts.warp(candidate)) and fcts.validate_coords(candidate) and n > 0:
                    out.append((candidate,n))

        # filter best mooves
        if len(out) == 0:
            return out

        out = sorted(out, key=lambda i: -i[1])
        while (out[-1][1] != out[0][1]):
            del out[-1]
        
        return [x[0] for x in out]

    def get_all_takes(self, coord: tuple, player: str):
        """ list takes for all possible moves

        :coords: (x,y,z) valid coordonates of the board
        :player: 'white' or 'black' is the current player

        :return: a list of the coords of the takable pieces
        """
        out = []

        for i in self.get_moves(coord, player):
            out += self.get_takes(coord, i, player)
        return list(dict.fromkeys(out))

    def get_winner(self):
        """ returns which player wins
        
        :return: 'white' or 'black'
        """
        black_pieces = [p for p in self._pieces if p.player == "black"]
        white_pieces = [p for p in self._pieces if p.player == "white"]
        return "white" if len(black_pieces) == 0 else "black"

    def is_game_finished(self):
        """ 
        :return: True if a player wins, False if not
        """
        string = self.__str__()  # this is not a good way to implement this, but it looks cooler
        return len(findall("white", string)) == 0 or len(findall("black", string)) == 0
        # black_pieces = [p for p in self._pieces if p.player == "black"]
        # white_pieces = [p for p in self._pieces if p.player == "white"]
        # return len(black_pieces) == 0 or len(white_pieces) == 0

    def get_preselection(self,player):
        """ return the coords of the preselected piece if any
        :player: 'white' or 'black' is the current player

        :return: the coord of the piece to be selected or None
        """
        out = []
        for p in self._pieces:
            if p.player == player:
                out.append((p.coord,len(self.get_all_takes(p.coord,player))))
        out = sorted(out, key=lambda i: -i[1])
        if len(out) > 0 and out[0][1] > 0:
            return out[0][0]
