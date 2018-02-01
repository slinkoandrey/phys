def arab_to_rim(s):
    rim = ''
    while s >= 1000:
        rim = rim + 'M'
        s = s - 1000
    if s >= 900:
        rim = rim + 'CM'
        s = s - 900
    if s >= 500:
        rim = rim + 'D'
        s = s - 500
    if s >= 400:
        rim = rim + 'CD'
        s = s - 400
    while s >= 100:
        rim = rim + 'C'
        s = s - 100
    if s >= 90:
        rim = rim + 'XC'
        s = s - 90
    if s >= 50:
        rim = rim + 'L'
        s = s - 50
    if s >= 40:
        rim = rim + 'XL'
        s = s - 40
    while s >= 10:
        rim = rim + 'X'
        s = s - 10
    if s >= 9:
        rim = rim + 'IX'
        s = s - 9
    if s >= 5:
        rim = rim + 'V'
        s = s - 5
    if s >= 4:
        rim = rim + 'IV'
        s = s - 4
    while s > 0:
        rim = rim + 'I'
        s = s - 1
    return rim
    
print (arab_to_rim(3999))
print (arab_to_rim(2491))
print (arab_to_rim(1842))
print (arab_to_rim(981))
print (arab_to_rim(34))
