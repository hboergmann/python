import turtle as tu

lines = 500_000

with open("04_1_million_digits_of_pi.txt", "r") as f:
  pi = f.read()

tu.mode('logo')
tu.tracer(False)
tu.screensize(8000, 8000, 'black')
tu.colormode(255)


for n in range(lines):
  color = int(n/(lines/255))
  tu.pencolor(255, 255-color, color)
  zahl = int(pi[n])
  rotation = zahl * 36
  tu.setheading(rotation)
  tu.forward(1)
  if n % 10_000 == 0:
    tu.update()

tu.getcanvas().postscript(file='PI_Picture.ps')
tu.done()
