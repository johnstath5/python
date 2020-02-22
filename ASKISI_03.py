# ========	
# ASKISI-3
# ========	


#gia kathe proion sti lista exoume to onoma tin timi monadas , ton fpa kai tis monades :
proion1= [ ['gala', 1.5, 0.08 , 1],['mpiskota', 2.40, 0.12,2],['eisitirio', 10.0, 0.12,2],['aporypantiko', 7.50, 0.24,1] , ['sokolata', 2.80, 0.24,2] , ['psomi', 0.80, 0.08,2],['krasi', 9.50, 0.08,1]]
proion2= [ ['gala', 1.5, 0.08 , 3],['mpiskota', 2.40, 0.12,4],['eisitirio', 10.0, 0.12,4],['aporypantiko', 7.50, 0.24,2] , ['sokolata', 2.80, 0.24,3] , ['psomi', 0.80, 0.08,5],['krasi', 9.50, 0.08,1]]


def function1(mylist):
    s = 0.0;
    i =len(mylist);
    print("==============================")
    print("H lista periexei [%2d] stoixeia" %i)
    print("==============================")
    

    for row in range(i):
            r = (mylist[row][1] + (mylist[row][1] * mylist[row][2])) * mylist[row][3]
            s = s + r
            print("PROION %16s   TIMH %5.2f  FPA %.2f   POSOTHTA %2d AXIA %5.2f" %(mylist[row][0],mylist[row][1] , mylist[row][2] , mylist[row][3] , r) )


    print("SYNOLO : %62.2f" %(s))

    return s    



print( function1(proion1))
print( function1(proion2))
