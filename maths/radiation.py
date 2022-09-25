from .helperfuncs import *
import random


def save_a_b_particles_question(filepath):
    num_alphas = random.randint(2,5)
    num_betas = random.randint(2,5)
    y = [-2*num_alphas+num_betas,-4*num_alphas-num_betas]
    q = f"A unstable nucleus X decays into the stable nucleus Y by emitting {num_alphas} " + r"$\alpha$" + f" particles and {num_betas} " + r"$\beta^-$" + " particles.\n"
    aob = random.randint(0,1)
    if aob:
        q += "How many fewer neutrons does Y contain than X?"
    else:
        q += "How many fewer protons does Y contain than X?"
    save_text(q, filepath)
    if aob: return -y[1], q
    else: return -y[0], q

def save_half_life_question(filepath):
    hl = random.randint(2,5)
    hls = random.randint(2,6)
    tp = hl*hls
    q = f"A sample initially contains the same number of a radioactive isotope X and a stable isotope Y.\n X has a half-life of {hl} years and decays in a single stage to Y.\n After {tp} years, the ratio of X:Y is 1:a. Find a."
    save_text(q, filepath)
    return (2-2**(-hls))/(2**(-hls)), q
    
if __name__ == "__main__":
    print(save_half_life_question("foo.png"))