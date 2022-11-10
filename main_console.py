from classes.app import App
import bin.fcts as fcts

app = App()

if __name__ == '__main__':
	#setup board
	app.init_board()

	while True:
		print(app)
		try:
			if app._clicked_coord == None:
				tmp = input("enter a coordonate to select a piece [x,y,z], type quit to exit: ").split(",")
				if tmp == ["quit"]:
					break
				click_coords = (int(tmp[0]),int(tmp[1]),int(tmp[2]))
			else:
				tmp = input("enter a coordonate to move to [x,y,z]: ").split(",")
				if tmp == ["quit"]:
					break
				click_coords = (int(tmp[0]),int(tmp[1]),int(tmp[2]))
		except:
			pass
			
		#discard invalid clicks
		if not fcts.validate_click(click_coords):
			continue

		#select piece
		if app.is_piece(click_coords) and app.get_piece(click_coords).player == app._curent_player:
			app._clicked_coord = click_coords
			print("you have selected:",click_coords)
			app._possible_moves = app.get_moves(app._clicked_coord,app._curent_player)
			print(F"Possible moves {app._possible_moves}")

		#move selected
		elif not app.is_piece(click_coords) and app._clicked_coord != None:
			#only if move is valid
			if click_coords in app._possible_moves:
				app.get_piece(app._clicked_coord).coord = click_coords
				app._clicked_coord = None

				#remove taken pieces
				for i in app._possible_takes:
					app.take_piece(i)
					app._possible_takes = []

		#update gamestate
		if app._clicked_coord != None:

			#mark new takes
			app._possible_takes = app.get_takes(app._clicked_coord,app._curent_player)

		#AT temporary
		if app._clicked_coord == None:
			app.AI_move()
		if app.finish_game():
			break
