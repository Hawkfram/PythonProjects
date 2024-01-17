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
	dim = len(setting.GRILLEJEUX)
	for row in range(dim):
		for col in range((dim-1),-1,-1):
			#print("Row : " + str(row) + " | Col : " + str(col) )
			#print("Value :"+ str(setting.GRILLEJEUX[row][col]))
			if(setting.GRILLEJEUX[row][col] != 0 and col != (dim-1)):
				colTmp = col
				while(colTmp != (dim-1)):
					if(setting.GRILLEJEUX[row][colTmp+1] == 0):
						moveRight(row,colTmp,0)
					elif(setting.GRILLEJEUX[row][colTmp+1] == setting.GRILLEJEUX[row][colTmp]):
						moveRight(row,colTmp,1)
					colTmp += 1
			
def moveRight(row,col,option):
	if(option):
		setting.GRILLEJEUX[row][(col+1)] = setting.GRILLEJEUX[row][col] * 2
	else:
		setting.GRILLEJEUX[row][(col+1)] = setting.GRILLEJEUX[row][col]
	setting.GRILLEJEUX[row][col] = 0

def moveElementLeft():
	dim = len(setting.GRILLEJEUX)
	for row in range(dim):
		for col in range(0,dim,1):
			#print("Row : " + str(row) + " | Col : " + str(col) )
			#print("Value :"+ str(setting.GRILLEJEUX[row][col]))
			if(setting.GRILLEJEUX[row][col] != 0 and col != dim):
				colTmp = col
				while(colTmp != 0):
					if(setting.GRILLEJEUX[row][colTmp-1] == 0):
						moveLeft(row,colTmp,0)
					elif(setting.GRILLEJEUX[row][colTmp-1] == setting.GRILLEJEUX[row][colTmp]):
						moveLeft(row,colTmp,1)
					colTmp -= 1

def moveLeft(row,col,option):
	if(option):
		setting.GRILLEJEUX[row][(col-1)] = setting.GRILLEJEUX[row][col] * 2
	else:
		setting.GRILLEJEUX[row][(col-1)] = setting.GRILLEJEUX[row][col]
	setting.GRILLEJEUX[row][col] = 0

def moveElementUp():
	dim = len(setting.GRILLEJEUX)
	for col in range(dim):
		for row in range((dim-1),-1,-1):
			#print("Col : " + str(col) + " | Row : " + str(row) )
			#print("Value :"+ str(setting.GRILLEJEUX[row][col]))
			if(setting.GRILLEJEUX[row][col] != 0):
				rowTmp = row
				while(rowTmp != 0):
					if(setting.GRILLEJEUX[rowTmp-1][col] == 0):
						moveUp(rowTmp,col,0)
					elif(setting.GRILLEJEUX[rowTmp-1][col] == setting.GRILLEJEUX[rowTmp][col]):
						moveUp(rowTmp,col,1)
					rowTmp-= 1

def moveUp(row,col,option):
	if(option):
		setting.GRILLEJEUX[(row-1)][col] = setting.GRILLEJEUX[row][col] * 2
	else:
		setting.GRILLEJEUX[(row-1)][col] = setting.GRILLEJEUX[row][col]
	setting.GRILLEJEUX[row][col] = 0

def moveElementDown():
	dim = len(setting.GRILLEJEUX)
	for col in range(dim):
		for row in range(0,(dim),1):
			#print("Col : " + str(col) + " | Row : " + str(row) )
			#print("Value :"+ str(setting.GRILLEJEUX[row][col]))
			if(setting.GRILLEJEUX[row][col] != 0):
				rowTmp = row
				while(rowTmp != (dim-1)):
					if(setting.GRILLEJEUX[rowTmp+1][col] == 0):
						moveDown(rowTmp,col,0)
					elif(setting.GRILLEJEUX[rowTmp+1][col] == setting.GRILLEJEUX[rowTmp][col]):
						moveDown(rowTmp,col,1)
					rowTmp+= 1

def moveDown(row,col,option):
	if(option):
		setting.GRILLEJEUX[(row+1)][col] = setting.GRILLEJEUX[row][col] * 2
	else:
		setting.GRILLEJEUX[(row+1)][col] = setting.GRILLEJEUX[row][col]
	setting.GRILLEJEUX[row][col] = 0

""" Version 1
def moveElementRight():
	for i in range(len(setting.GRILLEJEUX[0])):
		for j in range(len(setting.GRILLEJEUX)):
			if(setting.GRILLEJEUX[j][i] != 0 and len(setting.GRILLEJEUX[0])-1 != i):
				if(setting.GRILLEJEUX[j][(i+1)] == 0):
					setting.GRILLEJEUX[j][(i+1)] = setting.GRILLEJEUX[j][i]
					setting.GRILLEJEUX[j][i] = 0
				elif(setting.GRILLEJEUX[j][(i+1)] == setting.GRILLEJEUX[j][i]):
					setting.GRILLEJEUX[j][(i+1)] = setting.GRILLEJEUX[j][i] * 2
					setting.GRILLEJEUX[j][i] = 0

def moveElementLeft():
	for i in range(len(setting.GRILLEJEUX[0])):
		for j in range((len(setting.GRILLEJEUX)-1),0,-1):
			if(setting.GRILLEJEUX[i][j] != 0 and j != 0):
				if(setting.GRILLEJEUX[i][(j-1)] == 0):
					setting.GRILLEJEUX[i][(j-1)] = setting.GRILLEJEUX[i][j]
					setting.GRILLEJEUX[i][j] = 0
				elif(setting.GRILLEJEUX[i][(j-1)] == setting.GRILLEJEUX[j][i]):
					setting.GRILLEJEUX[i][(j-1)] = setting.GRILLEJEUX[i][j] * 2
					setting.GRILLEJEUX[i][j] = 0

def moveElementDown():
	for i in range(len(setting.GRILLEJEUX[0])):
		for j in range(len(setting.GRILLEJEUX)):
			if(setting.GRILLEJEUX[j][i] != 0 and j != (len(setting.GRILLEJEUX)-1)):
				if(setting.GRILLEJEUX[(j+1)][i] == 0):
					setting.GRILLEJEUX[(j+1)][i] = setting.GRILLEJEUX[j][i]
					setting.GRILLEJEUX[j][i] = 0
				if(setting.GRILLEJEUX[(j+1)][i] == setting.GRILLEJEUX[j][i]):
					setting.GRILLEJEUX[(j+1)][i] = setting.GRILLEJEUX[j][i] * 2
					setting.GRILLEJEUX[j][i] = 0

def moveElementUp():
	for i in range(len(setting.GRILLEJEUX[0])):
		for j in range((len(setting.GRILLEJEUX)-1),0,-1):
			if(setting.GRILLEJEUX[j][i] != 0 and j != 0):
				if(setting.GRILLEJEUX[(j-1)][i] == 0):
					setting.GRILLEJEUX[(j-1)][i] = setting.GRILLEJEUX[j][i]
					setting.GRILLEJEUX[j][i] = 0
				if(setting.GRILLEJEUX[(j-1)][i] == setting.GRILLEJEUX[j][i]):
					setting.GRILLEJEUX[(j-1)][i] = setting.GRILLEJEUX[j][i] * 2
					setting.GRILLEJEUX[j][i] = 0
""" 