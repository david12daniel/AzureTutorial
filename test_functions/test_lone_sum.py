import lone_sum as test

assert 6 == test.lone_sum(1,2,3)

assert 20 == test.lone_sum(5,13,2)

assert 29 == test.lone_sum(14,13,2)

assert 45 == test.lone_sum(14,13,18)

assert 26 == test.lone_sum(8,16,2)

assert 27 == test.lone_sum(8,17,2)

assert 28 == test.lone_sum(8,18,2)

assert 29 == test.lone_sum(8,19,2)

assert 30 == test.lone_sum(8,20,2)

assert 20 == test.lone_sum(2,20,2)

assert 0 == test.lone_sum(2,2,2)

assert 20 == test.lone_sum(2,2,20)

assert 20 == test.lone_sum(20,2,2)