# JinglePings Image Generator
Generates a list of ping commands to use for the IPv6 Christmas Tree LED Wall. After generating these commands, you can pipe them into parallel to display an image on the wall.


	usage: jinglepings.py [-h] [--xy x y] [--size width height] image_file

	Converts an image file to a list of ping commands to pipe into parallel.
	
	positional arguments:
  
		image_file		The image file to generate commands for.

	optional arguments:
  
		-h, --help		show this help message and exit
  
  		--xy x y		Where to display the image on the LED wall. The origin is from the top-left of the image.
  
  		--size width height	Resize the image to the given width and height.
