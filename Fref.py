class SSB:
    def __init__(self, Nref):
        self.r = Nref

    def Fref(self):
        print("************Fref******************")
        print("check band from : (https://en.wikipedia.org/wiki/5G_NR_frequency_bands)")
        print("frequency range : 0-3000 MHZ = 0 , 3000-24250 MHZ = 1 , 24250-100000 MHZ = 2")
        try:
            freq_range = int(input("ENTER CHOICE :  "))
        except (ValueError, NameError):
            print("ENTER VALID VALUE  ")

        if freq_range == 1:
            FRef = 3000 + 15 * ((self.r - 600000) / 1000)
            print("*********************************")
            print("Fref = {}MHz".format(FRef))
            return FRef
        elif freq_range == 0:
            FRef = 0 + 5 * ((self.r - 0) / 1000)
            print("*********************************")
            print("Fref = {}MHz".format(FRef))
            return FRef
        else:
            FRef = 24250 + 60 * ((self.r - 2016667) / 1000)
            print("*********************************")
            print("Fref = {}MHz".format(FRef))
            return FRef
        
    
    def afssb_afpa(self,sec) : 
        print('****************************')
        afssb = self.Fref()
        afpa =  sec.Fref()
        diff = (afssb - afpa)*1000
        diff_r = round(diff , 2)
        print('****************************')
        print("DIFF BETWEEN ABSOLUTEFREQUENCYSSB AND ABSOULTEFREQUENCYPOINTA :  {}".format(diff_r))

s = int(input("ENTER ABSOLUTEFREQUENCYSSB :  "))
a = int(input("ENTER ABSOULTEFREQUENCYPONTA :  "))
afssb = SSB(s)
afpa = SSB(a)
afssb.afssb_afpa(afpa)
