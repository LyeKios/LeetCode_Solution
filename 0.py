dict = {'A':{'E': 1, 'F': 0, 'G': 1, 'H': 0}, 'B':{'E': 0, 'F': 1, 'G': 0, 'H': 1}, 'C':{'E': 1, 'F': 0, 'G': 0, 'H': 1}, 'D':{'E': 0, 'F': 0, 'G': 1, 'H': 0}}


def checkIfUnique(dict, Char):
    '''
    input: 
            dict: dictionary
            Char: char to check the times of apperance
    return: boolean
    '''
    i = 0
    for male in dict:
        if dict['{}'.format(male)]['{}'.format(Char)]:
            i += 1
            pair = male
    if i == 1:
        return pair
    return False

if __name__ == '__main__':
    # while(1):
    for male in dict:
        for female in dict['{}'.format(male)]:
            if checkIfUnique(dict, female):
                print([checkIfUnique(dict, female), female])
                dict['{}'.format(checkIfUnique(dict, female))]['{}'.format(female)] = dict['{}'.format(checkIfUnique(dict, female))]['{}'.format(female)] - 1
                print (dict)

    