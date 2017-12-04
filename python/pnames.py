import os, sys, re
# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------
PDGNAME = {}
PDGNAME[1]	= "d"
PDGNAME[-1]	= "d~"
PDGNAME[2]	= "u"
PDGNAME[-2]	= "u~"
PDGNAME[3]	= "s"
PDGNAME[-3]	= "s~"
PDGNAME[4]	= "c"
PDGNAME[-4]	= "c~"
PDGNAME[5]	= "b"
PDGNAME[-5]	= "b~"
PDGNAME[6]	= "t"
PDGNAME[-6]	= "t~"
PDGNAME[7]	= "b'"
PDGNAME[-7]	= "b'~"
PDGNAME[8]	= "t'"
PDGNAME[-8]	= "t'~"
PDGNAME[11]	= "e^-"
PDGNAME[-11]	= "e^+"
PDGNAME[12]	= "nu_e"
PDGNAME[-12]	= "nu_e~"
PDGNAME[13]	= "mu^-"
PDGNAME[-13]	= "mu^+"
PDGNAME[14]	= "nu_mu"
PDGNAME[-14]	= "nu_mu~"
PDGNAME[15]	= "tau^-"
PDGNAME[-15]	= "tau^+"
PDGNAME[16]	= "nu_tau"
PDGNAME[-16]	= "nu_tau~"
PDGNAME[17]	= "tau'^-"
PDGNAME[-17]	= "tau'^+"
PDGNAME[18]	= "nu_tau'"
PDGNAME[-18]	= "nu_tau'~"
PDGNAME[21]	= "g"
PDGNAME[22]	= "gamma"
PDGNAME[23]	= "Z^0"
PDGNAME[24]	= "W^+"
PDGNAME[-24]	= "W^-"
PDGNAME[25]	= "H_1^0"
PDGNAME[32]	= "Z_2^0"
PDGNAME[33]	= "Z_3^0"
PDGNAME[34]	= "W_2^+"
PDGNAME[-34]	= "W_2^-"
PDGNAME[35]	= "H_2^0"
PDGNAME[36]	= "H_3^0"
PDGNAME[37]	= "H^+"
PDGNAME[-37]	= "H^-"
PDGNAME[39]	= "G"
PDGNAME[41]	= "R^0"
PDGNAME[-41]	= "R~^0"
PDGNAME[42]	= "LQ_c"
PDGNAME[-42]	= "LQ_c~"
PDGNAME[51]	= "H_L^0"
PDGNAME[52]	= "H_1^++"
PDGNAME[-52]	= "H_1^--"
PDGNAME[53]	= "H_2^+"
PDGNAME[-53]	= "H_2^-"
PDGNAME[54]	= "H_2^++"
PDGNAME[-54]	= "H_2^--"
PDGNAME[55]	= "H_4^0"
PDGNAME[-55]	= "H_4~^0"
PDGNAME[81]	= "generator-specific+81"
PDGNAME[-81]	= "generator-specific-81"
PDGNAME[82]	= "generator-specific+82"
PDGNAME[-82]	= "generator-specific-82"
PDGNAME[83]	= "generator-specific+83"
PDGNAME[-83]	= "generator-specific-83"
PDGNAME[84]	= "generator-specific+84"
PDGNAME[-84]	= "generator-specific-84"
PDGNAME[85]	= "generator-specific+85"
PDGNAME[-85]	= "generator-specific-85"
PDGNAME[86]	= "generator-specific+86"
PDGNAME[-86]	= "generator-specific-86"
PDGNAME[87]	= "generator-specific+87"
PDGNAME[-87]	= "generator-specific-87"
PDGNAME[88]	= "generator-specific+88"
PDGNAME[-88]	= "generator-specific-88"
PDGNAME[89]	= "generator-specific+89"
PDGNAME[-89]	= "generator-specific-89"
PDGNAME[90]	= "generator-specific+90"
PDGNAME[-90]	= "generator-specific-90"
PDGNAME[91]	= "generator-specific+91"
PDGNAME[-91]	= "generator-specific-91"
PDGNAME[92]	= "generator-specific+92"
PDGNAME[-92]	= "generator-specific-92"
PDGNAME[93]	= "generator-specific+93"
PDGNAME[-93]	= "generator-specific-93"
PDGNAME[94]	= "generator-specific+94"
PDGNAME[-94]	= "generator-specific-94"
PDGNAME[95]	= "generator-specific+95"
PDGNAME[-95]	= "generator-specific-95"
PDGNAME[96]	= "generator-specific+96"
PDGNAME[-96]	= "generator-specific-96"
PDGNAME[97]	= "generator-specific+97"
PDGNAME[-97]	= "generator-specific-97"
PDGNAME[98]	= "generator-specific+98"
PDGNAME[-98]	= "generator-specific-98"
PDGNAME[99]	= "generator-specific+99"
PDGNAME[-99]	= "generator-specific-99"
PDGNAME[100]	= "generator-specific+100"
PDGNAME[-100]	= "generator-specific-100"
PDGNAME[101]	= "geantino"
PDGNAME[102]	= "charged-geantino"
PDGNAME[110]	= "reggeon"
PDGNAME[111]	= "pi^0"
PDGNAME[113]	= "rho(770)^0"
PDGNAME[115]	= "a_2(1320)^0"
PDGNAME[117]	= "rho_3(1690)^0"
PDGNAME[119]	= "a_4(2040)^0"
PDGNAME[130]	= "K_L^0"
PDGNAME[211]	= "pi^+"
PDGNAME[-211]	= "pi^-"
PDGNAME[213]	= "rho(770)^+"
PDGNAME[-213]	= "rho(770)^-"
PDGNAME[215]	= "a_2(1320)^+"
PDGNAME[-215]	= "a_2(1320)^-"
PDGNAME[217]	= "rho_3(1690)^+"
PDGNAME[-217]	= "rho_3(1690)^-"
PDGNAME[219]	= "a_4(2040)^+"
PDGNAME[-219]	= "a_4(2040)^-"
PDGNAME[221]	= "eta"
PDGNAME[223]	= "omega(782)"
PDGNAME[225]	= "f_2(1270)"
PDGNAME[227]	= "omega_3(1670)"
PDGNAME[229]	= "f_4(2050)"
PDGNAME[310]	= "K_S^0"
PDGNAME[311]	= "K^0"
PDGNAME[-311]	= "K~^0"
PDGNAME[313]	= "K*(892)^0"
PDGNAME[-313]	= "K*(892)~^0"
PDGNAME[315]	= "K*_2(1430)^0"
PDGNAME[-315]	= "K*_2(1430)~^0"
PDGNAME[317]	= "K*_3(1780)^0"
PDGNAME[-317]	= "K*_3(1780)~^0"
PDGNAME[319]	= "K*_4(2045)^0"
PDGNAME[-319]	= "K*_4(2045)~^0"
PDGNAME[321]	= "K^+"
PDGNAME[-321]	= "K^-"
PDGNAME[323]	= "K*(892)^+"
PDGNAME[-323]	= "K*(892)^-"
PDGNAME[325]	= "K*_2(1430)^+"
PDGNAME[-325]	= "K*_2(1430)^-"
PDGNAME[327]	= "K*_3(1780)^+"
PDGNAME[-327]	= "K*_3(1780)^-"
PDGNAME[329]	= "K*_4(2045)^+"
PDGNAME[-329]	= "K*_4(2045)^-"
PDGNAME[331]	= "eta'(958)"
PDGNAME[333]	= "phi(1020)"
PDGNAME[335]	= "f'_2(1525)"
PDGNAME[337]	= "phi_3(1850)"
PDGNAME[411]	= "D^+"
PDGNAME[-411]	= "D^-"
PDGNAME[413]	= "D*(2010)^+"
PDGNAME[-413]	= "D*(2010)^-"
PDGNAME[415]	= "D*_2(2460)^+"
PDGNAME[-415]	= "D*_2(2460)^-"
PDGNAME[421]	= "D^0"
PDGNAME[-421]	= "D~^0"
PDGNAME[423]	= "D*(2007)^0"
PDGNAME[-423]	= "D*(2007)~^0"
PDGNAME[425]	= "D*_2(2460)^0"
PDGNAME[-425]	= "D*_2(2460)~^0"
PDGNAME[431]	= "D_s^+"
PDGNAME[-431]	= "D_s^-"
PDGNAME[433]	= "D*_s^+"
PDGNAME[-433]	= "D*_s^-"
PDGNAME[435]	= "D*_s2(2573)^+"
PDGNAME[-435]	= "D*_s2(2573)^-"
PDGNAME[441]	= "eta_c(1S)"
PDGNAME[443]	= "J/psi(1S)"
PDGNAME[445]	= "chi_c2(1P)"
PDGNAME[511]	= "B^0"
PDGNAME[-511]	= "B~^0"
PDGNAME[513]	= "B*^0"
PDGNAME[-513]	= "B*~^0"
PDGNAME[515]	= "B*_2^0"
PDGNAME[-515]	= "B*_2~^0"
PDGNAME[521]	= "B^+"
PDGNAME[-521]	= "B^-"
PDGNAME[523]	= "B*^+"
PDGNAME[-523]	= "B*^-"
PDGNAME[525]	= "B*_2^+"
PDGNAME[-525]	= "B*_2^-"
PDGNAME[531]	= "B_s^0"
PDGNAME[-531]	= "B_s~^0"
PDGNAME[533]	= "B*_s^0"
PDGNAME[-533]	= "B*_s~^0"
PDGNAME[535]	= "B*_s2^0"
PDGNAME[-535]	= "B*_s2~^0"
PDGNAME[541]	= "B_c^+"
PDGNAME[-541]	= "B_c^-"
PDGNAME[543]	= "B*_c^+"
PDGNAME[-543]	= "B*_c^-"
PDGNAME[545]	= "B*_c2^+"
PDGNAME[-545]	= "B*_c2^-"
PDGNAME[551]	= "eta_b(1S)"
PDGNAME[553]	= "Upsilon(1S)"
PDGNAME[555]	= "chi_b2(1P)"
PDGNAME[557]	= "Upsilon_3(1D)"
PDGNAME[611]	= "T^+"
PDGNAME[-611]	= "T^-"
PDGNAME[613]	= "T*^+"
PDGNAME[-613]	= "T*^-"
PDGNAME[621]	= "T^0"
PDGNAME[-621]	= "T~^0"
PDGNAME[623]	= "T*^0"
PDGNAME[-623]	= "T*~^0"
PDGNAME[631]	= "T_s^+"
PDGNAME[-631]	= "T_s^-"
PDGNAME[633]	= "T*_s^+"
PDGNAME[-633]	= "T*_s^-"
PDGNAME[641]	= "T_c^0"
PDGNAME[-641]	= "T_c~^0"
PDGNAME[643]	= "T*_c^0"
PDGNAME[-643]	= "T*_c~^0"
PDGNAME[651]	= "T_b^+"
PDGNAME[-651]	= "T_b^-"
PDGNAME[653]	= "T*_b^+"
PDGNAME[-653]	= "T*_b^-"
PDGNAME[661]	= "eta_t"
PDGNAME[663]	= "theta"
PDGNAME[711]	= "L^0"
PDGNAME[-711]	= "L~^0"
PDGNAME[713]	= "L*^0"
PDGNAME[-713]	= "L*~^0"
PDGNAME[721]	= "L^-"
PDGNAME[-721]	= "L^+"
PDGNAME[723]	= "L*^-"
PDGNAME[-723]	= "L*^+"
PDGNAME[731]	= "L_s^0"
PDGNAME[-731]	= "L_s~^0"
PDGNAME[733]	= "L*_s^0"
PDGNAME[-733]	= "L*_s~^0"
PDGNAME[741]	= "L_c^-"
PDGNAME[-741]	= "L_c^+"
PDGNAME[743]	= "L*_c^-"
PDGNAME[-743]	= "L*_c^+"
PDGNAME[751]	= "L_b^0"
PDGNAME[-751]	= "L_b~^0"
PDGNAME[753]	= "L*_b^0"
PDGNAME[-753]	= "L*_b~^0"
PDGNAME[761]	= "L_t^-"
PDGNAME[-761]	= "L_t^+"
PDGNAME[763]	= "L*_t^-"
PDGNAME[-763]	= "L*_t^+"
PDGNAME[771]	= "eta_l"
PDGNAME[773]	= "theta_l"
PDGNAME[811]	= "H^+"
PDGNAME[-811]	= "H^-"
PDGNAME[813]	= "H*^+"
PDGNAME[-813]	= "H*^-"
PDGNAME[821]	= "H^0"
PDGNAME[-821]	= "H~^0"
PDGNAME[823]	= "H*^0"
PDGNAME[-823]	= "H*~^0"
PDGNAME[831]	= "H_s^+"
PDGNAME[-831]	= "H_s^-"
PDGNAME[833]	= "H*_s^+"
PDGNAME[-833]	= "H*_s^-"
PDGNAME[841]	= "H_c^0"
PDGNAME[-841]	= "H_c~^0"
PDGNAME[843]	= "H*_c^0"
PDGNAME[-843]	= "H*_c~^0"
PDGNAME[851]	= "H_b^+"
PDGNAME[-851]	= "H_b^-"
PDGNAME[853]	= "H*_b^+"
PDGNAME[-853]	= "H*_b^-"
PDGNAME[861]	= "H_t^0"
PDGNAME[-861]	= "H_t~^0"
PDGNAME[863]	= "H*_t^0"
PDGNAME[-863]	= "H*_t~^0"
PDGNAME[871]	= "H_l^+"
PDGNAME[-871]	= "H_l^-"
PDGNAME[873]	= "H*_l^+"
PDGNAME[-873]	= "H*_l^-"
PDGNAME[881]	= "eta_h"
PDGNAME[883]	= "theta_H"
PDGNAME[990]	= "pomeron"
PDGNAME[1103]	= "dd_1"
PDGNAME[-1103]	= "dd_1~"
PDGNAME[1112]	= "Delta(1620)^-"
PDGNAME[1114]	= "Delta^-"
PDGNAME[-1114]	= "Delta~^+"
PDGNAME[1116]	= "Delta(1905)^-"
PDGNAME[1118]	= "Delta(1950)^-"
PDGNAME[1212]	= "Delta(1620)^0"
PDGNAME[1214]	= "N(1520)^0"
PDGNAME[1216]	= "Delta(1905)^0"
PDGNAME[1218]	= "N(2190)^0"
PDGNAME[2101]	= "ud_0"
PDGNAME[-2101]	= "ud_0~"
PDGNAME[2103]	= "ud_1"
PDGNAME[-2103]	= "ud_1~"
PDGNAME[2112]	= "n^0"
PDGNAME[-2112]	= "n~^0"
PDGNAME[2114]	= "Delta^0"
PDGNAME[-2114]	= "Delta~^0"
PDGNAME[2116]	= "N(1675)^0"
PDGNAME[2118]	= "Delta(1950)^0"
PDGNAME[2122]	= "Delta(1620)^+"
PDGNAME[2124]	= "N(1520)^+"
PDGNAME[2126]	= "Delta(1905)^+"
PDGNAME[2128]	= "N(2190)^+"
PDGNAME[2203]	= "uu_1"
PDGNAME[-2203]	= "uu_1~"
PDGNAME[2212]	= "p^+"
PDGNAME[-2212]	= "p~^-"
PDGNAME[2214]	= "Delta^+"
PDGNAME[-2214]	= "Delta~^-"
PDGNAME[2216]	= "N(1675)^+"
PDGNAME[2218]	= "Delta(1950)^+"
PDGNAME[2222]	= "Delta(1620)^++"
PDGNAME[2224]	= "Delta^++"
PDGNAME[-2224]	= "Delta~^--"
PDGNAME[2226]	= "Delta(1905)^++"
PDGNAME[2228]	= "Delta(1950)^++"
PDGNAME[3101]	= "sd_0"
PDGNAME[-3101]	= "sd_0~"
PDGNAME[3103]	= "sd_1"
PDGNAME[-3103]	= "sd_1~"
PDGNAME[3112]	= "Sigma^-"
PDGNAME[-3112]	= "Sigma~^+"
PDGNAME[3114]	= "Sigma*^-"
PDGNAME[-3114]	= "Sigma*~^+"
PDGNAME[3116]	= "Sigma(1775)^-"
PDGNAME[-3116]	= "Sigma~(1775)^-"
PDGNAME[3118]	= "Sigma(2030)^-"
PDGNAME[-3118]	= "Sigma~(2030)^-"
PDGNAME[3122]	= "Lambda^0"
PDGNAME[-3122]	= "Lambda~^0"
PDGNAME[3124]	= "Lambda(1520)^0"
PDGNAME[-3124]	= "Lambda~(1520)^0"
PDGNAME[3126]	= "Lambda(1820)^0"
PDGNAME[-3126]	= "Lambda~(1820)^0"
PDGNAME[3128]	= "Lambda(2100)^0"
PDGNAME[-3128]	= "Lambda~(2100)^0"
PDGNAME[3201]	= "su_0"
PDGNAME[-3201]	= "su_0~"
PDGNAME[3203]	= "su_1"
PDGNAME[-3203]	= "su_1~"
PDGNAME[3212]	= "Sigma^0"
PDGNAME[-3212]	= "Sigma~^0"
PDGNAME[3214]	= "Sigma*^0"
PDGNAME[-3214]	= "Sigma*~^0"
PDGNAME[3216]	= "Sigma(1775)^0"
PDGNAME[-3216]	= "Sigma~(1775)^0"
PDGNAME[3218]	= "Sigma(2030)^0"
PDGNAME[-3218]	= "Sigma~(2030)^0"
PDGNAME[3222]	= "Sigma^+"
PDGNAME[-3222]	= "Sigma~^-"
PDGNAME[3224]	= "Sigma*^+"
PDGNAME[-3224]	= "Sigma*~^-"
PDGNAME[3226]	= "Sigma(1775)^+"
PDGNAME[-3226]	= "Sigma~(1775)^+"
PDGNAME[3228]	= "Sigma(2030)^+"
PDGNAME[-3228]	= "Sigma~(2030)^+"
PDGNAME[3303]	= "ss_1"
PDGNAME[-3303]	= "ss_1~"
PDGNAME[3312]	= "Xi^-"
PDGNAME[-3312]	= "Xi~^+"
PDGNAME[3314]	= "Xi*^-"
PDGNAME[-3314]	= "Xi*~^+"
PDGNAME[3322]	= "Xi^0"
PDGNAME[-3322]	= "Xi~^0"
PDGNAME[3324]	= "Xi*^0"
PDGNAME[-3324]	= "Xi*~^0"
PDGNAME[3334]	= "Omega^-"
PDGNAME[-3334]	= "Omega~^+"
PDGNAME[4101]	= "cd_0"
PDGNAME[-4101]	= "cd_0~"
PDGNAME[4103]	= "cd_1"
PDGNAME[-4103]	= "cd_1~"
PDGNAME[4112]	= "Sigma_c^0"
PDGNAME[-4112]	= "Sigma_c~^0"
PDGNAME[4114]	= "Sigma*_c^0"
PDGNAME[-4114]	= "Sigma*_c~^0"
PDGNAME[4122]	= "Lambda_c^+"
PDGNAME[-4122]	= "Lambda_c~^-"
PDGNAME[4132]	= "Xi_c^0"
PDGNAME[-4132]	= "Xi_c~^0"
PDGNAME[4201]	= "cu_0"
PDGNAME[-4201]	= "cu_0~"
PDGNAME[4203]	= "cu_1"
PDGNAME[-4203]	= "cu_1~"
PDGNAME[4212]	= "Sigma_c^+"
PDGNAME[-4212]	= "Sigma_c~^-"
PDGNAME[4214]	= "Sigma*_c^+"
PDGNAME[-4214]	= "Sigma*_c~^-"
PDGNAME[4222]	= "Sigma_c^++"
PDGNAME[-4222]	= "Sigma_c~^--"
PDGNAME[4224]	= "Sigma*_c^++"
PDGNAME[-4224]	= "Sigma*_c~^--"
PDGNAME[4232]	= "Xi_c^+"
PDGNAME[-4232]	= "Xi_c~^-"
PDGNAME[4301]	= "cs_0"
PDGNAME[-4301]	= "cs_0~"
PDGNAME[4303]	= "cs_1"
PDGNAME[-4303]	= "cs_1~"
PDGNAME[4312]	= "Xi'_c^0"
PDGNAME[-4312]	= "Xi'_c~^0"
PDGNAME[4314]	= "Xi*_c^0"
PDGNAME[-4314]	= "Xi*_c~^0"
PDGNAME[4322]	= "Xi'_c^+"
PDGNAME[-4322]	= "Xi'_c~^-"
PDGNAME[4324]	= "Xi*_c^+"
PDGNAME[-4324]	= "Xi*_c~^-"
PDGNAME[4332]	= "Omega_c^0"
PDGNAME[-4332]	= "Omega_c~^0"
PDGNAME[4334]	= "Omega*_c^0"
PDGNAME[-4334]	= "Omega*_c~^0"
PDGNAME[4403]	= "cc_1"
PDGNAME[-4403]	= "cc_1~"
PDGNAME[4412]	= "Xi_cc^+"
PDGNAME[-4412]	= "Xi_cc~^-"
PDGNAME[4414]	= "Xi*_cc^+"
PDGNAME[-4414]	= "Xi*_cc~^-"
PDGNAME[4422]	= "Xi_cc^++"
PDGNAME[-4422]	= "Xi_cc~^--"
PDGNAME[4424]	= "Xi*_cc^++"
PDGNAME[-4424]	= "Xi*_cc~^--"
PDGNAME[4432]	= "Omega_cc^+"
PDGNAME[-4432]	= "Omega_cc~^-"
PDGNAME[4434]	= "Omega*_cc^+"
PDGNAME[-4434]	= "Omega*_cc~^-"
PDGNAME[4444]	= "Omega*_ccc^++"
PDGNAME[-4444]	= "Omega*_ccc~^--"
PDGNAME[5101]	= "bd_0"
PDGNAME[-5101]	= "bd_0~"
PDGNAME[5103]	= "bd_1"
PDGNAME[-5103]	= "bd_1~"
PDGNAME[5112]	= "Sigma_b^-"
PDGNAME[-5112]	= "Sigma_b~^+"
PDGNAME[5114]	= "Sigma*_b^-"
PDGNAME[-5114]	= "Sigma*_b~^+"
PDGNAME[5122]	= "Lambda_b^0"
PDGNAME[-5122]	= "Lambda_b~^0"
PDGNAME[5132]	= "Xi_b^-"
PDGNAME[-5132]	= "Xi_b~^+"
PDGNAME[5142]	= "Xi_bc^0"
PDGNAME[-5142]	= "Xi_bc~^0"
PDGNAME[5201]	= "bu_0"
PDGNAME[-5201]	= "bu_0~"
PDGNAME[5203]	= "bu_1"
PDGNAME[-5203]	= "bu_1~"
PDGNAME[5212]	= "Sigma_b^0"
PDGNAME[-5212]	= "Sigma_b~^0"
PDGNAME[5214]	= "Sigma*_b^0"
PDGNAME[-5214]	= "Sigma*_b~^0"
PDGNAME[5222]	= "Sigma_b^+"
PDGNAME[-5222]	= "Sigma_b~^-"
PDGNAME[5224]	= "Sigma*_b^+"
PDGNAME[-5224]	= "Sigma*_b~^-"
PDGNAME[5232]	= "Xi_b^0"
PDGNAME[-5232]	= "Xi_b~^0"
PDGNAME[5242]	= "Xi_bc^+"
PDGNAME[-5242]	= "Xi_bc~^-"
PDGNAME[5301]	= "bs_0"
PDGNAME[-5301]	= "bs_0~"
PDGNAME[5303]	= "bs_1"
PDGNAME[-5303]	= "bs_1~"
PDGNAME[5312]	= "Xi'_b^-"
PDGNAME[-5312]	= "Xi'_b~^+"
PDGNAME[5314]	= "Xi*_b^-"
PDGNAME[-5314]	= "Xi*_b~^+"
PDGNAME[5322]	= "Xi'_b^0"
PDGNAME[-5322]	= "Xi'_b~^0"
PDGNAME[5324]	= "Xi*_b^0"
PDGNAME[-5324]	= "Xi*_b~^0"
PDGNAME[5332]	= "Omega_b^-"
PDGNAME[-5332]	= "Omega_b~^+"
PDGNAME[5334]	= "Omega*_b^-"
PDGNAME[-5334]	= "Omega*_b~^+"
PDGNAME[5342]	= "Omega_bc^0"
PDGNAME[-5342]	= "Omega_bc~^0"
PDGNAME[5401]	= "bc_0"
PDGNAME[-5401]	= "bc_0~"
PDGNAME[5403]	= "bc_1"
PDGNAME[-5403]	= "bc_1~"
PDGNAME[5412]	= "Xi'_bc^0"
PDGNAME[-5412]	= "Xi'_bc~^0"
PDGNAME[5414]	= "Xi*_bc^0"
PDGNAME[-5414]	= "Xi*_bc~^0"
PDGNAME[5422]	= "Xi'_bc^+"
PDGNAME[-5422]	= "Xi'_bc~^-"
PDGNAME[5424]	= "Xi*_bc^+"
PDGNAME[-5424]	= "Xi*_bc~^-"
PDGNAME[5432]	= "Omega'_bc^0"
PDGNAME[-5432]	= "Omega'_bc~^0"
PDGNAME[5434]	= "Omega*_bc^0"
PDGNAME[-5434]	= "Omega*_bc~^0"
PDGNAME[5442]	= "Omega_bcc^+"
PDGNAME[-5442]	= "Omega_bcc~^-"
PDGNAME[5444]	= "Omega*_bcc^+"
PDGNAME[-5444]	= "Omega*_bcc~^-"
PDGNAME[5503]	= "bb_1"
PDGNAME[-5503]	= "bb_1~"
PDGNAME[5512]	= "Xi_bb^-"
PDGNAME[-5512]	= "Xi_bb~^+"
PDGNAME[5514]	= "Xi*_bb^-"
PDGNAME[-5514]	= "Xi*_bb~^+"
PDGNAME[5522]	= "Xi_bb^0"
PDGNAME[-5522]	= "Xi_bb~^0"
PDGNAME[5524]	= "Xi*_bb^0"
PDGNAME[-5524]	= "Xi*_bb~^0"
PDGNAME[5532]	= "Omega_bb^-"
PDGNAME[-5532]	= "Omega_bb~^+"
PDGNAME[5534]	= "Omega*_bb^-"
PDGNAME[-5534]	= "Omega*_bb~^+"
PDGNAME[5542]	= "Omega_bbc^0"
PDGNAME[-5542]	= "Omega_bbc~^0"
PDGNAME[5544]	= "Omega*_bbc^0"
PDGNAME[-5544]	= "Omega*_bbc~^0"
PDGNAME[5554]	= "Omega*_bbb^-"
PDGNAME[-5554]	= "Omega*_bbb~^+"
PDGNAME[6101]	= "td_0"
PDGNAME[-6101]	= "td_0~"
PDGNAME[6103]	= "td_1"
PDGNAME[-6103]	= "td_1~"
PDGNAME[6112]	= "Sigma_t^0"
PDGNAME[-6112]	= "Sigma_t~^0"
PDGNAME[6114]	= "Sigma*_t^0"
PDGNAME[-6114]	= "Sigma*_t~^0"
PDGNAME[6122]	= "Lambda_t^+"
PDGNAME[-6122]	= "Lambda_t~^-"
PDGNAME[6132]	= "Xi_t^0"
PDGNAME[-6132]	= "Xi_t~^0"
PDGNAME[6142]	= "Xi_tc^+"
PDGNAME[-6142]	= "Xi_tc~^-"
PDGNAME[6152]	= "Xi_tb^0"
PDGNAME[-6152]	= "Xi_tb~^0"
PDGNAME[6201]	= "tu_0"
PDGNAME[-6201]	= "tu_0~"
PDGNAME[6203]	= "tu_1"
PDGNAME[-6203]	= "tu_1~"
PDGNAME[6212]	= "Sigma_t^+"
PDGNAME[-6212]	= "Sigma_t~^-"
PDGNAME[6214]	= "Sigma*_t^+"
PDGNAME[-6214]	= "Sigma*_t~^-"
PDGNAME[6222]	= "Sigma_t^++"
PDGNAME[-6222]	= "Sigma_t~^--"
PDGNAME[6224]	= "Sigma*_t^++"
PDGNAME[-6224]	= "Sigma*_t~^--"
PDGNAME[6232]	= "Xi_t^+"
PDGNAME[-6232]	= "Xi_t~^-"
PDGNAME[6242]	= "Xi_tc^++"
PDGNAME[-6242]	= "Xi_tc~^--"
PDGNAME[6252]	= "Xi_tb^+"
PDGNAME[-6252]	= "Xi_tb~^-"
PDGNAME[6301]	= "ts_0"
PDGNAME[-6301]	= "ts_0~"
PDGNAME[6303]	= "ts_1"
PDGNAME[-6303]	= "ts_1~"
PDGNAME[6312]	= "Xi'_t^0"
PDGNAME[-6312]	= "Xi'_t~^0"
PDGNAME[6314]	= "Xi*_t^0"
PDGNAME[-6314]	= "Xi*_t~^0"
PDGNAME[6322]	= "Xi'_t^+"
PDGNAME[-6322]	= "Xi'_t~^-"
PDGNAME[6324]	= "Xi*_t^+"
PDGNAME[-6324]	= "Xi*_t~^-"
PDGNAME[6332]	= "Omega_t^0"
PDGNAME[-6332]	= "Omega_t~^0"
PDGNAME[6334]	= "Omega*_t^0"
PDGNAME[-6334]	= "Omega*_t~^0"
PDGNAME[6342]	= "Omega_tc^+"
PDGNAME[-6342]	= "Omega_tc~^-"
PDGNAME[6352]	= "Omega_tb^0"
PDGNAME[-6352]	= "Omega_tb~^0"
PDGNAME[6401]	= "tc_0"
PDGNAME[-6401]	= "tc_0~"
PDGNAME[6403]	= "tc_1"
PDGNAME[-6403]	= "tc_1~"
PDGNAME[6412]	= "Xi'_tc^+"
PDGNAME[-6412]	= "Xi'_tc~^-"
PDGNAME[6414]	= "Xi*_tc^+"
PDGNAME[-6414]	= "Xi*_tc~^-"
PDGNAME[6422]	= "Xi'_tc^++"
PDGNAME[-6422]	= "Xi'_tc~^--"
PDGNAME[6424]	= "Xi*_tc^++"
PDGNAME[-6424]	= "Xi*_tc~^--"
PDGNAME[6432]	= "Omega'_tc^+"
PDGNAME[-6432]	= "Omega'_tc~^-"
PDGNAME[6434]	= "Omega*_tc^+"
PDGNAME[-6434]	= "Omega*_tc~^-"
PDGNAME[6442]	= "Omega_tcc^++"
PDGNAME[-6442]	= "Omega_tcc~^--"
PDGNAME[6444]	= "Omega*_tcc^++"
PDGNAME[-6444]	= "Omega*_tcc~^--"
PDGNAME[6452]	= "Omega_tbc^+"
PDGNAME[-6452]	= "Omega_tbc~^-"
PDGNAME[6501]	= "tb_0"
PDGNAME[-6501]	= "tb_0~"
PDGNAME[6503]	= "tb_1"
PDGNAME[-6503]	= "tb_1~"
PDGNAME[6512]	= "Xi'_tb^0"
PDGNAME[-6512]	= "Xi'_tb~^0"
PDGNAME[6514]	= "Xi*_tb^0"
PDGNAME[-6514]	= "Xi*_tb~^0"
PDGNAME[6522]	= "Xi'_tb^+"
PDGNAME[-6522]	= "Xi'_tb~^-"
PDGNAME[6524]	= "Xi*_tb^+"
PDGNAME[-6524]	= "Xi*_tb~^-"
PDGNAME[6532]	= "Omega'_tb^0"
PDGNAME[-6532]	= "Omega'_tb~^0"
PDGNAME[6534]	= "Omega*_tb^0"
PDGNAME[-6534]	= "Omega*_tb~^0"
PDGNAME[6542]	= "Omega'_tbc^+"
PDGNAME[-6542]	= "Omega'_tbc~^-"
PDGNAME[6544]	= "Omega*_tbc^+"
PDGNAME[-6544]	= "Omega*_tbc~^-"
PDGNAME[6552]	= "Omega_tbb^0"
PDGNAME[-6552]	= "Omega_tbb~^0"
PDGNAME[6554]	= "Omega*_tbb^0"
PDGNAME[-6554]	= "Omega*_tbb~^0"
PDGNAME[6603]	= "tt_1"
PDGNAME[-6603]	= "tt_1~"
PDGNAME[6612]	= "Xi_tt^+"
PDGNAME[-6612]	= "Xi_tt~^-"
PDGNAME[6614]	= "Xi*_tt^+"
PDGNAME[-6614]	= "Xi*_tt~^-"
PDGNAME[6622]	= "Xi_tt^++"
PDGNAME[-6622]	= "Xi_tt~^--"
PDGNAME[6624]	= "Xi*_tt^++"
PDGNAME[-6624]	= "Xi*_tt~^--"
PDGNAME[6632]	= "Omega_tt^+"
PDGNAME[-6632]	= "Omega_tt~^-"
PDGNAME[6634]	= "Omega*_tt^+"
PDGNAME[-6634]	= "Omega*_tt~^-"
PDGNAME[6642]	= "Omega_ttc^++"
PDGNAME[-6642]	= "Omega_ttc~^--"
PDGNAME[6644]	= "Omega*_ttc^++"
PDGNAME[-6644]	= "Omega*_ttc~^--"
PDGNAME[6652]	= "Omega_ttb^+"
PDGNAME[-6652]	= "Omega_ttb~^-"
PDGNAME[6654]	= "Omega*_ttb^+"
PDGNAME[-6654]	= "Omega*_ttb~^-"
PDGNAME[6664]	= "Omega*_ttt^++"
PDGNAME[-6664]	= "Omega*_ttt~^--"
PDGNAME[7101]	= "b'd_0"
PDGNAME[-7101]	= "b'd_0~"
PDGNAME[7103]	= "b'd_1"
PDGNAME[-7103]	= "b'd_1~"
PDGNAME[7112]	= "Sigma_b'^-"
PDGNAME[-7112]	= "Sigma_b'~^+"
PDGNAME[7114]	= "Sigma*_b'^-"
PDGNAME[-7114]	= "Sigma*_b'~^+"
PDGNAME[7122]	= "Lambda_b'^0"
PDGNAME[-7122]	= "Lambda_b'~^0"
PDGNAME[7132]	= "Xi_b'^-"
PDGNAME[-7132]	= "Xi_b'~^+"
PDGNAME[7142]	= "Xi_b'c^0"
PDGNAME[-7142]	= "Xi_b'c~^0"
PDGNAME[7152]	= "Xi_b'b^-"
PDGNAME[-7152]	= "Xi_b'b~^+"
PDGNAME[7162]	= "Xi_b't^0"
PDGNAME[-7162]	= "Xi_b't~^0"
PDGNAME[7201]	= "b'u_0"
PDGNAME[-7201]	= "b'u_0~"
PDGNAME[7203]	= "b'u_1"
PDGNAME[-7203]	= "b'u_1~"
PDGNAME[7212]	= "Sigma_b'^0"
PDGNAME[-7212]	= "Sigma_b'~^0"
PDGNAME[7214]	= "Sigma*_b'^0"
PDGNAME[-7214]	= "Sigma*_b'~^0"
PDGNAME[7222]	= "Sigma_b'^+"
PDGNAME[-7222]	= "Sigma_b'~^-"
PDGNAME[7224]	= "Sigma*_b'^+"
PDGNAME[-7224]	= "Sigma*_b'~^-"
PDGNAME[7232]	= "Xi_b'^0"
PDGNAME[-7232]	= "Xi_b'~^0"
PDGNAME[7242]	= "Xi_b'c^+"
PDGNAME[-7242]	= "Xi_b'c~^-"
PDGNAME[7252]	= "Xi_b'b^0"
PDGNAME[-7252]	= "Xi_b'b~^0"
PDGNAME[7262]	= "Xi_b't^+"
PDGNAME[-7262]	= "Xi_b't~^-"
PDGNAME[7301]	= "b's_0"
PDGNAME[-7301]	= "b's_0~"
PDGNAME[7303]	= "b's_1"
PDGNAME[-7303]	= "b's_1~"
PDGNAME[7312]	= "Xi'_b'^-"
PDGNAME[-7312]	= "Xi'_b'~^+"
PDGNAME[7314]	= "Xi*_b'^-"
PDGNAME[-7314]	= "Xi*_b'~^+"
PDGNAME[7322]	= "Xi'_b'^0"
PDGNAME[-7322]	= "Xi'_b'~^0"
PDGNAME[7324]	= "Xi*_b'^0"
PDGNAME[-7324]	= "Xi*_b'~^0"
PDGNAME[7332]	= "Omega'_b'^-"
PDGNAME[-7332]	= "Omega'_b'~^+"
PDGNAME[7334]	= "Omega*_b'^-"
PDGNAME[-7334]	= "Omega*_b'~^+"
PDGNAME[7342]	= "Omega_b'c^0"
PDGNAME[-7342]	= "Omega_b'c~^0"
PDGNAME[7352]	= "Omega_b'b^-"
PDGNAME[-7352]	= "Omega_b'b~^+"
PDGNAME[7362]	= "Omega_b't^0"
PDGNAME[-7362]	= "Omega_b't~^0"
PDGNAME[7401]	= "b'c_0"
PDGNAME[-7401]	= "b'c_0~"
PDGNAME[7403]	= "b'c_1"
PDGNAME[-7403]	= "b'c_1~"
PDGNAME[7412]	= "Xi'_b'c^0"
PDGNAME[-7412]	= "Xi'_b'c~^0"
PDGNAME[7414]	= "Xi*_b'c^0"
PDGNAME[-7414]	= "Xi*_b'c~^0"
PDGNAME[7422]	= "Xi'_b'c^+"
PDGNAME[-7422]	= "Xi'_b'c~^-"
PDGNAME[7424]	= "Xi*_b'c^+"
PDGNAME[-7424]	= "Xi*_b'c~^-"
PDGNAME[7432]	= "Omega'_b'c^0"
PDGNAME[-7432]	= "Omega'_b'c~^0"
PDGNAME[7434]	= "Omega*_b'c^0"
PDGNAME[-7434]	= "Omega*_b'c~^0"
PDGNAME[7442]	= "Omega'_b'cc^+"
PDGNAME[-7442]	= "Omega'_b'cc~^-"
PDGNAME[7444]	= "Omega*_b'cc^+"
PDGNAME[-7444]	= "Omega*_b'cc~^-"
PDGNAME[7452]	= "Omega_b'bc^0"
PDGNAME[-7452]	= "Omega_b'bc~^0"
PDGNAME[7462]	= "Omega_b'tc^+"
PDGNAME[-7462]	= "Omega_b'tc~^-"
PDGNAME[7501]	= "b'b_0"
PDGNAME[-7501]	= "b'b_0~"
PDGNAME[7503]	= "b'b_1"
PDGNAME[-7503]	= "b'b_1~"
PDGNAME[7512]	= "Xi'_b'b^-"
PDGNAME[-7512]	= "Xi'_b'b~^+"
PDGNAME[7514]	= "Xi*_b'b^-"
PDGNAME[-7514]	= "Xi*_b'b~^+"
PDGNAME[7522]	= "Xi'_b'b^0"
PDGNAME[-7522]	= "Xi'_b'b~^0"
PDGNAME[7524]	= "Xi*_b'b^0"
PDGNAME[-7524]	= "Xi*_b'b~^0"
PDGNAME[7532]	= "Omega'_b'b^-"
PDGNAME[-7532]	= "Omega'_b'b~^+"
PDGNAME[7534]	= "Omega*_b'b^-"
PDGNAME[-7534]	= "Omega*_b'b~^+"
PDGNAME[7542]	= "Omega'_b'bc^0"
PDGNAME[-7542]	= "Omega'_b'bc~^0"
PDGNAME[7544]	= "Omega*_b'bc^0"
PDGNAME[-7544]	= "Omega*_b'bc~^0"
PDGNAME[7552]	= "Omega'_b'bb^-"
PDGNAME[-7552]	= "Omega'_b'bb~^+"
PDGNAME[7554]	= "Omega*_b'bb^-"
PDGNAME[-7554]	= "Omega*_b'bb~^+"
PDGNAME[7562]	= "Omega_b'tb^0"
PDGNAME[-7562]	= "Omega_b'tb~^0"
PDGNAME[7601]	= "b't_0"
PDGNAME[-7601]	= "b't_0~"
PDGNAME[7603]	= "b't_1"
PDGNAME[-7603]	= "b't_1~"
PDGNAME[7612]	= "Xi'_b't^0"
PDGNAME[-7612]	= "Xi'_b't~^0"
PDGNAME[7614]	= "Xi*_b't^0"
PDGNAME[-7614]	= "Xi*_b't~^0"
PDGNAME[7622]	= "Xi'_b't^+"
PDGNAME[-7622]	= "Xi'_b't~^-"
PDGNAME[7624]	= "Xi*_b't^+"
PDGNAME[-7624]	= "Xi*_b't~^-"
PDGNAME[7632]	= "Omega'_b't^0"
PDGNAME[-7632]	= "Omega'_b't~^0"
PDGNAME[7634]	= "Omega*_b't^0"
PDGNAME[-7634]	= "Omega*_b't~^0"
PDGNAME[7642]	= "Omega'_b'tc^+"
PDGNAME[-7642]	= "Omega'_b'tc~^-"
PDGNAME[7644]	= "Omega*_b'tc^+"
PDGNAME[-7644]	= "Omega*_b'tc~^-"
PDGNAME[7652]	= "Omega'_b'tb^0"
PDGNAME[-7652]	= "Omega'_b'tb~^0"
PDGNAME[7654]	= "Omega*_b'tb^0"
PDGNAME[-7654]	= "Omega*_b'tb~^0"
PDGNAME[7662]	= "Omega'_b'tt^+"
PDGNAME[-7662]	= "Omega'_b'tt~^-"
PDGNAME[7664]	= "Omega*_b'tt^+"
PDGNAME[-7664]	= "Omega*_b'tt~^-"
PDGNAME[7703]	= "b'b'_1"
PDGNAME[-7703]	= "b'b'_1~"
PDGNAME[7712]	= "Xi'_b'b'^-"
PDGNAME[-7712]	= "Xi'_b'b'~^+"
PDGNAME[7714]	= "Xi*_b'b'^-"
PDGNAME[-7714]	= "Xi*_b'b'~^+"
PDGNAME[7722]	= "Xi'_b'b'^0"
PDGNAME[-7722]	= "Xi'_b'b'~^0"
PDGNAME[7724]	= "Xi*_b'b'^0"
PDGNAME[-7724]	= "Xi*_b'b'~^0"
PDGNAME[7732]	= "Omega'_b'b'^-"
PDGNAME[-7732]	= "Omega'_b'b'~^+"
PDGNAME[7734]	= "Omega*_b'b'^-"
PDGNAME[-7734]	= "Omega*_b'b'~^+"
PDGNAME[7742]	= "Omega'_b'b'c^0"
PDGNAME[-7742]	= "Omega'_b'b'c~^0"
PDGNAME[7744]	= "Omega*_b'b'c^0"
PDGNAME[-7744]	= "Omega*_b'b'c~^0"
PDGNAME[7752]	= "Omega'_b'b'b^-"
PDGNAME[-7752]	= "Omega'_b'b'b~^+"
PDGNAME[7754]	= "Omega*_b'b'b^-"
PDGNAME[-7754]	= "Omega*_b'b'b~^+"
PDGNAME[7762]	= "Omega'_b'b't^0"
PDGNAME[-7762]	= "Omega'_b'b't~^0"
PDGNAME[7764]	= "Omega*_b'b't^0"
PDGNAME[-7764]	= "Omega*_b'b't~^0"
PDGNAME[7774]	= "Omega*_b'b'b'^-"
PDGNAME[-7774]	= "Omega*_b'b'b'~^+"
PDGNAME[8101]	= "t'd_0"
PDGNAME[-8101]	= "t'd_0~"
PDGNAME[8103]	= "t'd_1"
PDGNAME[-8103]	= "t'd_1~"
PDGNAME[8112]	= "Sigma_t'^0"
PDGNAME[-8112]	= "Sigma_t'~^0"
PDGNAME[8114]	= "Sigma*_t'^0"
PDGNAME[-8114]	= "Sigma*_t'~^0"
PDGNAME[8122]	= "Lambda_t'^+"
PDGNAME[-8122]	= "Lambda_t'~^-"
PDGNAME[8132]	= "Xi_t'^0"
PDGNAME[-8132]	= "Xi_t'~^0"
PDGNAME[8142]	= "Xi_t'c^+"
PDGNAME[-8142]	= "Xi_t'c~^-"
PDGNAME[8152]	= "Xi_t'b^0"
PDGNAME[-8152]	= "Xi_t'b~^0"
PDGNAME[8162]	= "Xi_t't^+"
PDGNAME[-8162]	= "Xi_t't~^-"
PDGNAME[8172]	= "Xi_t'b'^0"
PDGNAME[-8172]	= "Xi_t'b'~^0"
PDGNAME[8201]	= "t'u_0"
PDGNAME[-8201]	= "t'u_0~"
PDGNAME[8203]	= "t'u_1"
PDGNAME[-8203]	= "t'u_1~"
PDGNAME[8212]	= "Sigma_t'^+"
PDGNAME[-8212]	= "Sigma_t'~^-"
PDGNAME[8214]	= "Sigma*_t'^+"
PDGNAME[-8214]	= "Sigma*_t'~^-"
PDGNAME[8222]	= "Sigma_t'^++"
PDGNAME[-8222]	= "Sigma_t'~^--"
PDGNAME[8224]	= "Sigma*_t'^++"
PDGNAME[-8224]	= "Sigma*_t'~^--"
PDGNAME[8232]	= "Xi_t'^+"
PDGNAME[-8232]	= "Xi_t'~^-"
PDGNAME[8242]	= "Xi_t'c^++"
PDGNAME[-8242]	= "Xi_t'c~^--"
PDGNAME[8252]	= "Xi_t'b^+"
PDGNAME[-8252]	= "Xi_t'b~^-"
PDGNAME[8262]	= "Xi_t't^++"
PDGNAME[-8262]	= "Xi_t't~^--"
PDGNAME[8272]	= "Xi_t'b'^+"
PDGNAME[-8272]	= "Xi_t'b'~^-"
PDGNAME[8301]	= "t's_0"
PDGNAME[-8301]	= "t's_0~"
PDGNAME[8303]	= "t's_1"
PDGNAME[-8303]	= "t's_1~"
PDGNAME[8312]	= "Xi'_t'^0"
PDGNAME[-8312]	= "Xi'_t'~^0"
PDGNAME[8314]	= "Xi*_t'^0"
PDGNAME[-8314]	= "Xi*_t'~^0"
PDGNAME[8322]	= "Xi'_t'^+"
PDGNAME[-8322]	= "Xi'_t'~^-"
PDGNAME[8324]	= "Xi*_t'^+"
PDGNAME[-8324]	= "Xi*_t'~^-"
PDGNAME[8332]	= "Omega'_t'^0"
PDGNAME[-8332]	= "Omega'_t'~^0"
PDGNAME[8334]	= "Omega*_t'^0"
PDGNAME[-8334]	= "Omega*_t'~^0"
PDGNAME[8342]	= "Omega_t'c^+"
PDGNAME[-8342]	= "Omega_t'c~^-"
PDGNAME[8352]	= "Omega_t'b^0"
PDGNAME[-8352]	= "Omega_t'b~^0"
PDGNAME[8362]	= "Omega_t't^+"
PDGNAME[-8362]	= "Omega_t't~^-"
PDGNAME[8372]	= "Omega_t'b'^0"
PDGNAME[-8372]	= "Omega_t'b'~^0"
PDGNAME[8401]	= "t'c_0"
PDGNAME[-8401]	= "t'c_0~"
PDGNAME[8403]	= "t'c_1"
PDGNAME[-8403]	= "t'c_1~"
PDGNAME[8412]	= "Xi'_t'c^+"
PDGNAME[-8412]	= "Xi'_t'c~^-"
PDGNAME[8414]	= "Xi*_t'c^+"
PDGNAME[-8414]	= "Xi*_t'c~^-"
PDGNAME[8422]	= "Xi'_t'c^++"
PDGNAME[-8422]	= "Xi'_t'c~^--"
PDGNAME[8424]	= "Xi*_t'c^++"
PDGNAME[-8424]	= "Xi*_t'c~^--"
PDGNAME[8432]	= "Omega'_t'c^+"
PDGNAME[-8432]	= "Omega'_t'c~^-"
PDGNAME[8434]	= "Omega*_t'c^+"
PDGNAME[-8434]	= "Omega*_t'c~^-"
PDGNAME[8442]	= "Omega'_t'cc^++"
PDGNAME[-8442]	= "Omega'_t'cc~^--"
PDGNAME[8444]	= "Omega*_t'cc^++"
PDGNAME[-8444]	= "Omega*_t'cc~^--"
PDGNAME[8452]	= "Omega_t'bc^+"
PDGNAME[-8452]	= "Omega_t'bc~^-"
PDGNAME[8462]	= "Omega_t'tc^++"
PDGNAME[-8462]	= "Omega_t'tc~^--"
PDGNAME[8472]	= "Omega_t'b'c ^+"
PDGNAME[-8472]	= "Omega_t'b'c ~^-"
PDGNAME[8501]	= "t'b_0"
PDGNAME[-8501]	= "t'b_0~"
PDGNAME[8503]	= "t'b_1"
PDGNAME[-8503]	= "t'b_1~"
PDGNAME[8512]	= "Xi'_t'b^0"
PDGNAME[-8512]	= "Xi'_t'b~^0"
PDGNAME[8514]	= "Xi*_t'b^0"
PDGNAME[-8514]	= "Xi*_t'b~^0"
PDGNAME[8522]	= "Xi'_t'b^+"
PDGNAME[-8522]	= "Xi'_t'b~^-"
PDGNAME[8524]	= "Xi*_t'b^+"
PDGNAME[-8524]	= "Xi*_t'b~^-"
PDGNAME[8532]	= "Omega'_t'b^0"
PDGNAME[-8532]	= "Omega'_t'b~^0"
PDGNAME[8534]	= "Omega*_t'b^0"
PDGNAME[-8534]	= "Omega*_t'b~^0"
PDGNAME[8542]	= "Omega'_t'bc^+"
PDGNAME[-8542]	= "Omega'_t'bc~^-"
PDGNAME[8544]	= "Omega*_t'bc^+"
PDGNAME[-8544]	= "Omega*_t'bc~^-"
PDGNAME[8552]	= "Omega'_t'bb^0"
PDGNAME[-8552]	= "Omega'_t'bb~^0"
PDGNAME[8554]	= "Omega*_t'bb^0"
PDGNAME[-8554]	= "Omega*_t'bb~^0"
PDGNAME[8562]	= "Omega_t'tb^+"
PDGNAME[-8562]	= "Omega_t'tb~^-"
PDGNAME[8572]	= "Omega_t'b'b ^0"
PDGNAME[-8572]	= "Omega_t'b'b ~^0"
PDGNAME[8601]	= "t't_0"
PDGNAME[-8601]	= "t't_0~"
PDGNAME[8603]	= "t't_1"
PDGNAME[-8603]	= "t't_1~"
PDGNAME[8612]	= "Xi'_t't^+"
PDGNAME[-8612]	= "Xi'_t't~^-"
PDGNAME[8614]	= "Xi*_t't^+"
PDGNAME[-8614]	= "Xi*_t't~^-"
PDGNAME[8622]	= "Xi'_t't^++"
PDGNAME[-8622]	= "Xi'_t't~^--"
PDGNAME[8624]	= "Xi*_t't^++"
PDGNAME[-8624]	= "Xi*_t't~^--"
PDGNAME[8632]	= "Omega'_t't^+"
PDGNAME[-8632]	= "Omega'_t't~^-"
PDGNAME[8634]	= "Omega*_t't^+"
PDGNAME[-8634]	= "Omega*_t't~^-"
PDGNAME[8642]	= "Omega'_t'tc^++"
PDGNAME[-8642]	= "Omega'_t'tc~^--"
PDGNAME[8644]	= "Omega*_t'tc^++"
PDGNAME[-8644]	= "Omega*_t'tc~^--"
PDGNAME[8652]	= "Omega'_t'tb^+"
PDGNAME[-8652]	= "Omega'_t'tb~^-"
PDGNAME[8654]	= "Omega*_t'tb^+"
PDGNAME[-8654]	= "Omega*_t'tb~^-"
PDGNAME[8662]	= "Omega'_t'tt^++"
PDGNAME[-8662]	= "Omega'_t'tt~^--"
PDGNAME[8664]	= "Omega*_t'tt^++"
PDGNAME[-8664]	= "Omega*_t'tt~^--"
PDGNAME[8672]	= "Omega_t'b't ^+"
PDGNAME[-8672]	= "Omega_t'b't ~^-"
PDGNAME[8701]	= "t'b'_0"
PDGNAME[-8701]	= "t'b'_0~"
PDGNAME[8703]	= "t'b'_1"
PDGNAME[-8703]	= "t'b'_1~"
PDGNAME[8712]	= "Xi'_t'b'^0"
PDGNAME[-8712]	= "Xi'_t'b'~^0"
PDGNAME[8714]	= "Xi*_t'b'^0"
PDGNAME[-8714]	= "Xi*_t'b'~^0"
PDGNAME[8722]	= "Xi'_t'b'^+"
PDGNAME[-8722]	= "Xi'_t'b'~^-"
PDGNAME[8724]	= "Xi*_t'b'^+"
PDGNAME[-8724]	= "Xi*_t'b'~^-"
PDGNAME[8732]	= "Omega'_t'b'^0"
PDGNAME[-8732]	= "Omega'_t'b'~^0"
PDGNAME[8734]	= "Omega*_t'b'^0"
PDGNAME[-8734]	= "Omega*_t'b'~^0"
PDGNAME[8742]	= "Omega'_t'b'c^+"
PDGNAME[-8742]	= "Omega'_t'b'c~^-"
PDGNAME[8744]	= "Omega*_t'b'c^+"
PDGNAME[-8744]	= "Omega*_t'b'c~^-"
PDGNAME[8752]	= "Omega'_t'b'b^0"
PDGNAME[-8752]	= "Omega'_t'b'b~^0"
PDGNAME[8754]	= "Omega*_t'b'b^0"
PDGNAME[-8754]	= "Omega*_t'b'b~^0"
PDGNAME[8762]	= "Omega'_t'b't^+"
PDGNAME[-8762]	= "Omega'_t'b't~^-"
PDGNAME[8764]	= "Omega*_t'b't^+"
PDGNAME[-8764]	= "Omega*_t'b't~^-"
PDGNAME[8772]	= "Omega'_t'b'b'^0"
PDGNAME[-8772]	= "Omega'_t'b'b'~^0"
PDGNAME[8774]	= "Omega*_t'b'b'^0"
PDGNAME[-8774]	= "Omega*_t'b'b'~^0"
PDGNAME[8803]	= "t't'_1"
PDGNAME[-8803]	= "t't'_1~"
PDGNAME[8812]	= "Xi'_t't'^+"
PDGNAME[-8812]	= "Xi'_t't'~^-"
PDGNAME[8814]	= "Xi*_t't'^+"
PDGNAME[-8814]	= "Xi*_t't'~^-"
PDGNAME[8822]	= "Xi'_t't'^++"
PDGNAME[-8822]	= "Xi'_t't'~^--"
PDGNAME[8824]	= "Xi*_t't'^++"
PDGNAME[-8824]	= "Xi*_t't'~^--"
PDGNAME[8832]	= "Omega'_t't'^+"
PDGNAME[-8832]	= "Omega'_t't'~^-"
PDGNAME[8834]	= "Omega*_t't'^+"
PDGNAME[-8834]	= "Omega*_t't'~^-"
PDGNAME[8842]	= "Omega'_t't'c^++"
PDGNAME[-8842]	= "Omega'_t't'c~^--"
PDGNAME[8844]	= "Omega*_t't'c^++"
PDGNAME[-8844]	= "Omega*_t't'c~^--"
PDGNAME[8852]	= "Omega'_t't'b^+"
PDGNAME[-8852]	= "Omega'_t't'b~^-"
PDGNAME[8854]	= "Omega*_t't'b^+"
PDGNAME[-8854]	= "Omega*_t't'b~^-"
PDGNAME[8862]	= "Omega'_t't't^++"
PDGNAME[-8862]	= "Omega'_t't't~^--"
PDGNAME[8864]	= "Omega*_t't't^++"
PDGNAME[-8864]	= "Omega*_t't't~^--"
PDGNAME[8872]	= "Omega'_t't'b'^+"
PDGNAME[-8872]	= "Omega'_t't'b'~^-"
PDGNAME[8874]	= "Omega*_t't'b'^+"
PDGNAME[-8874]	= "Omega*_t't'b'~^-"
PDGNAME[8884]	= "Omega*_t't't'^++"
PDGNAME[-8884]	= "Omega*_t't't'~^--"
PDGNAME[9990]	= "odderon"
PDGNAME[10022]	= "virtual-photon"
PDGNAME[10111]	= "a_0(1450)^0"
PDGNAME[10113]	= "b_1(1235)^0"
PDGNAME[10115]	= "pi_2(1670)^0"
PDGNAME[10211]	= "a_0(1450)^+"
PDGNAME[-10211]	= "a_0(1450)^-"
PDGNAME[10213]	= "b_1(1235)^+"
PDGNAME[-10213]	= "b_1(1235)^-"
PDGNAME[10215]	= "pi_2(1670)^+"
PDGNAME[-10215]	= "pi_2(1670)^-"
PDGNAME[10221]	= "f_0(1370)"
PDGNAME[10223]	= "h_1(1170)"
PDGNAME[10225]	= "eta_2(1645)"
PDGNAME[10311]	= "K*_0(1430)^0"
PDGNAME[-10311]	= "K*_0(1430)~^0"
PDGNAME[10313]	= "K_1(1270)^0"
PDGNAME[-10313]	= "K_1(1270)~^0"
PDGNAME[10315]	= "K_2(1770)^0"
PDGNAME[-10315]	= "K_2(1770)~^0"
PDGNAME[10321]	= "K*_0(1430)^+"
PDGNAME[-10321]	= "K*_0(1430)^-"
PDGNAME[10323]	= "K_1(1270)^+"
PDGNAME[-10323]	= "K_1(1270)^-"
PDGNAME[10325]	= "K_2(1770)^+"
PDGNAME[-10325]	= "K_2(1770)^-"
PDGNAME[10331]	= "f_0(1710)"
PDGNAME[10333]	= "h_1(1380)"
PDGNAME[10335]	= "eta_2(1870)"
PDGNAME[10411]	= "D*_0(2400)^+"
PDGNAME[-10411]	= "D*_0(2400)^-"
PDGNAME[10413]	= "D_1(2420)^+"
PDGNAME[-10413]	= "D_1(2420)^-"
PDGNAME[10421]	= "D*_0(2400)^0"
PDGNAME[-10421]	= "D*_0(2400)~^0"
PDGNAME[10423]	= "D_1(2420)^0"
PDGNAME[-10423]	= "D_1(2420)~^0"
PDGNAME[10431]	= "D*_s0(2317)^+"
PDGNAME[-10431]	= "D*_s0(2317)^-"
PDGNAME[10433]	= "D_s1(2536)^+"
PDGNAME[-10433]	= "D_s1(2536)^-"
PDGNAME[10441]	= "chi_c0(1P)"
PDGNAME[10443]	= "hc(1P)"
PDGNAME[10511]	= "B*_0^0"
PDGNAME[-10511]	= "B*_0~^0"
PDGNAME[10513]	= "B_1(L)^0"
PDGNAME[-10513]	= "B_1(L)~^0"
PDGNAME[10521]	= "B*_0^+"
PDGNAME[-10521]	= "B*_0^-"
PDGNAME[10523]	= "B_1(L)^+"
PDGNAME[-10523]	= "B_1(L)^-"
PDGNAME[10531]	= "B*_s0^0"
PDGNAME[-10531]	= "B*_s0~^0"
PDGNAME[10533]	= "B_s1(L)^0"
PDGNAME[-10533]	= "B_s1(L)~^0"
PDGNAME[10541]	= "B*_c0^+"
PDGNAME[-10541]	= "B*_c0^-"
PDGNAME[10543]	= "B_c1(L)^+"
PDGNAME[-10543]	= "B_c1(L)^-"
PDGNAME[10551]	= "chi_b0(1P)"
PDGNAME[10553]	= "h_b(1P)"
PDGNAME[10555]	= "eta_b2(1D)"
PDGNAME[11114]	= "Delta(1700)^-"
PDGNAME[11116]	= "Delta(1930)^-"
PDGNAME[11216]	= "Delta(1930)^0"
PDGNAME[12112]	= "N(1440)^0"
PDGNAME[12114]	= "Delta(1700)^0"
PDGNAME[12116]	= "N(1680)^0"
PDGNAME[12126]	= "Delta(1930)^+"
PDGNAME[12212]	= "N(1440)^+"
PDGNAME[12214]	= "Delta(1700)^+"
PDGNAME[12216]	= "N(1680)^+"
PDGNAME[12224]	= "Delta(1700)^++"
PDGNAME[12226]	= "Delta(1930)^++"
PDGNAME[13112]	= "Sigma(1660)^-"
PDGNAME[-13112]	= "Sigma~(1660)^-"
PDGNAME[13114]	= "Sigma(1670)^-"
PDGNAME[-13114]	= "Sigma~(1670)^-"
PDGNAME[13116]	= "Sigma(1915)^-"
PDGNAME[-13116]	= "Sigma~(1915)^-"
PDGNAME[13122]	= "Lambda(1405)^0"
PDGNAME[-13122]	= "Lambda~(1405)^0"
PDGNAME[13124]	= "Lambda(1690)^0"
PDGNAME[-13124]	= "Lambda~(1690)^0"
PDGNAME[13126]	= "Lambda(1830)^0"
PDGNAME[-13126]	= "Lambda~(1830)^0"
PDGNAME[13212]	= "Sigma(1660)^0"
PDGNAME[-13212]	= "Sigma~(1660)^0"
PDGNAME[13214]	= "Sigma(1670)^0"
PDGNAME[-13214]	= "Sigma~(1670)^0"
PDGNAME[13216]	= "Sigma(1915)^0"
PDGNAME[-13216]	= "Sigma~(1915)^0"
PDGNAME[13222]	= "Sigma(1660)^+"
PDGNAME[-13222]	= "Sigma~(1660)^+"
PDGNAME[13224]	= "Sigma(1670)^+"
PDGNAME[-13224]	= "Sigma~(1670)^+"
PDGNAME[13226]	= "Sigma(1915)^+"
PDGNAME[-13226]	= "Sigma~(1915)^+"
PDGNAME[13314]	= "Xi(1820)^-"
PDGNAME[-13314]	= "Xi(1820)~^+"
PDGNAME[13324]	= "Xi(1820)^0"
PDGNAME[-13324]	= "Xi(1820)~^0"
PDGNAME[14122]	= "Lambda_c(2593)^+"
PDGNAME[-14122]	= "Lambda_c~(2593)^-"
PDGNAME[14124]	= "Lambda_c(2625)^+"
PDGNAME[-14124]	= "Lambda_c~(2625)^-"
PDGNAME[20022]	= "Cerenkov-radiation"
PDGNAME[20113]	= "a_1(1260)^0"
PDGNAME[20213]	= "a_1(1260)^+"
PDGNAME[-20213]	= "a_1(1260)^-"
PDGNAME[20223]	= "f_1(1285)"
PDGNAME[20313]	= "K_1(1400)^0"
PDGNAME[-20313]	= "K_1(1400)~^0"
PDGNAME[20315]	= "K_2(1820)^0"
PDGNAME[-20315]	= "K_2(1820)~^0"
PDGNAME[20323]	= "K_1(1400)^+"
PDGNAME[-20323]	= "K_1(1400)^-"
PDGNAME[20325]	= "K_2(1820)^+"
PDGNAME[-20325]	= "K_2(1820)^-"
PDGNAME[20333]	= "f_1(1420)"
PDGNAME[20413]	= "D_1(H)^+"
PDGNAME[-20413]	= "D_1(H)^-"
PDGNAME[20423]	= "D_1(2430)^0"
PDGNAME[-20423]	= "D_1(2430)~^0"
PDGNAME[20433]	= "D_s1(2460)^+"
PDGNAME[-20433]	= "D_s1(2460)^-"
PDGNAME[20443]	= "chi_c1(1P)"
PDGNAME[20513]	= "B_1(H)^0"
PDGNAME[-20513]	= "B_1(H)~^0"
PDGNAME[20523]	= "B_1(H)^+"
PDGNAME[-20523]	= "B_1(H)^-"
PDGNAME[20533]	= "B_s1(H)^0"
PDGNAME[-20533]	= "B_s1(H)~^0"
PDGNAME[20543]	= "B_c1(H)^+"
PDGNAME[-20543]	= "B_c1(H)^-"
PDGNAME[20553]	= "chi_b1(1P)"
PDGNAME[20555]	= "Upsilon_2(1D)"
PDGNAME[21112]	= "Delta(1910)^-"
PDGNAME[21114]	= "Delta(1920)^-"
PDGNAME[21212]	= "Delta(1910)^0"
PDGNAME[21214]	= "N(1700)^0"
PDGNAME[22112]	= "N(1535)^0"
PDGNAME[22114]	= "Delta(1920)^0"
PDGNAME[22122]	= "Delta(1910)^+"
PDGNAME[22124]	= "N(1700)^+"
PDGNAME[22212]	= "N(1535)^+"
PDGNAME[22214]	= "Delta(1920)^+"
PDGNAME[22222]	= "Delta(1910)^++"
PDGNAME[22224]	= "Delta(1920)^++"
PDGNAME[23112]	= "Sigma(1750)^-"
PDGNAME[-23112]	= "Sigma~(1750)^-"
PDGNAME[23114]	= "Sigma(1940)^-"
PDGNAME[-23114]	= "Sigma~(1940)^-"
PDGNAME[23122]	= "Lambda(1600)^0"
PDGNAME[-23122]	= "Lambda~(1600)^0"
PDGNAME[23124]	= "Lambda(1890)^0"
PDGNAME[-23124]	= "Lambda~(1890)^0"
PDGNAME[23126]	= "Lambda(2110)^0"
PDGNAME[-23126]	= "Lambda~(2110)^0"
PDGNAME[23212]	= "Sigma(1750)^0"
PDGNAME[-23212]	= "Sigma~(1750)^0"
PDGNAME[23214]	= "Sigma(1940)^0"
PDGNAME[-23214]	= "Sigma~(1940)^0"
PDGNAME[23222]	= "Sigma(1750)^+"
PDGNAME[-23222]	= "Sigma~(1750)^+"
PDGNAME[23224]	= "Sigma(1940)^+"
PDGNAME[-23224]	= "Sigma~(1940)^+"
PDGNAME[30113]	= "rho(1700)^0"
PDGNAME[30213]	= "rho(1700)^+"
PDGNAME[-30213]	= "rho(1700)^-"
PDGNAME[30223]	= "omega(1650)"
PDGNAME[30313]	= "K*(1680)^0"
PDGNAME[-30313]	= "K*(1680)~^0"
PDGNAME[30323]	= "K*(1680)^+"
PDGNAME[-30323]	= "K*(1680)^-"
PDGNAME[30443]	= "psi(3770)"
PDGNAME[30553]	= "Upsilon_1(1D)"
PDGNAME[31114]	= "Delta(1600)^-"
PDGNAME[31214]	= "N(1720)^0"
PDGNAME[32112]	= "N(1650)^0"
PDGNAME[32114]	= "Delta(1600)^0"
PDGNAME[32124]	= "N(1720)^+"
PDGNAME[32212]	= "N(1650)^+"
PDGNAME[32214]	= "Delta(1600)^+"
PDGNAME[32224]	= "Delta(1600)^++"
PDGNAME[33122]	= "Lambda(1670)^0"
PDGNAME[-33122]	= "Lambda~(1670)^0"
PDGNAME[42112]	= "N(1710)^0"
PDGNAME[42212]	= "N(1710)^+"
PDGNAME[43122]	= "Lambda(1800)^0"
PDGNAME[-43122]	= "Lambda~(1800)^0"
PDGNAME[53122]	= "Lambda(1810)^0"
PDGNAME[-53122]	= "Lambda~(1810)^0"
PDGNAME[100111]	= "pi(1300)^0"
PDGNAME[100113]	= "rho(1450)^0"
PDGNAME[100211]	= "pi(1300)^+"
PDGNAME[-100211]	= "pi(1300)^-"
PDGNAME[100213]	= "rho(1450)^+"
PDGNAME[-100213]	= "rho(1450)^-"
PDGNAME[100221]	= "eta(1295)"
PDGNAME[100223]	= "omega(1420)"
PDGNAME[100311]	= "K(1460)^0"
PDGNAME[-100311]	= "K(1460)~^0"
PDGNAME[100313]	= "K*(1410)^0"
PDGNAME[-100313]	= "K*(1410)~^0"
PDGNAME[100321]	= "K(1460)^+"
PDGNAME[-100321]	= "K(1460)^-"
PDGNAME[100323]	= "K*(1410)^+"
PDGNAME[-100323]	= "K*(1410)^-"
PDGNAME[100325]	= "K_2(1980)^+"
PDGNAME[-100325]	= "K_2(1980)^-"
PDGNAME[100331]	= "eta(1475)"
PDGNAME[100333]	= "phi(1680)"
PDGNAME[100411]	= "D(2S)^+"
PDGNAME[-100411]	= "D(2S)^-"
PDGNAME[100413]	= "D*(2S)^+"
PDGNAME[-100413]	= "D*(2S)^+"
PDGNAME[100421]	= "D(2S)^0"
PDGNAME[-100421]	= "D(2S)~^0"
PDGNAME[100423]	= "D*(2S)^0"
PDGNAME[-100423]	= "D*(2S)~^0"
PDGNAME[100441]	= "eta_c(2S)"
PDGNAME[100443]	= "psi(2S)"
PDGNAME[100445]	= "chi_c2(2P)"
PDGNAME[100551]	= "eta_b(2S)"
PDGNAME[100553]	= "Upsilon(2S)"
PDGNAME[100555]	= "chi_b2(2P)"
PDGNAME[100557]	= "Upsilon_3(2D)"
PDGNAME[110551]	= "chi_b0(2P)"
PDGNAME[110553]	= "h_b(2P)"
PDGNAME[110555]	= "eta_b2(2D)"
PDGNAME[120553]	= "chi_b1(2P)"
PDGNAME[120555]	= "Upsilon_2(2D)"
PDGNAME[130553]	= "Upsilon_1(2D)"
PDGNAME[200551]	= "eta_b(3S)"
PDGNAME[200553]	= "Upsilon(3S)"
PDGNAME[200555]	= "chi_b2(3P)"
PDGNAME[210551]	= "chi_b0(3P)"
PDGNAME[210553]	= "h_b(3P)"
PDGNAME[220553]	= "chi_b1(3P)"
PDGNAME[300553]	= "Upsilon(4S)"
PDGNAME[ 1000001] = "susy-d_L"
PDGNAME[-1000001] = "susy-d_L~"
PDGNAME[ 1000002] = "susy-u_L"
PDGNAME[-1000002] = "susy-u_L~"
PDGNAME[ 1000003] = "susy-s_L"
PDGNAME[-1000003] = "susy-s_L~"
PDGNAME[ 1000004] = "susy-c_L"
PDGNAME[-1000004] = "susy-c_L~"
PDGNAME[ 1000005] = "susy-b_1"
PDGNAME[-1000005] = "susy-b_1~"
PDGNAME[ 1000006] = "susy-t_1"
PDGNAME[-1000006] = "susy-t_1~"
PDGNAME[ 1000011] = "susy-e_L^-"
PDGNAME[-1000011] = "susy-e_L^+"
PDGNAME[ 1000012] = "susy-nu_eL"
PDGNAME[-1000012] = "susy-nu_eL~"
PDGNAME[ 1000013] = "susy-mu_L^-"
PDGNAME[-1000013] = "susy-mu_L^+"
PDGNAME[ 1000014] = "susy-nu_muL"
PDGNAME[-1000014] = "susy-nu_muL~"
PDGNAME[ 1000015] = "susy-tau_L^-"
PDGNAME[-1000015] = "susy-tau_L^+"
PDGNAME[ 1000016] = "susy-nu_tauL"
PDGNAME[-1000016] = "susy-nu_tauL~"
PDGNAME[ 1000021] = "gluino"
PDGNAME[ 1000022] = "susy-chi_1^0"
PDGNAME[ 1000023] = "susy-chi_2^0"
PDGNAME[ 1000024] = "susy-chi_1^+"
PDGNAME[-1000024] = "susy-chi_1^-"
PDGNAME[ 1000025] = "susy-chi_3^0"
PDGNAME[ 1000035] = "susy-chi_4^0"
PDGNAME[ 1000037] = "susy-chi_2^+"
PDGNAME[-1000037] = "susy-chi_2^-"
PDGNAME[ 1000039] = "gravitino"
PDGNAME[ 2000001] = "susy-d_R"
PDGNAME[-2000001] = "susy-d_R~"
PDGNAME[ 2000002] = "susy-u_R"
PDGNAME[-2000002] = "susy-u_R~"
PDGNAME[ 2000003] = "susy-s_R"
PDGNAME[-2000003] = "susy-s_R~"
PDGNAME[ 2000004] = "susy-c_R"
PDGNAME[-2000004] = "susy-c_R~"
PDGNAME[ 2000005] = "susy-b_R"
PDGNAME[-2000005] = "susy-b_R~"
PDGNAME[ 2000006] = "susy-t_R"
PDGNAME[-2000006] = "susy-t_R~"
PDGNAME[ 2000011] = "susy-e_R^-"
PDGNAME[-2000011] = "susy-e_R^+"
PDGNAME[ 2000012] = "susy-nu_eR"
PDGNAME[-2000012] = "susy-nu_eR~"
PDGNAME[ 2000013] = "susy-mu_R^-"
PDGNAME[-2000013] = "susy-mu_R^+"
PDGNAME[ 2000014] = "susy-nu_muR"
PDGNAME[-2000014] = "susy-nu_muR~"
PDGNAME[ 2000015] = "susy-tau_R^-"
PDGNAME[-2000015] = "susy-tau_R^+"
PDGNAME[ 2000016] = "susy-nu_tauR"
PDGNAME[-2000016] = "susy-nu_tauR~"

def particleName(pid):
    if PDGNAME.has_key(pid):
        return PDGNAME[pid]
    else:
        return 'noname'
    