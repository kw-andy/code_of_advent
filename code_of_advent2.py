"""
premiere partie: J'ai fait un tri via une feuille excel, pour une 
séparation sur les trois valeurs, forward, down et up, pour 
obtenir le résultat. Effective
"""

"""
deuxième partie du deuxième jour: Effective
"""

def forward():
    with open('code2.csv') as csv_input:
        horiz_pos = 0
        aim = 0
        depth = 0
        final_depth = 0
        for line_val in csv_input:
            values = line_val.split()
            if values[0] == 'forward':
                if aim == 0:
                    horiz_pos += int(values[1])
                else:
                    horiz_pos += int(values[1])
                    depth = aim*int(values[1])
                    final_depth += depth
            elif values[0] == 'up':
                aim -= int(values[1])
            elif values[0] == 'down':
                aim += int(values[1])
        print("final result ",horiz_pos,final_depth,horiz_pos*final_depth)        

forward()