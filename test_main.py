from main import *
import math

def test_simple_work():
	""" done. """
	assert simple_work_calc(10, 2, 2) == 36
	assert simple_work_calc(20, 3, 2) == 230
	assert simple_work_calc(30, 4, 2) == 650
	# added tests:
	assert simple_work_calc(10, 2, 3) == 20
	assert simple_work_calc(12, 9, 3) == 129
	assert simple_work_calc(1, 2, 1) == 1

def test_work():
	assert work_calc(10, 2, 2, lambda n: 1) == 15
	assert work_calc(20, 1, 2, lambda n: n*n) == 530
	assert work_calc(30, 3, 2, lambda n: n) == 300
	# added tests:
	assert work_calc(1, 1, 2, lambda n: 1) == 1
	assert work_calc(10000, 1, 2, lambda n: n) == 19995
	assert work_calc(1000, 1, 2, lambda n: 1) == 10


def test_compare_work():
	# curry work_calc to create multiple work
	# functions taht can be passed to compare_work

	# create work_fn1
	# create work_fn2

	# Case where root dominates
	work_fn1 = lambda n: work_calc(n, 8, 2, lambda n: n**2)
	# Balanced Case
	work_fn2 = lambda n: work_calc(n, 8, 4, lambda n: n**2)
	# Case where leaf dominates
	work_fn3 = lambda n: work_calc(n, 8, 6, lambda n: n**2)
	
	res = compare_work(work_fn1, work_fn2, work_fn3)

	print(res)

	
def test_compare_span():
	# O(1) runtime
	span_fn1 = lambda n: work_calc(n, 1, 2, lambda n: 1)
	# O(logn) runtime
	span_fn2 = lambda n: work_calc(n, 1, 2, lambda n: math.log(n))
	# O(n) runtime
	span_fn3 = lambda n: work_calc(n, 1, 2, lambda n: n)

	res = compare_span(span_fn1, span_fn2, span_fn3)

	print(res)
