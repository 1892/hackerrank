def all_elements_are_factor_of_x(sett, x):
    return all([x % i == 0 for i in sett])

def x_is_factor_of_all_elements(sett, x):
    return all([i % x == 0 for i in sett ])

if __name__ == "__main__":
    n,m = input().strip().split(' ')
    n,m = [int(n),int(m)]
    a = [int(a_temp) for a_temp in input().strip().split(' ')]
    b = [int(b_temp) for b_temp in input().strip().split(' ')]

    t_a = list(a)
    t_b = list(b)
    t_a.extend(t_b)

    r = [i for i in range(min(t_a), max(t_a)+1) if all_elements_are_factor_of_x(a, i) and x_is_factor_of_all_elements(b, i)]

    print(len(r))