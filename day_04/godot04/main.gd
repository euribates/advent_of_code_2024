extends Node2D

@onready var file_dialog: FileDialog = %SelectFileDialog
@onready var tile_map: TileMapLayer = %TileMap

var width : int = 0
var height: int = 0

func _ready():
	print('ok')
	
	
func _on_button_button_up() -> void:
	file_dialog.show()


func _on_select_file_dialog_file_selected(path: String) -> void:
	print('path:', path)
	print(file_dialog.get_current_path())
	var file = FileAccess.open(path, FileAccess.READ)
	height = 0
	tile_map.clear()
	while not file.eof_reached():
		var line = file.get_line()
		if line != '':
			height = height + 1
			width = line.length()
			var col: int = 0
			for chr in line:
				if chr == ' ':
					tile_map.set_cell(Vector2(col, height), 0, Vector2(0, 0))
				elif chr == '.':
					tile_map.set_cell(Vector2(col, height), 0, Vector2(1, 0))
				elif chr == 'X':
					tile_map.set_cell(Vector2(col, height), 0, Vector2(2, 0))
				elif chr == 'M':
					tile_map.set_cell(Vector2(col, height), 0, Vector2(3, 0))
				elif chr == 'A':
					tile_map.set_cell(Vector2(col, height), 0, Vector2(4, 0))
				elif chr == 'S':
					tile_map.set_cell(Vector2(col, height), 0, Vector2(5, 0))
				col = col + 1
					
	print('width:', width)
	print('height:', height)
	var panel: Panel = %Panel
	panel.set_size(Vector2(width * 23, height * 32))
