from scene import *
from settings import data


def getTileSize((w, h)):
    return data.dtilesize

class Tile(object):
    def __init__(self, num, pos, size):
        #print size
        self.num = num
        self.img, self.imgsize = render_text(self.num,
                                                data.dfontfamily,
                                                data.dfontsize)
        self.size = size
        self.bounds = Rect(pos.x - size.w/2, pos.y - size.h/2, *size)
        self.bgcolour = data.dtilecolour
        
        self.strokecolour = data.dstrokecolour
        self.strokeweight = data.dstrokeweight
    
    def draw(self):
        #fill(1, 0, 0)
        #rect(*self.bounds)
        x, y, w, h = self.bounds
        
        stroke(*self.strokecolour)
        stroke_weight(self.strokeweight)
        
        fill(*self.bgcolour)
        rect(x, y, w, h)
        
        iw, ih = self.imgsize
        image(self.img, x + w/2 - iw, y + h/2 - ih)
