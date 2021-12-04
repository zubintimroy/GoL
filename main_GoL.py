from GoL import GoL
import sys


if len(sys.argv) < 4:
    print('Incorrect number of arguments. Required format:')
    print('main.py Size of Lattice Dynamics Mode')
    print('Size of Lattice: Integer representing one side of the square lattice')
    print('Dynamics: r for random, g for glider and o for oscillator')
    print('Mode: a for animate m for taking measurements')
    quit()
else:
    filename = sys.argv[0]
    N  = int(sys.argv[1])
    dynamics = str(sys.argv[2])
    Mode = str(sys.argv[3])


if Mode == 'a':	
	model=GoL(N,str(dynamics))   
	model.display()
	
if Mode == 'm':
	model=GoL(N,str(dynamics))
	model.runmodel()    

if Mode == 'm' and dynamics == 'r':	
    for x in range(500): # need to include intialisation in this loop otherwise uses same intial conditions each time. 
        model=GoL(N,str(dynamics))
        model.runmodel()
	
