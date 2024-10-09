from tkinter import Canvas
from vpython import sphere, vector, color, rate, norm, mag, cross, sqrt
import imageio

# for saving as gif
frames = []
canvas = Canvas()

G = 6.67e-11
m1 = 4e30
m2 = 2e30
rdist = 10e10
M = m1 + m2
radius1 = 7e9
radius2 = 3e9
vadd = 1

x1 = -(m2 / M) * rdist
x2 = (m1 / M) * rdist

star1 = sphere(
    pos=vector(x1, 0, 0), radius=radius1, color=color.yellow, make_trail=True
)
star2 = sphere(pos=vector(x2, 0, 0), radius=radius2, color=color.cyan, make_trail=True)

Rcom = (star1.pos * m1 + star2.pos * m2) / M
r = star2.pos - star1.pos

v1circle = sqrt(G * m2 * mag(star1.pos) / mag(r) ** 2)

star1.v = vector(0, vadd * v1circle, 0)
star1.m = m1 * star1.v
star2.m = -star1.m

mu = m1 + m2 / M
l = mag(cross(star1.pos, star1.m) + cross(star2.pos, star2.m))

t = 0
dt = 10000

while t < 1e8:
    rate(100)
    r = star2.pos - star1.pos
    F2 = -G * m1 * m2 * norm(r) / mag(r) ** 2
    star1.m -= F2 * dt
    star2.m += F2 * dt
    star1.pos += star1.m * dt / m1
    star2.pos += star2.m * dt / m2
    t += dt

#     img = canvas.getsnapshot()  # Captures a snapshot of the current scene
#     frames.append(img)

# imageio.mimsave('simulation.gif', frames, fps=30)