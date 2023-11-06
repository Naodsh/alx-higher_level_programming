#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    pad_tuple_a = tuple_a + (0, 0)
    pad_tuple_b = tuple_b + (0, 0)

    sum_t = (pad_tuple_a[0] + pad_tuple_b[0], pad_tuple_a[1] + pad_tuple_b[1])

    return sum_t
