d=input('enter an integer')

def digit_multiplier(number):
        result=0
        m=int(d)
        h=int(d)
        res=1
        count=0
        while(m!=0):
                w=m%10
                m=m-w
                m=m/10
                count=count+1
        for i in range(0, count):
                a=int(h)%10
                h=int(h)/10
                if (a!=0):
                        res=a*res
        print(res)
        return result

digit_multiplier(d)

if __name__ == '__main__':
        try:
            assert True
            assert digit_multiplier(123405) == 120
            assert digit_multiplier(999) == 729
            assert digit_multiplier(1000) == 1
            assert digit_multiplier(1111) == 1

        except AssertionError:
                print('An error')

input('end')
