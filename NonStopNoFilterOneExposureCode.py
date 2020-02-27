# IronPython Pad. Write code snippets here and F5 to run. If code is selected, only selection is run.
import time
ZWO = SharpCap.SelectedCamera = SharpCap.Cameras[0]
dir = "C:\Users\veron\OneDrive\Desktop\SharpCap Captures"

##################################################################################
#type which filter you are using : 1-780nm, 2-790nm, 3-830nm, 4-850nm, 5-532nm
#exposure time : in seconds (lower than the interval seconds)
#interval : in seconds (interval includes "exptime" + "pause time") (total time should be divisible by the interval)
#total time : in minutes
totaltime = 2
exptime = 1
##################################################################################

# To turn on cooler, go to camera control panel on right side, and turn Thermal Controls On
cooler = SharpCap.SelectedCamera.Controls.Find(lambda x: x.Name == "Cooler")
cooler = True
	# range(180) = every 10 seconds for 30 minutes (1 frame per 10 seconds)
for i in range(totaltime*60):
	print(SharpCap.SelectedCamera.Controls.FindById(CommonPropertyIDs.Temperature).Value)
		# Set the exposure time in s
	exposure_time = SharpCap.SelectedCamera.Controls.Exposure.Value = exptime
	SharpCap.SelectedCamera.CaptureSingleFrameTo(dir + str(exptime)+"s" + "/frame_" + str(i) + "\exp" +str(exptime)+ ".png")
	
print("done")
