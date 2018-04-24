from enum import Enum


class HouseParamsEnum(Enum):
    LandContour = 1
    Utilities = 2


class MSSubClass(Enum):
    """Identifies the type of dwelling involved in the sale"""
    MS20 = 20  # 1-STORY 1946 & NEWER ALL STYLES
    MS30 = 30  # 1-STORY 1945 & OLDER
    MS40 = 40  # 1-STORY W/FINISHED ATTIC ALL AGES
    MS45 = 45  # 1-1/2 STORY - UNFINISHED ALL AGES
    MS50 = 50  # 1-1/2 STORY FINISHED ALL AGES
    MS60 = 60  # 2-STORY 1946 & NEWER
    MS70 = 70  # 2-STORY 1945 & OLDER
    MS75 = 75  # 2-1/2 STORY ALL AGES
    MS80 = 80  # SPLIT OR MULTI-LEVEL
    MS85 = 85  # SPLIT FOYER
    MS90 = 90  # DUPLEX - ALL STYLES AND AGES
    MS120 = 120  # 1-STORY PUD (Planned Unit Development) - 1946 & NEWER
    MS150 = 150  # 1-1/2 STORY PUD - ALL AGES
    MS160 = 160  # 2-STORY PUD - 1946 & NEWER
    MS180 = 180  # PUD - MULTILEVEL - INCL SPLIT LEV/FOYER
    MS190 = 190  # 2 FAMILY CONVERSION - ALL STYLES AND AGES


class MSZoning(Enum):
    """Identifies the general zoning classification of the sale"""
    Agriculture = "A"
    Commercial = "C"
    FloatingVillageResidential = "FV"
    Industrial = "I"
    ResidentialHighDensity = "RH"
    ResidentialLowDensity = "RL"
    ResidentialLowDensityPark = "RP"
    ResidentialMediumDensity = "RM"


class Street(Enum):
    """Type of road access to property"""
    Gravel = "Grvl"
    Paved = "Pave"


class Alley(Enum):
    """Type of alley access to property"""
    Gravel = "Grvl"
    Paved = "Pave"
    NoAlleyAccess = "NA"


class LotShape(Enum):
    """General shape of property"""
    Regular = "Reg"
    SlightlyIrregular = "IR1"
    ModeratelyIrregular = "IR2"
    Irregular = "IR3"


class LandContour(Enum):
    """Flatness of the property"""
    Level = "Lvl"  # Near Flat/Level
    Banked = "Bnk"  # Quick and significant rise from street grade to building
    Hillside = "HLS"  # Significant slope from side to side
    Depression = "Low"


class Utilities(Enum):
    """Type of utilities available"""
    AllPublicUtilities = "AllPub"  # All public Utilities (E,G,W,& S)
    ElectricityGasWater = "NoSewr"  # Electricity, Gas, and Water (Septic Tank)
    ElectricityGas = "NoSeWa"  # Electricity and Gas Only
    ElectricityOnly = "ELO"  # Electricity only


class LotConfig(Enum):
    """Lot configuration"""
    InsideLot = "Inside"  # Inside lot
    CornerLot = "Corner"  # Corner lot
    CulDeSac = "CulDSac"  # Cul-de-sac
    FrontageOn2Sides = "FR2"  # Frontage on 2 sides of property
    FrontageOn3Sides = "FR3"  # Frontage on 3 sides of property


class LandSlope(Enum):
    """Slope of property"""
    GentleSlope = "Gtl"
    ModerateSlope = "Mod"
    SevereSlope = "Sev"


class Neighborhood(Enum):
    """Physical locations within Ames city limits"""
    BloomingtonHeights = "Blmngtn"
    Bluestem = "Blueste"
    Briardale = "BrDale"
    Brookside = "BrkSide"
    ClearCreek = "ClearCr"
    CollegeCreek = "CollgCr"
    Crawford = "Crawfor"
    Edwards = "Edwards"
    Gilbert = "Gilbert"
    IowaDOTAndRailRoad = "IDOTRR"
    MeadowVillage = "MeadowV"
    Mitchell = "Mitchel"
    NorthAmes = "Names"
    Northridge = "NoRidge"
    NorthparkVilla = "NPkVill"
    NorthridgeHeights = "NridgHt"
    NorthwestAmes = "NWAmes"
    OldTown = "OldTown"
    IowaStateUniversity = "SWISU"  # South & West of Iowa State University
    Sawyer = "Sawyer"
    SawyerWest = "SawyerW"
    Somerset = "Somerst"
    StoneBrook = "StoneBr"
    Timberland = "Timber"
    Veenker = "Veenker"


class Condition1(Enum):
    """Proximity to various conditions"""
    AdjacentToArterialStreet = "Artery"
    AdjacentToFeederStreet = "Feedr"
    Normal = "Norm"
    Within200OfNorthSouthRailroad = "RRNn"
    AdjacentToNorthSouthRailroad = "RRAn"
    NearPositiveOffSiteFeature = "PosN"  # Park, greenbelt, etc.
    AdjacentToPostiveOffSiteFeature = "PosA"
    Within20OfEastWestRailroad = "RRNe"
    AdjacentToEastWestRailroad = "RRAe"


class Condition2(Enum):
    """Proximity to various conditions (if more than one is present)"""
    AdjacentToArterialStreet = "Artery"
    AdjacentToFeederStreet = "Feedr"
    Normal = "Norm"
    Within200OfNorthSouthRailroad = "RRNn"
    AdjacentToNorthSouthRailroad = "RRAn"
    NearPositiveOffSiteFeature = "PosN"  # Park, greenbelt, etc.
    AdjacentToPostiveOffSiteFeature = "PosA"
    Within20OfEastWestRailroad = "RRNe"
    AdjacentToEastWestRailroad = "RRAe"


class BldgType(Enum):
    """Type of dwelling"""
    SingleFamilyDetached = "1Fam"
    TwoFamilyConversion = "2FmCon"  # originally built as one-family dwelling
    Duplex = "Duplx"
    TownhouseEndUnit = "TwnhsE"
    TownhouseInsideUnit = "TwnhsI"


class HouseStyle(Enum):
    """Style of dwelling"""
    OneStory = "1Story"
    OneAndOneHalfStory2ndLevelFinished = "1.5Fin"
    OneAndOneHalfStory2ndLevelUnfinished = "1.5Unf"
    TwoStory = "2Story"
    TwoAndOneHalfStory2ndLevelFinished = "2.5Fin"
    TwoAndOneHalfStory2ndLevelUnfinished = "2.5Unf"
    SplitFoyer = "SFoyer"
    SplitLevel = "SLvl"


class OverallQual(Enum):
    """Rates the overall material and finish of the house"""
    VeryExcellent = 10
    Excellent = 9
    VeryGood = 8
    Good = 7
    AboveAverage = 6
    Average = 5
    BelowAverage = 4
    Fair = 3
    Poor = 2
    VeryPoor = 1


class OverallCond(Enum):
    """Rates the overall condition of the house"""
    VeryExcellent = 10
    Excellent = 9
    VeryGood = 8
    Good = 7
    AboveAverage = 6
    Average = 5
    BelowAverage = 4
    Fair = 3
    Poor = 2
    VeryPoor = 1


class RoofStyle(Enum):
    """Type of roof"""
    Flat = "Flat"
    Gable = "Gable"
    Gambrel = "Gambrel"
    Hip = "Hip"
    Mansard = "Mansard"
    Shed = "Shed"


class RoofMatl(Enum):
    """Roof material"""
    ClayOrTile = "ClyTile"
    CompositeShingle = "CompShg"  # Standard (Composite) Shingle
    Membrane = "Membran"
    Metal = "Metal"
    Roll = "Roll"
    GravelAndTar = "Tar&Grv"
    WoodShakes = "WdShake"
    WoodShingles = "WdShngl"


class Exterior1st(Enum):
    """Exterior covering on house"""
    AsbestosShingles = "AsbShng"
    AsphaltShingles = "AsphShn"
    BrickCommon = "BrkComm"
    BrickFace = "BrkFace"
    CinderBlock = "CBlock"
    CementBoard = "CemntBd"
    HardBoard = "HdBoard"
    ImitationStucco = "ImStucc"
    MetalSiding = "MetalSd"
    Other = "Other"
    Plywood = "Plywood"
    PreCastExterior = "PreCast"
    Stone = "Stone"
    Stucco = "Stucco"
    VinylSiding = "VinylSd"
    WoodSiding = "Wd Sdng"
    WoodShingles = "WdShing"


class Exterior2nd(Enum):
    """Exterior covering on house (if more than one material)"""
    AsbestosShingles = "AsbShng"
    AsphaltShingles = "AsphShn"
    BrickCommon = "BrkComm"
    BrickFace = "BrkFace"
    CinderBlock = "CBlock"
    CementBoard = "CemntBd"
    HardBoard = "HdBoard"
    ImitationStucco = "ImStucc"
    MetalSiding = "MetalSd"
    Other = "Other"
    Plywood = "Plywood"
    PreCastExterior = "PreCast"
    Stone = "Stone"
    Stucco = "Stucco"
    VinylSiding = "VinylSd"
    WoodSiding = "Wd Sdng"
    WoodShingles = "WdShing"


class MasVnrType(Enum):
    """Masonry veneer type"""
    BrickCommon = "BrkCmn"
    BrickFace = "BrkFace"
    CinderBlock = "CBlock"
    NONE = "None"
    Stone = "Stone"


class ExterQual(Enum):
    """Evaluates the quality of the material on the exterior"""
    Excellent = "Ex"
    Good = "Gd"
    Average = "TA"  # Average/Typical
    Fair = "Fa"
    Poor = "Po"


class ExterCond(Enum):
    """Evaluates the present condition of the material on the exterior"""
    Excellent = "Ex"
    Good = "Gd"
    Average = "TA"  # Average/Typical
    Fair = "Fa"
    Poor = "Po"


class Foundation(Enum):
    """Type of foundation"""
    BrickAndTile = "BrkTil"
    CinderBlock = "CBlock"
    PouredContrete = "PConc"
    Slab = "Slab"
    Stone = "Stone"
    Wood = "Wood"


class BsmtQual(Enum):
    """Evaluates the height of the basement"""
    Excellent = "Ex"  # (100+ inches)
    Good = "Gd"  # (90-99 inches)
    Typical = "TA"  # (80-89 inches)
    Fair = "Fa"  # (70-79 inches)
    Poor = "Po"  # (<70 inches)
    NoBasement = "NA"


class BsmtCond(Enum):
    """Evaluates the general condition of the basement"""
    Excellent = "Ex"
    Good = "Gd"
    Typical = "TA"  # slight dampness allowed
    Fair = "Fa"  # dampness or some cracking or settling
    Poor = "Po"  # severe cracking, settling, or wetness
    NoBasement = "NA"


class BsmtExposure(Enum):
    """Refers to walkout or garden level walls"""
    Good = "Gd"
    Average = "Av"  # split levels or foyers typically score average or above
    Mimimum = "Mn"
    NoExposure = "No"
    NoBasement = "NA"


class BsmtFinType1(Enum):
    """Rating of basement finished area"""
    GoodLivingQuarters = "GLQ"
    AverageLivingQuarters = "ALQ"
    BelowAverageLivingQuarters = "BLQ"
    AverageRecRoom = "Rec"
    LowQuality = "LwQ"
    Unfinshed = "Unf"
    NoBasement = "NA"


class BsmtFinType2(Enum):
    """Rating of basement finished area (if multiple types)"""
    GoodLivingQuarters = "GLQ"
    AverageLivingQuarters = "ALQ"
    BelowAverageLivingQuarters = "BLQ"
    AverageRecRoom = "Rec"
    LowQuality = "LwQ"
    Unfinshed = "Unf"
    NoBasement = "NA"


class Heating(Enum):
    """Type of heating"""
    FloorFurnace = "Floor"
    GasForcedWarmAirFurnace = "GasA"
    GasHotWaterOrSteamHeat = "GasW"
    GravityFurnace = "Grav"
    HotWaterOrSteamHeatOtherThanGas = "OthW"
    WallFurnace = "Wall"


class HeatingQC(Enum):
    """Heating quality and condition"""
    Excellent = "Ex"
    Good = "Gd"
    Average = "TA"  # Average/Typical
    Fair = "Fa"
    Poor = "Po"


class CentralAir(Enum):
    """Central air conditioning"""
    No = "N"
    Yes = "Y"


class Electrical(Enum):
    """Electrical system"""
    StandardCircuitBreakersAndRomex = "SBrkr"
    FuseBoxOver60AMPAndAllRomexWiring = "FuseA"
    AMP60FuseBoxAndMostlyRomexWiring = "FuseF"  # (Fair)
    AMP60FuseBoxAndMostlyKnobAndTubeWiring = "FuseP"  # (Poor)
    Mixed = "Mix"


class KitchenQual(Enum):
    """Kitchen quality"""
    Excellent = "Ex"
    Good = "Gd"
    Average = "TA"  # Average/Typical
    Fair = "Fa"
    Poor = "Po"


class Functional(Enum):
    """Home functionality (Assume typical unless deductions are warranted)"""
    TypicalFunctionality = "Typ"
    MinorDeductions1 = "Min1"
    MinorDeductions2 = "Min2"
    ModerateDeductions = "Mod"
    MajorDeductions1 = "Maj1"
    MajorDeductions2 = "Maj2"
    SeverelyDamaged = "Sev"
    Salvageonly = "Sal"


class FireplaceQu(Enum):
    """Fireplace quality"""
    Excellent = "Ex"  # Exceptional Masonry Fireplace
    Good = "Gd"  # Masonry Fireplace in main level
    Average = "TA"  # Prefabricated Fireplace in main living area or Masonry Fireplace in basement
    Fair = "Fa"  # Prefabricated Fireplace in basement
    Poor = "Po"  # Ben Franklin Stove
    NoFireplace = "NA"


class GarageType(Enum):
    """Garage location"""
    MoreThanOneType = "2Types"
    AttachedToHome = "Attchd"
    BasementGarage = "Basment"
    BuiltIn = "BuiltIn"  # Garage part of house - typically has room above garage
    CarPort = "CarPort"
    DetachedFromHome = "Detchd"
    NoGarage = "NA"


class GarageFinish(Enum):
    """Interior finish of the garage"""
    Finished = "Fin"
    RoughFinished = "RFn"
    Unfinished = "Unf"
    NoGarage = "NA"


class GarageQual(Enum):
    """Garage quality"""
    Excellent = "Ex"
    Good = "Gd"
    Typical = "TA"  # Typical/Average
    Fair = "Fa"
    Poor = "Po"
    NoGarage = "NA"


class GarageCond(Enum):
    """Garage condition"""
    Excellent = "Ex"
    Good = "Gd"
    Typical = "TA"  # Typical/Average
    Fair = "Fa"
    Poor = "Po"
    NoGarage = "NA"


class PavedDrive(Enum):
    """Paved driveway"""
    Paved = "Y"
    PartialPavement = "P"
    DirtOrGravel = "N"


class PoolQC:
    """Pool quality"""
    Excellent = "Ex"
    Good = "Gd"
    Typical = "TA"  # Typical/Average
    Fair = "Fa"
    NoPool = "NA"


class Fence(Enum):
    """Fence quality"""
    GoodPrivacy = "GdPrv"
    MinimumPrivacy = "MnPrv"
    GoodWood = "GdWo"
    MinimumWoodOrWire = "MnWw"
    NoFence = "NA"


class MiscFeature(Enum):
    """Miscellaneous feature not covered in other categories"""
    Elevator = "Elev"
    Garage2nd = "Gar2"  # if not described in garage section
    Other = "Othr"
    Shed = "Shed"  # (over 100 SF)
    TennisCourt = "TenC"
    NONE = "NA"


class SaleType(Enum):
    """Type of sale"""
    WarrantyDeedConventional = "WD"
    WarrantyDeedCash = "CWD"
    WarrantyDeedVALoan = "VWD"
    HomeJustConstructedAndSold = "New"
    CourtOfficerDeedOrEstate = "COD"
    Contract15PercentDownPaymentRegularTerms = "Con"
    ContractLowDownPaymentAndLowInterest = "ConLw"
    ContractLowInterest = "ConLI"
    ContractLowDown = "ConLD"
    Other = "Oth"


class SaleCondition(Enum):
    """Condition of sale"""
    Normal = "Normal"  # Normal Sale
    Abnormal = "Abnorml"  # Abnormal Sale -  trade, foreclosure, short sale
    AdjoiningLandPurchase = "AdjLand"  # Adjoining Land Purchase
    Allocation = "Alloca"  # - two linked properties with separate deeds, typically condo with a garage unit
    Family = "Family"  # Sale between family members
    Partial = "Partial"  # Home was not completed when last assessed (associated with New Homes)
