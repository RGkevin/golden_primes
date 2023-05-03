import sympy


def primes_in_range_mapper(num_range):
    start = num_range[0] + 1
    end = num_range[1] + 1
    primes_in_range = list(sympy.primerange(start, end))
    p_in_range = len(primes_in_range)

    print('primes_in_range_mapper num_range {} primerange({}, <{}) primes: {}'
          .format(num_range, start, end, p_in_range))

    n_nums_in_range = num_range[-1] - num_range[0]
    return [num_range[1], n_nums_in_range, [num_range[0] + 1, num_range[-1]], p_in_range]