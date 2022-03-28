#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#16777215 é o número decimal do hexadecimal mais alto em cores:
#rgb(255, 255, 255) em hexadecimal é “FFFFFF” que é 16777215 quando convertido em número decimal.
#Basicamente, eles estão escolhendo um número aleatório entre 000000-FFFFFF

import random
import math

quantity = int(input("Quantas cores você quer gerar?"))
colors = []

for i in range(quantity):
    color = math.ceil(random.random() * 16777215)
    color = hex(color)
    color = str(color)
    color = color.replace("0x", "")
    color = "#" + color
    colors.append(color)

colors = list(map(lambda color: color.upper(), colors))
print("As suas cores são: {}".format(", ".join(colors)))

