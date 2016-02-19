import xalglib

def PESreadin(FILE) :
	LIST_IN = FILE.readlines()
	PES_data = []
	X = []
	Xf = []
	Yf = []
	Y = []
	E = []
	for line in LIST_IN:
		Line_split = line.split()
		PES_data.append(Line_split)
		if Line_split[0] not in X:
			X.append(Line_split[0])
		if Line_split[1] not in Y:
			Y.append(Line_split[1])
	for y in Y:
		for x in X:
			for line2 in PES_data:
				if x == line2[0] and y == line2[1]:
					E.append(float(line2[2]))
					break
	for x in X:
		Xf.append(float(x))
	for y in Y:
		Yf.append(float(y))
	return Xf, Yf, E

def InitGuessreadin(FILE):
	LIST_IN = FILE.readlines()
	Nbeads = int(LIST_IN[0])	
	FirstCoorS = LIST_IN[1].split()
	LastCoorS = LIST_IN[2].split()
	FirstCoor = [float(FirstCoorS[0]),float(FirstCoorS[1])]
	LastCoor = [float(LastCoorS[0]),float(LastCoorS[1])]
	String = []
	DeltaX = (LastCoor[0]-FirstCoor[0])/(Nbeads-1)
	DeltaY = (LastCoor[1]-FirstCoor[1])/(Nbeads-1)
	for i in range (Nbeads):
		Tmp = [i*DeltaX+FirstCoor[0], i*DeltaY+FirstCoor[1]]
		String.append(Tmp)
	return String

def PrintResult(File, S, X, Y, E):
	S_new = []
	N_x = len(X)
	N_y = len(Y)
	inter = xalglib.spline2dbuildbicubicv(X, N_x, Y, N_y, E, 1)
	for coor in S:
		Ener = xalglib.spline2dcalcv(inter, coor[0], coor[1])
		string = str(coor[0]) + "    " + str(coor[1]) + "    " + str(Ener[0]) + "\n"
		File.write(string)
	
	





