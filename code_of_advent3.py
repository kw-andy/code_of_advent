import itertools
from copy import copy


"""
première partie du jour 3 : effective
"""


def binary_counter():
    compteur = 0
    with open('code3.csv') as csv_file:
        liste_val = []
        for csv_line in csv_file:
            longueur = len(csv_line)
    while compteur < longueur-1:
        with open('code3.csv') as csv_file:
            liste_val = []
            max_val_liste = []
            min_val_liste = []
            for csv_line in csv_file:
                if compteur <= len(csv_line)-2:
                    liste_val.append(csv_line[compteur])
            max_val_liste.append(max(set(liste_val), key=liste_val.count))
            min_val_liste.append(min(set(liste_val), key=liste_val.count))
        print(max_val_liste,min_val_liste)    
   
        compteur += 1
    
#binary_counter()

"""
deuxième partie du jour 3: Non effective
"""

def binary_counter_with_sort():
    compteur = 0
    with open('code3.csv') as csv_file, \
         open('code3_outfile.csv', mode='w') as out_file:
        liste_val = []
        for csv_line in csv_file:
            list_finale = [x.split(',') for x in csv_line]

            merged = list(itertools.chain(*list_finale))  
            out_file.write(str(merged))

#binary_counter_with_sort()            

#125

def binary_counter_with_sort_amend():
    with open('code3.csv') as csv_file, \
        open('code3_outfile.csv', mode='w') as out_file:
        lignes = csv_file.readlines()
        diagnos = [entry.strip() for entry in lignes]
        print(diagnos)
        oxygen_diagnostics = copy(diagnos)
        for i in range(len(diagnos[0])):
            if len(oxygen_diagnostics) == 1:
                break
            all_entries_at_pos = [entry[i] for entry in oxygen_diagnostics]
            common_bit = '1' if all_entries_at_pos.count('1') >= len(oxygen_diagnostics)/2 \
                        else '0'
            oxygen_diagnostics = [entry for entry in oxygen_diagnostics 
                                            if entry[i]==common_bit]
            print(oxygen_diagnostics[0])                                
        oxygen_rating = int(oxygen_diagnostics[0], base=2)
        print('oxygen', oxygen_diagnostics[0], oxygen_rating)


        co2_diagnostics = copy(diagnos)
        for i in range(len(diagnos[0])):
            if len(co2_diagnostics) == 1:
                break
            all_entries_at_pos = [entry[i] for entry in co2_diagnostics]
            least_common_bit = '0' if all_entries_at_pos.count('1') >= len(co2_diagnostics)/2 \
                            else '1'
            co2_diagnostics = [entry for entry in co2_diagnostics
                                        if entry[i]==least_common_bit]
        co2_rating = int(co2_diagnostics[0], base=2)
        print('co2', co2_diagnostics[0], co2_rating)

binary_counter_with_sort_amend()        