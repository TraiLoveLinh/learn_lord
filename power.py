def calc_used_bottle_of_power(army, bottle_of_power):
    n = len(army)
    count = 0
    for i in range(1, n):
        if army[i] <= army[i - 1]:
            use_amount = (army[i - 1] - army[i] + bottle_of_power) // bottle_of_power
            army[i] = use_amount * bottle_of_power
            count += use_amount
    return count


def main():
    army = [9, 8, 7, 6, 5, 10]
    bottle_size = 2
    print(calc_used_bottle_of_power(army, bottle_size))


main()