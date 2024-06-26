from enum import Enum


class ColorsEnum(str, Enum):
    RED = 'red'
    GREEN = 'green'
    BLUE = 'blue'
    BLACK = 'black'
    WHITE = 'white'
    YELLOW = 'yellow'
    MAGENTA = 'magenta'
    CYAN = 'cyan'
    PINK = 'pink'
    BROWN = 'brown'


class StatisticEnum(str, Enum):
    MEAN = 'mean'
    MEDIAN = 'median'
    SUM = 'muc'
    MAX = 'max'
    MIN = 'min'
    STDEV = 'stdev'
    VAR = 'var'
    AREA = 'area'
    VARBC = 'varbc'


class ShapeEnum(str, Enum):
    DISK = 'disk'
    SQUARE = 'square'


class PSFTypeEnum(str, Enum):
    BESSEL = 'bessel'
    GAUSS = 'gauss'
    EXP = 'exp'
    CONFOCAL_BESSEL = 'confocal_bessel'
    ONES = 'ones'


class Connectivity3dEnum(str, Enum):
    SIX = '6'
    TWENTY_SIX = '26'


class ConnectivityEnum(str, Enum):
    FOUR = '4'
    EIGHT = '8'


class DistanceTransformEnum(str, Enum):
    THREE = '3'
    FIVE = '5'
    SEVEN = '7'


class SoloEnum(str, Enum):
    NUCLEAR = 'nuclear'
    ENERGRID = 'energid'
    OUTNUC = 'outnuc'


class APEnum(str, Enum):
    A = 'A'
    P = 'P'


class AndifFunction_typeEnum(str, Enum):
    EXP = 'exp'
    FRAC = 'frac'


class Plot_spFunctionEnum(str, Enum):
    LOG = 'log'
    EQN = 'eqn'


class SselectRuleEnum(str, Enum):
    ACCEPT = 'accept'
    REJECT = 'reject'


class ThresholdMethodEnum(str, Enum):
    PLAIN = 'plain'
    OTSU = 'otsu'


class VtxtFormatEnum(str, Enum):
    XYZ = 'xyz'
    VRML_SPHERE = 'vrml_sphere'


class Surf3dFormatEnum(str, Enum):
    VTK = 'vtk'
    OOGL = 'oogl'
    OOGLB = 'ooglb'
    GTS = 'gts'


class Grid3d_iTypeEnum(str, Enum):
    CARTESIAN = 'cartesian'
    ELLIPTICAL = 'elliptical'


class Surf3dfullFunctionEnum(str, Enum):
    CARTESIAN = 'cartesian'
    TETRA = 'tetra'
    TETRA_BOUNDED = 'tetra_bounded'
    TETRA_BCL = 'tetra_bcl'


class MlsregTypeEnum(str, Enum):
    AFFINE = 'affine'
    SIMILAR = 'similar'
    RIGID = 'rigid'


class ContrasttransferTransfer_funcEnum(str, Enum):
    EXP = 'exp'
    LOG = 'log'
    INVLOG = 'invlog'
    SQR = 'sqr'
    SQRT = 'sqrt'
    TANH = 'tanh'


