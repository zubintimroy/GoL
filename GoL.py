import numpy as np
import matplotlib.animation as animation
import matplotlib.pyplot as plt
import matplotlib.patches as patch
import math

class GoL:
    
    def __init__(self, N, conditions, sweeps = 10000, new_lattice = None):
                """
                Initialises square lattice of spins
                :param N: System size will be N x N
                :param conditions: either 'r' for random intial lattice, 'g' for glider intital conditions or 'o' for  an oscillator intial condition
                :param sweeps: number of sweeps completed in the simulation as an integer
                :param steps: There will be N x N steps in each sweep
                :param lattice: size * size system of cells which are either dead = 0 or alive = 1
                :param new_lattice: As updating in parralle need an identical lattice which will be used for updating 
                """
                self.N = N    
                self.conditions = conditions            
                self.lattice = self.make_lattice()
                if new_lattice is None:
                    new_lattice = np.zeros((self.N,self.N))
                self.new_lattice = new_lattice
                self.sweeps = sweeps
                self.steps = self.N * self.N
                    
    def make_lattice(self):
        """
        Creates intial lattice depending on conditions specificed (r,g,o)
        :return self.lattice: Intialized lattice
        """
        if self.conditions == 'r':
            lattice = np.random.randint(2,size = (self.N,self.N))                    
        if self.conditions == 'g':
            lattice = np.zeros((self.N,self.N))
            G = int((self.N/2))
            lattice[G,G] = 1
            lattice[G,G+1] = 1
            lattice [G,G-1] = 1
            lattice [G-1,G+1] = 1
            lattice[G-2,G] = 1
        if self.conditions == 'o':
            lattice = np.zeros((self.N,self.N))
            G = int((self.N/2))
            lattice[G,G] = 1
            lattice[G+1,G] = 1
            lattice[G+2,G] = 1
        return lattice
            
                
    def Neighbours_check(self,i,j):
            """
            Carries out a neigherest neighbour check for alive cells for 8 neighbours.
            :return nn: number of neighbours which are in the alive state.
            """
            nn = self.lattice[(i+1)%self.N,j]+ self.lattice[i,(j+1)%self.N]+self.lattice[(i-1)%self.N,j]+self.lattice[i,(j-1)%self.N]+self.lattice[(i+1)%self.N,(j+1)%self.N]+ self.lattice[(i-1)%self.N,(j+1)%self.N]+self.lattice[(i-1)%self.N,(j-1)%self.N]+self.lattice[(i+1)%self.N,(j-1)%self.N]
            
            return nn   
            
    def dead(self,i,j):
        """
        Update for if a cell is in a dead state
        """
        
        states = self.Neighbours_check(i,j)
                
        if states < 2 or states > 3:
            self.new_lattice[i,j] = 0
        else:
            self.new_lattice[i,j] = 1
            
    def alive(self,i,j):
        """
        Update for if a cell is in an alive state
        """  
        
        states = self.Neighbours_check(i,j)
                      
        if states == 3:
            self.new_lattice[i,j] = 1
        else:
            self.new_lattice[i,j] = 0
                
    def update(self):
        """
        Updates lattice using parrallel update.
        :return: self.lattice updated lattice 
        """
        for i in range(self.N):
            for j in range(self.N):
                self.lattice[i][j] = self.new_lattice[i][j]
                
    def active(self):
            """
            Calculates total number of alive cells in lattice
            :return A: integer of total number of alive cells 
            """
            A = 0.
            # Iterating over all alive cells in the lattice and adds them up
            for i in range(self.N):
                    for j in range(self.N):
                            A += self.lattice[i][j]
                
            return A
                       
    def animate(self,i):
        """
        Function that makes frames for animation.
        
        :return [frame]: plot of frame created in a list which is used in display
        """
        X,Y = np.meshgrid(range(self.N), range(self.N))
        mesh = plt.pcolormesh(X,Y, self.lattice, cmap = 'binary_r')
        
        for i in range(self.N):
            for j in range(self.N):
                if self.lattice[i,j] == 1: 
                    self.dead(i,j)
                else: 
                    self.alive(i,j)
     
        self.update() 
        #print(self.active())
               
        return mesh,
        
    def CoM(self):
        """
        Calculates CoM of a glider state but ignores boundary conditions
        :return positions: List of positions for every cell that is alive in the glider. 
        """
        positions = []
        
        for i in range(self.N):
            for j in range(self.N):
                if i > 1 and i < (self.N-1):
                    if self.lattice[i,j] ==1:
                        positions.append([i,j])

        return positions
        

                
    def display(self):
        """
        Allows user to visualize every sweep and how the Game of Life model changes over time using Funcanimation
        """
        fig = plt.figure(figsize=(10,10),dpi=80)
               
        fig.suptitle("The Game of Life",fontsize=20, fontweight = 'bold')
        a = animation.FuncAnimation(fig, self.animate, frames = self.sweeps, interval = 0.1, blit = True, repeat = False)
        
        #Visualises alive and dead cells of the system
        spinup = patch.Patch(color='white', label='Alive')
        spindown = patch.Patch(color='black', label='Dead')
        fig.legend(handles = [spinup, spindown], loc = 3)
        
        plt.show()
        
    def runmodel(self):
        """
        Runs model without animation and make measurements recording to an output file.
        
   
        :return A: Number of alive cells for a given timestep
        :return CoM: An array of positions for alive cells for a glider
        """
        
        
        # make empty list for alive cells
        active_sites = []
           
        for sweep in range(0, self.sweeps):
            
            # indicate percentage of completion
            if sweep % int(self.sweeps/10) == 0:
                print(str(sweep*100/self.sweeps) + '% of sweeps' + ' complete')
            
            for i in range(self.N):
                for j in range(self.N):
                    if self.lattice[i,j] == 1: 
                        self.dead(i,j)
                    else: 
                        self.alive(i,j)
                        
                        
            self.update()
            A = self.active()
            active_sites.append(A)
            pos = self.CoM()
            CoM = np.array(pos)
            #for sweep % int(self.sweeps/10) == 0:
            if self.conditions == 'g':
				
				if len(CoM) == 5:
					CoM_data = (np.mean(CoM, axis=0))
					file = open('Conditions = ' + str(self.conditions) + ' CoM, X.txt', 'a+')
					file.write('\n' + 't = ' + str(sweep) + ' ' + str(CoM_data[0]) + ' ' + str(CoM_data[1]))
					file.close()
            

            if sweep > 20 and self.conditions == 'r': 
                #Three points could all have the same number of alive cells but system still not reached equilibrium hence why used sum of last 10 points vs 10*last point
                if (active_sites[-1]*10) == np.sum(active_sites[-10:-1]):
                    file = open('Equilibrate Data.txt', 'a+')
                    file.write('\n' + 't = ' + str(sweep) + ' ' + str(A))
                    file.close()
                    #system goes to equilibrium so to save computional time stops recording once it hits this point
                    break
                    
            
            
            
            
            

              

"""
for x in range(500): # need to include intialisation in this loop otherwise uses same intial conditions each time. 
    model=GoL(50,'r')
    model.runmodel()

"""


                

