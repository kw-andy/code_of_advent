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
    
binary_counter()

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