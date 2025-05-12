from random import choice
def gene():
    return choice(['D','r'])
def genotype(alelle):
    alelle = (alelle)
    iter = 0
    type = ''
    while iter != alelle:
        type = type + gene()
        iter = iter + 1
    return type

def genoset(gene, alelle):
    gene = abs(gene)
    character = ''
    iter = 0
    while iter != gene:
        character = character + f'\n{genotype(alelle)}'
        iter = iter + 1
    return character
    
genes = int(input('Genotype Count: '))
alelle = int(input('Alelle Count: '))
print(genoset(genes, alelle))