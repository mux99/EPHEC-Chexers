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

    def is_piece(self, coord: tuple):
        """
        :coords: (x,y,z) valid coordonates of the board

        :return: True if a piece is in that place, False otherwise
        """
        for piece in self._pieces:
            if coord == piece.coord:
                return True
        return False

    def get_piece(self, coord: tuple) -> Piece:
        """
        :coords: (x,y,z) valid coordonates of the board

        :return: the piece a the given coordonates, None if empty tile
        """
        for piece in self._pieces:
            if piece.coord == coord:
                return piece

    def take_piece(self, coord: tuple):
        """ take piece at given coords if any

        :coords: (x,y,z) valid coordonates of the board

        a taken piece is removed from the board
        """
        board = self._pieces
        for i in range(len(board)):
            if board[i].coord == coord:
                board[i].delete()
                del board[i]
                break

    def get_all_takes(self, coord: tuple, player: str):
        """ list takes for all possible moves

        :coords: (x,y,z) valid coordonates of the board
        :player: 'white' or 'black' is the current player

        :return: a list of the coords of the takable pieces
        """
        out = []

        # list possible moves
        if self.get_piece(coord).promotion:
            moves = self.filter_moves(
                coord, player, self.get_moves_queen(coord))
        else:
            moves = self.filter_moves(
                coord, player, self.get_moves(coord, player))

        # list takes for each moves
        for i in moves:
            out += self.get_takes(coord, i, player)
        return list(dict.fromkeys(out))

    def get_takes(self, coord, coord_2, player):
        """ list all takes for given moves

        :coords: (x,y,z) valid coordonates of the board, the current position
        :coords_2: (x,y,z) valid coordonates of the board, the new position
        :player: 'white' or 'black' is the current player

        :return: a list of the coords of the takable pieces
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
        tmp = coord
        while True:  # do while tmp2 != move
            if tmp == coord_2:
                break
            if base_move is None:
                break
            for i in valid_takes[base_move]:
                take_coord = fcts.vector_add(tmp, i)
                if self.is_piece(take_coord) and self.get_piece(take_coord).player == fcts.other_player(player):
                    out.append(take_coord)
            tmp = fcts.vector_add(base_move, tmp)
        return out

    def get_moves(self, coord, player):
        """ all coords of valid move from given coord
        
        :coords: (x,y,z) valid coordonates of the board
        :player: 'white' or 'black' is the current player

        :return: a list of the coords of new coords to move to, empty if none
        """
        out = []
        valid_moves = {"white": [(2, -1, -1), (1, -2, 1), (1, 1, -2)],
                       "black": [(-2, 1, 1), (-1, 2, -1), (-1, -1, 2)]}
        valid_back_moves = {
            "white": [(-1, 2, -1), (-1, -1, 2)], "black": [(1, 1, -2), (1, -2, 1)]}

        # forward moves
        for i in valid_moves[player]:
            tmp = fcts.vector_add(coord, i)

            # warp
            warp_coord = fcts.warp(tmp)
            if warp_coord is not None and not self.is_piece(warp_coord):
                out.append(warp_coord)

            # normal
            if not self.is_piece(tmp) and fcts.validate_coords(tmp):
                out.append(tmp)

        # back takes
        for i in valid_back_moves[player]:
            tmp = fcts.vector_add(coord, i)
            n = len(self.get_takes(coord, tmp, player))
            if not self.is_piece(tmp) and fcts.validate_coords(tmp) and n > 0:
                out.append(tmp)

        return out

    def get_moves_queen(self, coord):
        """ return coords of valid moves form given coord for queen (promoted pieces)
        
        :coords: (x,y,z) valid coordonates of the board

        :return: a list of the coords of new coords to move to, empty if none
        """
        out = []
        valid_moves = [(2, -1, -1), (1, -2, 1), (1, 1, -2),
                       (-1, 2, -1), (-2, 1, 1), (-1, -1, 2)]
        warp_coords = {}

        for i in valid_moves:
            tmp = fcts.vector_add(coord, i)
            warp_coord = fcts.warp(tmp)
            if warp_coord is not None and not self.is_piece(warp_coord):
                out.append(warp_coord)
                warp_coords[warp_coord] = i
            while not self.is_piece(tmp) and fcts.validate_coords(tmp):
                out.append(tmp)
                tmp = fcts.vector_add(tmp, i)
                warp_coord = fcts.warp(tmp)
                if warp_coord is not None and not self.is_piece(warp_coord):
                    out.append(warp_coord)
                    warp_coords[warp_coord] = i

        for w, m in warp_coords.items():
            tmp = fcts.vector_add(w, m)
            while not self.is_piece(tmp) and fcts.validate_coords(tmp):
                out.append(tmp)
                tmp = fcts.vector_add(tmp, m)
        return out

    def filter_moves(self, coord, player, moves):
        """ filter given moves acording tu rule of priority
        
        :coords: (x,y,z) valid coordonates of the board
        :player: 'white' or 'black' is the current player
        :moves: [(x,y,z),...] list of valid coordonates of the board
			can be empty

        :return: a list of the coords of new coords to move to, empty if none
        """
        out = []
        for i in moves:
            out.append((i, len(self.get_takes(coord, i, player))))

        # sort moves by number of takes
        out = sorted(out, key=lambda i: -i[1])
        i = 0
        while i < len(out):
            if out[i][1] < out[0][1]:
                del out[i]
            else:
                i += 1
        return [x[0] for x in out]

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
        string = self.__str__()  # this is not a good way to implement this but it looks cooler
        return len(findall("white", string)) == 0 or len(findall("black", string)) == 0
        # black_pieces = [p for p in self._pieces if p.player == "black"]
        # white_pieces = [p for p in self._pieces if p.player == "white"]
        # return len(black_pieces) == 0 or len(white_pieces) == 0

    def get_preselection(self,player):
        """ return the coords of the preselected piece if any
        :player: 'white' or 'black' is the current player
        """
        out = []
        for p in self._pieces:
            if p.player == player:
                out.append((p.coord,len(self.get_all_takes(p.coord,player))))
        out = sorted(out, key=lambda i: -i[1])
        if len(out) > 0 and out[0][1] > 0:
            return out[0][0]
