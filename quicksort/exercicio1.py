#!/usr/bin/env python
# -*- coding: utf-8 -*-


# Considerando o seguinte vetor:
#    [25, 48, 37, 12, 57, 86, 33, 92]
#  
# 1) Realize a ordenação do vetor em ordem crescente.


# Instance a list
quick = [25, 48, 37, 12, 57, 86, 33, 92]
# Make a function with a argument
def quickSort(arr):
    # Instance a list with a number less that pivot
    number_less = []
    # Instance a pivot list
    pivot_list = []
    # Instance a list with a number more that pivot
    number_more = []
    # If length list less that one return pivot else 
    if len(arr) <= 1:
        return arr
    else:
    	#pass
        # Instance a pivot with a list empty
        pivot = []
        # Write a for in i to argument arr, the arr contain the amount of list and traveling all elements of list
        for i in arr:
            # If less pivot
            if i < pivot:
                # Add i to list number_less
                number_less.append(i)
            elif i > pivot:
                # Add i to list number_more
                number_more.append(i)
            else:
                # Else no one, add in pivot_list
                pivot_list.append(i)
        # After travel all list return all elements in order number_less, pivot_list and numer_more        
        return number_less + pivot_list + number_more


quick = quickSort(quick)
# Show
print quick