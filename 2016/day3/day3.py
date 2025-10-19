with open("input.txt") as f:
    lines = f.readlines()

total = 0

triangles = []
t1, t2, t3 = [], [], []

for line in lines:
    a, b, c = map(int, line.split())

    t1.append(a)
    t2.append(b)
    t3.append(c)

    if len(t1) >= 3:
        triangles.append(t1)
        triangles.append(t2)
        triangles.append(t3)
        t1 = []
        t2 = []
        t3 = []

for triangle in triangles:
    a, b, c = triangle
    if a + b > c and a + c > b and b + c > a:
        total += 1

print(total)
