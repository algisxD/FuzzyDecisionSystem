import shapely
from shapely.geometry import LineString, Point

#######################################
# CONSTANTS
#######################################

letiniuLiguSk = 0
rukymoLaikotarpisM = 15
zmogausAmzius = 32

#######################################
# Trikampis ir trapecija
#######################################

class Trapecija:
    def __init__(self, a, b, c, d):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
    
    def f_reiksme(self, x):
        funkcija = 0
        if x < self.a:
            funkcija = 0
        elif x >= self.a and x < self.b:
            funkcija = (x - self.a) / (self.b - self.a)
        elif self.b <= x and x < self.c:
            funkcija = 1
        elif self.c <= x and x < self.d:
            funkcija = (self.d - x) / (self.d - self.c)
        else:
            funkcija = 0
        return funkcija

class Trikampis:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def f_reiksme(self, x):
        funkcija = 0
        if x < self.a:
            funkcija = 0
        elif x >= self.a and x < self.b:
            funkcija = (x - self.a) / (self.b - self.a)
        elif self.b <= x and x < self.c:
            funkcija = (self.c - x) / (self.c - self.b)
        else:
            funkcija = 0
        return funkcija

#######################################
# Ivesties kintamieji
#######################################

class letinesLigos:
    def __init__(self, liguSkaicius):
        self.mazas = Trapecija(0, 0, 3, 7)
        self.vidutinis = Trikampis(4, 8, 12)
        self.didelis = Trapecija(8, 12, 15, 15)
        self.liguSkaicius = liguSkaicius
        self.mazasReiksme = self.rast(self.mazas)
        self.vidutinisReiksme = self.rast(self.vidutinis) 
        self.didelisReiksme = self.rast(self.didelis) 
    
    def rast(self, figura):
        return figura.f_reiksme(self.liguSkaicius)

    def spausdint(self):
        print("Letiniu ligu skaicius")
        print("Mazas: ", self.mazasReiksme, "Vidutinis: ", self.vidutinisReiksme, "Didelis: ", self.didelisReiksme)
        print()

class rukymoLaikotarpis:
    def __init__(self, rukymoLaikotarpisM):
        self.trumpas = Trapecija(0, 0, 5, 10)
        self.vidutinis = Trapecija(5, 10, 20, 30)
        self.ilgas = Trapecija(20, 30, 50, 50)
        self.rukymoLaikotarpisM = rukymoLaikotarpisM
        self.trumpasReiksme = self.rast(self.trumpas)
        self.vidutinisReiksme = self.rast(self.vidutinis) 
        self.ilgasReiksme = self.rast(self.ilgas) 
    
    def rast(self, figura):
        return figura.f_reiksme(self.rukymoLaikotarpisM)

    def spausdint(self):
        print("Rukimo laikotarpis")
        print("Trumpas:", self.trumpasReiksme, "Vidutinis: ", self.vidutinisReiksme, "Ilgas: ", self.ilgasReiksme)
        print()

class amzius:
    def __init__(self, zmogausAmzius):
        self.jaunas = Trapecija(0, 0, 30, 45)
        self.vidutinis = Trapecija(35, 45, 55, 65)
        self.senas = Trapecija(55, 65, 100, 100)
        self.zmogausAmzius = zmogausAmzius
        self.jaunasReiksme = self.rast(self.jaunas)
        self.vidutinisReiksme = self.rast(self.vidutinis) 
        self.senasReiksme = self.rast(self.senas) 
    
    def rast(self, figura):
        return figura.f_reiksme(self.zmogausAmzius)

    def spausdint(self):
        print("Amzius")
        print("Jaunas: ", self.jaunasReiksme, "Vidutinio amziaus: ", self.vidutinisReiksme, "Senas: ",  self.senasReiksme)
        print()

#######################################
# Metodai
#######################################

def mean(skaicius1, skaicius2):
    return (skaicius1 + skaicius2) / 2

def MOM(visuMax, trumpoMax, vidutinioMax, ilgoMax):
    pirmasTaskas = 0
    antrasTaskas = 0

    if visuMax == trumpoMax and visuMax == 1:
        pirmasTaskas = 7
        antrasTaskas = 9
    elif visuMax == trumpoMax and visuMax < 1:
        pirmasTaskas = 7
        antrasTaskas = 14 - 5 * visuMax

    if visuMax == vidutinioMax and visuMax == 1:
        pirmasTaskas = 14
        antrasTaskas = 16
    elif visuMax == vidutinioMax and visuMax < 1:
        pirmasTaskas = (visuMax + 9 / 5) * 5
        antrasTaskas = (9 - visuMax) * 2

    if visuMax == ilgoMax and visuMax == 1:
        pirmasTaskas = 18
        antrasTaskas = 22
    elif visuMax == ilgoMax and visuMax < 1:
        pirmasTaskas = (visuMax + 8) * 2
        antrasTaskas = 22
    
    return mean(pirmasTaskas, antrasTaskas)

#surandu kur susikerta viena einanti zemyn, o kita aukstyn sienos, nes ten bus zemiausi taskai, pagal susikirtimo tasko x reiksme surandu y reiksme
def SOM(visuMax, trumpoMax, vidutinioMax, ilgoMax):
    zemiausiasMaxTaskas = 0

    A = (9,1)
    B = (14,0)
    trumpaTrapecijosDesineKrastine = LineString([A, B]) 

    A = (9,0)
    B = (14,1)
    vidutineTrapecijosKaireKrastine = LineString([A, B])

    A = (16,1)
    B = (18,0)
    vidutineTrapecijosDesineKrastine = LineString([A, B])

    A = (16,0)
    B = (18,1)
    ilgaTrapecijosKaireKrastine = LineString([A, B])

    if visuMax == trumpoMax:
        susikirtimoTaskas = trumpaTrapecijosDesineKrastine.intersection(vidutineTrapecijosKaireKrastine)
        return susikirtimoTaskas.x

    elif visuMax == vidutinioMax:
        susikirtimoTaskas = vidutineTrapecijosDesineKrastine.intersection(ilgaTrapecijosKaireKrastine)
        zemiausiasMaxTaskas = susikirtimoTaskas.y
        susikirtimoTaskas = trumpaTrapecijosDesineKrastine.intersection(vidutineTrapecijosKaireKrastine)
        zemiausiasMaxTaskas2 = susikirtimoTaskas.y
        if(zemiausiasMaxTaskas > zemiausiasMaxTaskas2):
            return zemiausiasMaxTaskas2.x
        else:
            return zemiausiasMaxTaskas.x

    elif visuMax == ilgoMax:
        susikirtimoTaskas = vidutineTrapecijosDesineKrastine.intersection(ilgaTrapecijosKaireKrastine)
        return susikirtimoTaskas.x


#######################################
# 
#######################################

let = letinesLigos(letiniuLiguSk)
ruk = rukymoLaikotarpis(rukymoLaikotarpisM)
amz = amzius(zmogausAmzius)
ruk.spausdint()
let.spausdint()
amz.spausdint()

taisykliuTrumpuReiksmiuList = []
taisykliuVidutiniuReiksmiuList = []
taisykliuIlguReiksmiuList = []

#######################################
# Taisykliu reiksmiu skaiciavimas
#######################################
taisykliuTrumpuReiksmiuList.append(min(amz.jaunasReiksme, ruk.trumpasReiksme))
taisykliuTrumpuReiksmiuList.append(min(amz.jaunasReiksme, ruk.trumpasReiksme))
taisykliuTrumpuReiksmiuList.append(min(amz.jaunasReiksme, ruk.trumpasReiksme))
taisykliuTrumpuReiksmiuList.append(min(amz.jaunasReiksme, let.mazasReiksme))
taisykliuIlguReiksmiuList.append(max(amz.senasReiksme, let.vidutinisReiksme))
taisykliuVidutiniuReiksmiuList.append(max(amz.senasReiksme, let.vidutinisReiksme))
taisykliuVidutiniuReiksmiuList.append(amz.senasReiksme)
taisykliuVidutiniuReiksmiuList.append(min(amz.jaunasReiksme, ruk.ilgasReiksme))
taisykliuVidutiniuReiksmiuList.append(min(let.vidutinisReiksme, ruk.vidutinisReiksme))
taisykliuTrumpuReiksmiuList.append(max(amz.jaunasReiksme, ruk.trumpasReiksme))
taisykliuIlguReiksmiuList.append(min(amz.vidutinisReiksme, let.didelisReiksme))
taisykliuVidutiniuReiksmiuList.append(min(amz.jaunasReiksme, let.didelisReiksme))
taisykliuIlguReiksmiuList.append(max(amz.senasReiksme, let.didelisReiksme))


#######################################
# Agregacija
#######################################
trumpoMax = max(taisykliuTrumpuReiksmiuList)
vidutinioMax = max(taisykliuVidutiniuReiksmiuList)
ilgoMax = max(taisykliuIlguReiksmiuList)
visuMax = max(trumpoMax, vidutinioMax, ilgoMax)

#print("Trumpa: ", taisykliuTrumpuReiksmiuList)
#print("Vidutine: ", taisykliuVidutiniuReiksmiuList)
#print("Ilga: ", taisykliuIlguReiksmiuList)
#print("Maksimumas: ", visuMax)
#######################################
# 
#######################################
    

sirgimoDienuSkaiciusMOM = MOM(visuMax, trumpoMax, vidutinioMax, ilgoMax)
sirgimoDienuSkaiciusSOM = SOM(visuMax, trumpoMax, vidutinioMax, ilgoMax)

print("MOM metodu gautas dienu skaicius: ", sirgimoDienuSkaiciusMOM)
print("SOM metodu gautas dienu skaicius: ", sirgimoDienuSkaiciusSOM)
