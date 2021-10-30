import numpy as np
import matplotlib.pyplot as plt

def gaussian(x, mu, sig):
    return np.exp(-np.power(x - mu, 2.) / (2 * np.power(sig, 2.)))


def main():
    
    dist = [1,2,3,1.5, 8,9,10,15, 34, 35, 36]
    gaus_amount = 3 # Amount of gaussians fitted to the dist
    init_mu = 1 # initial 
    init_dev = 1
    init_offest = 1
    gaussians = []
    dist.sort()
    
    
    
    # --- Create Initial gaussians --- 
    for i in range(gaus_amount):
        
        if i == 0:
            mu = init_mu
        else:
            mu = gaussians[-1]["mu"] + init_offest
        
        gaussians.append(
            {
                "mu": mu,
                "std": init_dev
            }
        )
     
    
    
    # Draw - Estimate and update for each step
    for i in range(10):    
        
        
        smallest_x = dist[0] -2
        biggest_x = dist[-1] +2
    
        x = np.arange(smallest_x, biggest_x, (biggest_x - smallest_x) / 300)
    
        for gauss_dist in gaussians:
        
            plt.plot(x, gaussian(x, gauss_dist['mu'], gauss_dist['std']))
    
    
        plt.plot(dist,  np.zeros( len(dist)), 'ro')
    
    
    
        mu = []
        for gauss_dist in gaussians:
                mu.append(gauss_dist['mu'])
         
    

        plt.axis([ smallest_x, biggest_x, 0 , max(mu) ])
        plt.ylabel('some numbers')
        plt.show()
        
    
        for i, gauss in enumerate(gaussians):
        
            b = []
            for x in dist:
            
                b.append(( gaussian(x, gauss["mu"], gauss["std"])  ) / sum([gaussian(x, i_gauss["mu"], i_gauss["std"] )for i_gauss in gaussians]))
            # --- Update Step
            
            m_new = sum([b_i * x_i for b_i, x_i in zip(b, dist)])/sum( [b_j for b_j in b])
            
            gaussians[i]["mu"] = m_new
    
            
            
            
    
    
    
    
    # ---- plot ----
    
  
    
    
    
    
    pass


if __name__ == '__main__':
    main()