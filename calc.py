class SSB:
    def __init__(self, Nref , SCS , freq_range):
        self.r = Nref
        self.scs = SCS
        self.freq_range = freq_range

    def Fref(self):
        print("************Fref******************")
        print("check band from : (https://en.wikipedia.org/wiki/5G_NR_frequency_bands)")
        print("frequency range : 0-3000 MHZ = 0 , 3000-24250 MHZ = 1 , 24250-100000 MHZ = 2")
        # try:
        #     freq_range = int(input("ENTER CHOICE :  "))
        # except (ValueError, NameError):
        #     print("ENTER VALID VALUE  ")

        if self.freq_range == 1:
            FRef = 3000 + 15 * ((self.r - 600000) / 1000)
            print("*********************************")
            print("Fref = {}MHz".format(FRef))
            return FRef
        elif self.freq_range == 0:
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
        return diff_r

    def lower10PRBs(self) : 
        l10rb = 10 * self.scs * 12  # 10 RBS , 12Sc , scs
        return l10rb
    
    def calc(self) :
        print("assuming scs = 15KHz for FR1 and 60KHz for FR2")
        print("Scope of this code is FR1")
        r = self.afssb_afpa(afpa)  
        s = self.lower10PRBs()  
        offsetfre = r - s
        offset = (r - s) / 180  # 180 = 12 * 15
        offset_r =  (r - s) // 180 # offsettopointA
        print("*****************************")
        print("OFFSETTOPOINTA = {}".format(offset_r)) # offsettopointA
        k = (offsetfre - (offset_r*12*15))/15 # KSSB in subcarriers
        print("*****************************")
        print("KSSB = {}".format(k))
        
        SSBoffsettoPOINTA = offset_r + k 
        print("*****************************")
        print("SSB OFFSET TO POINT A  = {}".format(SSBoffsettoPOINTA))
        


s1 = int(input("ENTER ABSOLUTEFREQUENCYSSB :  "))
s2 = int(input("ENTER SUBCARRIER SPACING : "))
print("frequency range : 0-3000 MHZ = 0 , 3000-24250 MHZ = 1 , 24250-100000 MHZ = 2")
s3 = int(input("ENTER CHOICE :  "))
a = int(input("ENTER ABSOULTEFREQUENCYPONTA :  "))
a2 = int(input("ENTER SUBCARRIER SPACING : "))
afssb = SSB(s1,s2,s3)
afpa = SSB(a,a2,s3)
afssb.calc()


