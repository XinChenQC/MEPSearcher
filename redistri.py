import xalglib

#####################################
# This module is the most           #
#    important part                 #
# My code is a little dirty         #
#    and hard too understand        #
# For details, plz refer E weinan's #
#           article                 #
#                                   #
#         2016.2.18    Chen Xin     #
#####################################

def Redistri(S):
	ds = range(len(S))
	ds[0] = 0
	for i in range(1,len(S)):
		ds[i] = ((S[i][0]-S[i-1][0])**2+(S[i][1]-S[i-1][1])**2)**0.5
	
	Sum = 0
	ds_cum=range(len(S))
	for i in range(len(ds)):
		Sum = Sum + ds[i]
		ds_cum[i] = Sum 
	
	DS = range(len(S))
	for i in range(len(ds_cum)):
		DS[i] = ds_cum[i]/Sum

	h = range(len(DS))
	for i in range(len(h)):
		h[i] = h[i]/float(len(h)-1)

	x = range(len(S))
	y = range(len(S))
	for i in range(len(S)):
		x[i] = S[i][0]
		y[i] = S[i][1]

	interX = xalglib.spline1dbuildcubic(DS,x)
	interY = xalglib.spline1dbuildcubic(DS,y)
	
	S_new = range(len(S))
	for i in range(len(h)):
		X_new = xalglib.spline1dcalc(interX,h[i])
		Y_new = xalglib.spline1dcalc(interY,h[i])
		S_new[i] = [X_new, Y_new]
	
	return S_new
