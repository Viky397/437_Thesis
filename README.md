# Quantum Key Distribution
This repository contains all the scripts necessary for my fourth year thesis (Phys 437), under Dr. Thomas Jennewein at the Institute of Quantum Computing at the University of Waterloo.


## Downloading the Appropriate Drivers
ASCOM drivers must be downloaded [here](https://astronomy-imaging-camera.com/software-drivers) in order for the CCD and Filter Wheel to function through SharpCap.

## Dark Count Analysis
This script is used for analyzing the dark measurements that are taken.

### Dependencies
- matplotlib
- Pandas
- numpy
- glob
- PIL

## Star and Light Pollution Analysis
This script is used for analyzing the images of the stars and light pollution that are taken.

### Dependencies
- matplotlib
- numpy

## SharpCap Scripting
This script is used in the SharpCap software, to automate the imaging process. Through this, the motorized filter wheel can be controlled, ZWO CCD fan can be temperature controlled, and images can be taken and saved automatically with specified exposure times and gains. 

### Dependencies
- time

## Running the Scripts

To run the python scripts from the command line, navigate to the folder in which the script is located, and run as follows:

``` python example_script.py ```
