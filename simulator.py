from Battery import *

# Open Testing File
#fin = open('sim_3600_pulse.csv', 'r')
#fout = open('sim_3600_pulse_out.csv', 'w')
fin = open('sim_glasgow.csv', 'r')
fout = open('sim_glasgow_out.csv', 'w')

Battery.P_GAIN = 15
Battery.I_GAIN = 0.01
Battery.HYST_GAIN = 17.45
Battery.SHORT_TERM_DAMP = 1.8
Battery.SOC_CORRECTION_INTERVAL = 60
# Battery(Initial SOC, initial time)
cell0 = Battery(95,0)

fin.readline()

for line in fin:
#	[t,I,Vt,T,SOC_matlab] = line.split(',')
	[t,I,Vt,T,dummy] = line.split(',')
	SOC_py = cell0.Update((eval(Vt)/10000) - 0.004*eval(I),eval(I),eval(T),eval(t))
	#fout.write(str(t) + ',' + str(SOC_py) + ',' + str(SOC_matlab) )
	fout.write(str(t) + ',' + str(SOC_py) + '\n')
	print str(t) + ',' + str(SOC_py)