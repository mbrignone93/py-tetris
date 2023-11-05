#
#  Developed by Maximiliano Brignone 
#  https://github.com/mbrignone93
#  © 2023	
#

from engine.pieces.commons.block import Block
from engine.position import Position

class ZBlock(Block):

	def __init__(self):
		super().__init__(id = 7)
		self.cells = {
			0: [Position(0, 0), Position(0, 1), Position(1, 1), Position(1, 2)],
			1: [Position(0, 2), Position(1, 1), Position(1, 2), Position(2, 1)],
			2: [Position(1, 0), Position(1, 1), Position(2, 1), Position(2, 2)],
			3: [Position(0, 1), Position(1, 0), Position(1, 1), Position(2, 0)]
		}
		self.move(0, 3)