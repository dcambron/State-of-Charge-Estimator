===============================================================================
SOC ESTIMATOR
===============================================================================
Auth: Daniel Cambron, University of Kentucky
Date: 6/19/2015
License: MIT
===============================================================================
Desc:

Python scripts which estimate the State of Charge of a LiFePO4 Battery pack.
Script uses an adaptive PI method where the State of Charge measurement is 
continuously updated and improved based upon information supplied
to the program.

files:

LUT.py:
	Class that implements a 1-dimensional interpolating look-up table
BatteryLUTS.py;
	File that declares global look-up tables corresponding to 
    battery parameters. The data in these tables corresponds
	to a 20AH Pouch LiFePO4 cell.
Battery.py:
	Class that implements the SOC Estimator for a battery cell. To use this
	class, create an instance using Battery(SOC_init,timestamp_init). Note 
	that SOC is in percent and timestamp is in seconds (typically 0 for init)
	All other parameters are in SI units. To update the state of this instance
	of a battery cell, call Update(Vt,I,T,timestamp) where Vt is the terminal
	voltage, I is the terminal current (passive convention) and T is
	temperature of the cell. This function will return the estimated State of
	Charge. Make sure the timestamp is in seconds and is accurate with the data
	being supplied to the script. The more often the update routine is called
	with new data, the better the performance will be.
BatteryPack.py:
	Script that shows an instantiation of 40 Battery cell objects corresponding
	to a complete vehicle battery pack.
simulator.py:
	Script that tests the program by reading in simulated data from a file and 
	generating an output timeseries of SOC for a single cell. 
Library dependencies: none

TODO:

Implement 2D look-up tables for more accurate model
Replace PI observer with Kalman filter based approach
Tune parameters to empirically match test battery pack

GOAL:

This module is meant to be integrated into a Telemetry viewing program
for the University of Kentucky Solar Car Team.


