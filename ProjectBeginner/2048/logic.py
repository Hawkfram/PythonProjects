import random as rd
import settings as setting

def generationElement2():
	ligne = rd.randint(0,3)
	col = rd.randint(0,3)

	while(setting.GRILLEJEUX[ligne][col] != 0):
		ligne = rd.randint(0,3)
		col = rd.randint(0,3)
	
	setting.GRILLEJEUX[ligne][col] = 2

def moveElementRight():
	for i in range(len(setting.GRILLEJEUX)):
		for j in range(len(setting.GRILLEJEUX[i])):
			if setting.GRILLEJEUX[i][j] != 0:
				if(setting.GRILLEJEUX[i][3] == 0):
					setting.GRILLEJEUX[i][x] = setting.GRILLEJEUX[i][j]			
				else:
					for x in range(j,len(setting.GRILLEJEUX[i])-1):
						if setting.GRILLEJEUX[i][x+1] != 0:
							setting.GRILLEJEUX[i][x] = setting.GRILLEJEUX[i][j]
