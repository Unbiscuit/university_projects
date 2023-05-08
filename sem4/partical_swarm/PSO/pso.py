import numpy as np
 
def f(x1:float, x2:float) -> float:
        "Objective function"
        return -12*x2 + 4*x1**2 + 4*x2**2 - 4*x1*x2

class pso:

    def __init__(self, particles: int, w: float, c1:float, c2:float) -> None:
        self.particles = particles
        self.w = w
        self.c1 = c1
        self.c2 = c2

        self.X = np.random.rand(2, particles) * 5
        self.V = np.random.randn(2, particles) * 0.1

        self.pbest = self.X
        self.pbest_obj = f(self.X[0], self.X[1])
        self.gbest = self.pbest[:, self.pbest_obj.argmin()]
        self.gbest_obj = self.pbest_obj.min()     

    def update(self) -> None:
        "Method to do one iteration of particle swarm optimization"
        r1, r2 = np.random.rand(2)
        self.V = self.w * self.V + self.c1*r1*(self.pbest - self.X) + self.c2*r2*(self.gbest.reshape(-1,1)-self.X)
        self.X = self.X + self.V
        obj = f(self.X[0], self.X[1])
        self.pbest[:, (self.pbest_obj >= obj)] = self.X[:, (self.pbest_obj >= obj)]
        self.pbest_obj = np.array([self.pbest_obj, obj]).min(axis=0)
        self.gbest = self.pbest[:, self.pbest_obj.argmin()]
        self.gbest_obj = self.pbest_obj.min()

    def get_particals(self) -> np.ndarray:
         return self.X

    def get_velocity(self) -> np.ndarray:
         return self.V
    
    def get_pbest(self) -> np.ndarray:
         return self.pbest
    
    def get_gbest(self) -> np.ndarray:
         return self.gbest
    
    def get_gbest_obj(self) -> np.ndarray:
         return self.gbest_obj
    

 