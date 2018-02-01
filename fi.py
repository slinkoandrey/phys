def fi():
    lst = [1,2]
    while lst[­1] < 40000:
        lst = lst + [lst[­1] + lst[­2]]
    chet = [x for x in lst if x%2 == 0]
    x2 = [x**2 for x in chet]
    x3 = [x**3 for x in chet]
    s2 = sum (x2)
    s3 = sum (x3)
    s = 1.0 * s3/s2
    print (s)

fi()
