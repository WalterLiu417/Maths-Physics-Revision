import time, random, cython
print(help(cython))
with open("Python/Python39/Data/a_solution.txt", "r") as file:
    A_SOLUTION = [[int(b) for b in a.strip().split(",")] for a in file.readlines()]
    A_SOLUTION = A_SOLUTION[2:]


c = time.time()
CIRCLES = [[8,8,8,8]]
def unallowed_points(circle):
    no = []
    for x in range(abs(circle[3]-circle[0]), abs(circle[0]+circle[3])):
        if x < 1 or x > 16:
            continue
        for y in range(abs(circle[3]-circle[1]), abs(circle[1]+circle[3])):
            if y < 1 or y > 16:
                continue
            for z in range(abs(circle[2]-circle[0]), abs(circle[2]+circle[3])):
                if z < 1 or z > 16:
                    continue
                if threed_distance(x, y, z, circle[0], circle[1], circle[2]) < circle[3]:
                    no.append([x, y, z])
    return no
                


def threed_distance(m1x,m1y,m1z,m2x,m2y,m2z):
    return ((m2x-m1x)**2+(m2y-m1y)**2+(m2z-m1z)**2)**(1/2)


def display(stuff):
    for st in stuff:
        res = ""
        for ch in st:
            res += str(ch) + ","
        print(res[:-1])


def count(circles):
    nums = dict()
    for circle in circles:
        try:
            nums[circle[3]] += 1
        except:
            nums[circle[3]] = 1
    return nums


def volume(circles):
    vol = 0
    nums = count(circles)
    for key in nums:
        vol += (key**3)*nums[key]
    return vol


def check(circles):
    for i in range(len(circles)):
        for coords in circles[i]:
            if coords <= 0 or coords >= 17:
                print("non")
                print(circles[i], i)
        for j in range(i+1, len(circles)):
            if circles[i][:-1] == circles[j][:-1]:
                print("nonon")
                print(circles[i], circles[j], i, j)
            dist = threed_distance(circles[i][0], circles[i][1], circles[i][2], circles[j][0], circles[j][1], circles[j][2]) 
            if dist < max(circles[i][3], circles[j][3]):
                if dist != abs(circles[i][3] - circles[j][3]):
                    print("nononon")
                    print(circles[i], circles[j], i, j, dist)
            else:
                if dist < circles[i][3] + circles[j][3]:
                    print("nonoonononoo")
                    print(circles[i], circles[j], i, j, dist)
    return True


def all_unallowed_points():
    notallowed = []
    for circle in CIRCLES:
        for no in unallowed_points(circle):
            if no not in notallowed:
                notallowed.append(no)
    return notallowed





notallowed = all_unallowed_points()
two_candidates = []


for x in range(2, 16):
    for y in range(2, 16):
        for z in range(2, 16):
            if [x, y, z] not in notallowed:
                two_candidates.append([x,y,z])


standard = 18
maxlen = 0
two_solns = []
a = time.time()
for i in range(1000000):
    random.shuffle(two_candidates)
    if i == 9998:
        two_candidates.sort()
    elif i == 9999:
        two_candidates = [two_candidates[c] for c in range(len(two_candidates)) if c%2 == 0] + [two_candidates[c] for c in range(len(two_candidates)) if c%2 == 1]
    circles = [[8, 8, 8, 8]]
    for candidate in two_candidates:
        yes = True
        for circle in circles:
            if ((candidate[0]-circle[0])**2+(candidate[1]-circle[1])**2+(candidate[2]-circle[2])**2)**(1/2) < (2+circle[3]):
                yes = False
                break
        if yes:
            #print(str(candidate[0]) + "," + str(candidate[1]) + "," + str(candidate[2]) + "," + "2")
            circles.append([candidate[0], candidate[1], candidate[2], 2])
    circles = sorted(circles)
    if len(circles) >= standard and circles not in two_solns:
        two_solns.append(circles)
    if len(circles) > maxlen:
        maxlen = len(circles)
    if (i%100) == 0:
        print(i, time.time()-a)

print(time.time()-a, "for twos")
print(len(two_solns), "solutions")
maxvol = 0
maxc = []
counting = 0
b = time.time()
for two in two_solns:
    CIRCLES = two
    notallowed = all_unallowed_points()
    one_candidates = []


    for x in range(1, 17):
        for y in range(1, 17):
            for z in range(1, 17):
                if [x, y, z] not in notallowed:
                    one_candidates.append([x,y,z])

    localmaxvol = 0
    for i in range(1):
        random.shuffle(one_candidates)
        if i == 9998:
            one_candidates.sort()
        elif i == 9999:
            one_candidates = [one_candidates[c] for c in range(len(one_candidates)) if c%2 == 0] + [one_candidates[c] for c in range(len(one_candidates)) if c%2 == 1]
        circles = two
        for candidate in one_candidates:
            yes = True
            for circle in circles:
                if ((candidate[0]-circle[0])**2+(candidate[1]-circle[1])**2+(candidate[2]-circle[2])**2)**(1/2) < (1+circle[3]):
                    yes = False
                    break
            if yes:
                #print(str(candidate[0]) + "," + str(candidate[1]) + "," + str(candidate[2]) + "," + "2")
                circles.append([candidate[0], candidate[1], candidate[2], 1])
        circles = sorted(circles)
        if volume(circles) > maxvol:
            maxvol = volume(circles)
            maxc = circles
        if volume(circles) > localmaxvol:
            localmaxvol = volume(circles)
        if (i%1000) == 0:
            print(i, counting)
            if i != 0:
                print(time.time()-a)
            a = time.time()
    print(localmaxvol, counting, "local max")
    counting += 1
        

print(time.time()-b, "for ones")
display(maxc)
print(count(maxc))
print(maxvol)
print(time.time()-c, "overall")


print(check(A_SOLUTION))
print(count(A_SOLUTION))
print(volume(A_SOLUTION))