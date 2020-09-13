def all_divisors(number):
    nb_list = []
    i = 2
    while i <= number:
        if number%i == 0:
            nb_list.append(str(i))
            number //= i
            i = 2
            continue
        i += 1
    return nb_list


if __name__ == '__main__':
    # print(all_divisors(100))
    print(' '.join(all_divisors(288)))
    