from argparse import ArgumentParser as Parser
from qqq_poetry.harmonic_mean import harmonic_mean
import turtle as t

FGCOLOR_DEFAULT = 'grey'
BGCOLOR_DEFAULT = 'on_white'
ATTRS_DEFAULT   = ['bold']
ANGLE_DEFAULT   = 59
DELAY_DEFAULT   = 10
SIZE_DEFAULT    = 128

def f(t1: t.Turtle, i: int, angle: int, delay: int, size: int) -> None:
	t1.color(t.colors[i % len(t.colors)])
	t1.width(i / 100 + 0.8)
	t1.fd(i)
	t1.lt(angle)
	if (i < size):
		t.ontimer(lambda: f(t1, i + 1, angle, delay, size), delay)

def main() -> None:
	parser = Parser(
          prog        = 'harmonic-mean',
          description = 'Print harmonic mean in color',
          epilog      = 'Text at bottom of help',
        )
	parser.add_argument('floats', metavar = 'n', type = float, nargs = '+', help = 'A float')
	parser.add_argument('--fgcolor', default = FGCOLOR_DEFAULT, help = 'Foreground color')
	parser.add_argument('--bgcolor', default = BGCOLOR_DEFAULT, help = 'Background color')
	parser.add_argument('--angle',   type = int, default = ANGLE_DEFAULT,   help = "Angle in degrees for turtle left turn")
	parser.add_argument('--delay',   type = int, default = DELAY_DEFAULT,   help = "Delay in milliseconds between screen updates")
	parser.add_argument('--size',    type = int, default = SIZE_DEFAULT,    help = "Size of each pinwheel")
	# parser.add_argument('--version', action = 'store_true',  help = 'Version number')
	__version_info__ = ('2013','03','14')
	__version__ = '-'.join(__version_info__)
	parser.add_argument('-V', '--version', action='version', version="%(prog)s ("+__version__+")")
	args = parser.parse_args()
	floats  = args.floats
	fgcolor = args.fgcolor
	bgcolor = args.bgcolor
	angle   = args.angle
	delay   = args.delay
	size    = args.size
	v       = 'v' # args.version
	for elt in dir(args):
		print(elt)
	print(floats, fgcolor, bgcolor, angle, delay, size, v)
	# if v:
	# 	print(getattr('version'))
	# 	exit()
	print(harmonic_mean([float(n) for n in floats]))
	t1 = t.Turtle()
	t2 = t.Turtle()
	t1.reset()
	t2.reset()
	t1.home()
	t1.ht()
	t2.ht()
	t.tracer(0)
	t.bgcolor('black')
	t.colors = ['pink', 'orange', 'olive drab', 'blue', 'yellow', 'violet', 'steel blue', 'red', 'cyan', 'gray', 'white']
	t1.setpos(size, size)
	t1.pd()
	f(t1, 0, angle, delay, size)
	# t1.pu()
	t2.setpos(-size, -size)
	t2.pd()
	f(t2, 0, angle, delay, size)
	# t2.pu()
	t.done()
