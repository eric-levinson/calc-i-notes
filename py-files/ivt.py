import numpy as np
import matplotlib.pyplot as plt


# intermediate value theorem
def ivt(func, interval, verbose=False):
    """
    func: f(x)
    interval: closed interval [a, b] (numpy array)
    """
    
    # evaluate function at each endpoint
    f_a = func(interval[0])
    f_b = func(interval[1])
    
    # display calculation results
    if verbose:
        print(f'\nf(a) = {f_a}')
        print(f'f(b) = {f_b}', end='\n\n')
        plot_func(func, interval)
    
    # return boolean indicating sign change
    return np.sign(f_a) != np.sign(f_b)


# plot f(x) over the closed interval
def plot_func(func, interval):
    x = np.arange(interval[0], interval[1], 0.01)
    y = func(x)
    fig, ax = plt.subplots()
    ax.plot(x, y)
    ax.set(xlabel='x', ylabel='f(x)',
           title='Intermediate Value Theorem')
    ax.grid()
    fig.savefig("ivt.png")
    plt.show()


if __name__ == '__main__':
    
    # ivt returns True if there is a sign change
    print('solution exists') if ivt(
        lambda x: -x**2+3*x,
        np.array([2, 5]),
        verbose=True
    ) else print('no solution')
