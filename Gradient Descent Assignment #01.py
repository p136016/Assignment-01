import matplotlib.pyplot as plt
import numpy as np
area = [1, 4, 6, 6, 8, 10, 14, 18, 24, 30, 41, 47, 49, 53,
        58, 66, 68, 82, 86, 96]
price=[100, 400, 600, 600, 800, 1000, 1400, 1800, 2400, 3000, 4100,
       4700, 4900, 5300, 5800, 6600, 6800, 8200, 8600, 9600]

area.sort()
price.sort()
m = len(area)
theta0 = (0)
theta1 = (0)
alpha = 0.000009

def costfunction(theta0, theta1, m, area, price):
    newtheta0 = 0
    newtheta1 = 0
    for i in range(m):
        newtheta0 += (( theta0 + theta1 *area[i]) - price[i])
        newtheta1 += (((theta0 + theta1 * area[i])- price[i])* area[i]) 
    return (newtheta0/m, newtheta1/m)
    
def gradient_descent():
    old_theta0 = 0
    old_theta1 = 0
    list_theta_0 = []
    list_theta_1 = []
    counter = 0
    arraycounter=[]

    while True:
        counter+=1
        arraycounter.append(counter)

        error_in_f1,error_in_f2 = costfunction(old_theta0,old_theta1, m, area,price)
        old_theta0 = old_theta0 - (alpha/m) * (error_in_f1)
        old_theta1 = old_theta1 - (alpha/m) * (error_in_f2)
        list_theta_0.append(old_theta0)
        list_theta_1.append(old_theta1)
        
        error_in_f1 = abs(error_in_f1)
        error_in_f2 = abs(error_in_f2)
        print(error_in_f1, "  ",error_in_f2)
        if error_in_f1<=0.01 or error_in_f2 <=0.01:
            list_theta_0 = np.asarray(list_theta_0)
            list_theta_1 = np.asarray(list_theta_1)
            plt.plot(arraycounter, list_theta_0)
            plt.ylabel('Area')
            plt.plot(arraycounter, list_theta_1)
            plt.xlabel('Price')
            break
    return

gradient_descent()