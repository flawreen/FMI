s = "abccabcababcc"
t = "abc"
i = []
poz = 0
try:
    poz = s.index(t)
    while True:
        i.append(poz)
        poz = s.index(t, poz+len(t))
except ValueError:
    pass

print(i)

# Cod Cezar
