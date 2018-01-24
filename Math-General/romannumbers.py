def inttoroman(num):
    ints=[1000,900,500,400,100,90,50,40,10,9,5,4,1] #Need to break it into these 13 values
    roman=['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
    result=[]
    for i in range(len(ints)):
        count=int(num/ints[i])
        result.append(roman[i]*count)
        num -= ints[i]*count
    return ''.join(result)

def romantoint(roman):
    romanval={'M':1000, 'D':100, 'C':100, 'L':50, 'X':10, 'V':5, 'I':1}
    romannew=list(roman)
    sum_=0
    for i in range(len(romannew)):
        value=romanval[romannew[i]]
        if i+1 <len(romannew) and romanval[romannew[i+1]]>value: # If next numeral in larger then we have to negate from this value
            sum_-=value
        else:sum_+=value
    return sum_

print(inttoroman(4589))
print(romantoint('XCIX'))
