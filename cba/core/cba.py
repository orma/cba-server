import numpy as np

from .default import dWorkEvaluated


class CostBenefitAnalysisModel:

    def __init__(self):
        self.dWorkEvaluated = dWorkEvaluated

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