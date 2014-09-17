# Tim Jordan
# 9/16/14
# This program creates a sodium chloride lattice using vpython

import visual as vi
total=0
twototal=total+1
for i in range(3):
	twototal+=1
	for j in range(3):
		twototal+=1
		for k in range(3):
			total+=1
			if total%2==0:
				coloring = vi.color.blue
			else:
				coloring = vi.color.red
			vi.sphere(pos=[i,j,k], radius=0.3, color=coloring)
