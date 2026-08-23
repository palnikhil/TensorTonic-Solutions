import numpy as np

def dot_product(x: list, y: list) -> float:
    """Return the dot product of x and y."""
    # Write code here
    x_np=np.array(x)
    y_np=np.array(y)
    
    sum=0
    for i in range(len(x_np)):
        sum += x_np[i]*y_np[i]

    return float(sum)