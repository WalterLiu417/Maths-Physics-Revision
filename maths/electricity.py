from fractions import Fraction
from .helperfuncs import *
import random

def save_simple_power_question(filepath):
    pwr = random.randint(1,10)*10
    eff = random.randint(1,99)
    obj = random.choice(ELECTRICS)
    t = random.randint(1,10)
    q = f"A {obj} converts electrical energy at a rate of {pwr} W.\nThe {obj} has an efficiency of {eff}%.\n"
    uow = random.randint(0,1)
    if not uow:
        q += f"How much energy is wasted by the {obj} in {t} minutes?"
        ans = round_sfs(pwr*(100-eff)*t*60/100, 2)
    else:
        q += f"How much energy is used by the {obj} in {t} minutes?"
        ans = round_sfs(pwr*(eff)*t*60/100, 2)
    q += " Answer to 2 s.f."
    save_text(q, filepath)
    return ans, q

def save_power_ke_question(filepath):
    volt = random.randint(1,10)*100
    eff = random.randint(1,10)*10
    cur = abs(random.choice(EASY_INTS_NO_ZERO))
    resist = volt / cur
    tp = random.randint(1,10)
    vcr = random.randint(0,2)
    if vcr == 0:
        q = f"The current and the resistance are {cur} A and {resist} ohms in "
    elif vcr == 1:
        q = f"The potential difference and the resistance are {volt} V and {resist} ohms in "
    else:
        q = f"The potential difference and the current are {volt} V and {cur} A in "
    obj = random.choice(OBJECTS)
    q += f"the motor of an electric {obj}.\nThe efficiency of the motor is {eff}%.\n The {obj} accelerates from rest for {tp} s.\nWhat is the kinetic energy of the {obj} at the end of {tp} s?"
    ans = volt*cur*eff*tp/100
    save_text(q, filepath)
    return ans, q

def save_wire_wastes_energy_question(filepath):
    length = abs(random.choice(EASY_INTS_NO_ZERO)*1000)
    cross_section = abs(random.choice(EASY_INTS_NO_ZERO)/10000)
    resistivity = abs(random.choice(EASY_SCIENTIFIC_INTS_NO_ZERO))
    resistivity_pwr = -random.choice([6,7,8])
    volt = abs(random.choice(EASY_SQUARES_NO_ZERO)*100)
    resistance = resistivity*length*(10**resistivity_pwr)/cross_section
    current = abs(random.choice(EASY_SQUARES_NO_ZERO))
    inp_pwr = volt*current
    ans = (current**2)*resistance
    q = f"A {random.choice(METALS)} wire of length {length/1000} km and cross-sectional area of {cross_section*10000} $cm^2$ has resistivity {resistivity}*$10^" + "{" + f"{resistivity_pwr}" + "}$ ohm-meters.\n"
    q += f"The input voltage to the wire is {volt} V.\n What is the energy wasted if the input power is {inp_pwr} W?"
    save_text(q, filepath)
    return ans, q

def save_transformer_pwr_question(filepath):
    final_current = abs(random.choice(EASY_SQUARES_NO_ZERO))
    mulfactor = abs(random.choice(EASY_INTS_NO_ZERO))
    rand_int = abs(random.choice(EASY_INTS_NO_ZERO))
    resist = abs(random.choice(EASY_INTS_NO_ZERO))*(10**abs(random.choice(VERY_EASY_INTS_NO_ZERO)))
    pwr = resist*final_current**2
    q = f"An ideal 100% efficient transformer is connected to a resistor by cables of resistance {resist} ohms.\nThe current in the primary coil is {final_current*mulfactor} A.\nThere are {rand_int} coils in the primary coil and {rand_int*mulfactor} coils in the secondary coil.\nWhat is the power dissipated in the cables?"
    save_text(q,filepath)
    return pwr, q

def save_speaker_phase_question(filepath):
    triple = random.choice(PYTHS)
    dist = triple[2] - triple[1]
    speed_sound = random.randint(30,36)*10
    phase_diff = Fraction(speed_sound,360).denominator*random.randint(1,5)*dist
    frequency = Fraction(phase_diff*speed_sound,(dist*360))
    q = f"Two small loudspeakers are placed side by side {triple[0]} m apart.\n"
    q += f"They are connected to the same signal generator so they emit sound of frequency {frequency} Hz in phase with each other.\n"
    q += f"The sounds both reach a microphone placed {triple[1]} m directly in front of one of the two loudspeakers.\n"
    q += f"The speed of sound in this medium is {speed_sound} m/s.\n"
    wop = random.randint(0,1)
    if wop == 0:
        q += "What is the wavelength of the sound waves?\n"
        ans = speed_sound/frequency
    else:
        q += "What is the phase difference in degrees?\n"
        ans = phase_diff
    save_text(q, filepath)
    return ans, q



    
if __name__ == "__main__":
    print(save_speaker_phase_question("foo.png"))
