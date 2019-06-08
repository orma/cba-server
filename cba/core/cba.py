import numpy as np

from .default import (
    dDiscount_Rate, dEconomic_Factor, dGrowth, dTrafficLevels, dVehicleFleet,
    iSurfaceDefaults, dWidthDefaults, dConditionData, dRoadWorks,
    dRecurrent, dRecMult, dWorkEvaluated, dm_coeff, dVOC, dSPEED, dRoadDet
)


class CostBenefitAnalysisModel:

    def __init__(self):
        self.dDiscount_Rate = dDiscount_Rate
        self.dEconomic_Factor = dEconomic_Factor
        self.dGrowth = dGrowth
        self.dTrafficLevels = dTrafficLevels
        self.dVehicleFleet = dVehicleFleet
        self.iSurfaceDefaults = iSurfaceDefaults
        self.dWidthDefaults = dWidthDefaults
        self.dConditionData = dConditionData
        self.dRoadWorks = dRoadWorks
        self.dRecurrent = dRecurrent
        self.dRecMult = dRecMult
        self.dWorkEvaluated = dWorkEvaluated
        self.dm_coeff = dm_coeff
        self.dVOC = dVOC
        self.dSPEED = dSPEED
        self.dRoadDet = dRoadDet

    def compute_cba(self, section):
        """
        Main entry to computer Cost Benefit Analysis for each road section
        """

        # Step 1: Get input attributes from section
        dLength = section.length
        iLanes = section.lanes
        dWidth = section.width
        iRoadClass = section.road_class
        iTerrain = section.terrain
        iTemperature = section.temperature
        iMoisture = section.moisture
        iRoadType = section.road_type
        iSurfaceType = section.surface_type
        iConditionClass = section.condition_class
        dRoughness = section.roughness
        dStructuralNo = section.structural_no
        iPavementAge = section.pavement_age
        iDrainageClass = None
        iTrafficLevel = section.traffic_level
        iGrowthScenario = section.traffc_growth

        dAADT = np.zeros((13, 20), dtype=np.float64)
        dAADT[0][0] = section.aadt_motorcyle
        dAADT[1][0] = section.aadt_carsmall
        dAADT[2][0] = section.aadt_carmedium
        dAADT[3][0] = section.aadt_delivery
        dAADT[4][0] = section.aadt_4wheel
        dAADT[5][0] = section.aadt_smalltruck
        dAADT[6][0] = section.aadt_mediumtruck
        dAADT[7][0] = section.aadt_largetruck
        dAADT[8][0] = section.aadt_articulatedtruck
        dAADT[9][0] = section.aadt_smallbus
        dAADT[10][0] = section.aadt_mediumbus
        dAADT[11][0] = section.aadt_largebus
        dAADT[12][0] = section.aadt_total

        iNoAlernatives = self.compute_alternatives(iSurfaceType, iRoadClass, iConditionClass)

        dCostFactor = self.compute_cost_factor(iSurfaceType, iRoadClass, iConditionClass)

        # Annual traffic
        dAADT = self.compute_annual_traffic(dAADT, iGrowthScenario)
        # ESA Loading
        dESATotal = self.compute_esa_loading(dAADT, iLanes)
        # Truck percent
        dTRucks = self.compute_trucks_percent(dAADT)
        # Vehicle Utilization
        dUtilization = self.compute_vehicle_utilization(dAADT, dLength)

        ########################
        # Output variables
        ########################
        sRoadCode = np.empty((13, 20), dtype='<U30') # alternatives, years
        dCondIRI = np.zeros((13, 20), dtype=np.float64) # alternatives, years
        dCondCON = np.zeros((13, 20), dtype=np.int16) # alternatives, years
        dCondSNC = np.zeros((13, 20), dtype=np.float64) #    ' alternatives, years
        iCondAge = np.zeros((13, 20), dtype=np.int16) #    ' alternatives, years
        iCondLanes = np.zeros((13, 20), dtype=np.int16) #' alternatives, years
        dCondWidth = np.zeros((13, 20), dtype=np.float64)  #   ' alternatives, years
        dCondLength = np.zeros((13, 20), dtype=np.float64)  #   ' alternatives, years
        iCondSurface = np.zeros((13, 20), dtype=np.int16) #' alternatives, years
        dCostCapitalFin = np.zeros((13, 20), dtype=np.float64)  #   ' alternatives, years
        dCostRepairFin = np.zeros((13, 20), dtype=np.float64)  #   ' alternatives, years
        dCostRecurrentFin = np.zeros((13, 20), dtype=np.float64)  #   ' alternatives, years
        dCostAgencyFin = np.zeros((13, 20), dtype=np.float64)  #   ' alternatives, years
        dCostCapitalEco = np.zeros((13, 20), dtype=np.float64)  #   ' alternatives, years
        dCostRepairEco = np.zeros((13, 20), dtype=np.float64)  #   ' alternatives, years
        dCostRecurrentEco = np.zeros((13, 20), dtype=np.float64)  #   ' alternatives, years
        dCostAgencyEco = np.zeros((13, 20), dtype=np.float64)  #   ' alternatives, years
        dCostVOC = np.zeros((13, 20), dtype=np.float64)  #   ' alternatives, years
        dCostTime = np.zeros((13, 20), dtype=np.float64)  #   ' alternatives, years
        dCostUsers = np.zeros((13, 20), dtype=np.float64)  #   ' alternatives, years
        dCondSpeed = np.zeros((13, 20, 12), dtype=np.float64)  #uble  ' alterntive, years, vehicles
        dCondSpeedAve = np.zeros((13, 20), dtype=np.float64)  # ' alternative, year
        dCostTotal = np.zeros((13, 20), dtype=np.float64)  #   ' alternatives, years
        dNetTotal = np.zeros((13, 20), dtype=np.float64)  #   ' alternatives, years
        dSolIRR = np.zeros((13,), dtype=np.float64) # As Double '  alternatives
        dSolNPV = np.zeros((13,), dtype=np.float64) # As Double ' altertnatives
        dSolNPVKm = np.zeros((13,), dtype=np.float64) # As Double ' alternatives
        dSolNPVCost = np.zeros((13,), dtype=np.float64) # As Double ' alternatives
        sSolClass = np.empty((13,), dtype='<U30') # As String ' alternatives
        sSolCode = np.empty((13,), dtype='<U30') # As String ' alternatives
        sSolName = np.empty((13,), dtype='<U30') # As String ' alternatives
        dSolCost = np.zeros((13,), dtype=np.float64) # As Double ' alternatives
        dSolCostkm = np.zeros((13,), dtype=np.float64) # As Double ' alternatives
        iSolYear = np.zeros((13,), dtype=np.float64) # As Double ' alternatives
        dNPVMax = 0.0
        dYearRoughness = 0.0
        iYearAge = 0
        dYearSNC = 0.0
        iYearLanes = 0
        dYearWidth = 0.0
        dYearLength = 0.0
        iYearSurface = 0

    def compute_alternatives(self, iSurfaceType, iRoadClass, iConditionClass):
        iNoAlernatives = 0
        dAlternatives = np.zeros((13, 2), dtype=np.float64)

        # Get initial road work for the 13 alternatives
        dAlternatives[0, 0] = int(self.dWorkEvaluated[(iSurfaceType - 1) * 50 + (iRoadClass - 1) * 5 + iConditionClass - 1, 1])
        dAlternatives[1, 0] = int(self.dWorkEvaluated[(iSurfaceType - 1) * 50 + (iRoadClass - 1) * 5 + iConditionClass - 1, 2])
        dAlternatives[2, 0] = int(self.dWorkEvaluated[(iSurfaceType - 1) * 50 + (iRoadClass - 1) * 5 + iConditionClass - 1, 2])
        dAlternatives[3, 0] = int(self.dWorkEvaluated[(iSurfaceType - 1) * 50 + (iRoadClass - 1) * 5 + iConditionClass - 1, 2])
        dAlternatives[4, 0] = int(self.dWorkEvaluated[(iSurfaceType - 1) * 50 + (iRoadClass - 1) * 5 + iConditionClass - 1, 2])
        dAlternatives[5, 0] = int(self.dWorkEvaluated[(iSurfaceType - 1) * 50 + (iRoadClass - 1) * 5 + iConditionClass - 1, 2])
        dAlternatives[6, 0] = int(self.dWorkEvaluated[(iSurfaceType - 1) * 50 + (iRoadClass - 1) * 5 + iConditionClass - 1, 2])
        dAlternatives[7, 0] = int(self.dWorkEvaluated[(iSurfaceType - 1) * 50 + (iRoadClass - 1) * 5 + iConditionClass - 1, 3])
        dAlternatives[8, 0] = int(self.dWorkEvaluated[(iSurfaceType - 1) * 50 + (iRoadClass - 1) * 5 + iConditionClass - 1, 3])
        dAlternatives[9, 0] = int(self.dWorkEvaluated[(iSurfaceType - 1) * 50 + (iRoadClass - 1) * 5 + iConditionClass - 1, 3])
        dAlternatives[10, 0] = int(self.dWorkEvaluated[(iSurfaceType - 1) * 50 + (iRoadClass - 1) * 5 + iConditionClass - 1, 3])
        dAlternatives[11, 0] = int(self.dWorkEvaluated[(iSurfaceType - 1) * 50 + (iRoadClass - 1) * 5 + iConditionClass - 1, 3])
        dAlternatives[12, 0] = int(self.dWorkEvaluated[(iSurfaceType - 1) * 50 + (iRoadClass - 1) * 5 + iConditionClass - 1, 3])

        # Define years of initial works for 13 alternatives
        dAlternatives[0, 1] = int(self.dWorkEvaluated[(iSurfaceType - 1) * 50 + (iRoadClass - 1) * 5 + iConditionClass - 1, 0])

        if dAlternatives[1, 0] > 0:  # first road work defined: evaluate at least 7 alternatives
            dAlternatives[1, 1] = 1
            dAlternatives[2, 1] = 2
            dAlternatives[3, 1] = 3
            dAlternatives[4, 1] = 4
            dAlternatives[5, 1] = 5
            dAlternatives[6, 1] = 6
            iNoAlernatives = 7

        if dAlternatives[7, 0] > 0:  # second road work defined: evaluate 13 alternatives
            dAlternatives[7, 1] = 1
            dAlternatives[8, 1] = 2
            dAlternatives[9, 1] = 3
            dAlternatives[10, 1] = 4
            dAlternatives[11, 1] = 5
            dAlternatives[12, 1] = 6
            iNoAlernatives = 13

        if dAlternatives[1, 0] == 0 and dAlternatives[7, 0] == 0:   # no road works defined: evaluate 2 base alternatives
            dAlternatives[1, 0] = self.dWorkEvaluated[(iSurfaceType - 1) * 50 + (iRoadClass - 1) * 5 + iConditionClass - 1, 1]
            dAlternatives[1, 1] = self.dWorkEvaluated[(iSurfaceType - 1) * 50 + (iRoadClass - 1) * 5 + iConditionClass - 1, 0]
            iNoAlernatives = 2
        
        return iNoAlernatives

    def compute_cost_factor(self, iSurfaceType, iRoadClass, iConditionClass):
        return self.dWorkEvaluated[(iSurfaceType - 1) * 50 + (iRoadClass - 1) * 5 + iConditionClass - 1, 4]

    def compute_annual_traffic(self, dAADT, iGrowthScenario):
        for iv in range(12):
            for iy in range(1, 20):
                dAADT[iv, iy] = dAADT[iv, iy - 1] * (1 + self.dGrowth[iGrowthScenario - 1, iv])

        for iy in range(1, 20):
            dAADT[12, iy] = 0
            for iv in range(12):
                dAADT[12, iy] = dAADT[12, iy] + dAADT[iv, iy]
        
        return dAADT

    def compute_esa_loading(self, dAADT, iLanes):
        dESATotal = np.zeros((20,), dtype=np.float64)

        for iy in range(0, 20):
            dESATotal[iy] = 0
            for iv in range(0, 12):
                dESATotal[iy] = dESATotal[iy] + dAADT[iv, iy] * self.dVehicleFleet[iv, 0] / 1000000 * 365 / self.dWidthDefaults[iLanes - 1, 1]

    def compute_trucks_percent(self, dAADT):
        return (dAADT[5, 0] + dAADT[6, 0] + dAADT[7, 0] + dAADT[8, 0]) / dAADT[12, 0]

    def compute_vehicle_utilization(dAADT, dLength):
        dUtilization = 0
        for iv in range(0, 12):
            dUtilization = dUtilization + dAADT[iv, 0] * dLength * 365 / 1000000
        return dUtilization