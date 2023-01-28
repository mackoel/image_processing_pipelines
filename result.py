from cvlib import *
from files_manager import FilesManager

input_A = FilesManager('file:///users/kkozlov/storage1/c_projects/ProStack/examples/k167/d218.tif')
input_B = FilesManager('file:///users/kkozlov/storage1/c_projects/ProStack/examples/k167/f218.tif')
input_C = FilesManager('file:///users/kkozlov/storage1/c_projects/ProStack/examples/k167/r218.tif')


A = strel()
B = strel()
C = strel()
D = strel()
E = strel()
F = strel()
G = strel()
H = expand(input_A)
I = threshold(input_A)
J = expand(input_B)
K = expand(input_C)
L = mul(I + input_A)
M = invert(J)
N = heq(K)
O = shrink(J)
P = heqm(L + I)
Q = heq(M)
R = despekle(N)
S = andif(P)
T = gerosion(R + C)
U = despekle(Q)
V = expand(S)
W = gerosion(U + C)
X = gerosion(V + A)
Y = avg2(W + T)
Z = reconstruct(V + X)
BA = invert(Z)
BB = andif(Y)
BC = gerosion(BA + A)
BD = gerosion(BB + D)
BE = reconstruct(BA + BC)
BF = reconstruct(BB + BD)
BG = cwtsd(BE)
BH = invert(BF)
BI = mul(BG + V)
BJ = gerosion(BH + D)
BK = threshold(BI)
BL = reconstruct(BH + BJ)
BM = gerosion(BK + B)
BN = gclose(BL + F)
BO = median(BM + B)
BP = gmag(BN)
BQ = gmag(BO)
BR = gerosion(BO + G)
BS = invert(BO)
BT = threshold(BP)
BU = threshold(BQ)
BV = gmag(BR)
BW = mul(BS + BN)
BX = movl2(BU + H)
BY = cwtsd(BW)
BZ = shrink(BV)
CA = reconstruct(BY + BO)
CB = minusabs(CA + BY)
CC = gclose(CB + E)
CD = invert(CC)
CE = mul(CA + CD)
CF = gerosion(CE + E)
CG = invert(CF)
CH = mul(CG + CD)
CI = movl3(J + BV + CH)
CJ = shrink(CH)
CK = movl3(O + BZ + CJ)
CL = max2(CJ + O)
