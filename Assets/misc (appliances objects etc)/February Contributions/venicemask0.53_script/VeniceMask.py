#!BPY

"""
Name: 'Venice Mask'
Blender: 249
Group: 'Image'
Tip: 'Next-gen mask generator.'
"""


# version 0.53
# Januari 28, 2010
# by Gert De Roost		http://users.telenet.be/EWOCprojects
# --------------------------------------------------------------------------
# ***** BEGIN GPL LICENSE BLOCK *****
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# If you have Internet access, you can find the license text at
# http://www.gnu.org/licenses/gpl.txt,
# if not, write to the Free Software Foundation,
# Inc., 59 Temple Place - Suite 330, Boston, MA 02111-1307, USA.
#
# ***** END GPL LICENCE BLOCK *****
# --------------------------------------------------------------------------

__author__ = 'Gert De Roost'
__version__ = '0.53 Januari 28, 2010'
__url__ = ("EWOCprojects, http://users.telenet.be/EWOCprojects")
__email__ = ("Gert De Roost, sheddingskins@telenet.be")
__bpydoc__ = """\
An image-masking application to be used with Blenders compositing engine, although it is not wired into this engine: you need to save masks and re-open them in the compositing engine (hopefully compositing integration will be on the list for 2.50 python API). It revolves around a new user-friendly and interactive use of the Photoshop/Gimp magic wand tool. During selection an extensive preview system and on-the-fly interactive parameter adjustment make this tool a lot more natural than these original magic wands. All selection activity will be recorded in "selection actions" that can be adjusted later on or combined in different ways non-destructively in a node-based structure.

Documentation

Unzip the package into the main Blender scripts directory or the user defined script directory. Now create a working area in Blender that is big enough for working with images. Switch this area to scripts window and choose in the menu: Scripts -> Image -> Venice Mask. The script will start and show you a file selector. In this selector now either select an image file, to start a new project, or a Venice Mask .vnc project file to load a previous project.

MAGIC WAND

There are three selecting tools in the application. Default is the magic wand tool: when you move the mouse pointer over the image, a stippled pattern will in real time show the magic wand selection based on the current parameters. Magic wand is a tool that selects adjacent pixels that are within certain color value boundaries starting from the center pixel value(on which your mouse pointer is). By moving the mouse you change this center pixel. You can also interactively use the mousewheel to change the overall treshold value that changes, for all parameters, how far the extent of the selection will be. On the right you find the selection parameter sliders which change the influence of each of the parameters. Among these parameters: R(red component), G(green component), B(blue component), H(color hue), S(color saturation), V(color value). Use each slider to set its parameter, use toggle boxes with R, G, B, ... on them to switch on and off the influence of each parameter. Default: H, S and V are off. Use the "v"-labelled toggles ("view") to switch to an image view of the selected parameter (to make it easier to judge which parameters to change). When doing this for the first time for each toggle, the operation will take a somewhat longer time to finish, because the new view will need to be calculated. Later activations will be almost instantaneous.
Press the left mouse button to freeze the selection into place and press it again on the image to restart realtime sampling.
Then there are the flood and treshold parameters. Treshold is the same parameter than the one that changes through using the mousewheel, but can be used to change the value in bigger steps at once. Flood is the "broadness" of alpha downscaling at the edges of your selection. It is like your selection starts to "flood" into the surrounding areas dependent on how close these boundary pixels are to the center pixel. Standard this flooding is zero but some "anti-aliasing" will still exist on the selection edges. If anyone has a need for real sharp on/off masks, please email me and I will implement such a mode.

TRESH DRAW

The second tool is the tool labelled "TRESH DRAW". It is somewhat similar to magic wand in that it selects pixels within a range from a starting color. Here though, this starting value is obtained by using the color picker on the right (the colored rectangle). This can also be used to sample a color from the screen. Now move the pointer over the image and you will see a circle and in this circle the underlying pixels will be shown with a stippled pattern for those pixels that are within a certain parameter range (for parameter use, see magic wand use above). By pressing the left mouse button you can draw these selection pixels on the image. Use the mousewheel to change the radius of the drawing circle.
ROLLING UNDO: if you make a mistake while drawing, you can roll your operation back by either using the undo slider on the right (for broad changes) or using the CTRL+mousewheel combination. This way you can "roll back" your drawing operation at any time.

PLAIN DRAW

Then there is the "PLAIN DRAW" tool. It is like tresh draw but draws simple filled circle selections when pressing the left mouse button and moving the pointer with the button pressed. Use it to fill up unselected "isles" inside your selection. It also comes in handy when drawing dikes (see later on).
ROLLING UNDO: like in tresh draw, above.


SELECTION NODES PARADIGM

This program uses a node-based structure to make sure every action can be undone, redone, changed, and recombined at a later stage of your selecting activity. When making a selection, it is contained inside a box or "node" that stands on its own and can be combined with other boxes. So as long as you don't create a new box, all your selection activity will be restricted to the same box and in some instances (when changing selection type) overwrite your previous actions.
To go one step further in the selection process you need to create new selection nodes: you do this by pressing the SPACEBAR. For every press, a selection box will be added. To revert to older selections press the selections name tag (Selection 1,2,3..): now you can replace or change the parameters of your old selections. Delete a box by pressing the DELETE key after selecting a box. A box can be moved by hovering your mouse pointer over it and pressing the middle mouse button and moving your mouse.
You can choose which nodes will be displayed by using the "v" labelled toggle boxes on the selection nodes. Use them to toggle display on/off. Also, there is a "S" labelled solo button that results in "only this" node to be displayed. Toggle it off to switch back to viewing multiple nodes. Then there is a colored rectangle "colorpicker" for each selection which enables colouring the selection pattern of each of your nodes, for discrimination purposes. Where selection areas overlap, the mean color will be displayed. This has a bizarre side effect: when combining nodes, these mean colors always get displayed, even when one of the selections that makes it up, is not displayed. So some color weirdness might occur. At the time of writing I have not found a means of proper node coloring without significantly slowing down the visualisation code.

COMBINING NODES

Nodes can be combined. Use the right mouse button to view your options. A menu appears(use left button outside menu to make it disappear without selecting anything). Left-clicking in the menu creates a new node, either a union, intersection or subtraction. These are normal boolean operations. Union adds two node contents together, intersections intersects two node contents and subtraction subtracts one of the nodes contents from those of another. Use the out (at the bottom of the nodes) box and in box (at the top) to connect nodes together. Leftclick a box and a line will appear between it and your pointer. Click a box of the other type to conclude the connection. For example connect two selection nodes into one union node. Now you can also connect this union node into, for example, an intersection node. So everything can be connected together. The subtraction box operation depends on the order of the connected nodes. The node connected first to its in will be the node that is subtracted from. All nodes connected afterwards will the be the ones that are subtracted from the first. A better solution for visualizing subtraction order will be implemented in a later program version. All boolean nodes also have view and solo toggles, they work as their respective selection node cousins.
So, you might wonder, what is the "in" box on the selection nodes for ? It is used to implement dikes, a feature that only works with the magic wand selection tool. It is used to create "dike" areas that stop the "flooding" of the magic wand tool. It is used very often in these cases where seperate areas with comparable color contents touch so when upping the treshold to much, the selection floods into unwanted territory. What you do is simply creating a new selection node and using for example (mostly) the plain draw tool to draw a boundary next to the area to be selected with magic wand and the wand selection will not go beyond this "dike". Connect this selection node into the "dike in" box of the magic wand selection node to be affected. At the moment connecting anything else but single selection nodes to "dike in" will not work!


WHAT ELSE?

One major issue with this application is speed. It is written in Python and so this does not make for a bleeding fast application. Especially when displaying a large selection, activity becomes slow, certainly on lower-grade machines. I tried to streamline it as much as possible, so there you go. One thing you can do is untoggle the "PREVIEW" toggle. It will desactivate the "selected image preview". This will give you quite some more selection speed. Also by rightclicking the PREVIEW toggle a menu appears. Select low preview mode for somewhat faster display than high preview gives you. Then there is rendering mode. Don't use it unless you are very patient. It starts a rendering mode that generates a one-pixel precision image in the preview window, effectively giving you a rendered image of what your selection will be. It will re-render everytime you freeze your magic wand selection and every time you finish an continuous drawing stroke in one of the other tools. In fact this mode is more of a proof of concept than a real feature (too slow) but if you like it let me know! It seems to be easier to be using the RENDER button onscreen to trigger a one-pixel precision render at any time you want (also outside rendering mode).
Further on there are the usual OPEN, SAVE, SAVE AS buttons for opening a .vnc file, saving projectfile under the current name or under a new name. The EXIT button will simply exit the script. Then there is the "SAVE MASK" button. It will render your mask to one-pixel accuracy and save it as a black(not selected) and white(selected) mask image on the disk. Use this for example as a mask in Blenders compositing engine, but of course nothing keeps you from using the mask in other applications like the Gimp or Photoshop.

That kind of wraps it up. Be sure to mail (or use the forum) suggestions, bug reports, and so on. Be aware of this applications alpha state: it will not always operate as expected. I put this version out as a first taster of what is to come and more features are already on the to-do list! Sometimes the application will not immediately update the display to mirror made changes. When you are in such a situation, you can press the REBUILD push button: it will recalculate all selections and rebuild the display.
"""

import Blender

from Blender import Image, Draw, Window, Text, Scene
from Blender.BGL import *
import random
import time
import cPickle
from copy import *
from math import *

version = 0.5


def startfile(filename):
	global savefilename, imagefilename, image, pixelscale, width, height, awidth, aheight, imagelist, zoom, oldzoom
	global horizontal, vertical
	if filename.count(".vnc"):
		savefilename = filename
		openfile(filename)
	else:
		imagefilename = filename
		image["rgb"] = Image.Load(imagefilename)
		pixelscale = {}
		width = image["rgb"].getSize()[0]
		height = image["rgb"].getSize()[1]
		pixels = width * height
		areawidth, areaheight = Window.GetAreaSize()
		zoom1 = min(((areawidth - 260)*0.9) / (float(width)*2.0), (areaheight*0.9) / (float(height)))
		zoom2 = min((areaheight*0.9) / (float(height)*2.0), ((areawidth - 260)*0.9) / (float(width)))
		if zoom1 > zoom2:
			zoom = zoom1
			horizontal = 2.0
			vertical = 1.0
		else:
			zoom = zoom2
			horizontal = 1.0
			vertical = 2.0
		oldzoom = zoom
		awidth = pixelscale["x"] = int(width * zoom)
		aheight = pixelscale["y"] = int(height * zoom)
		imagelist = []
		for y in range(height):
			for x in range(width):
				r, g, b, dummy = image["rgb"].getPixelF(x, y)
				imagelist.append([r, g, b])
		addselnode()
		makeblancolist()
	Draw.Draw()
	Draw.Register(refresh, event, sliders)




Window.FileSelector(startfile, "Open image or vnc file")


	

def deftoggles():
	global ntoggle, hdtoggle
	ntoggle = {}
	ntoggle["in"] = {}
	ntoggle["out"] = {}
	ntoggle["view"] = {}
	ntoggle["solo"] = {}
	ntoggle["in"]["un"] = []
	ntoggle["out"]["un"] = []
	ntoggle["view"]["un"] =[]
	ntoggle["solo"]["un"] = []
	ntoggle["in"]["int"] = []
	ntoggle["out"]["int"] = []
	ntoggle["view"]["int"] =[]
	ntoggle["solo"]["int"] = []
	ntoggle["in"]["sub"] = []
	ntoggle["out"]["sub"] =[]
	ntoggle["view"]["sub"] =[]
	ntoggle["solo"]["sub"] = []
	ntoggle["in"]["sel"] = []
	ntoggle["out"]["sel"] = []
	hdtoggle = {}
	hdtoggle["un"] = []
	hdtoggle["int"] = []
	hdtoggle["sub"] = []


	
	
doall = 0
movingbox = ["sel", 0]
tresholding = 0
shortcutting = 0	
dikelist = []
leftjustdown = 0
doall = 0
preshaping = 0
image = {}
hd = {}	
ni = {}
no = {}
nv = {}
ns = {}
justopen = 0
savefilename = None
toggle = {}
slider = {}	
deleted = {}
solo = 0	
saving = 0	
undostatus = 0	
floodvalue = 100	
alist = []
rendernow = 0
comparesetlist = []
lowpreview = 1
highpreview = 0
renderpreview = 0	
premenustart = 0
premenuing = 0
premenupush = {}	
recalctrigger = 1
wanding = []
readyfordisplay = []
scalemoving = 0
overscale = 0	
color = []	
clist = []	
breakstart = 0
breaking = 0
online = -1
displayset = set([])
dset = {}
dset["sel"] = []
dset["un"] = []
dset["int"] = []
dset["sub"] = []
viewpos = []
savedviewpos = []
conndata = {}
conndata["in"] = {}
conndata["in"]["sel"] = {}
conndata["in"]["un"] = {}
conndata["in"]["int"] = {}
conndata["in"]["sub"] = {}
conndata["out"]	= {}
conndata["out"]["sel"] = {}
conndata["out"]["un"] = {}
conndata["out"]["int"] = {}
conndata["out"]["sub"] = {}
conndata["check"]	= {}
conndata["check"]["sel"] = {}
conndata["check"]["un"] = {}
conndata["check"]["int"] = {}
conndata["check"]["sub"] = {}
selcomps = 6
uncomps = 4
intcomps = 4
subcomps = 4
last = {}
last["x"] = 0
last["y"] = 0
viewtoggle = {}
imagelist = {}
menustart = 0
menupush = {}
numconns = {}
box = {}
box["in"] = []
box["out"] = []
connecting = 0
deftoggles()
box["x"] = {}
box["y"] = {}
box["x"]["sel"] = []
box["y"]["sel"] = []
box["x"]["un"] = []
box["y"]["un"] = []
box["x"]["int"] = []
box["y"]["int"] = []
box["x"]["sub"] = []
box["y"]["sub"] = []
num = {}
num["un"] = 0
num["int"] = 0
num["sub"] = 0
num["sel"] = 0
menuing = 0
moving = 0
fill = 0
setundo = 0
calckind = []
undoing = 0
bltime = []
blinking = []
blink = []
base = {}
base["tresh"] = []
base["flood"] = []
base["r"] = []
base["g"] = []
base["b"] = []
base["h"] = []
base["s"] = []
base["v"] = []
base["radius"] = []
base["pos"] = []
base["x"] = []
base["y"] = []
listpos = -1
selcols = []
solos = []
views = []
selections = []
drawing = 0
calc = 0
radius = 40
first = {}
first["r"] = first["g"] = first["b"] = first["h"] = first["s"] = first["v"] = 1
oldx = oldy = 0
drawset = set([])
colordir = {}
alphadir ={}
middledown = 0
rightdown = 0
leftdown = 0
enter = 0
mousecoords = [0, 0]
areax, areay = Window.GetAreaSize()
areaid = Window.GetAreaID()
for dict in Window.GetScreenInfo():
	if dict['id'] == areaid:
		windowx, windowy, dummy1, dummy2 = dict['vertices']
lookupstep = 2



x, y = Window.GetAreaSize()
toggle["r"] = Draw.Toggle("R", 3, x - 140, 60, 20, 20, 1, "Toggle red influence on/off")
toggle["g"] = Draw.Toggle("G", 4, x - 140, 40, 20, 20, 1, "Toggle green influence on/off")
toggle["b"] = Draw.Toggle("B", 5, x - 140, 20, 20, 20, 1, "Toggle blue influence on/off")
slider["r"] = Draw.Slider("red    ", 0, x - 120, 60, 120, 20, 50, 1, 100, 1, "Change red influence")
slider["g"] = Draw.Slider("green ", 1, x - 120, 40, 120, 20, 50, 1, 100, 1, "Change green influence")
slider["b"] = Draw.Slider("blue   ", 2, x - 120, 20, 120, 20, 50, 1, 100, 1, "Change blue influence")
viewtoggle["r"] = Draw.Toggle("v", 14, x - 160, 60, 20, 20, 0, "View red channel")
viewtoggle["g"] = Draw.Toggle("v", 15, x - 160, 40, 20, 20, 0, "View green channel")
viewtoggle["b"] = Draw.Toggle("v", 16, x - 160, 20, 20, 20, 0, "View blue channel")

toggle["h"] = Draw.Toggle("H", 10, x - 140, 180, 20, 20, 0, "Toggle hue influence on/off")
toggle["s"] = Draw.Toggle("S", 11, x - 140, 160, 20, 20, 0, "Toggle saturation influence on/off")
toggle["v"] = Draw.Toggle("V", 12, x - 140, 140, 20, 20, 0, "Toggle value influence on/off")
slider["h"] = Draw.Slider("hue   ", 7, x - 120, 180, 120, 20, 50, 1, 100, 1, "Change hue influence")
slider["s"] = Draw.Slider("satur ", 8, x - 120, 160, 120, 20, 50, 1, 100, 1, "Change saturation influence")
slider["v"] = Draw.Slider("value ", 9, x - 120, 140, 120, 20, 50, 1, 100, 1, "Change saturation influence")
viewtoggle["h"] = Draw.Toggle("v", 17, x - 160, 180, 20, 20, 0, "View hue")
viewtoggle["s"] = Draw.Toggle("v", 18, x - 160, 160, 20, 20, 0, "View saturation")
viewtoggle["v"] = Draw.Toggle("v", 19, x - 160, 140, 20, 20, 0, "View value")

slider["t"] = Draw.Slider("tresh", 13, x - 120, 220, 120, 20, 100, 0, 1000, 1, "Change treshold")

colourpicker = Draw.ColorPicker(20, x - 160, 80, 40, 60, (1.0, 0.0, 0.0), "Select colourpicker")

toggle["f"] = Draw.Toggle("FILL-IN", 24, x - 260, 140, 100, 60, 0, "Toggle fill draw mode")
toggle["d"] = Draw.Toggle("DRAW", 21, x - 260, 80, 100, 60, 0, "Toggle draw mode")
toggle["p"] = Draw.Toggle("PREVIEW", 22, x - 260, 20, 100, 60, 1, "Toggle realtime preview mode")
slider["u"] = Draw.Slider("undo", 23, x - 120, 300, 120, 40, 100, 0, 100, 1, "Set rolling undo percentage")
slider["f"] = Draw.Slider("flood", 26, x - 120, 300, 120, 40, 0, 0, 100, 1, "Set flooding value")






def drawoverlay():
	global fastdrawset, recalctrigger, rendernow, olddisplayset, frombutton, alphadir2
	glEnable(GL_BLEND)
	glBlendFunc (GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
	if recalctrigger:
		recalctrigger = 0
		fastdrawset = set([])
		alphadir2 = {}
		glBegin(GL_POINTS)		
		if rendernow:
			rendernow = 0
			for coords in olddisplayset:
				drawselpixel(coords)
			if toggle["p"].val or frombutton:
				frombutton = 0
				for coords in displayset:
					x = coords % awidth
					y = coords // awidth			
					lcoords = int((y // zoom) * width + (x // zoom) + 0.5)
					rm, gm, bm = imagelist[lcoords]
					alpha = 0
					for adir in alist:
						try:
							a1 = adir[coords]
							alpha = max(alpha, a1)
						except:
							pass
					glColor4f(rm, gm, bm, alpha)
					if horizontal == 2:
						xm = awidth + x
						ym = y
					else:
						ym = aheight + y
						xm = x
					glVertex2f(xm, ym)
					fastdrawset.add((xm, ym, rm, gm, bm, alpha))
			doalloperations()
			recalctrigger = 0
		else:
			for coords in displayset:
				x, y = drawselpixel(coords)		
				if toggle["p"].val:
					if lowpreview:
						lcoords = int((y // zoom) * width + (x // zoom))
						rm, gm, bm = imagelist[lcoords]
						alpha = alphadir2[coords]
						glColor4f(rm, gm, bm, alpha)
						x = awidth*(horizontal - 1) + x
						y = aheight*(vertical - 1) + y
						glVertex2f(x, y)
						fastdrawset.add((x, y, rm, gm, bm, alpha))
						glVertex2f(x, y + 1)
						fastdrawset.add((x, y + 1, rm, gm, bm, alpha))
						x += 1
						glVertex2f(x, y + 1)
						fastdrawset.add((x, y + 1, rm, gm, bm, alpha))
						glVertex2f(x, y)
						fastdrawset.add((x, y, rm, gm, bm, alpha))				
					elif highpreview:
						lcoords = int((y // zoom) * width + (x // zoom))
						alpha = alphadir2[coords]
						rm, gm, bm = imagelist[lcoords]
						glColor4f(rm, gm, bm, alpha)
						x = awidth*(horizontal - 1) + x
						y = aheight*(vertical - 1) + y
						glVertex2f(x, y)
						fastdrawset.add((x, y, rm, gm, bm, alpha))
						rm, gm, bm = imagelist[lcoords + width]
						glColor4f(rm, gm, bm, alpha)
						glVertex2f(x, y + 1)
						fastdrawset.add((x, y + 1, rm, gm, bm, alpha))
						rm, gm, bm = imagelist[lcoords + width + 1]
						glColor4f(rm, gm, bm, alpha)
						x += 1
						glVertex2f(x, y + 1)
						fastdrawset.add((x, y + 1, rm, gm, bm, alpha))
						rm, gm, bm = imagelist[lcoords + 1]
						glColor4f(rm, gm, bm, alpha)
						glVertex2f(x, y)
						fastdrawset.add((x, y, rm, gm, bm, alpha))
			olddisplayset = displayset.copy()
		glEnd( )
	else:
		glBegin(GL_POINTS)		
		for pixel in fastdrawset:
			x, y, r, g, b, a = pixel
			glColor4f(r, g, b, a)
			glVertex2f(x, y)
		if preshaping:
			for coords in preshapeset:
				x = coords % awidth
				y = coords // awidth
				r, g, b = color[precolordir[coords]]
				a = prealphadir[coords]
				glColor4f(r, g, b, a)
				glVertex2f(x, y)
				if toggle["p"].val:
					previewdraw(x, y, a)

		if shortcutting:
			for coords in drawset:
				x = coords % awidth
				y = coords // awidth
				r, g, b = color[colordir[coords]]
				a = alphadir[coords]
				glColor4f(r, g, b, a)
				glVertex2f(x, y)
				if toggle["p"].val:
					previewdraw(x, y, a)
		glEnd()
	glDisable(GL_BLEND)

	
def previewdraw(x, y, alpha):
	if lowpreview:
		lcoords = int((y // zoom) * width + (x // zoom))
		rm, gm, bm = imagelist[lcoords]
		glColor4f(rm, gm, bm, alpha)
		x = awidth*(horizontal - 1) + x
		y = aheight*(vertical - 1) + y
		glVertex2f(x, y)
		glVertex2f(x, y + 1)
		x += 1
		glVertex2f(x, y + 1)
		glVertex2f(x, y)
	elif highpreview:
		lcoords = int((y // zoom) * width + (x // zoom))
		rm, gm, bm = imagelist[lcoords]
		glColor4f(rm, gm, bm, alpha)
		x = awidth*(horizontal - 1) + x
		y = aheight*(vertical - 1) + y
		glVertex2f(x, y)
		rm, gm, bm = imagelist[lcoords + width]
		glColor4f(rm, gm, bm, alpha)
		glVertex2f(x, y + 1)
		rm, gm, bm = imagelist[lcoords + width + 1]
		glColor4f(rm, gm, bm, alpha)
		x += 1
		glVertex2f(x, y + 1)
		rm, gm, bm = imagelist[lcoords + 1]
		glColor4f(rm, gm, bm, alpha)
		glVertex2f(x, y)

					
def drawselpixel(coords):
	global fastdrawset, alphadir2
	x = coords % awidth
	y = coords // awidth
	r, g, b, a = getcolor(coords)
	glColor4f(r, g, b, a)
	glVertex2f(x, y)
	fastdrawset.add((x, y, r, g, b, a))
	return x, y


def getcolor(coords):
	global alphadir2
	r = g = b = a = le = 0
	for cdir in clist:
		try:
			r1, g1, b1 = color[cdir[coords]]
			a1 = alist[clist.index(cdir)][coords]
			r += r1
			g += g1
			b += b1
			a = max(a, a1)
			le += 1
		except:
			pass
	if le == 0:
		r = 1.0
		g = 1.0
		b = 1.0
		a = 1.0
	else:
		r = r / le
		g = g / le
		b = b / le
	alphadir2[coords] = a
	return r, g, b, a

	
def makedisplayset():
	global displayset, conndata
	displayset = set([])
	if viewpos == []:
		for step in range(num["sel"]):
			if readyfordisplay[step]:
				displayset.update(dset["sel"][step])
	else:
		for coords in viewpos:
			if coords[0] == "sel" and readyfordisplay[coords[1]] == 0:
				pass
			else:
				if not(conndata["check"][coords[0]][coords[1]]):
					processnode(coords)
					conndata["check"][coords[0]][coords[1]] = 1
						
				displayset.update(dset[coords[0]][coords[1]])


				
def recreatenodes(kind, offset, pos):
	global hdtoggle, ntoggle
	if kind == "un":
		string = "Union"
	elif kind == "int":
		string = "Intersection"
	elif kind == "sub":
		string = "Subtraction"
	hdtoggle[kind].append(Draw.Toggle(string, 48 + offset, areax - box["x"][kind][pos], areay - box["y"][kind][pos], 100, 20, hd[kind][pos], "No function"))
	ntoggle["in"][kind].append(Draw.Toggle("", 49 + offset, areax - box["x"][kind][pos] + 40, areay - box["y"][kind][pos] + 20, 20, 20, ni[kind][pos], "In"))
	ntoggle["out"][kind].append(Draw.Toggle("", 50 + offset, areax - box["x"][kind][pos] + 40, areay - box["y"][kind][pos] - 20, 20, 20, no[kind][pos], "Out"))
	ntoggle["view"][kind].append(Draw.Toggle("v", 51 + offset, areax - box["x"][kind][pos] - 40, areay - box["y"][kind][pos], 20, 20, nv[kind][pos], "Toggle view to this node"))
	ntoggle["solo"][kind].append(Draw.Toggle("S", 52 + offset, areax - box["x"][kind][pos] - 20, areay - box["y"][kind][pos], 20, 20, ns[kind][pos], "Toggle solo selection"))


def refresh():
	global slider, toggle
	global viewtoggle
	global radius, width, height, zoom, pixels, oldx, oldy, enter, colourpicker, calc, calclist, drawing, drawset, selections
	global imagelist, awidth, aheight
	global solos, views, selcols, windowx, windowy, blinking, blink, bltime, cpush
	global base, listpos, undoing, setundo, fill
	global menupush, menux, menuy, menuing, menustart
	global num, box, hdtoggle, ntoggle
	global connecting, connx, conny, connpos, connkind, conndata
	global selcomps, displayset, dset, viewpos, viewkind, online, breakstart, breaking, overscale
	global premenustart, premenuing, premenupush, comparesetlist, recalctrigger, rendernow
	global renpush, deleted, justopen, areax, areay
	
	areax, areay = Window.GetAreaSize()

	area = Window.GetAreaID()
	for dict in Window.GetScreenInfo():
		if dict['id'] == area:
			windowx, windowy, dummy1, dummy2 = dict['vertices']


	if justopen:
		justopen = 0
		
		selections = []
		views = []
		solos = []
		selcols = []
		deftoggles()
		for pos in range(num["sel"]):
			blinking.append(0)
			selections.append(Draw.Toggle("Selection " + str(num["sel"] + 1), 42 + pos*selcomps, areax - box["x"]["sel"][pos] + 40,  areay - box["y"]["sel"][pos], 80, 20, ses[pos], "Select for edit: " + str(num["sel"] + 1)))
			views.append(Draw.Toggle("v", 44 + pos*selcomps, areax - box["x"]["sel"][pos],  areay - box["y"]["sel"][pos], 20, 20, vis[pos], "Switch on view"))
			solos.append(Draw.Toggle("S", 43 + pos*selcomps, areax - box["x"]["sel"][pos] + 20,  areay - box["y"]["sel"][pos], 20, 20, sos[pos], "Toggle solo selection"))
			selcols.append(Draw.ColorPicker(45 + pos*selcomps, areax - box["x"]["sel"][pos] - 20, areay - box["y"]["sel"][pos], 20, 20, cols[pos], "Set selection colourpicker"))
			ntoggle["in"]["sel"].append(Draw.Toggle("", 46 + pos*selcomps, areax - box["x"]["sel"][pos] + 40, areay - box["y"]["sel"][pos] + 20, 20, 20, ni["sel"][pos], "Dike in"))
			ntoggle["out"]["sel"].append(Draw.Toggle("", 47 + pos*selcomps, areax - box["x"]["sel"][pos] + 40, areay - box["y"]["sel"][pos] - 20, 20, 20, no["sel"][pos], "Selection out"))
	
		
		for pos in range(num["un"]):
			offset = num["sel"]*selcomps + num["un"]*uncomps
			recreatenodes("un", offset, pos)
		for pos in range(num["int"]):
			offset = num["sel"]*selcomps + num["un"]*uncomps + num["int"]*intcomps
			recreatenodes("int", offset, pos)
		for pos in range(num["sub"]):
			offset = num["sel"]*selcomps + num["un"]*uncomps + num["int"]*intcomps + num["sub"]*subcomps
			recreatenodes("sub", offset, pos)



	if viewtoggle["r"].val:
		Draw.Image(image["r"], 0, 0, zoom, zoom)
	elif viewtoggle["g"].val:
		Draw.Image(image["g"], 0, 0, zoom, zoom)
	elif viewtoggle["b"].val:
		Draw.Image(image["b"], 0, 0, zoom, zoom)
	elif viewtoggle["h"].val:
		Draw.Image(image["h"], 0, 0, zoom, zoom)
	elif viewtoggle["s"].val:
		Draw.Image(image["s"], 0, 0, zoom, zoom)
	elif viewtoggle["v"].val:
		Draw.Image(image["v"], 0, 0, zoom, zoom)
	else:
		Draw.Image(image["rgb"], 0, 0, zoom, zoom)

		
	x2 = mousecoords[0]
	y2 = mousecoords[1]
	if x2 >= awidth*horizontal - 20 and x2 <= awidth*horizontal + 20 and y2 >= aheight*vertical - 20 and y2 <= aheight*vertical + 20:
		overscale = 1
		glColor3f(1.0, 1.0, 1.0)
	else:
		overscale = 0
		glColor3f(0.0, 0.0, 0.0)
	offset = 20
	glBegin(GL_LINE_LOOP)
	glVertex2f(awidth*horizontal - offset, aheight*vertical - offset)
	glVertex2f(awidth*horizontal - offset, aheight*vertical + offset)
	glVertex2f(awidth*horizontal + offset, aheight*vertical + offset)
	glVertex2f(awidth*horizontal + offset, aheight*vertical - offset)
	glEnd()

	glColor3f(0.0, 0.0, 0.0)
	glBegin(GL_QUADS)
	if horizontal == 2:
		glVertex2f(awidth, 0)
		glVertex2f(awidth, aheight)
		glVertex2f(awidth*2, aheight)
		glVertex2f(awidth*2, 0)
	else:
		glVertex2f(0, aheight)
		glVertex2f(awidth, aheight)
		glVertex2f(awidth, aheight*2)
		glVertex2f(0, aheight*2)
	glEnd()
	
	
	if not(x2 >= 0 and x2 < awidth - 1 and  y2 >= 0 and y2 < aheight - 1):
		preshaping = 0

	if (["sel", listpos] in viewpos):
		shortcutting = 1
	else:
		shortcutting = 0

	if calckind[listpos] == "venice":
		preshaping = 0
		shortcutting = 0
	
	if leftdown and shortcutting:
		recalctrigger = 0

	if not(scalemoving):
		if recalctrigger:
			makedisplayset()
		drawoverlay()


	online = -1
	for pos in range(len(box["in"])):
		if box["out"][pos][0] == "sel":
			x1 = areax - box["x"]["sel"][box["out"][pos][1]] + 50
			y1 = areay - box["y"]["sel"][box["out"][pos][1]] - 20
		elif box["out"][pos][0] == "un":
			x1 = areax - box["x"]["un"][box["out"][pos][1]] + 50
			y1 = areay - box["y"]["un"][box["out"][pos][1]] - 20
		elif box["out"][pos][0] == "int":
			x1 = areax - box["x"]["int"][box["out"][pos][1]] + 50
			y1 = areay - box["y"]["int"][box["out"][pos][1]] - 20
		elif box["out"][pos][0] == "sub":
			x1 = areax - box["x"]["sub"][box["out"][pos][1]] + 50
			y1 = areay - box["y"]["sub"][box["out"][pos][1]] - 20
		if box["in"][pos][0] == "sel":
			x2 = areax - box["x"]["sel"][box["in"][pos][1]] + 50
			y2 = areay - box["y"]["sel"][box["in"][pos][1]] + 40
		elif box["in"][pos][0] == "un":
			x2 = areax - box["x"]["un"][box["in"][pos][1]] + 50
			y2 = areay - box["y"]["un"][box["in"][pos][1]] + 40
		elif box["in"][pos][0] == "int":
			x2 = areax - box["x"]["int"][box["in"][pos][1]] + 50
			y2 = areay - box["y"]["int"][box["in"][pos][1]] + 40
		elif box["in"][pos][0] == "sub":
			x2 = areax - box["x"]["sub"][box["in"][pos][1]] + 50
			y2 = areay - box["y"]["sub"][box["in"][pos][1]] + 40

		mx = mousecoords[0]
		my = mousecoords[1]
		dist = ((mx - x1)*(y2 - y1) - (my - y1)*(x2 - x1)) / sqrt((x2 - x1)**2 + (y2 - y1)**2)
		on = 1
		if abs(dist) > 5:
			on = 0
		if x2 > x1:
			if mx < x1:
				on = 0
			if mx > x2:
				on = 0
		elif x1 > x2:
			if mx > x1:
				on = 0
			if mx < x2:
				on = 0
		if y2 > y1:
			if my < y1:
				on = 0
			if my > y2:
				on = 0
		elif y1 > y2:
			if my > y1:
				on = 0
			if my < y2:
				on = 0
		if on:
			online = pos
			glColor3f(1.0, 0.5, 0)
		else:
			glColor3f(1.0, 1.0, 1.0)
		glBegin(GL_LINES)
		glVertex2f(x1, y1)
		glVertex2f(x2, y2)
		glEnd()



	x, y = Window.GetAreaSize()
	

	if selection[0] == "sel":
		if not(toggle["f"].val):
			toggle["r"] = Draw.Toggle("R", 3, x - 140, 60, 20, 20, toggle["r"].val, "Toggle red influence on/off")
			toggle["g"] = Draw.Toggle("G", 4, x - 140, 40, 20, 20, toggle["g"].val, "Toggle green influence on/off")
			toggle["b"] = Draw.Toggle("B", 5, x - 140, 20, 20, 20, toggle["b"].val, "Toggle blue influence on/off")
			if toggle["r"].val:
				slider["r"] = Draw.Slider("red    ", 0, x - 120, 60, 120, 20, slider["r"].val, 1, 100, 0, "Change red influence")
			if toggle["g"].val:
				slider["g"] = Draw.Slider("green ", 1, x - 120, 40, 120, 20, slider["g"].val, 1, 100, 0, "Change green influence")
			if toggle["b"].val:
				slider["b"] = Draw.Slider("blue   ", 2, x - 120, 20, 120, 20, slider["b"].val, 1, 100, 0, "Change blue influence")

			toggle["h"] = Draw.Toggle("H", 10, x - 140, 180, 20, 20, toggle["h"].val, "Toggle hue influence on/off")
			toggle["s"] = Draw.Toggle("S", 11, x - 140, 160, 20, 20, toggle["s"].val, "Toggle saturation influence on/off")
			toggle["v"] = Draw.Toggle("V", 12, x - 140, 140, 20, 20, toggle["v"].val, "Toggle value influence on/off")
			if toggle["h"].val:
				slider["h"] = Draw.Slider("hue  ", 7, x - 120, 180, 120, 20, slider["h"].val, 1, 100, 0, "Change hue influence")
			if toggle["s"].val:
				slider["s"] = Draw.Slider("satur ", 8, x - 120, 160, 120, 20, slider["s"].val, 1, 100, 0, "Change saturation influence")
			if toggle["v"].val:
				slider["v"] = Draw.Slider("value ", 9, x - 120, 140, 120, 20, slider["v"].val, 1, 100, 0, "Change value influence")

			slider["t"] = Draw.Slider("tresh", 13, x - 120, 220, 120, 40, slider["t"].val, 0, 1000, 0, "Change treshold")
			slider["f"] = Draw.Slider("flood", 26, x - 120, 260, 120, 40, slider["f"].val, 0, 100, 0, "Set alpha flooding value")

		viewtoggle["r"] = Draw.Toggle("v", 14, x - 160, 60, 20, 20, viewtoggle["r"].val, "View red channel")
		viewtoggle["g"] = Draw.Toggle("v", 15, x - 160, 40, 20, 20, viewtoggle["g"].val, "View green channel")
		viewtoggle["b"] = Draw.Toggle("v", 16, x - 160, 20, 20, 20, viewtoggle["b"].val, "View blue channel")
		
		viewtoggle["h"] = Draw.Toggle("v", 17, x - 160, 180, 20, 20, viewtoggle["h"].val, "View hue")
		viewtoggle["s"] = Draw.Toggle("v", 18, x - 160, 160, 20, 20, viewtoggle["s"].val, "View saturation")
		viewtoggle["v"] = Draw.Toggle("v", 19, x - 160, 140, 20, 20, viewtoggle["v"].val, "View value")

		colourpicker = Draw.ColorPicker(20, x - 160, 80, 40, 60, colourpicker.val, "Select colourpicker")

		if undostatus:
			slider["u"] = Draw.Slider("undo", 23, x - 120, 300, 120, 40, slider["u"].val, 0, 100, 0, "Set rolling undo percentage")

	toggle["f"] = Draw.Toggle("PLAIN DRAW", 24, x - 260, 140, 100, 60, toggle["f"].val, "Toggle fill draw mode")
	toggle["d"] = Draw.Toggle("TRESH DRAW", 21, x - 260, 80, 100, 60, toggle["d"].val, "Toggle draw mode")
	toggle["p"] = Draw.Toggle("PREVIEW", 22, x - 260, 20, 100, 60, toggle["p"].val, "Toggle realtime preview")

	rebuildpush = Draw.PushButton("REBUILD", 32, x - 260, 200, 100, 60, "Rebuild display")
	renpush = Draw.PushButton("RENDER", 25, x - 260, 0, 100, 20, "Render")
	savmaskpush = Draw.PushButton("SAVE MASK", 27, x - 100, 0, 100, 20, "Save mask")
	openpush = Draw.PushButton("OPEN", 30, x - 120, 120, 120, 20, "Open working file")
	savepush = Draw.PushButton("SAVE", 28, x - 120, 100, 120, 20, "Save working file")
	saveaspush = Draw.PushButton("SAVE AS", 29, x - 120, 80, 120, 20, "Save working file as...")
	exitpush = Draw.PushButton("EXIT", 31, x - 160, 0, 60, 20, "Leave program")

	for pos in range(len(selections)):
		if not(deleted["sel", pos]):
			selections[pos] = Draw.Toggle("Selection " + str(pos + 1), 42 + pos*selcomps, areax - box["x"]["sel"][pos] + 40, areay - box["y"]["sel"][pos], 80, 20, selections[pos].val, "Select for edit: " + str(pos + 1))
			solos[pos] = Draw.Toggle("S", 43 + pos*selcomps, areax - box["x"]["sel"][pos] + 20, areay - box["y"]["sel"][pos], 20, 20, solos[pos].val, "Toggle solo selection")
			views[pos] = Draw.Toggle("v", 44 + pos*selcomps, areax - box["x"]["sel"][pos], areay - box["y"]["sel"][pos], 20, 20, views[pos].val, "Switch on view")
			selcols[pos] = Draw.ColorPicker(45 + pos*selcomps, areax - box["x"]["sel"][pos] - 20, areay - box["y"]["sel"][pos], 20, 20, selcols[pos].val, "Set selection colourpicker")
			ntoggle["in"]["sel"][pos] = Draw.Toggle("", 46 + pos*selcomps, areax - box["x"]["sel"][pos] + 40, areay - box["y"]["sel"][pos] + 20, 20, 20, ntoggle["in"]["sel"][pos].val, "Dike in")
			ntoggle["out"]["sel"][pos] = Draw.Toggle("", 47 + pos*selcomps, areax - box["x"]["sel"][pos] + 40, areay - box["y"]["sel"][pos] - 20, 20, 20, ntoggle["out"]["sel"][pos].val, "Selection out")
			if blinking[pos]:
				glBegin(GL_LINE_LOOP)
				glColor3f(1.0, 1.0, 0.0)
				glVertex2f(areax - box["x"]["sel"][pos] - 21, areay - box["y"]["sel"][pos] - 1)
				glVertex2f(areax - box["x"]["sel"][pos] + 121, areay - box["y"]["sel"][pos] - 1)
				glVertex2f(areax - box["x"]["sel"][pos] + 121, areay - box["y"]["sel"][pos] + 21)
				glVertex2f(areax - box["x"]["sel"][pos] - 21, areay - box["y"]["sel"][pos] + 21)
				glEnd()
			
		
	if menustart:
		menustart = 0
		breaking = 0
		premenuing = 0
		menux = mousecoords[0]
		menuy = mousecoords[1]
	elif menuing:
		menupush[1] = Draw.PushButton("Union", 39, menux, menuy, 120, 20, "Add union block")
		menupush[2] = Draw.PushButton("Intersection", 40, menux, menuy - 20, 120, 20, "Add intersection block")
		menupush[3] = Draw.PushButton("Subtraction", 41, menux, menuy - 40, 120, 20, "Add subtraction block")

	if breakstart:
		breakstart = 0
		menuing = 0
		premenuing = 0
		menux = mousecoords[0]
		menuy = mousecoords[1]
	elif breaking:
		delpush = Draw.PushButton("Break link", 38, menux - 40, menuy - 10, 80, 20, "Break link")

	if premenustart:
		premenustart = 0
		breaking = 0
		menuing = 0
	elif premenuing:
		if lowpreview:
			premenupush[1] = Draw.PushButton("v Low preview", 35, x - 380, 60, 120, 20, "Switch on low quality preview")
		else:
			premenupush[1] = Draw.PushButton("  Low preview", 35, x - 380, 60, 120, 20, "Switch on low quality preview")
		if highpreview:
			premenupush[2] = Draw.PushButton("v High preview", 36, x - 380, 40, 120, 20, "Switch on high quality preview")
		else:
			premenupush[2] = Draw.PushButton("  High preview", 36, x - 380, 40, 120, 20, "Switch on high quality preview")
		if renderpreview:
			premenupush[3] = Draw.PushButton("v Rendering mode", 37, x - 380, 20, 120, 20, "Switch on rendering mode")
		else:
			premenupush[3] = Draw.PushButton("  Rendering mode", 37, x - 380, 20, 120, 20, "Switch on rendering mode")

		
	drawnodes("un")
	drawnodes("int")
	drawnodes("sub")



	x2 = mousecoords[0]
	y2 = mousecoords[1]
	
	if connecting:
		glColor4f(1.0, 1.0, 1.0, 1.0)
		glBegin(GL_LINES)
		glVertex2f(x2, y2)
		glVertex2f(connx, conny)
		glEnd()

		
	if x2 >= 0 and x2 - radius < awidth and y2 >= 0 and y2 - radius < aheight:
		if toggle["d"].val or toggle["f"].val:			
			glColor4f(0, 0, 0, 1)
			glBegin(GL_LINE_LOOP)
			step = 12
			for angle in range(0, 360, step):
				theta = pi*angle/180.0
				glVertex2f(x2 + radius*cos(theta), y2 + radius*sin(theta))
			glEnd()
			


		
		



def processnode(position):
	global dset, conndata
	start = 1
	kind1, pos1 = position
	for node in conndata["in"][kind1][pos1]:
		kind2, pos2 = node
		if kind2 == "sel" and not(readyfordisplay[pos2]):
			continue
		if not(conndata["check"][kind2][pos2]):
			processnode([kind2, pos2])
			conndata["check"][kind2][pos2] = 1
		if start:
			dset[kind1][pos1] = dset[kind2][pos2].copy()
			start = 0
		elif kind1 == "un":
			dset[kind1][pos1].update(dset[kind2][pos2])
		elif kind1 == "int":
			dset[kind1][pos1].intersection_update(dset[kind2][pos2])
		elif kind1 == "sub":
			dset[kind1][pos1].difference_update(dset[kind2][pos2])


def drawnodes(kind):
	global hdtoggle, ntoggle

	for pos in range(num[kind]):
		if not(deleted[kind, pos]):
			offset = calcoffset(kind, pos)
			if kind == "un":
				string = "Union"
			elif kind == "int":
				string = "Intersection"
			elif kind == "sub":
				string = "Subtraction"
			hdtoggle[kind][pos] = Draw.Toggle(string, 48 + offset, areax - box["x"][kind][pos], areay - box["y"][kind][pos], 100, 20, hdtoggle[kind][pos].val, "Toggle" + string + "node") 
			ntoggle["in"][kind][pos] = Draw.Toggle("", 49 + offset, areax - box["x"][kind][pos] + 40, areay - box["y"][kind][pos] + 20, 20, 20, ntoggle["in"][kind][pos].val, string + " in")
			ntoggle["out"][kind][pos] = Draw.Toggle("", 50 + offset, areax - box["x"][kind][pos] + 40, areay - box["y"][kind][pos] - 20, 20, 20, ntoggle["out"][kind][pos].val, string + " out")
			ntoggle["view"][kind][pos] = Draw.Toggle("v", 51 + offset, areax - box["x"][kind][pos] - 40, areay - box["y"][kind][pos], 20, 20, ntoggle["view"][kind][pos].val, "Toggle view to this node")
			ntoggle["solo"][kind][pos] = Draw.Toggle("S", 52 + offset, areax - box["x"][kind][pos] - 20, areay - box["y"][kind][pos], 20, 20, ntoggle["solo"][kind][pos].val, "Toggle solo selection")


def calcoffset(kind, pos):
	if kind == "sel":
		offset = pos*selcomps - 7
	elif kind == "un":
		offset = num["sel"]*selcomps + pos*uncomps
	elif kind == "int":
		offset = num["sel"]*selcomps + num["un"]*uncomps + pos*intcomps
	elif kind == "sub":
		offset = num["sel"]*selcomps + num["un"]*uncomps + num["int"]*intcomps + pos*subcomps
	return offset


def render():
	global lookupstep, rendernow
	lookupstep = 1
	doalloperations()
	lookupstep = 2
	rendernow = 1


def event(evt, val):
	global leftdown, rightdown, middledown, enter, radius, num, last, mousecoords, windowx, windowy, delpush
	global blinking, blink, width, height, undoing, base, moving, menuing, menustart, connecting, connpos, numconns
	global online, breakstart, breaking, line, drawing, setundo, calclist, scalemoving, oldzoom, wanding
	global premenuing, premenustart, lookupstep, undostatus, deleted, recalctrigger, dset, viewpos
	global listpos, conndata, slider, doall, leftjustdown, dikelist, tresholding, theresone

	if evt == Draw.ESCKEY:
		for key in image.keys():
			del image[key]
		Draw.Exit()

	if evt == Draw.LEFTMOUSE:
		leftdown = leftjustdown = val
		menuing = 0
		premenuing = 0
		if leftdown:
			breaking = 0
			x2 = mousecoords[0]
			y2 = mousecoords[1]
			if  x2 >= 0 and x2 < awidth - 1 and  y2 >= 0 and y2 < aheight - 1:
				if not(toggle["d"].val) and not(toggle["f"].val):
					wanding[listpos] = not(wanding[listpos])
				enter = 1
				dooperations()
			if overscale:
				scalemoving = 1
				oldzoom = zoom
			if online > -1:
				breakstart = 1
				breaking = 1
				line = online
		else:
			for node in conndata["out"]["sel"][listpos]:
				if node[0] == "sel" and calckind[node[1]] == "venice":
					oldlistpos = listpos
					listpos = node[1]
					adaptsliders()
					dovenice(base["x"][node[1]][0], base["y"][node[1]][0])
					listpos = oldlistpos
					adaptsliders()
					conndata["check"][node[0]][node[1]] = 1
			if calckind[listpos] == "venice" or calckind[listpos] == "none":		
				drawset = set([]) 
				colordir = {}
				alphadir = {}
			if scalemoving:
				doalloperations()
				scalemoving = 0
			elif renderpreview and wanding[listpos] == False:
				render()
			elif renderpreview and (calckind[listpos] == "calc" or calckind[listpos] == "fill"):
				render()
		Draw.Draw()

	if evt == Draw.MIDDLEMOUSE:
		middledown = val
		if connecting:
			numconns[connecting, connkind, connpos] -= 1
			if numconns[connecting, connkind, connpos] == 0:
				ntoggle[connecting][connkind][connpos].val = 0
			connecting = 0

	if evt == Draw.RIGHTMOUSE:
		rightdown = val
		if connecting:
			numconns[connecting, connkind, connpos] -= 1
			if numconns[connecting, connkind, connpos] == 0:
				ntoggle[connecting][connkind][connpos].val = 0
			connecting = 0
			rightdown = 0
		elif rightdown:
			x, dummy = Window.GetAreaSize()
			if mousecoords[0] >= x - 260 and mousecoords[0] <= x - 160 and mousecoords[1] >= 20 and mousecoords[1] <= 80:
				premenustart = 1
				premenuing = 1
			else:
				menustart = 1
				menuing = 1
			Draw.Draw()

	if evt == Draw.MOUSEX or evt == Draw.MOUSEY:
		x, y = Window.GetMouseCoords()
		mousecoords[0] = x - windowx
		mousecoords[1] = y - windowy
		if (evt == Draw.MOUSEX and x != val) or (evt == Draw.MOUSEY and y != val):
			return

		if scalemoving:
			rescale()
		else:
			dooperations()
		
		theresone = 0
		handleselbox()

		movebox("un")
		movebox("int")
		movebox("sub")

		if not(moving):
			last["x"] = mousecoords[0]
			last["y"] = mousecoords[1]

		Draw.Draw()

	if evt == Draw.WHEELDOWNMOUSE:
		if calckind[listpos] == "venice":
			while Window.QTest():
				evt2, val2 = Window.QRead()
		if not(undoing):
			if not(tresholding) and (toggle["d"].val or toggle["f"].val) and (mousecoords[0] < awidth + radius and mousecoords[1] < aheight + radius):
				radius -= 4
			else:
				if selection[0] == "sel":
					slider["t"].val -= 10
					if slider["t"].val < 1:
						slider["t"].val = 1
					enter = 1
					dooperations()
		else:
			base["pos"][listpos] -= 1
			if base["pos"][listpos] <= 0:
				base["pos"][listpos] = 0
				slider["u"].val = 0
				dset["sel"][listpos] = set([])
				recalctrigger = 1
			else:
				enter = 1
				dooperations()
		Draw.Draw()
		
	if evt == Draw.WHEELUPMOUSE:
		if calckind[listpos] == "venice":
			while Window.QTest():
				evt2, val2 = Window.QRead()
		if not(undoing):
			if not(tresholding) and (toggle["d"].val or toggle["f"].val) and (mousecoords[0] < awidth + radius and mousecoords[1] < aheight + radius):
				radius += 4
			else:
				if selection[0] == "sel":
					slider["t"].val += 10
					enter = 1
					dooperations()
		else:
			base["pos"][listpos] += 1
			if base["pos"][listpos] > len(base["x"][listpos]):
				base["pos"][listpos] = len(base["x"][listpos])
			else:
				enter = 1
				dooperations()
		Draw.Draw()

	if evt == Draw.SPACEKEY:
		if val:
			drawing = 0
			undostatus = 0
			if not(toggle["d"].val) and not(toggle["f"].val) and wanding[listpos]:
				dset["sel"][listpos] = set([])
				readyfordisplay[listpos] = 0
			elif toggle["d"].val or toggle["f"].val:
				slider["u"].val = 100
				slider["t"].val = 100
				slider["f"].val = 0
				slider["r"].val = 50
				slider["g"].val = 50
				slider["b"].val = 50
				slider["h"].val = 50
				slider["s"].val = 50
				slider["v"].val = 50
			
			addselnode()
			recalctrigger = 1
			Draw.Draw()
		
	if evt == Draw.LEFTCTRLKEY:
		undoing = val
		if undoing:
			base["pos"][listpos] = (len(base["x"][listpos]) * slider["u"].val) / 100.0


	if evt == Draw.LEFTSHIFTKEY:
		tresholding = val

			
	if evt == Draw.DELKEY:
		if val:
			kind, pos = selection
			deleted[kind, pos] = 1
			if kind == "sel":
				dset["sel"][pos] = set([])
			for node in conndata["in"][kind][pos]:
				if kind == "sel" and node[0] == "sel":
					found = 0
					for node2 in conndata["out"][node[0]][node[1]]:
						if node2[0] == "sel" and node2[1] != pos:
							found = 1
							break
					if found == 0:
						dikelist.pop(dikelist.index(node[1]))
				conndata["out"][node[0]][node[1]].pop(conndata["out"][node[0]][node[1]].index([kind, pos]))
			for node in conndata["out"][kind][pos]:
				conndata["in"][node[0]][node[1]].pop(conndata["in"][node[0]][node[1]].index([kind, pos]))
			conndata["in"][kind][pos] = []
			conndata["out"][kind][pos] = []
			minus = 0
			for p in range(len(box["in"])):
				if (box["in"][p - minus] == [kind, pos]) or (box["out"][p - minus] == [kind, pos]):
					box["in"].pop(p - minus)
					box["out"].pop(p - minus)
					minus += 1
			if [kind, pos] in viewpos:
				viewpos.pop(viewpos.index([kind, pos]))
			if kind == "sel":
				if pos in dikelist:
					dikelist.pop(dikelist.index(pos))
			dset[kind][pos] = set([])
			recalctrigger = 1
			Draw.Draw()
				

def doalloperations():
	global oldzoom, factor
	factor = zoom / oldzoom
	oldzoom = zoom
	for op in dikelist:
		operate(op)
	for op in range(num["sel"]):
		if not(op in dikelist):
			operate(op)
	
	
def operate(op):
	global listpos, base, drawset, colordir, alphadir, drawing, radius, calclist, doall
	if not(deleted["sel", op]):
		oldlistpos = listpos
		listpos = op
		adaptsliders()
		for pos in range(len(base["x"][op])):
			base["x"][op][pos] = base["x"][op][pos] * factor
			base["y"][op][pos] = base["y"][op][pos] * factor
			if calckind[op] != "venice":
				base["radius"][op][pos] = base["radius"][op][pos] * factor
		if calckind[op] == "venice":
			dovenice(base["x"][op][0], base["y"][op][0])
		elif calckind[op] == "calc" or calckind[op] == "fill":
			drawset = set([])
			colordir = {}
			alphadir = {}
			drawing = 1
			for circle in range(base["pos"][op]):
				calclist = []
				radius = int(base["radius"][op][circle] + 0.5)
				x2 = base["x"][op][circle] - radius
				y2 = base["y"][op][circle] - radius
				for y in range(radius*2):
					for x in range(radius*2):
						x1 = x + x2
						y1 = y + y2
						if x1 < awidth - 1 and x1 >= 0 and y1 >= 0 and y1 < aheight - 1:
							if sqrt((x - radius)**2 + (y - radius)**2) <= radius:
								calclist.append([x + x2, y + y2])
				doall = 1
				if calckind[op] == "calc"	:
					docalc()
				elif calckind[op] == "fill":
					dofill()
		listpos = oldlistpos
		adaptsliders()
		
		
def rescale():
	global pixelscale, zoom, zoom, last, awidth, aheight
	mx, my = mousecoords
	pixelscale["x"] = float(mx)
	pixelscale["y"] = float(my)
	zoom = min((pixelscale["x"] / horizontal) / width, (pixelscale["y"] / vertical) / height)
	awidth = int(width * zoom)
	aheight = int(height * zoom)
	makeblancolist()
	
		
		
def dooperations():
	global calc, fill, calclist, enter, oldx, oldy, calckind, setundo, drawset, drawing
	global slider, radius, conndata, leftdown, preshaping, preshapeset, precolordir, prealphadir
	global recalctrigger, leftjustdown, shortcutting, colordir, alphadir

	passnopre = 0

	x2 = mousecoords[0]
	y2 = mousecoords[1]
	if not(toggle["d"].val) and not(toggle["f"].val):
		r = 0
	else:
		r = radius

	if x2 >= 0 and x2 - r < awidth - 1 and  y2 >= 0 and y2 - r < aheight - 1:
		if toggle["d"].val or toggle["f"].val:

			if (["sel", listpos] in viewpos):
				shortcutting = 1
			else:
				shortcutting = 0

			if not(leftdown) and not(undoing) and not(setundo):
				preshaping = 1
				enter = 1
			else:
				preshaping = 0

			if leftjustdown and drawing:
				leftjustdown = 0
				for i in range(len(base["x"][listpos]) - base["pos"][listpos]):
					base["x"][listpos].pop(len(base["x"][listpos]) - 1)
					base["y"][listpos].pop(len(base["y"][listpos]) - 1)
					base["radius"][listpos].pop(len(base["radius"][listpos]) - 1)
				drawset = dset["sel"][listpos].copy()
				colordir = clist[listpos].copy()
				alphadir = alist[listpos].copy()
				undostatus = 1
			
			if toggle["f"].val:
				if calc == 1:
					drawing = 0
					slider["u"].val = 100
				fill = 1
				calc = 0
			elif toggle["d"].val:
				if fill == 1:
					drawing = 0
					slider["u"].val = 100
				calc = 1
				fill = 0


			calclist = []
			x2 -= radius
			y2 -= radius
			for y in range(radius*2):
				for x in range(radius*2):
					x1 = x + x2
					y1 = y + y2
					if x1 < awidth - 1 and x1 >= 0 and y1 >= 0 and y1 < aheight - 1:
						if sqrt((x - radius)**2 + (y - radius)**2) <= radius:
							calclist.append([x1, y1])
			if leftdown:
				enter = 1
			
		elif wanding[listpos]:
			calc = fill = 0
			if x2 == oldx and y2 == oldy:
				pass
			else:
				oldx = x2
				oldy = y2
				dovenice(x2, y2)
				calckind[listpos] = "venice"
	
	else:
		passnopre = 1
		
	
	if enter:
		enter = 0
		if undoing or setundo:
			drawset = set([])
			colordir = {}
			alphadir = {}
			drawing = 1
			slider["u"].val = (base["pos"][listpos] * 100.0) / len(base["x"][listpos])
			for circle in range(int(base["pos"][listpos])):
				calclist = []
				radius = int(base["radius"][listpos][circle] + 0.5)
				x2 = base["x"][listpos][circle] - radius
				y2 = base["y"][listpos][circle] - radius
				for y in range(radius*2):
					for x in range(radius*2):
						x1 = x + x2
						y1 = y + y2
						if x1 < awidth - 1 and x1 >= 0 and y1 >= 0 and y1 < aheight - 1:
							if sqrt((x - radius)**2 + (y - radius)**2) <= radius:
								calclist.append([x + x2, y + y2])
				if calckind[listpos] == "calc"	:
					docalc()
				elif calckind[listpos] == "fill":
					dofill()
			setundo = 0
		elif calc and (x2 != oldx and y2 != oldy):
			docalc()
			if not(preshaping):
				calckind[listpos] = "calc"
				oldx = x2
				oldy = y2
		elif fill and (x2 != oldx and y2 != oldy):
			dofill()
			if not(preshaping):
				calckind[listpos] = "fill"
				oldx = x2
				oldy = y2
		elif calckind[listpos] == "venice":
			dovenice(base["x"][listpos][0], base["y"][listpos][0])
			calckind[listpos] = "venice"
			
	if passnopre:
		if preshaping == 1:
			preshaping = 0
			recalctrigger = 1
		if dset["sel"][listpos] != set([]):
			if calckind[listpos] == "venice" and wanding[listpos]:
				dset["sel"][listpos] = set([])
				readyfordisplay[listpos] = 0
				recalctrigger = 1


def handleselbox():
	global mousecoords, blinking, moving, box, last
	x2 = mousecoords[0]
	y2 = mousecoords[1]
	coords = y2 * awidth + x2
	for pos in range(num["sel"]):
		if x2 < awidth and y2 < aheight:
			if not(leftdown) and (coords in dset["sel"][pos] or (coords + 1) in dset["sel"][pos] or (coords + awidth) in dset["sel"][pos] or (coords + awidth + 1) in dset["sel"][pos]):
				blinking[pos] = 1
			else:
				blinking[pos] = 0

		movebox("sel")
#		if last["x"] >= areax - box["x"]["sel"][pos] - 20 and last["x"] <= areax - box["x"]["sel"][pos] + 120 and last["y"] >= areay - #box["y"]["sel"][pos] and last["y"] <= areay - box["y"]["sel"][pos] + 20:
#			if middledown:
#				moving = 1
#				box["x"]["sel"][pos] = box["x"]["sel"][pos] - mousecoords[0] + last["x"]
#				box["y"]["sel"][pos] = box["y"]["sel"][pos] - mousecoords[1] + last["y"]
#				last["x"] = mousecoords[0]
#				last["y"] = mousecoords[1]
#			else:
#				moving = 0


def movebox(kind):
	if theresone:
		return
	found = checkover(movingbox[0], movingbox[1])
	if found:
		return
	for pos in range(num[kind]):
		found = checkover(kind, pos)
		if found:
			break
	
def checkover(kind, pos):
	global moving, box, last, movingbox, theresone
	if last["x"] >= areax - box["x"][kind][pos] - 20 and last["x"] <= areax - box["x"][kind][pos] + 100 and last["y"] >= areay - box["y"][kind][pos] and last["y"] <= areay - box["y"][kind][pos] + 20:
		if middledown:
			theresone = 1
			moving = 1
			box["x"][kind][pos] = box["x"][kind][pos] - mousecoords[0] + last["x"]
			box["y"][kind][pos] = box["y"][kind][pos] - mousecoords[1] + last["y"]
			last["x"] = mousecoords[0]
			last["y"] = mousecoords[1]
			movingbox = [kind, pos]
			return 1
		else:
			moving = 0
	return 0
				

def sliders(evt):
	global first
	global image, imagelist
	global enter, colourpicker, calclist, calc, oldx, oldy, pixels
	global listpos, undoing, base, setundo, fill
	global menuing, num, box, ntoggle, viewpos
	global connecting, connx, conny, connpos, connkind, box, numconns, conndata
	global selcomps, uncomps, intcomps, subcomps
	global breaking, line, recalctrigger, lowpreview, highpreview, renderpreview, premenuing,lookupstep
	global rendernow, frombutton, floodvalue, undostatus, savedviewpos, solo, selections, selection
	global slider, dikelist

	if (0 <= evt <= 5) or (7 <= evt <= 12):
		enter = 1
		dooperations()
		Draw.Draw()

	if evt == 6:
		calclist = []
		calc = 1
		for y in range(aheight):
			for x in range(awidth):
				calclist.append([x, y])
		enter = 1
		dooperations()

	
	if evt == 13:
		if num["sel"] > 0:
			if calckind[listpos] == "venice":
				fill = calc = 0
				enter = 1
				dooperations()
	
	
	if evt == 14:
		loadcomponent("r")
	if evt == 15:
		loadcomponent("g")		
	if evt == 16:
		loadcomponent("b")
	if evt == 17:
		loadcomponent("h")
	if evt == 18:
		loadcomponent("s")
	if evt == 19:
		loadcomponent("v")

	if evt == 21:
		if toggle["d"].val:
			toggle["f"].val = 0
		else:
			calc = 0
		
		
	if evt == 22:
		recalctrigger = 1
		Draw.Draw()


	if evt == 23:
		if calckind[listpos] == "venice":
			slider["u"].val = 100
		else:
			enter = 1
			setundo = 1
			base["pos"][listpos] = (len(base["x"][listpos]) * slider["u"].val) / 100.0
			dooperations()
			Draw.Draw()


	if evt == 24:
		if toggle["f"].val == 1:
			toggle["d"].val = 0
		else:
			fill = 0


	if evt == 25:
		render()
		frombutton = 1
		Draw.Draw()


	if evt == 26:
		floodvalue = 100 - slider["f"].val
		enter = 1
		dooperations()
		Draw.Draw()

		
	if evt == 27:
		Window.FileSelector(savemask, "Save Mask")


	if evt == 28:
		if savefilename == None:
			Window.FileSelector(savefile, "Save working file")
		else:
			savefile(savefilename)
		

	if evt == 29:
		Window.FileSelector(savefile, "Save working file as...")
		

	if evt == 30:
		Window.FileSelector(openfile, "Open working file")
		recalctrigger = 1
		Draw.Draw()
		
		
	if evt == 31:
		for key in image.keys():
			del image[key]
		Draw.Exit()
		
		
	if evt == 32:
		doalloperations()
		Draw.Draw()
		

	if evt == 35:
		toggle["p"].val =1
		lowpreview = 1
		highpreview = 0
		doalloperations()
		premenuing = 0
		Draw.Draw()
	if evt == 36:
		toggle["p"].val =1
		lowpreview = 0
		highpreview = 1
		doalloperations()
		premenuing = 0
		Draw.Draw()
	if evt == 37:
		if renderpreview:
			renderpreview = 0
		else:
			renderpreview = 1
			render()
			premenuing = 0
			Draw.Draw()
			
			
	if evt == 38:
		breaking = 0
		kindout, posout = box["out"][line]
		kindin, posin = box["in"][line]
		conndata["out"][kindout][posout].pop(conndata["out"][kindout][posout].index([kindin, posin]))
		numconns["out", kindout, posout] -= 1
		ntoggle["out"][kindout][posout].val = 0
		conndata["in"][kindin][posin].pop(conndata["in"][kindin][posin].index([kindout, posout]))
		numconns["in", kindin, posin] -= 1
		ntoggle["in"][kindin][posin].val = 0
		box["out"].pop(line)
		box["in"].pop(line)
		uncheckdownstream(kindin, posin)
		if kindout == "sel" and (posout in dikelist):
			dikelist.pop(dikelist.index(posout))


	if evt == 39:
		offset = num["sel"]*selcomps + num["un"]*uncomps
		addnode("un", offset)
	if evt == 40:
		offset = num["sel"]*selcomps + num["un"]*uncomps + num["int"]*intcomps
		addnode("int", offset)
	if evt == 41:
		offset = num["sel"]*selcomps + num["un"]*uncomps + num["int"]*intcomps + num["sub"]*subcomps
		addnode("sub", offset)



	for pos in range(num["sel"]):
		if evt == 43 + pos*selcomps:
			if solos[pos].val == 1:
				erasesolos()
				solos[pos].val = 1
				if solo == 0:
					savedviewpos = deepcopy(viewpos)
				viewpos = [["sel", pos]]
				solo = 1
			else:
				viewpos = deepcopy(savedviewpos)
				solo = 0
			recalctrigger = 1
		if evt == 42 + pos*selcomps:
			fill = calc = 0
			wanding[listpos] = False
			selection = ["sel", pos]
			if selections[pos].val == 0:
				selections[pos].val = 1
			else:
				listpos = pos
				if calckind[listpos] == "venice":
					undostatus = 0
					undoing = 0
					oldx = base["x"][pos][0]
					oldy = base["y"][pos][0]
					slider["t"].val = base["tresh"][listpos]
					slider["f"].val = base["flood"][listpos]
					slider["r"].val = base["r"][listpos]
					slider["g"].val = base["g"][listpos]
					slider["b"].val = base["b"][listpos]
					slider["h"].val = base["h"][listpos]
					slider["s"].val = base["s"][listpos]
					slider["v"].val = base["v"][listpos]
				elif calckind[listpos] == "calc":
					undostatus = 1
					slider["t"].val = base["tresh"][listpos]
					slider["f"].val = base["flood"][listpos]
					slider["r"].val = base["r"][listpos]
					slider["g"].val = base["g"][listpos]
					slider["b"].val = base["b"][listpos]
					slider["h"].val = base["h"][listpos]
					slider["s"].val = base["s"][listpos]
					slider["v"].val = base["v"][listpos]
					slider["u"].val = (base["pos"][listpos] / len(base["x"][listpos])) * 100
				elif calckind[listpos] == "fill":
					undostatus = 1
					slider["t"].val = 100
					slider["f"].val = 0
					slider["u"].val = (base["pos"][listpos] / len(base["x"][listpos])) * 100
				elif calckind[listpos] == "none":
					slider["t"].val = base["tresh"][listpos]
					slider["f"].val = base["flood"][listpos]
					slider["r"].val = base["r"][listpos]
					slider["g"].val = base["g"][listpos]
					slider["b"].val = base["b"][listpos]
					slider["h"].val = base["h"][listpos]
					slider["s"].val = base["s"][listpos]
					slider["v"].val = base["v"][listpos]
					slider["u"].val = 100
			eraseselections()
			selections[pos].val = 1
			Draw.Draw()
		if evt == 44 + pos*selcomps:
			recalctrigger = 1
			if not(solo):
				if views[pos].val:
					viewpos.append(["sel", pos])
				else:
					viewpos.pop(viewpos.index(["sel", pos]))
			else:
				if views[pos].val:
					savedviewpos.append(["sel", pos])
				else:
					savedviewpos.pop(savedviewpos.index(["sel", pos]))
		if evt == 45 + pos*selcomps:
			recalctrigger = 1
			color[pos] = selcols[pos].val
		if evt == 46 + pos*selcomps:
			handleconnection("in", "sel", pos)
		if evt == 47 + pos*selcomps:
			handleconnection("out", "sel", pos)

	handlenodes("un", evt)
	handlenodes("int", evt)
	handlenodes("sub", evt)	


	Draw.Redraw(1)


def openfile(filename):
	global oldx, oldy, radius, calc, fill, toggle, slider, viewtoggle, listpos, base
	global calckind, selections, views, solos, selcols, hdtoggle, ntoggle, num, box, numconns, conndata
	global viewpos, color, readyfordisplay, wanding, renderpreview, highpreview, lowpreview
	global floodvalue, solo, deleted, selection, zoom, pixelscale, first, oldzoom, savedviewpos
	global imagefilename, image, width, height, pixels, awidth, aheight, imagelist, justopen
	global ses, vis, sos, cols, ni, no, nv, ns, co, version, horizontal, vertical, slider
	global comparesetlist, dset, clist, alist, dikelist
	file = open(filename, "r")
	version = cPickle.load(file)
	oldx = cPickle.load(file)
	oldy = cPickle.load(file)
	radius = cPickle.load(file)
	calc = cPickle.load(file)
	fill = cPickle.load(file)
	toggle["r"].val = cPickle.load(file)
	toggle["g"].val = cPickle.load(file)
	toggle["b"].val = cPickle.load(file)
	toggle["h"].val = cPickle.load(file)
	toggle["s"].val = cPickle.load(file)
	toggle["v"].val = cPickle.load(file)
	toggle["f"].val = cPickle.load(file)
	toggle["d"].val = cPickle.load(file)
	toggle["p"].val = cPickle.load(file)
	viewtoggle["r"].val = cPickle.load(file)
	viewtoggle["g"].val = cPickle.load(file)
	viewtoggle["b"].val = cPickle.load(file)
	viewtoggle["h"].val = cPickle.load(file)
	viewtoggle["s"].val = cPickle.load(file)
	viewtoggle["v"].val = cPickle.load(file)
	colourpicker.val = cPickle.load(file)
	listpos = cPickle.load(file)
	base = cPickle.load(file)
	calckind = cPickle.load(file)
	ses = []
	vis = []
	sos = []
	cols = []
	ni["sel"] = []
	no["sel"] = []
	num	= cPickle.load(file)
	for pos in range(num["sel"]):
		ses.append(cPickle.load(file))
		vis.append(cPickle.load(file))
		sos.append(cPickle.load(file))
		cols.append(cPickle.load(file))
		ni["sel"].append(cPickle.load(file))
		no["sel"].append(cPickle.load(file))
	hd["un"] = []
	ni["un"] = []
	no["un"] = []
	nv["un"] = []
	ns["un"] = []
	for pos in range(num["un"]):
		hd["un"].append(cPickle.load(file))
		ni["un"].append(cPickle.load(file))
		no["un"].append(cPickle.load(file))
		nv["un"].append(cPickle.load(file))
		ns["un"].append(cPickle.load(file))
	hd["int"] = []
	ni["int"] = []
	no["int"] = []
	nv["int"] = []
	ns["int"] = []
	for pos in range(num["int"]):
		hd["int"].append(cPickle.load(file))
		ni["int"].append(cPickle.load(file))
		no["int"].append(cPickle.load(file))
		nv["int"].append(cPickle.load(file))
		ns["int"].append(cPickle.load(file))
	hd["sub"] = []
	ni["sub"] = []
	no["sub"] = []
	nv["sub"] = []
	ns["sub"] = []
	for pos in range(num["sub"]):
		hd["sub"].append(cPickle.load(file))
		ni["sub"].append(cPickle.load(file))
		no["sub"].append(cPickle.load(file))
		nv["sub"].append(cPickle.load(file))
		ns["sub"].append(cPickle.load(file))
	box = cPickle.load(file)
	numconns = cPickle.load(file)
	conndata = cPickle.load(file)
	viewpos = cPickle.load(file)
	savedviewpos = cPickle.load(file)
	color = cPickle.load(file)
	readyfordisplay = cPickle.load(file)
	wanding = cPickle.load(file)
	renderpreview = cPickle.load(file)
	lowpreview = cPickle.load(file)
	highpreview = cPickle.load(file)
	floodvalue = cPickle.load(file)
	solo = cPickle.load(file)
	deleted = cPickle.load(file)
	selection = cPickle.load(file)
	listpos = selection[1]
	zoom = cPickle.load(file)
	pixelscale = cPickle.load(file)
	imagefilename = cPickle.load(file)
	horizontal = cPickle.load(file)
	vertical = cPickle.load(file)
	dikelist = cPickle.load(file)
	slider["t"].val = base["tresh"][listpos]
	slider["f"].val = base["flood"][listpos]
	slider["r"].val = base["r"][listpos]
	slider["g"].val = base["g"][listpos]
	slider["b"].val = base["b"][listpos]
	slider["h"].val = base["h"][listpos]
	slider["s"].val = base["s"][listpos]
	slider["v"].val = base["v"][listpos]
	if len(base["x"][listpos]) > 0:
		slider["u"].val = (base["pos"][listpos] * 100.0) / len(base["x"][listpos])
	first["r"] = first["g"] = first["b"] = first["h"] = first["s"] = first["v"] = 1
	oldzoom = zoom
	image["rgb"] = Image.Load(imagefilename)
	width = image["rgb"].getSize()[0]
	height = image["rgb"].getSize()[1]
	pixels = width * height
	awidth = int(width * zoom)
	aheight = int(height * zoom)
	makeblancolist()
	imagelist = []
	for y in range(height):
		for x in range(width):
			r, g, b, dummy = image["rgb"].getPixelF(x, y)
			imagelist.append([r, g, b])
	dset = {}
	dset["sel"] = []
	dset["un"] = []
	dset["int"] = []
	dset["sub"] = []
	clist = []
	alist = []
	for pos in range(num["sel"]):
		comparesetlist.append(set([]))
		dset["sel"].append(set([]))
		clist.append({})
		alist.append({})
	for pos in range(num["un"]):
		conndata["check"]["un"][pos] = 0
		dset["un"].append(set([]))
	for pos in range(num["int"]):
		conndata["check"]["int"][pos] = 0
		dset["int"].append(set([]))
	for pos in range(num["sub"]):
		conndata["check"]["sub"][pos] = 0
		dset["sub"].append(set([]))
	doalloperations()

	justopen = 1
	file.close()
	
	


def savefile(filename):
	global imagefilename, savefilename
	if not(filename.count(".vnc")):
		filename = filename + ".vnc"
	savefilename = filename
	file = open(savefilename, "w")
	cPickle.dump(version, file)
	cPickle.dump(oldx, file)
	cPickle.dump(oldy, file)
	cPickle.dump(radius, file)
	cPickle.dump(calc, file)
	cPickle.dump(fill, file)
	cPickle.dump(toggle["r"].val, file)
	cPickle.dump(toggle["g"].val, file)
	cPickle.dump(toggle["b"].val, file)
	cPickle.dump(toggle["h"].val, file)
	cPickle.dump(toggle["s"].val, file)
	cPickle.dump(toggle["v"].val, file)
	cPickle.dump(toggle["f"].val, file)
	cPickle.dump(toggle["d"].val, file)
	cPickle.dump(toggle["p"].val, file)
	cPickle.dump(viewtoggle["r"].val, file)
	cPickle.dump(viewtoggle["g"].val, file)
	cPickle.dump(viewtoggle["b"].val, file)
	cPickle.dump(viewtoggle["h"].val, file)
	cPickle.dump(viewtoggle["s"].val, file)
	cPickle.dump(viewtoggle["v"].val, file)
	cPickle.dump(colourpicker.val, file)
	cPickle.dump(listpos, file)
	cPickle.dump(base, file)
	cPickle.dump(calckind, file)
	cPickle.dump(num, file)
	for pos in range(num["sel"]):
		cPickle.dump(selections[pos].val, file)
		cPickle.dump(views[pos].val, file)
		cPickle.dump(solos[pos].val, file)
		cPickle.dump(selcols[pos].val, file)		
		cPickle.dump(ntoggle["in"]["sel"][pos].val, file)
		cPickle.dump(ntoggle["out"]["sel"][pos].val, file)		
	for pos in range(num["un"]):
		cPickle.dump(hdtoggle["un"][pos].val, file)
		cPickle.dump(ntoggle["in"]["un"][pos].val, file)
		cPickle.dump(ntoggle["out"]["un"][pos].val, file)
		cPickle.dump(ntoggle["view"]["un"][pos].val, file)
		cPickle.dump(ntoggle["solo"]["un"][pos].val, file)
	for pos in range(num["int"]):
		cPickle.dump(hdtoggle["int"][pos].val, file)
		cPickle.dump(ntoggle["in"]["int"][pos].val, file)
		cPickle.dump(ntoggle["out"]["int"][pos].val, file)
		cPickle.dump(ntoggle["view"]["int"][pos].val, file)
		cPickle.dump(ntoggle["solo"]["int"][pos].val, file)
	for pos in range(num["sub"]):
		cPickle.dump(hdtoggle["sub"][pos].val, file)
		cPickle.dump(ntoggle["in"]["sub"][pos].val, file)
		cPickle.dump(ntoggle["out"]["sub"][pos].val, file)
		cPickle.dump(ntoggle["view"]["sub"][pos].val, file)
		cPickle.dump(ntoggle["solo"]["sub"][pos].val, file)
	cPickle.dump(box, file)
	cPickle.dump(numconns, file)
	cPickle.dump(conndata, file)
	cPickle.dump(viewpos, file)
	cPickle.dump(savedviewpos, file)
	cPickle.dump(color, file)
	cPickle.dump(readyfordisplay, file)
	cPickle.dump(wanding, file)
	cPickle.dump(renderpreview, file)
	cPickle.dump(lowpreview, file)
	cPickle.dump(highpreview, file)
	cPickle.dump(floodvalue, file)
	cPickle.dump(solo, file)
	cPickle.dump(deleted, file)
	cPickle.dump(selection, file)
	cPickle.dump(zoom, file)
	cPickle.dump(pixelscale, file)
	cPickle.dump(imagefilename, file)
	cPickle.dump(horizontal, file)
	cPickle.dump(vertical, file)
	cPickle.dump(dikelist, file)

	file.close()

	
def erasesolos():
	for pos in range(num["sel"]):
		solos[pos].val = 0
	for pos in range(num["un"]):
		ntoggle["solo"]["un"][pos].val = 0
	for pos in range(num["int"]):
		ntoggle["solo"]["int"][pos].val = 0
	for pos in range(num["sub"]):
		ntoggle["solo"]["sub"][pos].val = 0

		
def eraseselections():
	for pos in range(num["sel"]):
		selections[pos].val = 0
	for pos in range(num["un"]):
		hdtoggle["un"][pos].val = 0
	for pos in range(num["int"]):
		hdtoggle["int"][pos].val = 0
	for pos in range(num["sub"]):
		hdtoggle["sub"][pos].val = 0


def savemask(filename):
	global zoom, awidth, aheight, image
	oldzoom = zoom
	oldawidth = awidth
	oldaheight = aheight
	zoom = 1.0
	awidth = width
	aheight = height
	doalloperations()
	render()
	makedisplayset()
	for y in range(height):
		for x in range(width):
			coords = y * width + x
			if coords in displayset:
				alpha = 0
				for adir in alist:
					try:
						a1 = adir[coords]
						alpha = max(alpha, a1)
					except KeyError:
						pass
				image["rgb"].setPixelF(x, y, (0.0, 0.0, 0.0, 1.0))
				image["rgb"].setPixelF(x, y, (alpha, alpha, alpha, alpha))
			else:
				image["rgb"].setPixelF(x, y, (0.0, 0.0, 0.0, 1.0))
	oldfilename = image["rgb"].getFilename()
	image["rgb"].setFilename(filename)
	image["rgb"].save()
	image["rgb"].setFilename(oldfilename)
	image["rgb"].reload()
	zoom = oldzoom
	awidth = oldawidth
	aheight = oldaheight
	doalloperations()
	Draw.Draw()

	
def uncheckdownstream(kind, pos):
	if kind == "sel":
		conndata["check"][kind][pos] = 1
	else:
		conndata["check"][kind][pos] = 0
	for node in conndata["out"][kind][pos]:
		uncheckdownstream(node[0], node[1])
			


def handlenodes(kind, event):
	global viewpos, viewkind, recalctrigger, savedviewpos, solo, selection
	for pos in range(num[kind]):
		offset = calcoffset(kind, pos)
		if event == 48 + offset:
			eraseselections()
			hdtoggle[kind][pos].val = 1
			selection = [kind, pos]
			Draw.Draw()
		elif event == 52 + offset:
			if ntoggle["solo"][kind][pos].val == 1:
				erasesolos()
				ntoggle["solo"][kind][pos].val = 1
				if solo == 0:
					savedviewpos = deepcopy(viewpos)
				viewpos = [[kind, pos]]
				solo = 1
			else:
				viewpos = deepcopy(savedviewpos)
				solo = 0
			recalctrigger = 1
		elif event == 49 + offset:
			handleconnection("in", kind, pos)
		elif event == 50 + offset:
			handleconnection("out", kind, pos)
		elif event == 51 + offset:
			recalctrigger = 1
			if not(solo):
				if ntoggle["view"][kind][pos].val:
					viewpos.append([kind, pos])
				else:
					viewpos.pop(viewpos.index([kind, pos]))
			else:
				if ntoggle["view"][kind][pos].val:
					savedviewpos.append([kind, pos])
				else:
					savedviewpos.pop(savedviewpos.index([kind, pos]))


def loadcomponent(component):
	if first[component]:
		first[component] = 0
		image[component] = Image.New("red", width, height, 32)
		for y in range(height):
			for x in range(width):
				coords = y * width + x
				r, g, b = imagelist[coords]
				h, s, v = calcHSV(r, g, b)
				if component == "r":
					image["r"].setPixelF(x, y, (r, 0.0, 0.0, 1.0))
				elif component == "g":
					image["g"].setPixelF(x, y, (0.0, g, 0.0, 1.0))
				elif component == "b":
					image["b"].setPixelF(x, y, (0.0, 0.0, b, 1.0))
				elif component == "h":
					r, g, b = calcRGB(h, 1.0, 1.0)
					image["h"].setPixelF(x, y, (r, g, b, 1.0))
				elif component == "s":
					image["s"].setPixelF(x, y, (s, s, s, 1.0))
				elif component == "v":
					image["v"].setPixelF(x, y, (v, v, v, 1.0))
	for comp in viewtoggle.keys():
		if comp != component:
			viewtoggle[comp].val = 0
	enter = 1	

	
def addnode(kind, offset):
	global menuing, numconns, box, menux, menuy, hdtoggle, conndata, deleted
	menuing = 0
	if kind == "un":
		string = "Union"
	elif kind == "int":
		string = "Intersection"
	elif kind == "sub":
		string = "Subtraction"
	num[kind] += 1
	pos = num[kind] - 1
	dset[kind].append(set([]))
	numconns["in", kind, pos] = 0
	numconns["out", kind, pos] = 0
	box["x"][kind].append(areax - menux)
	box["y"][kind].append(areay - menuy)
	hdtoggle[kind].append(Draw.Toggle(string, 48 + offset, menux, menuy, 100, 20, 0, "Toggle solo selection"))
	ntoggle["in"][kind].append(Draw.Toggle("", 49 + offset, menux + 40, menuy + 20, 20, 20, 0, string + " in"))
	ntoggle["out"][kind].append(Draw.Toggle("", 50 + offset, menux + 40, menuy - 20, 20, 20, 0, string + " out"))
	ntoggle["view"][kind].append(Draw.Toggle("v", 51 + offset, menux - 40, menuy, 20, 20, 0, "Toggle view to this node"))
	ntoggle["solo"][kind].append(Draw.Toggle("S", 52 + offset, menux - 20, menuy, 20, 20, 0, "Toggle solo selection"))
	event = 51 + offset
	conndata["in"][kind][pos] = []
	conndata["out"][kind][pos] = []
	conndata["check"][kind][pos] = 0
	deleted[kind, pos] = 0


def handleconnection(dir, kind, pos):
	global ntoggle, box, connecting, connx, conny, connkind, connpos, numconns, recalctrigger, listpos, conndata
	global doall, dikelist
	if dir == "out":
		antidir = "in"
		yoffset = -20
	else:
		antidir = "out"
		yoffset = 40
	if connecting == 0:
		ntoggle[dir][kind][pos].val = 1
		connecting = dir
		connx = areax - box["x"][kind][pos] + 50
		conny = areay - box["y"][kind][pos] + yoffset
		connkind = kind
		connpos = pos
		numconns[dir, kind, pos] += 1
	if connecting == antidir:
		box[antidir].append([connkind, connpos])
		box[dir].append([kind, pos])
		k, p = box["in"][len(box["in"]) - 1]
		conndata["in"][k][p].append(box["out"][len(box["out"]) - 1])
		k, p = box["out"][len(box["out"]) - 1]
		conndata["out"][k][p].append(box["in"][len(box["in"]) - 1])
		connecting = 0
		numconns[dir, kind, pos] += 1
		k, p = box["in"][len(box["in"]) - 1]
		uncheckdownstream(k, p)
		if k == "sel":
			p2 = box["out"][len(box["out"]) - 1][1]
			if not(p2 in dikelist):
				dikelist.append(p2)
			if calckind[p] == "venice":
				oldlistpos = listpos
				listpos = p
				adaptsliders()
				dovenice(base["x"][p][0], base["y"][p][0])
				listpos = oldlistpos
				adaptsliders()
			conndata["check"][k][p] = 1
	if ntoggle[dir][kind][pos].val == 0 and numconns[dir, kind, pos] == 1:
		connecting = 0
		numconns[dir, kind, pos] = 0
	else:
		ntoggle[dir][kind][pos].val = 1

		
def adaptsliders():
	global slider
	slider["t"].val = base["tresh"][listpos]
	slider["f"].val = base["flood"][listpos]
	slider["r"].val = base["r"][listpos]
	slider["g"].val = base["g"][listpos]
	slider["b"].val = base["b"][listpos]
	slider["h"].val = base["h"][listpos]
	slider["s"].val = base["s"][listpos]
	slider["v"].val = base["v"][listpos]


def addselnode():
	global drawset, num, selections, solos, selcols, views, dset, conndata
	global listpos, base, box, blinking, blink
	global clist, color, colordir, wanding, comparsetlist, alist, calckind, selection
	global deleted
	x, y = Window.GetAreaSize()
	pos = num["sel"]
	listpos = pos
	wanding.append(True)
	drawset = set([])
	colordir = {}
	alphadir = {}
	comparesetlist.append(set([]))
	readyfordisplay.append(0)
	dset["sel"].append(set([]))
	clist.append(0)
	alist.append(0)
	calckind.append("none")
	base["x"].append([])
	base["y"].append([])
	base["pos"].append(1)
	base["radius"].append([])
	base["tresh"].append(100)
	base["flood"].append(0)
	base["r"].append(50)
	base["g"].append(50)
	base["b"].append(50)
	base["h"].append(50)
	base["s"].append(50)
	base["v"].append(50)
	slider["t"].val = base["tresh"][listpos]
	slider["f"].val = base["flood"][listpos]
	slider["r"].val = base["r"][listpos]
	slider["g"].val = base["g"][listpos]
	slider["b"].val = base["b"][listpos]
	slider["h"].val = base["h"][listpos]
	slider["s"].val = base["s"][listpos]
	slider["v"].val = base["v"][listpos]
	blinking.append(0)	
	fx, fy = freecoords()
	box["x"]["sel"].append(areax - (fx + 20))
	box["y"]["sel"].append(areay - (fy - 20))
	selections.append(Draw.Toggle("Selection " + str(pos + 1), 42 + pos*selcomps, areax - box["x"]["sel"][pos] + 40,  areay - box["y"]["sel"][pos], 80, 20, 1, "Select for edit: " + str(num["sel"] + 1)))
	for position in range(pos):
		selections[position].val = 0
	solos.append(Draw.Toggle("S", 43 + pos*selcomps, areax - box["x"]["sel"][pos] + 20,  areay - box["y"]["sel"][pos], 20, 20, 0, "Toggle solo selection"))
	views.append(Draw.Toggle("v", 44 + pos*selcomps, areax - box["x"]["sel"][pos],  areay - box["y"]["sel"][pos], 20, 20, 1, "Switch on view"))
	if solo:
		savedviewpos.append(["sel", pos])
	else:
		viewpos.append(["sel", pos])
	conndata["in"]["sel"][pos] = []
	conndata["out"]["sel"][pos] = []
	conndata["check"]["sel"][pos] = 1
	numconns["out", "sel", pos] = 0
	numconns["in", "sel", pos] = 0
	ntoggle["in"]["sel"].append(Draw.Toggle("", 46 + pos*selcomps, areax - box["x"]["sel"][pos] + 40, areay - box["y"]["sel"][pos] + 20, 20, 20, 0, "Dike in"))
	ntoggle["out"]["sel"].append(Draw.Toggle("", 47 + pos*selcomps, areax - box["x"]["sel"][pos] + 40, areay - box["y"]["sel"][pos] - 20, 20, 20, 0, "Selection out"))
	selcols.append(Draw.ColorPicker(45 + pos*selcomps, areax - box["x"]["sel"][pos] - 20, areay - box["y"]["sel"][pos], 20, 20, (1.0, 1.0, 1.0), "Set selection colourpicker"))
	color.append(selcols[listpos].val)
	deleted["sel", pos] = 0
	selection = ["sel", pos]
	num["sel"] += 1


def freecoords():
	wx, wy = Window.GetAreaSize()
	for ypos in range(wy - 20, 0, -20):	
		for xpos in range(awidth*horizontal, wx - 140, 10):
			if not(freespace("sel", xpos, ypos)):
				continue
			if not(freespace("un", xpos, ypos)):
				continue
			if not(freespace("int", xpos, ypos)):
				continue
			if not(freespace("sub", xpos, ypos)):
				continue
			return xpos, ypos

				
def freespace(kind, xpos, ypos):
	for pos in range(num[kind]):
		if xpos >= areax - box["x"][kind][pos] and xpos <= areax - box["x"][kind][pos] + 140 and ypos >= areay - box["y"][kind][pos] and ypos <= areay - box["y"][kind][pos] + 20:
			return 0
		if xpos + 140 >= areax - box["x"][kind][pos] and xpos + 140 <= areax - box["x"][kind][pos] + 140 and ypos >= areay - box["y"][kind][pos] and ypos <= areay - box["y"][kind][pos] + 20:
			return 0
		if xpos + 140 >= areax - box["x"][kind][pos] and xpos + 140 <= areax - box["x"][kind][pos] + 140 and ypos + 20 >= areay - box["y"][kind][pos] and ypos + 20 <= areay - box["y"][kind][pos] + 20:
			return 0
		if xpos >= areax - box["x"][kind][pos] and xpos <= areax - box["x"][kind][pos] + 140 and ypos + 20 >= areay - box["y"][kind][pos] and ypos + 20 <= areay - box["y"][kind][pos] + 20:
			return 0
	return 1


	
def calcHSV(rk, gk, bk):
	maxi = max(rk, gk, bk)
	mini = min(rk, gk, bk)

	if maxi == mini:
		# hue can be anything
		huek = 0
	else:
		if rk == maxi:
			huek = ((gk - bk) / (maxi - mini)) * 60.0
		elif gk == maxi:
			huek = (2 + (bk - rk) / (maxi - mini)) * 60.0
		elif bk == maxi:
			huek = (4 + (rk - gk) / (maxi - mini)) * 60.0
	if maxi == 0:
		satk = 0
	else:
		satk = (maxi - mini) / maxi
	valk = maxi

	if huek < 0:
		huek += 360

	return huek, satk, valk


def calcRGB(h, s, v):
	hi = h // 60
	f = h / 60 - hi
	p = v * (1 - s)
	q = v * (1 - f * s)
	t = v * (1 - (1 - f) * s)
	if hi == 0:
		r = v
		g = t
		b = p
	elif hi == 1:
		r = q
		g = v
		b = p
	elif hi == 2:
		r = p
		g = v
		b = t
	elif hi == 3:
		r = p
		g = q
		b = v
	elif hi == 4:
		r = t
		g = p
		b = v
	elif hi == 5:
		r = v
		g = p
		b = q
	return r, g, b


def makeblancolist():
	global blancolist
	blancolist = []
	for i in range(awidth * aheight):
		blancolist.append(0)
		
		
		
		
		
def checkneighbour(icoords, coordx, coordy):
	global currentset, drawset, colordir, alphadir, donelist
	
	cx = (coordx // lookupstep) * lookupstep
	cy = (coordy // lookupstep) * lookupstep
	acoords = int(cy * awidth + cx)

	for node in conndata["in"]["sel"][listpos]:
		if acoords in dset["sel"][node[1]]:
			return

	meanalpha = le = 0
	rk = imagelist[icoords][0]
	gk = imagelist[icoords][1]
	bk = imagelist[icoords][2]
	
	if toggle["h"].val or toggle["s"].val or toggle["v"].val:
		huek, satk, valk = calcHSV(rk, gk, bk)

	if toggle["r"].val:
		rdiff = abs(startr - rk)
		rl = rlim*slider["t"].val/100
		ralpha = 1 - (rdiff > rl)*(rdiff - rl)*floodvalue
		meanalpha += ralpha
		le += 1

	if toggle["g"].val:
		gdiff = abs(startg - gk)
		gl = glim*slider["t"].val/100
		galpha = 1 - (gdiff > gl)*(gdiff - gl)*floodvalue
		meanalpha += galpha
		le += 1

	if toggle["b"].val:
		bdiff = abs(startb - bk)
		bl = blim*slider["t"].val/100
		balpha = 1 - (bdiff > bl)*(bdiff - bl)*floodvalue
		meanalpha += balpha
		le += 1

	if toggle["h"].val:
		hdiff = abs(starth - huek)
		hl = hlim*slider["t"].val/100
		halpha = 1 - (hdiff > hl)*(hdiff - hl)*floodvalue
		meanalpha += halpha
		le += 1

	if toggle["s"].val:
		sdiff = abs(starts - satk)
		sl = slim*slider["t"].val/100
		salpha = 1 - (sdiff > sl)*(sdiff - sl)*floodvalue
		meanalpha += salpha
		le += 1

	if	toggle["v"].val:
		vdiff = abs(startv - valk)
		vl = vlim*slider["t"].val/100
		valpha = 1 - (vdiff > vl)*(vdiff - vl)*floodvalue
		meanalpha += valpha
		le += 1
	
	meanalpha /= le

	if meanalpha > 0:
		if lookupstep == 1:
			if acoords in comparesetlist[listpos] or (acoords + 1) in comparesetlist[listpos] or (acoords - 1) in comparesetlist[listpos] or (acoords - awidth) in comparesetlist[listpos] or (acoords - awidth + 1) in comparesetlist[listpos] or (acoords - awidth - 1) in comparesetlist[listpos] or (acoords + awidth) in comparesetlist[listpos] or (acoords + awidth - 1) in comparesetlist[listpos] or (acoords + awidth + 1) in comparesetlist[listpos]:
				currentset.add((coordx, coordy))
				drawset.add(acoords)
				colordir[acoords] = listpos
				alphadir[acoords] = meanalpha
		else:
			currentset.add((coordx, coordy))
			drawset.add(acoords)
			colordir[acoords] = listpos
			alphadir[acoords] = meanalpha


def dovenice(startx, starty):

	global imagelist, donelist, shapelist, drawset, pressurelist, currentset, width, height, awidth, aheight, shapecount, num
	global drawing, listpos, pixels, colordir, lookupstep, zoom, recalctrigger, comparesetlist, alphadir, clist, alist
	global startr, startg, startb, starth, starts, startv, rlim, glim, blim, hlim, slim, vlim
	global readyfordisplay, dset, conndata, base, undostatus, count, doneset, areaid
	
	start = time.time()
#	startx = 162
#	starty = 380


	drawset = set([])
	colordir = {}
	alphadir = {}
	donelist = blancolist[:]

	currentset = set([])
	oldcurrent = 0


	cx = (startx // lookupstep) * lookupstep
	cy = (starty // lookupstep) * lookupstep
	acoords = cy * awidth + cx
	drawset.add(acoords)
	colordir[acoords] = listpos
	alphadir[acoords] = 1.0
	
	startcoords = int((starty // zoom * width) + (startx // zoom) + 0.5)
	startr = imagelist[startcoords][0]
	startg = imagelist[startcoords][1]
	startb = imagelist[startcoords][2]
	if not(doall):
		colourpicker.val = (startr, startg, startb)
	starth, starts, startv = calcHSV(startr, startg, startb)


	rlim = 1.0-(0.8 + (slider["r"].val/500.0))
	glim = 1.0-(0.8 + (slider["g"].val/500.0))
	blim = 1.0-(0.8 + (slider["b"].val/500.0))

	hlim = 360-(360.0*(0.8 + (slider["h"].val/500.0)))
	slim = 1.0-(0.8 + (slider["s"].val/500.0))
	vlim = 1.0-(0.8 + (slider["v"].val/500.0))


	currentset.add((startx, starty))

	while len(currentset) > 0:

		if Window.QTest():
			evt, val = Window.QRead()
			if evt == Draw.WHEELDOWNMOUSE:
				slider["t"].val -= 10
			elif evt == Draw.WHEELUPMOUSE:
				slider["t"].val += 10
			elif evt == Draw.ESCKEY:
				for key in image.keys():
					del image[key]
				Draw.Exit()


		coordx, coordy = currentset.pop()
		cx = (coordx // lookupstep) * lookupstep
		cy = (coordy // lookupstep) * lookupstep
		acoords = int(cy * awidth + cx)
		coordxl = coordx - lookupstep
		if coordxl >= 0:
			if not(donelist[acoords - lookupstep]):
				coordyl = coordy
				coordsl = (int(coordyl / zoom + 0.5) * width) + (coordxl / zoom)
				checkneighbour(int(coordsl + 0.5), coordxl, coordyl)
		coordyt = coordy + lookupstep
		if coordyt < aheight:
			if not(donelist[acoords + lookupstep*awidth]):
				coordxt = coordx
				coordst = (int(coordyt / zoom + 0.5) * width) + (coordxt / zoom)
				checkneighbour(int(coordst + 0.5), coordxt, coordyt)
		coordxr = coordx + lookupstep
		if coordxr < awidth:
			if not(donelist[acoords + lookupstep]):
				coordyr = coordy
				coordsr = (int(coordyr / zoom + 0.5) * width) + (coordxr / zoom)
				checkneighbour(int(coordsr + 0.5), coordxr, coordyr)
		coordyb = coordy - lookupstep
		if coordyb >= 0:
			if not(donelist[acoords - lookupstep*awidth]):
				coordxb = coordx
				coordsb = (int(coordyb / zoom + 0.5) * width) + (coordxb / zoom)
				checkneighbour(int(coordsb + 0.5), coordxb, coordyb)

		donelist[acoords] = 1



	base["x"][listpos] = [startx]
	base["y"][listpos] = [starty]
	base["pos"][listpos] = 1
	base["radius"][listpos] = [1]

	base["tresh"][listpos] = slider["t"].val
	base["flood"][listpos] = slider["f"].val
	base["r"][listpos] = slider["r"].val
	base["g"][listpos] = slider["g"].val
	base["b"][listpos] = slider["b"].val
	base["h"][listpos] = slider["h"].val
	base["s"][listpos] = slider["s"].val
	base["v"][listpos] = slider["v"].val
	
	dset["sel"][listpos] = drawset.copy()
	if lookupstep == 2:
		comparesetlist[listpos] = drawset.copy()
	clist[listpos] = colordir.copy()
	alist[listpos] = alphadir.copy()
	readyfordisplay[listpos] = 1
	
	uncheckdownstream("sel", listpos)
	
	recalctrigger = 1
	undostatus = 0

	print "venice: ", time.time() - start
		

def docalc():
	global pixels, calclist, imagelist, drawset, drawing, selections, num, listpos, base, colordir, lookupstep
	global recalctrigger, undostatus, alphadir, preshapeset, base, precolordir, prealphadir
	
	start = time.time()

	

	if preshaping:
		preshapeset = set([])
		precolordir = {}
		prealphadir = {}


	if not(drawing):
		drawset = set([])
		colordir = {}
		alphadir = {}


	rlim = 1.0-(0.8 + (slider["r"].val/500.0))
	glim = 1.0-(0.8 + (slider["g"].val/500.0))
	blim = 1.0-(0.8 + (slider["b"].val/500.0))

	hlim = 360-(360.0*(0.8 + (slider["h"].val/500.0)))
	slim = 1.0-(0.8 + (slider["s"].val/500.0))
	vlim = 1.0-(0.8 + (slider["v"].val/500.0))

	r2, g2, b2 = colourpicker.val
	h2, s2, v2 = calcHSV(r2, g2, b2)
	
	for coords in calclist:
		x, y = coords
		if x % lookupstep == 1:
			continue
		if y % lookupstep == 1:
			continue

		icoords = int((y // zoom) * width + (x // zoom) + 0.5)
		r1 = imagelist[icoords][0]
		g1 = imagelist[icoords][1]
		b1 = imagelist[icoords][2]
		h1, s1, v1 = calcHSV(r1, g1, b1)
		
		rdiff = abs(r1 - r2)
		gdiff = abs(g1 - g2)
		bdiff = abs(b1 - b2)
		hdiff = abs(h1 - h2)
		sdiff = abs(s1 - s2)
		vdiff = abs(v1 - v2)
		
		if rdiff*toggle["r"].val <= rlim*slider["t"].val/100 and gdiff*toggle["g"].val <= glim*slider["t"].val/100 and bdiff*toggle["b"].val <= blim*slider["t"].val/100 and hdiff*toggle["h"].val <= hlim*slider["t"].val/100 and sdiff*toggle["s"].val <= slim*slider["t"].val/100 and vdiff*toggle["v"].val <= vlim*slider["t"].val/100:
			x = (x // lookupstep) * lookupstep
			y = (y // lookupstep) * lookupstep
			acoords = y * awidth + x
			if preshaping:
				preshapeset.add(acoords)
				precolordir[acoords] = listpos
				prealphadir[acoords] = 1.0
			else:
				drawset.add(acoords)
				colordir[acoords] = listpos
				alphadir[acoords] = 1.0


	if not(drawing) and not(preshaping):
		drawing = 1
		base["x"][listpos] = []
		base["y"][listpos] = []
		base["radius"][listpos] = []

	base["tresh"][listpos] = slider["t"].val
	base["flood"][listpos] = slider["f"].val
	base["r"][listpos] = slider["r"].val
	base["g"][listpos] = slider["g"].val
	base["b"][listpos] = slider["b"].val
	base["h"][listpos] = slider["h"].val
	base["s"][listpos] = slider["s"].val
	base["v"][listpos] = slider["v"].val

	if not(preshaping):
		dset["sel"][listpos] = drawset.copy()
		clist[listpos] = colordir.copy()
		alist[listpos] = alphadir.copy()
		readyfordisplay[listpos] = 1

		uncheckdownstream("sel", listpos)
		recalctrigger = 1	

	if not(undoing) and not(setundo) and not(scalemoving) and not(preshaping) and not(doall):
		base["x"][listpos].append(mousecoords[0])
		base["y"][listpos].append(mousecoords[1])
		base["radius"][listpos].append(radius)
		base["pos"][listpos] = len(base["x"][listpos])
		
	undostatus = 1
		
		
	print "calc: ", time.time() - start

	


def dofill():
	global drawing, drawset, calclist, base, listpos, colordir, lookupstep, recalctrigger
	global undostatus, alphadir, dset, alist, clist, base, preshapeset, precolordir, prealphadir

	start = time.time()


	if preshaping:
		preshapeset = set([])
		precolordir = {}
		prealphadir = {}

	if not(drawing):
		drawset = set([])
		colordir = {}
		alphadir = {}


	for coords in calclist:
		x, y = coords
		if x % lookupstep == 1:
			continue
		if y % lookupstep == 1:
			continue
		x = (x // lookupstep) * lookupstep
		y = (y // lookupstep) * lookupstep
		acoords = y * awidth + x
		if preshaping:
			preshapeset.add(acoords)
			precolordir[acoords] = listpos
			prealphadir[acoords] = 1.0
		else:
			drawset.add(acoords)
			colordir[acoords] = listpos
			alphadir[acoords] = 1.0
			
			
	if not(drawing) and not(preshaping):
		drawing = 1
		base["x"][listpos] = []
		base["y"][listpos] = []
		base["radius"][listpos] = []

	if not(preshaping):
		dset["sel"][listpos] = drawset.copy()
		clist[listpos] = colordir.copy()
		alist[listpos] = alphadir.copy()
		readyfordisplay[listpos] = 1

		uncheckdownstream("sel", listpos)
		recalctrigger = 1	
		
	if not(undoing) and not(setundo) and not(scalemoving) and not(preshaping) and not(doall):
		base["x"][listpos].append(mousecoords[0])
		base["y"][listpos].append(mousecoords[1])
		base["radius"][listpos].append(radius)
		base["pos"][listpos] = len(base["x"][listpos])

	undostatus = 1
		
		
		
	print "fill: ", time.time() - start