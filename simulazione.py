#-*- encoding: utf-8 -*-
import random
import math

class Unit(object):
    def __init__(self,forza,vita,tipo):
        self.forza = forza
        self.vita = vita
        self.tipo = tipo

    def __repr__(self):
        return "Unit(forza=%d,vita=%d,tipo='%s')" % (self.forza,self.vita,self.tipo)

class Esercito(object):
    def __init__(self,nome,units):
        self.nome = nome
        self.units = units

    @property
    def forza(self):
        return sum([u.forza for u in self.units])
    
    @property
    def vita(self):
        return sum([u.vita for u in self.units])

    @property
    def dadi(self):
        return int(math.floor(self.forza / 4))

    @property
    def attacco(self):
        return sum([attacco() for i in range(self.dadi)])

    @property
    def difesa(self):
        return sum([attacco() for i in range(self.dadi)])

    def __repr__(self):
        return "Esercito(nome=%s,units=%s)" % (self.nome,str(self.units))

    def subisci_danno(self,danno):
        # riordina casualmente la lista delle unità dell'esercito
        random.shuffle(self.units)
        # per ciascuna unità
        for unit in self.units:
            # prendi la vita della unità
            # se il danno residuo è superiore alla vita dell'unità
            if unit.vita <= danno:
                danno = danno - unit.vita
                # allora elimino l'unità
                unit.vita = 0
                print "AAARGH! unità uccisa",unit
                print "danno residuo",danno
            else:
                # altrimenti sottraggo alla vita dell'unità il danno residuo
                unit.vita = unit.vita - danno
                print "ARGH! unità ferita",unit
                danno = 0
                print "danno residuo",danno
                break
        self.units = [unit for unit in self.units if unit.vita>0]
        print self.units        
    
def vita_persa(valore):
    return valore

def dado():
    return random.randint(1,6)

def attacco():
    return vita_persa(dado())

def semiturno(esercito_a,esercito_b):
    attacco_a=esercito_a.attacco
    print "attacco esercito ",esercito_a.nome,attacco_a
    difesa_b=esercito_b.difesa
    print "difesa esercito ",esercito_b.nome,difesa_b
    danno_b=attacco_a - difesa_b
    if danno_b > 0:
        print "danno effettivo",danno_b
    else:
        danno_b=0
    return danno_b

def crea_fante():
    return Unit(forza=1,vita=2,tipo="fante")

def crea_arciere():
    return Unit(forza=2,vita=1,tipo="arciere")

def esempio():
    nomi = ["Artù",
            "Peppino",
            "Gundam",
            "Pitti"
    ]
    
    esercito = Esercito(nome=random.choice(nomi),
                        units=[crea_fante(),
                               crea_fante(),
                               crea_fante(),
                               crea_fante(),
                               crea_fante(),
                               crea_arciere(),
                               crea_arciere(),
                               crea_arciere(),
                               crea_arciere()])
    return esercito

def guerra():
    esercito_a = esempio()
    esercito_a.nome = "A "+esercito_a.nome
    esercito_b = esempio()
    esercito_b.nome = "B "+esercito_b.nome
    for i in range(10):
        print "********************"
        print "*  ROUND %02d       *" % i
        print "********************"
        danno_b=semiturno(esercito_a,esercito_b)
        danno_a=semiturno(esercito_b,esercito_a)
        esercito_a.subisci_danno(danno_a)
        esercito_b.subisci_danno(danno_b)
        if len(esercito_a.units)==0:
            print esercito_b.nome,"is THE WINNER"
            print esercito_a.nome,"you lose!"
            break
        if len(esercito_b.units)==0:
            print esercito_a.nome,"is THE WINNER"
            print esercito_b.nome,"you lose!"
            break
        if len(esercito_a.units)<4:
            print esercito_a.nome,"run away!!!"
            print esercito_b.nome,"is THE WINNER"
            break
        if len(esercito_b.units)<4:
            print esercito_b.nome,"run away!!!"
            print esercito_a.nome," is THE WINNER"
            break
