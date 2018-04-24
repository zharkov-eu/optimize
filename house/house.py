from house_enums import *


class House(object):
    @property
    def MSSubClass(self):
        """Identifies the type of dwelling involved in the sale"""
        return getattr(self, '_MSSubClass')

    @MSSubClass.setter
    def MSSubClass(self, value):
        if not self.in_enum(int(value), MSSubClass):
            raise ValueError("%s is not in MSSubClass enum", value)
        setattr(self, '_MSSubClass', int(value))

    @property
    def MSZoning(self):
        """Identifies the general zoning classification of the sale"""
        return getattr(self, '_MSZoning')

    @MSZoning.setter
    def MSZoning(self, value):
        if not self.in_enum(value, MSZoning):
            raise ValueError("%s is not in MSZoning enum", value)
        setattr(self, '_MSZoning', value)

    @property
    def LotFrontage(self):
        """Linear feet of street connected to property (can be None)"""
        return getattr(self, '_LotFrontage')

    @LotFrontage.setter
    def LotFrontage(self, value):
        try:
            setattr(self, "_LotFrontage", int(value))
        except ValueError:
            setattr(self, "_LotFrontage", None)

    @property
    def LotArea(self):
        """Lot size in square feet"""
        return getattr(self, '_LotArea')

    @LotArea.setter
    def LotArea(self, value):
        setattr(self, "_LotArea", int(value))

    @property
    def Street(self):
        """Type of road access to property"""
        return getattr(self, '_Street')

    @Street.setter
    def Street(self, value):
        if not self.in_enum(value, Street):
            raise ValueError("%s is not in Street enum", value)
        setattr(self, "_Street", value)

    @property
    def Alley(self):
        """Type of alley access to property"""
        return getattr(self, '_Alley')

    @Alley.setter
    def Alley(self, value):
        if not self.in_enum(value, Alley):
            raise ValueError("%s is not in Alley enum", value)
        setattr(self, "_Alley", value)

    @property
    def LotShape(self):
        """General shape of property"""
        return getattr(self, '_LotShape')

    @LotShape.setter
    def LotShape(self, value):
        if not self.in_enum(value, LotShape):
            raise ValueError("%s is not in LotShape enum", value)
        setattr(self, "_LotShape", value)

    @property
    def LandContour(self):
        """Flatness of the property"""
        return getattr(self, '_LandContour')

    @LandContour.setter
    def LandContour(self, value):
        if not self.in_enum(value, LandContour):
            raise ValueError("%s is not in LandContour enum", value)
        setattr(self, "_LandContour", value)

    @property
    def Utilities(self):
        """Type of utilities available"""
        return getattr(self, '_Utilities')

    @Utilities.setter
    def Utilities(self, value):
        if not self.in_enum(value, Utilities):
            raise ValueError("%s is not in Utilities enum", value)
        setattr(self, "_Utilities", value)

    @property
    def OverallQual(self):
        """Rates the overall material and finish of the house"""
        return getattr(self, '_OverallQual')

    @OverallQual.setter
    def OverallQual(self, value):
        setattr(self, "_OverallQual", int(value))

    @property
    def OverallCond(self):
        """Rates the overall condition of the house"""
        return getattr(self, '_OverallCond')

    @OverallCond.setter
    def OverallCond(self, value):
        setattr(self, "_OverallCond", int(value))

    @property
    def FirstFlrSF(self):
        """First Floor square feet"""
        return getattr(self, '_FirstFlrSF')

    @FirstFlrSF.setter
    def FirstFlrSF(self, value):
        setattr(self, "_FirstFlrSF", int(value))

    @property
    def SecondFlrSF(self):
        """Second floor square feet"""
        return getattr(self, '_SecondFlrSF')

    @SecondFlrSF.setter
    def SecondFlrSF(self, value):
        setattr(self, "_SecondFlrSF", int(value))


    @property
    def LowQualFinSF(self):
        """Low quality finished square feet (all floors)"""
        return getattr(self, '_LowQualFinSF')

    @LowQualFinSF.setter
    def LowQualFinSF(self, value):
        setattr(self, "_LowQualFinSF", int(value))

    @property
    def GarageType(self):
        """Garage location"""
        return getattr(self, '_GarageType')

    @GarageType.setter
    def GarageType(self, value):
        if not self.in_enum(value, GarageType):
            raise ValueError("%s is not in GarageType enum", value)
        setattr(self, "_GarageType", value)

    @property
    def PoolQC(self):
        """Pool quality"""
        return getattr(self, '_PoolQC')

    @PoolQC.setter
    def PoolQC(self, value):
        if not self.in_enum(value, PoolQC):
            raise ValueError("%s is not in PoolQC enum", value)
        setattr(self, "_PoolQC", value)

    @property
    def SalePrice(self):
        """Sale price"""
        return getattr(self, '_SalePrice')

    @SalePrice.setter
    def SalePrice(self, value):
        setattr(self, "_SalePrice", int(value))

    @staticmethod
    def in_enum(value, enum):
        return any(value == item.value for item in enum)

    def __init__(self, params):
        if not isinstance(params, dict):
            raise TypeError("params passed to House constructor is not a dict")

        if "MSSubClass" in params:
            self.MSSubClass = params.get("MSSubClass")
        if "MSZoning" in params:
            self.MSZoning = params.get("MSZoning")
        if "LotFrontage" in params:
            self.LotFrontage = params.get("LotFrontage")
        if "LotArea" in params:
            self.LotArea = params.get("LotArea")
        if "Street" in params:
            self.Street = params.get("Street")
        if "Alley" in params:
            self.Alley = params.get("Alley")
        if "LotShape" in params:
            self.LotShape = params.get("LotShape")
        if "LandContour" in params:
            self.LandContour = params.get("LandContour")
        if "Utilities" in params:
            self.Utilities = params.get("Utilities")
        if "OverallQual" in params:
            self.OverallQual = params.get("OverallQual")
        if "OverallCond" in params:
            self.OverallCond = params.get("OverallCond")
        if "1stFlrSF" in params:
            self.FirstFlrSF = params.get("1stFlrSF")
        if "2ndFlrSF" in params:
            self.SecondFlrSF = params.get("2ndFlrSF")
        if "LowQualFinSF" in params:
            self.LowQualFinSF = params.get("LowQualFinSF")
        if "GarageType" in params:
            self.GarageType = params.get("GarageType")
        if "PoolQC" in params:
            self.PoolQC = params.get("PoolQC")
        if "SalePrice" in params:
            self.SalePrice = params.get("SalePrice")


def house_filter(house, houseFilter):
    fit = True
    for attr, value in vars(houseFilter).iteritems():
        try:
            fit = value == vars(house).get(attr)
        except ValueError:
            fit = False
        if not fit:
            break
    return fit
