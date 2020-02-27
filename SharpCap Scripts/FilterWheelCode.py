# IronPython Pad. Write code snippets here and F5 to run. If code is selected, only selection is run.

dir = "C:\Users\Paul Rev Oh\Desktop\Doctorate\[task5]-Light Pollution\Image processing\Sharpcap Pollution Measurements\Data-"


for filt_wheel in range(5):

	filter_wheel = filt_wheel+1
	SharpCap.Wheels.SelectedWheel.Position=filt_wheel+1 #python index starts from 0, so +1 should be added.
	if filt_wheel+1==1:
		wavelength=780
	elif filt_wheel+1==2:
		wavelength=790
	elif filt_wheel+1==3:
		wavelength=830
	elif filt_wheel+1==4:
		wavelength=850
	elif filt_wheel+1==5:
		wavelength=532
		
	# Range denotes how many images you would like per exposure time
	for i in range(3):
		# Set the exposure time in ms
		exposure_time = SharpCap.SelectedCamera.Controls.Exposure.Value= 500
		SharpCap.SelectedCamera.CaptureSingleFrameTo(dir + "filter" + str(wavelength) + "_" + "5ms" + "/frame_" + str(i) + "\5ms.png")
	print("exp time = 0.5s done")
	for i in range(3):
		exposure_time = SharpCap.SelectedCamera.Controls.Exposure.Value= 1000
		SharpCap.SelectedCamera.CaptureSingleFrameTo(dir + "filter" + str(wavelength) + "_" + "1s/" + "/frame_" + str(i) + "\1s.png")
	print("exp time = 1.0s done")
	for i in range(3):
		exposure_time = SharpCap.SelectedCamera.Controls.Exposure.Value= 2000
		SharpCap.SelectedCamera.CaptureSingleFrameTo(dir + "filter" + str(wavelength) + "_" + "2s/" + "/frame_" + str(i) + "\2s.png")
	print("exp time = 2.0s done")
	for i in range(3):
		exposure_time = SharpCap.SelectedCamera.Controls.Exposure.Value= 5000
		SharpCap.SelectedCamera.CaptureSingleFrameTo(dir + "filter" + str(wavelength) + "_" + "5s/" + "/frame_" + str(i) + "\5s.png")
	print("exp time = 5.0s done")
	if filt_wheel+1==1:
		print("filter_780nm done")
	elif filt_wheel+1==2:
		print("filter_790nm done")
	elif filt_wheel+1==3:
		print("filter_830nm done")
	elif filt_wheel+1==4:
		print("filter_850nm done")
	elif filt_wheel+1==5:
		print("filter_532nm done")