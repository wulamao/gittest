"""
Does the function f have monotonicity?
f = -∑(θ_ij/2pi)(d_ij/d0)log((θ_ij/2pi)(d_ij/d0))
where θ_ij is the included angle of s_i and s_(i+1)

"""

import math
import random

# constant
d0 = 10;
theta0 = 2*math.pi;

# data structure
class Coordinate:
    def __init__(self, d, theta):
        self.d = d
        self.theta = theta

# calculate the 'entropy' function
def calc_f(set_temp):
    global d0,theta0
    arg = Coordinate(0,0)
    my_sum = 0

    for arg in set_temp:
        temp = (arg.d/d0)*(arg.theta/theta0)
        # consider that the relative angle equals zero
        if arg.theta == 0:
            temp = 0
        else:
            temp = -temp*math.log2(temp)
        my_sum += temp
    return my_sum


if __name__ == "__main__":

    # generate data set && initial
    big_set = []
    res_set = []
    flag = 0
    flag_old = 0
    theta_old = 0
    theta = 0
    cnt = 0

    # the number of sensors selected
    times = 1000

    for i in range(times):
        # generate d & theta
        d = random.uniform(0,10)
        # d = 10

        # calculate the relative angle
        if i>0:
            theta = random.uniform(0,2*math.pi)
            theta += theta_old
            if theta >= 2*math.pi:
                theta -= 2*math.pi

        theta_old = theta
        #print('random data [d:theta]: ',d,theta)

        big_set.append(Coordinate(d,theta))

        # calculate result
        res = calc_f(big_set)
        #
        res_set.append(res)
        # res_set.append(random.uniform(-1,1))

        # determine order: if they are the same value, pass it
        # cnt record the times of different data
        # cnt = 1, flag & flag_old is available
        # cnt = 2, flag & flag_old is comparable

        # print(res_set[i],res_set[i-1])
        if i>1:
            if res_set[i] != res_set[i-1] :
                cnt += 1
                if res_set[i] > res_set[i-1]:
                    flag = 1
                elif res_set[i] < res_set[i-1]:
                    flag = -1
            else:
                pass

        if cnt>2 :
            if flag != flag_old:
                print(" Nonmonotonic !!!!!!!!!!!!!!!!!!!!!!!")
                break

        # record latest flag
        flag_old = flag

        print('', i,res_set[i],flag,flag_old,cnt)


