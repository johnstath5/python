
#--------------------------------------------------
# H synarthsh epistrefei to triplasio enos arithmoy
# kai prosthetei 1
#--------------------------------------------------
def NewNumber(i):
	j = (3*i) + 1
	return j
#--------------------------------------------------
# H synarthsh ypologizei to athroisma ton psifion
# enos arithmou
#--------------------------------------------------
def DigitSum(i):
        ret = 0
        s = str(i)
        l = len(s)
        for j in range(l):   
                ret  = ret  + int(s[j])

        return ret

#----------------
# Kyrio Programma
#----------------
print("Dose tripsifio arithmo - 0 gia termatismo tou programmatos :")
i = int(input())

if (i==0):
    quit()


if (i >= 100 and i <= 999):

        print("Pliktrologisate :%4d" %i)
        i = NewNumber(i)
        s = DigitSum(i)
        k = 1
        
        print("%4d Neos Arithmos :[%4d] me athroisma psifion :[%4d]  (tha synexiso me 3 x %d + 1 = %4d)" %(k,i,s,s,(3*s)+1 ))
        
        while (s >= 10 ):
                k = k + 1
                i = NewNumber(s)
                s = DigitSum(i)

                if ( s >= 10 ):
                        print("%4d Neos Arithmos :[%4d] me athroisma psifion :[%4d]  (tha synexiso me 3 x %d + 1 = %4d)" %(k,i,s,s,(3*s)+1 ))
                else:
                        print("%4d Neos Arithmos :[%4d] me athroisma psifion :[%4d]  (monopsifios)" %(k,i,s))

        print("")
        print("")
        print("Katalixame sto %d meta apo %d epanalipseis" %(s,k))
        
else:
        print("Sfalma eisodou,  eprepe na dosete arithmo 100-999. To programma termatizetai")
