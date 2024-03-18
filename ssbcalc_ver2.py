class SSB:
    def __init__(self, absolute_frequency, subcarrier_spacing, freq_range):
        self.abs_freq = absolute_frequency
        self.scs = subcarrier_spacing
        self.freq_range = freq_range

    def calculate_reference_frequency(self):
        if self.freq_range == 1:
            FRef = 3000 + 15 * ((self.abs_freq - 600000) / 1000)
        elif self.freq_range == 0:
            FRef = 0 + 5 * ((self.abs_freq - 0) / 1000)
        else:
            FRef = 24250 + 60 * ((self.abs_freq - 2016667) / 1000)
        return FRef

    def absolute_frequency_diff(self, other):
        afssb = self.calculate_reference_frequency()
        afpa = other.calculate_reference_frequency()
        diff = (afssb - afpa) * 1000
        return round(diff, 2)

    def lower_10_PRBs(self):
        l10rb = 10 * self.scs * 12  # 10 RBs, 12 SCs per RB
        return l10rb

    def calculate_offset(self, other):
        r = self.absolute_frequency_diff(other)
        s = self.lower_10_PRBs()
        offset_r = r // 180  # Offset to Point A
        k = (r - offset_r * 12 * 15) / 15  # KSSB in subcarriers
        ssb_offset_to_point_a = offset_r + k
        return offset_r, k, ssb_offset_to_point_a
        
    def afssb_afpa(self,sec) : 
        afssb = self.Fref()
        afpa =  sec.Fref()
        diff = (afssb - afpa)*1000
        diff_r = round(diff , 2)
        return diff_r
        
    def print_reference_frequencies(self, other):
        afssb_freq = self.calculate_reference_frequency()
        afpa_freq = other.calculate_reference_frequency()
        print("Fref for SSB: {} MHz".format(afssb_freq))
        print("Fref for Absolute Point A: {} MHz".format(afpa_freq))
        
    def calc(self) :
        print("\nassuming scs = 15KHz for FR1 and 60KHz for FR2")
        print("Scope of this code is FR1\n")
        r = self.absolute_frequency_diff(afpa)  
        s = self.lower_10_PRBs()  
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

# Input validation and user prompts
try:
    afssb_freq = int(input("Enter Absolute Frequency SSB: "))
    scs = int(input("Enter Subcarrier Spacing for SSB (in KHz) : "))
    freq_range = int(input("Enter Frequency Range (0-3000 MHz = 0, 3000-24250 MHz = 1, 24250-100000 MHz = 2): "))
    afpa_freq = int(input("Enter Absolute Frequency Point A: "))
    afpa_scs = int(input("Enter Subcarrier Spacing for Point A (in KHz) : "))

    afssb = SSB(afssb_freq, scs, freq_range)
    afpa = SSB(afpa_freq, afpa_scs, freq_range)

    afssb.print_reference_frequencies(afpa)
    afssb.calc()

except ValueError:
    print("Please enter valid integer values for frequency and spacing.")
except Exception as e:
    print("An error occurred:", e)
