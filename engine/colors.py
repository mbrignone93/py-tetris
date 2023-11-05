#
#  Developed by Maximiliano Brignone 
#  https://github.com/mbrignone93
#  © 2023	
#

class Colors:

	dark_grey = (26, 31, 40)
	# color pieces
	cyan = (21, 204, 209)
	blue = (13, 64, 216)
	orange = (226, 116, 17)
	yellow = (237, 234, 4)
	green = (47, 230 ,23)
	purple = (166, 0, 247)
	red = (232, 18, 18)
	# ------------
	white = (255, 255, 255)
	dark_blue = (44, 44, 127)
	light_blue = (59, 85, 162)

	@classmethod
	def get_cell_colors(cls):
		return [cls.dark_grey, cls.cyan, cls.blue, cls.orange, cls.yellow, 
		cls.green, cls.purple, cls.red, cls.white, cls.dark_blue, cls.light_blue]
 