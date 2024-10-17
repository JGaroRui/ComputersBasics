x0 = float(input("Tell me the initial position in m: "))
v0 = float(input("Ingresa la velocidad inicial in m/s: "))
a = float(input("Tell me the acceleration en m/s^2: "))
t = float(input("Tell me the time in s: "))

x = x0 + v0 * t + (a*t)/2

v = v0 + a * t

print("Final position: {x:.2f} m")
print("Final velocity: {v:.2f} m/s")
print("Acceleration: {a:.2f} m/s^2")