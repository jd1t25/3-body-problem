from vpython import sphere, vector, color, rate, norm, mag, cross, sqrt

G = 6.67e-11
Ms = 1e30
Rs = 190e7

r1 = 2e10
m1 = 1 * Ms
m2 = 0.8 * Ms
m3 = 0.5 * Ms
r2 = r1 * m1 / m2

s1 = sphere(pos=vector(r1, 0, 0), radius=Rs, color=color.red, make_trail=True)
s2 = sphere(pos=vector(-r2, 0, 0), radius=Rs, color=color.green, make_trail=True)
s3 = sphere(pos=vector(0, 0, r1), radius=Rs, color=color.cyan, make_trail=True)

v1 = sqrt(G * m2 * r1) / (r1 + r2)
s1.p = m1 * v1 * vector(0, 1, 0)
s2.p = -s1.p
s3.p = vector(0,0, 0)

t = 0
dt = 2000

while t < 5000 * dt:
    rate(100)
    r12 = s2.pos - s1.pos
    r23 = s3.pos - s2.pos
    r31 = s1.pos - s3.pos
    F21 = G * m1 * m2 * norm(r12) / mag(r12)**2
    F32 = G * m3 * m2 * norm(r23) / mag(r23)**2
    F13 = G * m1 * m3 * norm(r31) / mag(r31)**2

    s1.F = F21 - F13
    s2.F = -F21 + F32
    s3.F = -F32 + F13

    s1.p = s1.p + s1.F * dt
    s2.p = s2.p + s2.F * dt
    s3.p = s3.p + s3.F * dt

    s1.pos = s1.pos + s1.p * dt / m1
    s2.pos = s2.pos + s2.p * dt / m2
    s3.pos = s3.pos + s3.p * dt / m3

    t = t + dt