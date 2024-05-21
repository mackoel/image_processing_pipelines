from cvlib import *
from cv_lib_parallel import CVLibParallel
from files_manager import File

def main(parallel_manager: CVLibParallel):
    input_A = File(r'output/.tif')

    output_A = r'output/_lum.tif'
    output_B = r'output/_mask.tif'
    output_C = r'output/_list.txt'
    output_D = r'output/_mark.tif'
    output_E = r'output/_tab.csv'
    output_F = r'output/_movl.tif'


    res = parallel_manager.run({
        'A': {'func': strel, 'args': (7, 7, ShapeEnum.DISK,)},
        'B': {'func': strel, 'args': (7, 7, ShapeEnum.DISK,)},
        'C': {'func': strel, 'args': (3, 3, ShapeEnum.SQUARE,)},
        'D': {'func': strel, 'args': (5, 5, ShapeEnum.DISK,)},
    })
    A = res['A'].get()
    B = res['B'].get()
    C = res['C'].get()
    D = res['D'].get()

    E = convert(input_A, 'R')

    res = parallel_manager.run({
        'F': {'func': ContrastTransfer, 'args': (E[1], 0.0, 0.9, 0.1, 0.05, 1.0, 1, ContrasttransferTransfer_funcEnum.INVLOG,)},
        'G': {'func': heq, 'args': (E[1],)},
    })
    F = res['F'].get()
    G = res['G'].get()


    res = parallel_manager.run({
        'H': {'func': invert, 'args': (G[1],)},
        'I': {'func': lhbg, 'args': (G[1] + B[1],)},
    })
    H = res['H'].get()
    I = res['I'].get()


    res = parallel_manager.run({
        'J': {'func': hystthresh, 'args': (H[1], 120.0, 130.0, 100, ConnectivityEnum.FOUR,)},
        'K': {'func': invert, 'args': (I[1],)},
    })
    J = res['J'].get()
    K = res['K'].get()

    L = threshold(K[1], 200.0, ThresholdMethodEnum.PLAIN, '-r 1')
    M = mcrop(L[1], 0, 0, 100, 100)
    N = mpad(M[1], 0, 0, 100, 100)
    O = vaff(L[1] + N[1], 1, -1, 0.0)
    P = mcrop(O[1], 100, 100, 0, 0)
    Q = mpad(P[1], 100, 100, 0, 0)
    R = vaff(O[1] + Q[1], 1, -1, 0.0)
    S = reconstruct(J[1] + R[1], ConnectivityEnum.FOUR)
    T = vaff(J[1] + S[1], 1, -1, 0.0)
    U = correlate(T[1], -1, 4.0)
    V = median(U[1] + B[1], 1)
    W = gerosion(V[1] + B[1], 1)
    X = reconstruct(V[1] + W[1], ConnectivityEnum.FOUR)
    Y = mul(X[1] + X[1])
    Z = hystthresh(Y[1], 15.0, 75.0, 100, ConnectivityEnum.EIGHT)
    BA = gclose(Z[1] + A[1], 1)
    BB = qu3dinit(BA[1] + BA[1], Connectivity3dEnum.TWENTY_SIX, 'channel1')
    BC = qu3dtrans(BB[1] + BB[1], 'Shape:0', '0', '0', 500, 20000)
    BD = qumap3d(BA[1] + BC[1], Connectivity3dEnum.TWENTY_SIX, 'channel1', 3)
    BE = chole(BD[1] + A[1])
    BF = vmax(BE[1] + BD[1])

    res = parallel_manager.run({
        'BG': {'func': gdilation, 'args': (BF[1] + A[1], 2,)},
        'BH': {'func': quthicken, 'args': (BF[1], Connectivity3dEnum.TWENTY_SIX, 4,)},
    })
    BG = res['BG'].get()
    BH = res['BH'].get()

    BI = threshold(BH[1], 1, ThresholdMethodEnum.PLAIN, '-r 1')
    BJ = mul(BI[1] + BG[1])
    BK = median(BJ[1] + D[1], 1)

    res = parallel_manager.run({
        'BL': {'func': gerosion, 'args': (BK[1] + C[1], 1,)},
        'BM': {'func': qumark3d, 'args': (BK[1], Connectivity3dEnum.SIX,)},
        'BN': {'func': qu3dinit, 'args': (F[1] + BK[1], Connectivity3dEnum.TWENTY_SIX, 'channel1',)},
    })
    BL = res['BL'].get()
    BM = res['BM'].get()
    BN = res['BN'].get()


    res = parallel_manager.run({
        'BO': {'func': vaff, 'args': (BK[1] + BL[1], 1.0, -1.0, 0.0,)},
        'BP': {'func': gdilation, 'args': (BM[1] + A[1], 1,)},
        'BQ': {'func': qu3d2csv, 'args': (BN[1],)},
    })
    BO = res['BO'].get()
    BP = res['BP'].get()
    BQ = res['BQ'].get()

    BR = movl2(F[1] + BO[1], ColorsEnum.WHITE, ColorsEnum.YELLOW)
    BS = impute_text(BR[1] + BQ[1], '255x0x0', 1.0, 2)
if __name__ == "__main__":
    main(CVLibParallel())
