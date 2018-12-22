#!/usr/bin/python
import argparse
from PIL import Image

# Sets up argument parser
parser = argparse.ArgumentParser(description='Converts an image file to a list of ping commands to pipe into parallel.')

parser.add_argument('image_file', type=str, help='The image file to generate commands for.')
parser.add_argument('--xy', type=int, nargs=2, metavar=('X', 'Y'), default=(0, 0), help='Where to display the image on the LED wall. The origin is from the top-left of the image.')
parser.add_argument('--size', '-s', type=int, nargs=2, metavar=('WIDTH', 'HEIGHT'), help='Resize the image to the given width and height.')
parser.add_argument('--cmd', '-c', type=str, default='ping -6 -c 4', help="What command to use with the IPv6 addresses. Defaults to 'ping -6 -c 4'.")

args = parser.parse_args()


# Opens image file
try:
	im = Image.open(args.image_file, 'r')
except:
	print "Error opening image at " + args.image_file
	exit()

# Sets origin coordinates. Defaults to 0, 0
x_orig = args.xy[0]
y_orig = args.xy[1]
x = x_orig
y = y_orig

# Resizes the image to provided width and height. Defaults to image's actual size.
if args.size != None:
	try:
		size = args.size[0], args.size[1]
		im = im.resize(size)
	except:
		print "Error resizing the image."
		exit()
else:
	size = im.size

# Generates ping command for each pixel in the image	
for pixel in im.getdata():
	red = pixel[0]
	green = pixel[1]
	blue = pixel[2]

	command = args.cmd + ' 2001:4c08:2028:' + str(x) + ':' + str(y) + ':' + hex(red)[2:] + ':' + hex(green)[2:] + ':' + hex(blue)[2:]
	print command
	
	x = x + 1
	
	# Returns x to origin if it goes beyond the image's size
	if x >= x_orig + size[0]:
		x = x_orig
		y = y + 1
