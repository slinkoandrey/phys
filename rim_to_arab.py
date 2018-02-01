a = {'M':1000, 'D':500, 'C':100, 'L':50, 'X':10, 'V':5, 'I':1}

def rim_to_arab(rim):
    i = 0
    ar = 0
    while i < len(rim):
        if i == len(rim) - 1:
          ar += a[rim[i]]
          i += 1
        else:
            if a[rim[i]] < a[rim[i+1]]:
                ar += a[rim[i+1]] - a[rim[i]]
                i += 2
            else:
              ar += a[rim[i]]
              i += 1
    return(ar)
  
print (rim_to_arab('CMXLIII'))
print (rim_to_arab('MMMCCCXXXIIII'))
print (rim_to_arab('MCMLXVII'))
print (rim_to_arab('LXXXIV'))
print (rim_to_arab('MDCDLXLVIV'))
