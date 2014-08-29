from scene import *
from namespace import Namespace

data = Namespace()

data.dfontsize = 25
data.dfontfamily = "Monofur"

data.dtilesize = Size(128, 128) # Tile size on iPad 3
data.dtilecolour = (0, 0.8, 0)

data.dstrokecolour = (0.01, 0.21, 0.286)
data.dstrokeweight = 1

data.dbgcolour   = (0.01, 0.21, 0.286)

data.boardsize   = (4, 4)
data.pstart      = Point(200, 700)
data.pbwidth     = 5
data.dpbbg       = (0, 0.196, 1)

data.UP          = 1
data.DOWN        = 2
data.LEFT        = 3
data.RIGHT       = 4

data.BDBG = (1.0, 1.0, 1.0) # Button Default BackGround
data.BPBG = (0.8, 0.8, 0.8) # Button Pressed BackGround

data.TDFG = (0.0, 0.0, 0.0) # Text Default ForeGround
data.TPFG = (0.0, 0.0, 0.0) # Text Pressed ForeGround
