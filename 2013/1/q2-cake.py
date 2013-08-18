size1 = float(input('Cake 1 side length (cm): '))**2
cost1 = float(input('Cake 1 cost ($): '))
size2 = float(input('Cake 2 side length (cm): '))**2
cost2 = float(input('Cake 2 cost ($): '))
price1 = cost1/size1
price2 = cost2/size2
print('Cake 1 costs $%.2f per cm2 for %d cm2' % (price1, size1))
print('Cake 2 costs $%.2f per cm2 for %d cm2' % (price2, size2))

# dealing with imprecision
if abs(p1 - p2) < 1e-8:
    print('Get either!')
elif p1 - p2 > 1e-8:
    print('Get cake 2!')
elif p1 - p2 < -1e-8:
    print('Get cake 1!')
