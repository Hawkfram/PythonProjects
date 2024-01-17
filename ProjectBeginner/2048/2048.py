import logic as lg
import tkinter as tk
import settings as setting

root = tk.Tk()
# Créer un cadre pour la grille
grid_frame = tk.Frame(root, bg="#92877D")
grid_frame.grid(padx=30, pady=10)

def boucle_jeu():
	genererMap()
	root.after(setting.IPS,boucle_jeu)

def on_left_arrow(event):
	lg.moveElementLeft()
	lg.generationElement2()
	score()
	genererMap()

def on_right_arrow(event):
	lg.moveElementRight()
	lg.generationElement2()
	score()
	genererMap()

def on_up_arrow(event):
	lg.moveElementUp()
	lg.generationElement2()
	score()
	genererMap()

def on_down_arrow(event):
	lg.moveElementDown()
	lg.generationElement2()
	score()
	genererMap()

def controle():
	root.bind("<Left>",on_left_arrow)
	root.bind("<Right>", on_right_arrow)
	root.bind("<Up>", on_up_arrow)
	root.bind("<Down>", on_down_arrow)

def genererMap():
	for i in range(len(setting.GRILLEJEUX)):
		for j in range(len(setting.GRILLEJEUX[i])):
			label = tk.Label(grid_frame, text=str(setting.GRILLEJEUX[i][j] if setting.GRILLEJEUX[i][j] != 0 else ""), bg=setting.couleur[setting.GRILLEJEUX[i][j]], fg="#fff", width=10, height=5, font=("Arial", 10))
			label.grid(row=i+1, column=j+1, padx=2, pady=2)

def score():
	score = 0
	for row in setting.GRILLEJEUX:
		score += sum(row)
	print(score)
	Label = tk.Label(grid_frame,text="Score : "+str(score), bg="#92877D")
	Label.grid(row=0, column=0, columnspan=len(setting.GRILLEJEUX),pady = 20,padx=20)

def init_game_window():
	root.title("2048")
	root.geometry("420x450")
	root.config(bg='#92877D')
	lg.generationElement2()


if __name__ == '__main__':
	init_game_window()
	controle()
	score()
	genererMap()
	root.mainloop()	
