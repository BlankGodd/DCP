#!/usr/bin/python3
# Author: @AgbaD | @Agba_dr3

from itertools import combinations
a = [10, 3, 17, 15]
k = 17


def check(a, k):
	c = combinations(a, 2)
	for i in c:
		if sum(i) == k:
			return True
	return False

