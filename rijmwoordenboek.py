vowels = {'@', 'A', 'a', 'E', 'I', 'e', '|', '}', 'o', 'O', 'i', 'y', 'u', 'L', 'K', 'M'}

def zoek_rijm(woord):
    accent = woord.rfind('\'')
    for i, letter in enumerate(woord[accent+1:]):
        if letter in vowels:
            return woord[accent+i+1:]
    return ""

def zoek_alliteratie(woord):
    accent = woord.rfind('\'')
    voorstuk = (woord[:accent])
    onset = ""
    for i, e in enumerate(voorstuk[::-1]):
        if e in vowels: break
        onset += e
    return onset[::-1]


def normaliseer(woord):
    return woord.replace('#e','é').replace('#a','á').replace('#o','ó').replace('`e','è').replace('`a','à').replace('`o','ò').replace('`u','ù').replace('`i','ì').replace('"a','ä').replace('"e','ë').replace('"i','ï').replace('"u','ü').replace(',c','ç').replace('"o','ö').replace('^a','â').replace('^e','ê').replace('^i','î').replace('^u','û').replace('^o','ô')

if __name__ == "__main__":

    rijmwoordenboek = {}

    with open("celex.txt","r") as celex:
        woordenlijst = celex.readlines()
        for regel in woordenlijst:
            woorden = regel.split('\\')
            rijm = zoek_rijm(woorden[2][:-1])
            lemma = normaliseer(woorden[0].split()[-1])
            if rijm == '': continue
            if rijm in rijmwoordenboek:
                rijmwoordenboek[rijm].add(lemma)
            else: rijmwoordenboek[rijm]={lemma}

    hulprijmwoordenboek = {}

    for rijm in rijmwoordenboek:
        for word in rijmwoordenboek[rijm]:
            hulprijmwoordenboek[word]=rijm

    rijmwoorden = lambda x: {w for w in rijmwoordenboek[hulprijmwoordenboek[x]] if not w == x}

    print (f"# coding=utf8\nrijmwoordenboek = {rijmwoordenboek}\nhulprijmwoordenboek={hulprijmwoordenboek}\nrijmwoorden = lambda x: {{w for w in rijmwoordenboek[hulprijmwoordenboek[x]] if not w == x}}", file=open('alliteratiewoord.py','w'))