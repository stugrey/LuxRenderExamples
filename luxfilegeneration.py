import math

w = open('materials-geometry.lxo', 'w')

materials = [['glass'],
             ['glossy'],
             ['matte'],
             ['mirror'],
             ['roughglass']
             ]

carpaints = ['ford f8','polaris silber','opel titan','bmw339',
             '2k acrylack','white','blue','blue matte']

metals = ['amorphous carbon','silver','gold','copper','aluminium']

for cp in carpaints:
    materials.append(['carpaint', '\"string name\" \"' + cp + '\"'],)

for m in metals:
    materials.append(['metal', '\"string name\" \"' + m + '\"'],)

models = ['Shape \"plymesh\" \"string filename\" [\"luxball3-outer.ply\"]',
          'Shape \"plymesh\" \"string filename\" [\"luxball3-inner.ply\"]']

length = len(materials)
side = int(math.ceil(math.sqrt(length)))
print side

x = 2.0
y = 2.0

for mat in materials:
    w.write("AttributeBegin\n")
    w.write("Translate " + str(x) + " " + str(y) + " 0.0\n")
    w.write("Scale 20 20 20\n")
    w.write("Material \"" + mat[0] + "\"\n")
    if len(mat) > 1:
        w.write(mat[1] + "\n")
    for mod in models:
        w.write(mod + "\n")
    w.write("AttributeEnd\n\n")
    if x < 12.0:
        x += 3.0
    else:
        x = 2.0
        y += 3.0
