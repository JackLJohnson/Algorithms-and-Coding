# 2d Array Manipulation
'''
-90 degree flip
+90 degree flip
'''

import re
import os
import numpy as np

class arraymanip(object):
    """docstring for arraymanip."""
    global listorg , listnew
    listnew = []
    # listorg = [ [0, 1, 2, 3, 4, 5],
    #             [6, 7, 8, 9, 10, 11],
    #             [12, 13, 14, 15, 16, 17],
    #             [18, 19, 20, 21, 22, 23],
    #             [24, 25, 26, 27, 28, 29],
    #             [30, 31, 32, 33, 34, 35]]
    listorg = [[0, 1, 2,],
                [3, 4, 5],
                [6, 7, 8]]

    '''
    output:
    [[30, 24, 18, 12, 6, 0],
    [31, 25, 19, 13, 7, 1],
    [32, 26, 20, 14, 8, 2],
    [33, 27, 21, 15, 9, 3],
    [34, 28, 22, 16, 10, 4],
    [35, 29, 23, 17, 11, 5]]
    '''
    def __init__(self, arg):
        super(arraymanip, self).__init__()
        self.arg = arg
        if arg == int(1):
            print("Print the original list here", listorg)
            # flip the thing by 90 degree
            '''
            1st option is non in spcace, ie O(1) space complexity
            2nd option is(probably)
            '''
            #self.flip90(listorg)
            #self.flip90python(listorg)
            #print("transposed list -90 degree (ccw) \n",self.transpose_mirror(listorg))
            self.transpose_plus90(listorg)
            print("Original list", listorg)
            # To do column inverse, create another function for swaping
            print("+ 90 degree cw", self.swap_colwise(listorg))
        else:
            return(-1)

    def swap(self, originallist, i, j):
        originallist[i][j], originallist[j][i] = originallist[j][i], originallist[i][j]
        #return originallist[i][j]

    def transpose_mirror(self,originallist):
        length = len(originallist[1])
        for i in range(0, length):
            for j in range(i, length):
                self.swap(originallist,i,j)
        #print("check-1",originallist)
        return(originallist[::-1])

    def transpose_plus90(self,originallist):
        #print("original list", originallist)
        length = len(originallist[1])
        for i in range(0, length):
            for j in range(i, length):
                self.swap(originallist,i,j)
        print("Before reversed and after Tr", originallist)

    def swap_colwise(self, listitem):
        length = len(listitem)
        for i in range(0, length):
            for j in range(0, int(length/2)):
                listitem[i][j] , listitem[i][length-1-j] =  listitem[i][length-1-j], listitem[i][j]
        return listitem

    def flip90(self, originallist):
        rotated = []
        templist = []
        # Flip the array by 90
        mirrorred = originallist[::-1]
        print("mirrorred list", mirrorred)

        #Assuming it is a squared list
        length = len(originallist[1])

        # get each element of the list
        for val in range(0,length):
            templist = []
            for sublist in mirrorred:
                templist.append(sublist[val])
            rotated.append(templist)

        print("90 degree rotated", rotated)

    def flip90python(self, originallist):
        rotated = list(zip(*originallist[::-1]))
        print("90 degree rotated", rotated)


x = arraymanip(1)
