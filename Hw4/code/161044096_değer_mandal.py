d = input('enter first int')
m = input('enter second int')

num1 = int(d)
num2 = int(m)

def fonk(firstnum, secondnum):
    topstepfirst = firstnum % 10
    topstepsecond = secondnum % 10
    counter = 0
    while topstepfirst == topstepsecond:
          firstnum = firstnum - topstepfirst
          firstnum  = firstnum / 10
          secondnum = secondnum - topstepsecond
          secondnum = secondnum  / 10
          counter = counter + 1
          topstepfirst = firstnum  % 10
          topstepsecond  = secondnum % 10
    print (counter)
    return(counter)



print ('the number of matching digits')
fonk (num1, num2)




input('the end')
