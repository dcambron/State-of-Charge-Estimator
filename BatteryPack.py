from Battery import *

# Config Params
Battery.P_GAIN = 15
Battery.I_GAIN = 0.01
Battery.HYST_GAIN = 17.45
Battery.SHORT_TERM_DAMP = 1.8
Battery.SOC_CORRECTION_INTERVAL = 60

# Initialize each cell of the battery pack with an initial state of charge
# Battery(Initial SOC, initial time)
cell = [Battery(95,0) for _ in range(40)]

# whenever you get new data, call the update method on a particular cell. It returns the current SOC
while True:
	instr = raw_input("t,Vt,I,T,cellnum: ")
	[t,Vt,I,T,cellnum] = instr.split(",")
	SOC_py = cell[eval(cellnum)].Update((eval(Vt)/10000) - 0.004*eval(I),eval(I),eval(T),eval(t))
	print "t=" + str(t) + ',SOC=' + str(round(SOC_py)) + ',cell=' + str(cellnum)
	
# Some useful info:
# cell[x].Voc = estimate for the open circuit voltage of the cell (depends on several factors)
# cell[x].R0 = estimate for internal resistance of the cell (depends on SOC)
# cell[x].Capacity * cell[x].SOC  =  coulombs of charge remaining in cell
# cell[x].Capacity * cell[x].SOC * 3600 =  Amp-Hours of charge remaining in cell