import xalglib

####################################
# Steepest descent optimization is #
# used in this module.             #
#                                  #
#                                  #
#                                  #
# 2016.2.18  Chen Xin              #
####################################





def  OptimizeString(X,Y,E,S,h):
	S_new = []
	N_x = len(X)
	N_y = len(Y)
	inter = xalglib.spline2dbuildbicubicv(X, N_x, Y, N_y, E, 1)
	for coor in S:
		Ener, dx, dy, dxy = xalglib.spline2ddiff(inter, coor[0], coor[1]) # dx = dE/dx, dy = dE/dy
		S_new.append([coor[0]-h*dx, coor[1]-h*dy])
	return S_new
