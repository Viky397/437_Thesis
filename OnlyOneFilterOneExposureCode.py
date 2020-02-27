# IronPython Pad. Write code snippets here and F5 to run. If code is selected, only selection is run.
import time
QHY=SharpCap.SelectedCamera=SharpCap.Cameras[0]
dir = "C:\Users\Paul Rev Oh\Desktop\Doctorate\[task5]-Light Pollution\Image processing\Sharpcap Pollution Measurements\Data-"

##################################################################################
#type which filter you are using : 1-780nm, 2-790nm, 3-830nm, 4-850nm, 5-532nm
#exposure time : in seconds (lower than the interval seconds)
#interval : in seconds (interval includes "exptime" + "pause time") (total time should be divisible by the interval)
#total time : in minutes
totaltime=30
FilterNumber=1
exptime=0.5
interval=10
##################################################################################

filt_wheel=FilterNumber-1

if FilterNumber==1:
	wavelength=780
elif FilterNumber==2:
	wavelength=790
elif FilterNumber==3:
	wavelength=830
elif FilterNumber==4:
	wavelength=850
elif FilterNumber==5:
	wavelength=532

SharpCap.Wheels.SelectedWheel.Position=filt_wheel+1 #python index starts from 0, so +1 should be added.

		
	# range(180) = every 10 seconds for 30 minutes (1 frame per 10 seconds)
for i in range(totaltime*60/interval):
		# Set the exposure time in ms
	exposure_time = SharpCap.SelectedCamera.Controls.Exposure.Value= exptime*1000
	SharpCap.SelectedCamera.CaptureSingleFrameTo(dir + "/filter_" + str(wavelength) + "nm_" + str(exptime)+"s" + "/frame_" + str(i) + "\.png")
	time.sleep(interval-exptime)
	
print("filter_"+str(wavelength)+"nm done")

