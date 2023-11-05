#
#  Developed by Maximiliano Brignone 
#  https://github.com/mbrignone93
#  © 2023	
#

from engine.pieces.commons.block import Block
from engine.position import Position

class IBlock(Block):

	def __init__(self):
		super().__init__(id = 3)
		self.cells = {
			0: [Position(1, 0), Position(1, 1), Position(1, 2), Position(1, 3)],
			1: [Position(0, 2), Position(1, 2), Position(2, 2), Position(3, 2)],
			2: [Position(2, 0), Position(2, 1), Position(2, 2), Position(2, 3)],
			3: [Position(0, 1), Position(1, 1), Position(2, 1), Position(3, 1)]
		}
		self.move(-1, 3)