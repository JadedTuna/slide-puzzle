from scene import *
from tile import Tile, getTileSize
from settings import data
from button import TextButton
import sound
import random

sound.load_effect("Click_1")

class PuzzleScene(Scene):
    # For use with pcista
    _pgwindowtitle = "Slide Puzzle (NOT SUPPORTED YET)"
    
    def setup(self):
        self.tsize = getTileSize(self.size)
        tsx, tsy   = data.dtilesize
        
        pos        = Point(data.pstart.x - (data.pbwidth + tsx/2),
                      data.pstart.y - (data.boardsize[1] * tsy + data.pbwidth - tsy/2))
        size       = Size(data.boardsize[0] * tsx + data.pbwidth * 2,
                          data.boardsize[1] * tsy + data.pbwidth * 2)
                          
        self.pbbounds = Rect(pos.x, pos.y, *size)
        self.board = self.generateBoard(data.boardsize[0],
                                        data.boardsize[1],
                                        data.pstart,
                                        data.dtilesize)
        self.animated_tile = None
        self.button = TextButton(
            "Shuffle",
            Point(550, 780),
            Size(99, 51),
            [data.BDBG, data.BPBG],
            [data.TDFG, data.TPFG],
            "Monofur",
            25,
            lambda: self.shuffle(80)
        )
    
    def generateBoard(self, rows, columns, (sx, sy), tsize):
        board = []
        for y in range(rows):
            row = []
            for x in range(columns):
                num = str(rows * y + (x + 1))
                if y == rows - 1 and x == columns - 1:
                    num = "blank"
                pos = Point(sx + tsize.w * x, sy - tsize.h * y)
                row.append(Tile(num, pos, tsize))
            board.append(row)
        return board
    
    def draw(self):
        background(*data.dbgcolour)
        self.button.draw()
        fill(*data.dpbbg)
        rect(*self.pbbounds)
        for row in self.board:
            for tile in row:
                if tile and not tile.num == "blank":
                    tile.draw()
    
    def getTileClicked(self, point):
        for y, row in enumerate(self.board):
            for x, tile in enumerate(row):
                if point in tile.bounds and tile.num != "blank":
                    return tile, (y, x)
    
    def getBlankPosition(self):
        for y, row in enumerate(self.board):
            for x, tile in enumerate(row):
                if tile.num == "blank":
                    return (y, x)
    
    def pathToBlank(self, ty, tx):
        by, bx = self.getBlankPosition()
        if ty == by and tx - 1 == bx:
            return data.LEFT
        elif ty == by and tx + 1 == bx:
            return data.RIGHT
        elif ty - 1 == by and tx == bx:
            return data.UP
        elif ty + 1 == by and tx == bx:
            return data.DOWN
    
    def makeMove(self, direction):
        by, bx = self.getBlankPosition()
        if direction == data.UP:
            ty, tx = by + 1, bx
        
        elif direction == data.DOWN:
            ty, tx = by - 1, bx
        
        elif direction == data.LEFT:
            ty, tx = by, bx + 1
        
        elif direction == data.RIGHT:
            ty, tx = by, bx - 1
        
        self.move(direction, self.board[ty][tx], ty, tx)
    
    def move(self, direction, tile, ty, tx):
        by, bx = self.getBlankPosition()
        btile  = self.board[by][bx]
        
        tile.bounds, btile.bounds = btile.bounds, tile.bounds
        self.board[ty][tx] = btile
        self.board[by][bx] = tile
        sound.play_effect("Click_1")
    
    def getRandomMove(self):
        moves = [data.UP, data.DOWN, data.LEFT, data.RIGHT]
        by, bx = self.getBlankPosition()
        try:
            self.board[by + 1][bx]
        except IndexError:
            moves.remove(data.UP)
        
        try:
            self.board[by - 1][bx]
        except IndexError:
            moves.remove(data.DOWN)
        
        try:
            self.board[by][bx + 1]
        except IndexError:
            moves.remove(data.LEFT)
        
        try:
            self.board[by][bx - 1]
        except IndexError:
            moves.remove(data.RIGHT)
        
        return random.choice(moves)
    
    def shuffle(self, moves=1):
        for i in range(moves):
            move = self.getRandomMove()
            self.makeMove(move)
    
    def touch_began(self, touch):
        if touch.location in self.button.bounds:
            self.button.touch_began(touch)
    
    def touch_moved(self, touch):
        self.button.touch_moved(touch)
    
    def touch_ended(self, touch):
        if touch.location in self.button.bounds:
            self.button.touch_ended(touch)
        tinfo = self.getTileClicked(touch.location)
        if tinfo:
            tile, (ty, tx) = tinfo
            direction = self.pathToBlank(ty, tx)
            if direction:
                self.move(direction, tile, ty, tx)
        
    def run(self):
        # Use scene.run method to run self
        run(self, PORTRAIT, 2)

if __name__ == '__main__':
    PuzzleScene().run()
