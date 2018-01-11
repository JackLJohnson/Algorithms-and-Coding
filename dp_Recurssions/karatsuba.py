'''
Karatsuba Multiplication with recurssion
'''
class karatsuba(object):
    """docstring for karatsuba."""
    def __init__(self):
        super(karatsuba, self).__init__()

    def karatsubamain(self,n1,n2):
        if len(str(n1))==1 or len(str(n2))==1:
            return n1*n2
        else:
            mid = int(max(len(str(n1)), len(str(n2)))/2)
            #a,b,c,d = int(str(n1)[:mid]),int(str(n1)[mid:]),int(str(n2)[:mid]),int(str(n2)[mid:])
            a,b,c,d = n1//10**(mid), n1%10**(mid), n2//10**(mid), n2%10**(mid)
            a_c = self.karatsubamain(a,c)
            b_d = self.karatsubamain(b,d)
            ad_plus_bc = self.karatsubamain(a+b,c+d)-a_c-b_d
            prodf = (a_c*10**(2*mid)) + (ad_plus_bc*(10**(mid)))+ b_d
            return prodf

obj = karatsuba()
nums1 = 3141592653589793238462643383279502884197169399375105820974944592
nums2 = 2718281828459045235360287471352662497757247093699959574966967627
#nums1=31415926
#nums2=27182818
print(nums1*nums2)
print(obj.karatsubamain(nums1, nums2))
