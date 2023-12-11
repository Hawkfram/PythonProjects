import logic as lg
import tkinter as tk
import settings as setting

root = tk.Tk()

def boucle_jeu():
	genererMap()
	root.after(setting.IPS,boucle_jeu)

def on_left_arrow(event):
	print("left")

def on_right_arrow(event):
	lg.moveElementRight()

def on_up_arrow(event):
	print("up")

def on_down_arrow(event):
	print("down")

def controle():
	root.bind("<Left>",on_left_arrow)
	root.bind("<Right>", on_right_arrow)
	root.bind("<Up>", on_up_arrow)
	root.bind("<Down>", on_down_arrow)

def genererMap():
	for i in range(len(setting.GRILLEJEUX)):
		for j in range(len(setting.GRILLEJEUX[i])):
			label = tk.Label(root, text=str(setting.GRILLEJEUX[i][j] if setting.GRILLEJEUX[i][j] != 0 else ""), bg="#9E948A" , width=10, height=5 )
			label.grid(row=i,column=j,padx=5,pady=5)

def init_game_window():
	root.title("2048")
	root.geometry("350x400")
	root.config(bg='#92877D')


if __name__ == '__main__':
	init_game_window()
	lg.generationElement2()
	controle()
	boucle_jeu()
	root.mainloop()	
