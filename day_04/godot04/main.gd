extends Node2D

@onready var file_dialog: FileDialog = %SelectFileDialog
@onready var tile_map: TileMapLayer = %TileMap

var width : int = 0
var height: int = 0

func _on_button_button_up() -> void:
	file_dialog.show()


func _on_select_file_dialog_file_selected(path: String) -> void:
	print('path:', path)
	print(file_dialog.get_current_path())
	var file = FileAccess.open(path, FileAccess.READ)
	height = 0
	while not file.eof_reached():
		var line = file.get_line()
		if line != '':
			height = height + 1
			width = line.length()
	print('width:', width)
	print('height:', height)
