class Solution(object):
    def funtionreturn(self, test):
        res = []
        len_=len(test)-1
        for v in test:res.append(v)
        dict_ = {'0':0, '1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9}
        #return int(''.join(res))
        sum_=0
        while res:
            d=res.pop(0)
            #print(dict_[d])
            sum_+=dict_[d]*(10**len_)
            len_-=1
        return sum_
obj = Solution()
test="1230000"
print(obj.funtionreturn(test))
