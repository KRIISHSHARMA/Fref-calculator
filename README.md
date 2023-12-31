# Fref-calculator
``` bash 
#  downlinkConfigCommon
    #frequencyInfoDL
      # this is 3450.72 MHz (center frequency)
      absoluteFrequencySSB                                          = 630048;
      dl_frequencyBand                                              = 78;
      # this is 3401.58 MHz
      dl_absoluteFrequencyPointA                                    = 626772;
      #scs-SpecificCarrierList
        dl_offstToCarrier                                           = 0;
# subcarrierSpacing
# 0=kHz15, 1=kHz30, 2=kHz60, 3=kHz120
        dl_subcarrierSpacing                                        = 1;
        dl_carrierBandwidth                                         = 273;
     #initialDownlinkBWP
      #genericParameters
       initialDLBWPlocationAndBandwidth                             = 1099; #38.101-1 Table 5.3.2-1 , TS 38.508-1 V17.5.0 (2022-06) - 4.3.1.0D-1
       
```
![unnamed](https://github.com/KRIISHSHARMA/OAI-config/assets/86760658/9552de5a-6f65-4576-bc16-2df16473d4de)
![Screenshot from 2023-12-04 22-50-38](https://github.com/KRIISHSHARMA/OAI-config/assets/86760658/375a9f76-cf6c-47f9-9587-e77803181b7f)
![Screenshot from 2023-12-04 22-51-02](https://github.com/KRIISHSHARMA/OAI-config/assets/86760658/803fc0ef-eab0-42bc-8413-db02e81e65e1)
![Screenshot from 2023-12-05 10-25-45](https://github.com/KRIISHSHARMA/OAI-config/assets/86760658/8175d883-5ded-4c46-b48c-a46f6ff0abec)

- **absoluteFrequencySSB** : It represent the center frequency of SSB Block
- **absoluteFrequencyPointA** : It represents the common reference point A
- **offsetToPointA** = It defines the frequency offset between point A and the lowest subcarrier of the RB overlapping with SSB. The unit for RB is expressed as 15KHz for FR1 and 60 KHz for FR2
- **Kssb** = it defines the frequency of RB#0 of SSB and The unit for RB is expressed as 15KHz for FR1 and 60 KHz for FR2
- **dl_offstToCarrier** : if dl_offstToCarrier is equal to 0, it means that the starting point of the communication at Point A aligns perfectly with the carrier frequency. There is no shift or difference in frequency; they match up directly. It's like saying they are on the same page in terms of where they are operating in the wireless spectrum.
- [Reference](https://www.techplayon.com/5g-nr-ssb-positioning-time-and-frequency-resources/)

- [initialDLBWPlocationAndBandwidth](https://www.linkedin.com/pulse/location-bandwidth-abhishek-ranjan/)  : CORRECTION **Max RBs would be 272 hence end point of the exmaple given above would be 272**

![Screenshot from 2023-12-05 10-09-58](https://github.com/KRIISHSHARMA/OAI-config/assets/86760658/983f711d-2f69-44c4-952d-4da22b492294)

- table from 3GPP `TS 38.508-1 V17.5.0 (2022-06) - 4.3.1.0D-1`
