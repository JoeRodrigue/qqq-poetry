from argparse import ArgumentParser as Parser
from random   import random
from time     import sleep
from qqq_poetry.harmonic_mean import harmonic_mean
import turtle as t

FGCOLOR_DEFAULT = 'grey'
BGCOLOR_DEFAULT = 'on_white'
ATTRS_DEFAULT   = ['bold']
ANGLE_DEFAULT   = 59
DELAY_DEFAULT   = 60

def f(i: int, angle: int, delay: int) -> None:
	t.color(t.colors[i % len(t.colors)])
	t.width(i / 100 + 0.8)
	t.fd(i)
	t.lt(angle)
	if (i < 256):
		t.ontimer(lambda: f(i + 1, angle, delay), delay)

def main() -> None:
	parser = Parser(
          prog        = 'harmonic-mean',
          description = 'Print harmonic mean in color',
          epilog      = 'Text at bottom of help',
        )
	parser.add_argument('floats', metavar = 'n', type = float, nargs = '+', help = 'A float')
	parser.add_argument('--fgcolor', default = FGCOLOR_DEFAULT, help = 'Foreground color')
	parser.add_argument('--bgcolor', default = BGCOLOR_DEFAULT, help = 'Background color')
	parser.add_argument('--angle',   type = int, default = ANGLE_DEFAULT,   help = "Angle in radians for turtle left turn")
	parser.add_argument('--delay',   type = int, default = DELAY_DEFAULT,   help = "Delay in milliseconds between screen updates")
	args = parser.parse_args()
	floats  = args.floats
	fgcolor = args.fgcolor
	bgcolor = args.bgcolor
	angle   = args.angle
	delay   = args.delay
	print(floats, fgcolor, bgcolor)
	print(harmonic_mean([float(n) for n in floats]))
	# t.screensize(700, 600)
	t.ht()
	t.tracer(0)
	t.bgcolor('black')
	t.colors = ['pink', 'orange', 'olive drab', 'blue', 'yellow', 'violet', 'steel blue', 'red', 'cyan', 'gray', 'white']
	f(0, angle, delay)
	t.done()
