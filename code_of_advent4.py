from itertools import zip_longest

#7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1

def grouper(iterable, n, *, incomplete='fill', fillvalue=None):
    args = [iter(iterable)] * n
    if incomplete == 'fill':
        return zip_longest(*args, fillvalue=fillvalue)
    if incomplete == 'strict':
        return zip(*args, strict=True)
    if incomplete == 'ignore':
        return zip(*args)
    else:
        raise ValueError('Expected fill, strict, or ignore')


def matrices():
    with open('code4.csv') as txt_file:
        lignes = (line.rstrip() for line in txt_file)
        lignes = list(ligne for ligne in lignes if ligne)
        values_to_search = lignes[0].split(",")
        intermediate_list = []
        for ligne in lignes[1:]:
            sublist = ligne.split(" ")
            sublist = list(filter(None, sublist))
            intermediate_list.append(list(sublist))
        dictio_sub = dict(enumerate(grouper(intermediate_list, 5), start=1))
        #print(dictio_sub)
        search_string = '23'
        for cle,valeurs in dictio_sub.items():
            for val in valeurs:
                #print(val)
                if search_string in val:
                    val.remove(search_string)
                    print(val)

"""
imaginons que vous ayez une liste avec des sous-listes de ce type

[[1,2,3],[4,5,6],[7,8,9],[10,11,12],[13,14,15],[16,17,18]]

{1: [1,2,3],[4,5,6],[7,8,9] 2:[10,11,12],[13,14,15],[16,17,18]}

dictio
"""



matrices()        