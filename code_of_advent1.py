
"""
première partie du jour 1: effective
"""

def depth_measurement():
    with open("code1.csv") as file_csv:
        val_liste = []
        for val_incsv in file_csv:
            val_liste.append(int(val_incsv))

    val_before = 0
    val_current = 0
    count_increased = 0
    count_decreased = 0
    for values in val_liste:
        if val_current == 0:
            print(int(values), "  (N/A - no previous measurement)")
            val_current = int(values)
        else:
            val_current = int(values)    
            if (val_current > val_before):
                print(val_current," (increased)")
                count_increased += 1 
            elif val_current < val_before:
                print(val_current," (decreased)")
                count_decreased += 1
        val_before = val_current
    print("count increase & count decrease: ", count_increased, count_decreased)       

depth_measurement()

#199,200,208,210,200,207,240,269,260,263



"""
deuxième partie du jour 1: effective
"""


def depth_measurement_2():
    with open("code1.csv") as file_csv:
        val_liste = []
        for val_incsv in file_csv:
            val_liste.append(int(val_incsv))

    val_before = 0
    val_current = 0
    count_increased = 0
    count_decreased = 0
    count_no_change = 0
    for counter,values in enumerate(val_liste):
        if counter +1 < len(val_liste)-1:
            if val_current == 0:
                num1 = int(val_liste[counter])
                num2 = int(val_liste[counter+1])
                num3 = int(val_liste[counter+2])
                print(num1 + num2 + num3, "  (N/A - no previous measurement)")
                val_current = num1 + num2 + num3
            else:
                num1 = int(val_liste[counter])
                num2 = int(val_liste[counter+1])
                num3 = int(val_liste[counter+2])
                val_current = num1 + num2 + num3    
                if (val_current > val_before):
                    print(val_current," (increased)")
                    count_increased += 1 
                elif val_current < val_before:
                    print(val_current," (decreased)")
                    count_decreased += 1
                elif val_current == val_before:
                    print(val_current," (no change)")
                    count_no_change += 1    
            val_before = val_current
    print("count increase , count decrease, no change : ", count_increased, count_decreased,count_no_change)



            


#depth_measurement_2()            