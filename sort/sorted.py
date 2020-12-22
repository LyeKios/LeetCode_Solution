people = [ [ 5, 0 ], [ 7, 0 ], [ 5, 2 ], [ 6, 1 ], [ 4, 4 ], [ 7, 1 ] ]

people = sorted(people, key = (lambda x:(x[0],-x[1])))