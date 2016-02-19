#!/usr/bin/python
#=================================================================
#        MEPSearcher (V1.0_alpha)                                +
#                                                                +
# 1. Brief Introduction                                          +
#    A program searching Minimun Energy Paths(MEPs).             +
#    This program is based on "string method" which is developed +
#    by  Weinan E et al. [ Phys.Rev.B 66, 052301(2002) ]         +
#                                                                +
# 2. Technical details                                           +
#    3 modules are used in this program                          +
#      -io.py: input and output                                  +
#      -optimize: optimize beads                                 +
#      -redistri: redistribute beads along MEPs                  +
#    Alglib is used to do interpolation.                         +
#                                                                +
#                                                                +
#        Developer:   Chen Xin                                   +
#            Email:   chenxin1211@mails.jlu.edu.cn               +
# Personal Website:   http://chen-xin.tk                         +
#                                           2016.2.18            +
#=================================================================


import xalglib
from io import *
from optimize import *
from redistri import *


##### SETTING ####### 
Max_iter = 1000
Tol = 1e-5
h = 0.5e-1
#####################


FILE_PES = open("PES.data","r")
FILE_IniGuess = open ("guess.data","r")
FileOut	= open("out.data","w")

# 1. read PES(potential energy surface) 
X_PES, Y_PES, Ener_PES = PESreadin(FILE_PES) 

# 2. read initial guess
String0 = InitGuessreadin(FILE_IniGuess)

# 3. searching MEP
N_iter=0
while N_iter < Max_iter:
	N_iter = N_iter + 1

	## update beads
	String = OptimizeString(X_PES, Y_PES, Ener_PES, String0, h) ###optimized
	String = Redistri(String)      ###interpolated

    ## check the convergency 	
	ds=0
	for i in range(len(String)):
		dx = (String[i][0]-String0[i][0])**2
		dy = (String[i][1]-String0[i][1])**2
		ds = ds+(dx+dy)**0.5

	String0 = String

	if ds < Tol:
		print "Successful !"
		break   #Reach the criterion, Stop interation
 
	## OUTPUT 
	if N_iter % 30 == 0:
		print "STEP: " ,N_iter, ";   diff =",ds
# 4. Output
print "Final steps = ",N_iter 	
PrintResult(FileOut, String, X_PES, Y_PES, Ener_PES)





