

def aantal_vakjes (getallen:list):
    totaal = 0
    huidig_maximum = getallen[0]
    for i in range(len(getallen)):
        if getallen[i] < huidig_maximum:
            totaal += huidig_maximum - getallen[i]
        else:
            huidig_maximum = getallen[i]
    return totaal


