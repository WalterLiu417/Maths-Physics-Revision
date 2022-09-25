from .helperfuncs import *
from fractions import Fraction
import random

def save_two_distances_and_times_question(filepath):
    u = random.randint(1,10)
    a = random.randint(1,10)
    q = f"A {random.choice(OBJECTS)} is travelling at a constant speed of u m/s when it experiences a constant acceleration of a m/s^2.\n"
    t1 = random.randint(2,4)
    t2 = random.randint(5,8)
    q += f"At time t1 = {t1} seconds it has travelled {u*t1 + 0.5*a*(t1**2)} meters.\n"
    q += f"At time t2 = {t2} seconds it has travelled {u*t2 + 0.5*a*(t2**2)} meters.\n Find u + a."
    save_text(q, filepath)
    return u + a, q

def save_collision_question(filepath):
    m1 = abs(random.choice(EASY_INTS_NO_ZERO))
    m2 = abs(random.choice(EASY_INTS_NO_ZERO))
    obj = random.choice(OBJECTS)
    u1, u2, v1 = random_x(EASY_INTS,3)
    v2 = (1/m2)*(m1*u1+m2*u2-m1*v1)
    t_col = abs(random.choice(EASY_INTS_NO_ZERO)/10)
    vels = [u1, u2, v1, v2]
    unknown_vel = random.randint(0,5)
    q = f"A {obj} P "
    if unknown_vel == 4:
        q += "of mass x kg "
    else:
        q += f"of mass {m1} kg "
    q += "is travelling at "
    if unknown_vel == 0:
        q += "x m/s and "
    else:
        q += f"{u1} m/s and "
    q += f"another {obj} Q "
    if unknown_vel == 5:
        q += "of mass x kg "
    else:
        q += f"of mass {m2} kg "
    q += "is travelling at "
    if unknown_vel == 1:
        q += "x m/s.\n"
    else:
        q += f"{u2} m/s.\n"
    q += f"They collide. The time of impact is {t_col} seconds.\nAfter the collision P is moving at "
    if unknown_vel == 2:
        q += "x m/s and Q is moving at "
    else:
        q += f"{v1} m/s and Q is moving at "
    if unknown_vel == 3:
        q += "x m/s.\n"
    else:
        q += f"{v2} m/s.\n"
    xof = random.randint(0,1)
    if xof == 0:
        q += f"Find x"
        au = vels + [m1, m2]
        ans = au[unknown_vel]
    else:
        q += f"Find the magnitude of the average force on {random.choice(['P','Q'])}.\n"
        ans = abs(m1*(v1-u1)/t_col)
    save_text(q, filepath)
    
    return ans, q
    
def save_obj_upward_obj_released_question(filepath):
    u1 = abs(random.choice(EASY_INTS_NO_ZERO)*10)
    delay_time = random.randint(1,5)
    hit_time = 2*u1/easy_g
    fall_time = hit_time - delay_time
    height = (1/2)*easy_g*(fall_time**2)
    udh = random.randint(0,2)
    unknowns = [u1, delay_time, height]
    if udh == 0:
        q = "An object is projected upwards at x m/s from the ground.\n"
    else:
        q = f"An object is projected upwards at {u1} m/s from the ground.\n"
    if udh == 1:
        q += "x seconds later a second object is released from "
    else:
        q += f"{delay_time} seconds later a second object is released from "
    if udh == 2:
        q += "a height of x meters.\n"
    else:
        q += f"a height of {height} meters.\n"
    q += "Both objects hit the ground at the same time. Find x.\nTake g = 10 $m/s^2$"
    save_text(q, filepath)
    return unknowns[udh], q

def save_fake_slope_fma_question(filepath):
    u1, u2 = sorted(random_randints((0,20), 2))
    mass = random.randint(1,10)
    deltake = (1/2)*(mass)*(u2**2 - u1**2)
    distance = random.choice(prime_factors(deltake))
    netf = deltake / distance
    rand_const_force = netf + random.randint(1,mass*10)
    
    q = f"A {random.choice(OBJECTS)} of mass {mass} kg is being pulled up a smooth slope by a constant force with magnitude {rand_const_force} N for a distance {distance} m.\n"
    q += f"The object has initial speed {u1} m/s, final speed {u2} m/s, and the acceleration is constant.\n"
    q += "What is the component of weight acting down the slope in newtons?"
    save_text(q, filepath)
    return rand_const_force - netf, q

def save_collision_vreversed_distance_question(filepath):
    u = abs(random.choice(EASY_SQUARES_NO_ZERO))
    if u%2 == 0: v = -abs(random.choice(EASY_EVEN_SQUARES_NO_ZERO))
    else: v = -abs(random.choice(EASY_ODD_SQUARES_NO_ZERO))
    taspfs = prime_factors(abs(v**2 + u**2))
    taspfs.remove(2)
    accel = random.choice(taspfs)
    s = abs(v**2 + u**2) / (2*accel)
    unknowns = [u, abs(v-u), accel, s]
    unknown = random.randint(0,3)
    obj = random.choice(OBJECTS)
    ans = unknowns[unknown]
    if unknown == 2:
        q = f"A {obj} is hit by a force that is causing a constant acceleration of x $m/s^2$.\n"
    else:
        q = f"A {obj} is hit by a force that is causing a constant acceleration of {accel} $m/s^2$.\n"
    if unknown == 1:
        q += f"As a result of the impact, the {obj} returns back along its original path having undergone a velocity change of magnitude x $m/s$.\n"
    else:
        q += f"As a result of the impact, the {obj} returns back along its original path having undergone a velocity change of {abs(v-u)} $m/s$.\n"
    if unknown == 0:
        q += f"The inital velocity of the {obj} is x m/s.\n"
        ans = max(v,u)
    else:
        q += f"The initial velocity of the {obj} is {u} m/s.\n"
    if unknown == 3:
        q += f"The total distance travelled by the {obj} is x m.\n"
    else:
        q += f"The total distance travelled by the {obj} is {s} m.\n"
    if unknown != 0:
        q += "Find x."
    else:
        q += "Find x. You may assume that the magnitude of the initial velocity is greater than the final velocity."
    print(q)
    save_text(q, filepath)
    return ans, q

def save_graph_ke_question(filepath):
    mass = abs(random.choice(EASY_INTS_NO_ZERO))
    endtime = abs(random.choice(EASY_INTS_NO_ZERO))
    pwr = abs(random.choice(VERY_EASY_INTS))
    const = abs(random.choice(EASY_INTS_NO_ZERO))
    vel = Fraction(1,(pwr+1))*(endtime**(pwr+1))*const/mass
    obj = random.choice(OBJECTS)
    q = f"A {obj} with mass {mass} kg is at rest at time = 0s.\nA resultant force acts on the object in a constant direction.\n"
    q += f"The graph of force against time varies as ${const}*x^{pwr}$.\n"
    vok = random.randint(0,1)
    if vok:
        q += f"Find the velocity of the {obj} at time = {endtime} s as a fraction in m/s."
        ans = vel
    else:
        q += f"Find the kinetic energy of the {obj} at time = {endtime} s as a fraction in joules."
        ans = Fraction(1,2)*mass*vel**2
    print(q)
    save_text(q, filepath)
    return ans, q

def save_ke_force_question(filepath):
    mass = random.randint(1,10)
    v1 = random.randint(0,3)
    accel = mass*random.randint(1,3)
    time = random.randint(1,4)
    v2 = v1 + accel*time
    ke1 = Fraction(1,2)*mass*(v1**2)
    ke2 = Fraction(1,2)*mass*(v2**2)
    q = f"The kinetic energy of a {random.choice(OBJECTS)}, travelling in a straight line, increases from {ke1}J to {ke2}J in {time} seconds due to a constant resultant force.\n"
    maf = random.randint(0,2)
    if maf == 0:
        q += f"The mass of the object is x kg. The resultant force is {accel*mass}N. Find x."
        ans = mass
    else:
        q += f"The mass of the object is {mass} kg."
    if maf == 1:
        q += f"Find the acceleration in $m/s^2$."
        ans = accel
    elif maf == 2:
        q += f"Find the resultant force in newtons."
        ans = accel*mass
    save_text(q, filepath)
    return ans, q


if __name__ == "__main__":
    print(save_collision_question("foo.png"))