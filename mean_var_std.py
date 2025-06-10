import numpy as np


def calculate(list):

    if len(list)!=9:
        raise ValueError("List must contain nine numbers.")
    matrix=np.array(list).reshape(3,3)
    m={
        'mean':[matrix.mean(axis=0).tolist(),
                matrix.mean(axis=1).tolist(),
                matrix.flatten().mean().item()],
        'variance':[matrix.var(axis=0).tolist(),
                    matrix.var(axis=1).tolist(),
                    matrix.flatten().var().item()],
        "standard deviation":[matrix.std(axis=0).tolist(),
                              matrix.std(axis=1).tolist(),
                              matrix.flatten().std().item()],
        "max":[matrix.max(axis=0).tolist(),
                    matrix.max(axis=1).tolist(),
                    matrix.flatten().max().item()],
        "min":[matrix.min(axis=0).tolist(),
                    matrix.min(axis=1).tolist(),
                    matrix.flatten().min().item()],
        'sum':[matrix.sum(axis=0).tolist(),
                    matrix.sum(axis=1).tolist(),
                    matrix.flatten().sum().item()]
        
        }
    return m



    

