#!/usr/bin/env python3
# by vdelaluz@enesmorelia.unam.mx
# GNU/GPL License

import numpy as np

data_list = np.arange(1,11,1)

for x in data_list:
    print("value: " + str(x))

x = "hola"
z = 0

try:
    z = int(x) + 1
    print("ok")
except:
    print("Error in sum of z.")

print(z)

#
# x = '1';
# x = "1";   '1''\0'
# for(int x=1; x<=10;x++){
#   printf("%i\n",x);
# }
#
#x = np.cos(x)

print(data_list)
