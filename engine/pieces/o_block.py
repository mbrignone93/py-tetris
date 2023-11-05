#
#  Developed by Maximiliano Brignone 
#  https://github.com/mbrignone93
#  © 2023	
#

from engine.pieces.commons.block import Block
from engine.position import Position

class OBlock(Block):

	def __init__(self):
		super().__init__(id = 4)
		self.cells = {
			0: [Position(0, 0), Position(0, 1), Position(1, 0), Position(1, 1)]
		}
		self.move(0, 4)