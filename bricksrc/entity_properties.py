"""
Entity property definitions
"""
from rdflib import Literal
from .namespaces import BRICK, RDFS, SKOS, UNIT, XSD, SH, BSH, QUDT

# these are the "relationship"/predicates/OWL properties that
# relate a Brick entity to a structured value.
# These are all instances of Brick.EntityProperty, which is
# a subclass of OWL.ObjectProperty
entity_properties = {
    BRICK.area: {
        SKOS.definition: Literal("Entity has 2-dimensional area"),
        RDFS.range: BRICK.AreaShape,
        RDFS.label: Literal("Area"),
        "subproperties": {
            BRICK.grossArea: {
                SKOS.definition: Literal("Entity has gross 2-dimensional area"),
                RDFS.range: BRICK.AreaShape,
                RDFS.label: Literal("Gross area"),
            },
            BRICK.netArea: {
                SKOS.definition: Literal("Entity has net 2-dimensional area"),
                RDFS.range: BRICK.AreaShape,
                RDFS.label: Literal("Net area"),
            },
            BRICK.panelArea: {
                SKOS.definition: Literal("Surface area of a panel, such as a PV panel"),
                RDFS.range: BRICK.AreaShape,
                RDFS.label: Literal("Panel area"),
            },
        },
    },
    BRICK.volume: {
        SKOS.definition: Literal("Entity has 3-dimensional volume"),
        RDFS.range: BRICK.VolumeShape,
        RDFS.label: Literal("Volume"),
    },
    BRICK.azimuth: {
        SKOS.definition: Literal(
            "(Horizontal) angle between a projected vector and a reference vector (typically a compass bearing). The projected vector usually indicates the direction of a face or plane."
        ),
        RDFS.range: BRICK.AzimuthShape,
        RDFS.label: Literal("Azimuth"),
    },
    BRICK.tilt: {
        SKOS.definition: Literal(
            "The direction an entity is facing in degrees above the horizon"
        ),
        RDFS.range: BRICK.TiltShape,
        RDFS.label: Literal("Tilt"),
    },
    BRICK.coordinates: {
        SKOS.definition: Literal("The location of an entity in latitude/longitude"),
        RDFS.range: BRICK.CoordinateShape,
        RDFS.label: Literal("Coordinates"),
    },
    # electrical properties
    BRICK.powerComplexity: {
        SKOS.definition: Literal("Entity has this power complexity"),
        RDFS.range: BRICK.PowerComplexityShape,
        RDFS.label: Literal("Power complexity"),
    },
    BRICK.powerFlow: {
        SKOS.definition: Literal(
            "Entity has this power flow relative to the building'"
        ),
        RDFS.range: BRICK.PowerFlowShape,
        RDFS.label: Literal("Power flow"),
    },
    BRICK.electricalPhases: {
        SKOS.definition: Literal("Entity has these electrical AC phases"),
        RDFS.range: BRICK.PhasesShape,
        RDFS.label: Literal("Electrical phases"),
    },
    BRICK.electricalPhaseCount: {
        SKOS.definition: Literal("Entity has these phases"),
        RDFS.range: BRICK.PhaseCountShape,
        RDFS.label: Literal("Electrical phase count"),
    },
    BRICK.currentFlowType: {
        SKOS.definition: Literal("The current flow type of the entity"),
        RDFS.range: BRICK.CurrentFlowTypeShape,
        RDFS.label: Literal("Current flow type"),
    },
    BRICK.ratedPowerOutput: {
        SKOS.definition: Literal("The nominal rated power output of the entity"),
        RDFS.range: BRICK.PowerShape,
    },
    BRICK.measuredPowerOutput: {
        SKOS.definition: Literal("The nominal measured power output of the entity"),
        RDFS.range: BRICK.PowerShape,
    },
    BRICK.ratedPowerInput: {
        SKOS.definition: Literal("The nominal rated power input of the entity"),
        RDFS.range: BRICK.PowerShape,
    },
    BRICK.measuredPowerInput: {
        SKOS.definition: Literal("The nominal measured power input of the entity"),
        RDFS.range: BRICK.PowerShape,
    },
    BRICK.ratedVoltageInput: {
        SKOS.definition: Literal("The nominal rated voltage input of the entity"),
        RDFS.range: BRICK.VoltageShape,
        "subproperties": {
            BRICK.ratedMaximumVoltageInput: {
                SKOS.definition: Literal(
                    "The maximum voltage that can be input to the entity"
                ),
                RDFS.range: BRICK.VoltageShape,
            },
            BRICK.ratedMinimumVoltageInput: {
                SKOS.definition: Literal(
                    "The minimum voltage that can be input to the entity"
                ),
                RDFS.range: BRICK.VoltageShape,
            },
        },
    },
    BRICK.ratedVoltageOutput: {
        SKOS.definition: Literal("The nominal rated voltage output of the entity"),
        RDFS.range: BRICK.VoltageShape,
        "subproperties": {
            BRICK.ratedMaximumVoltageOutput: {
                SKOS.definition: Literal(
                    "The maximum voltage that can be output by the entity"
                ),
                RDFS.range: BRICK.VoltageShape,
            },
            BRICK.ratedMinimumVoltageOutput: {
                SKOS.definition: Literal(
                    "The minimum voltage that can be output by the entity"
                ),
                RDFS.range: BRICK.VoltageShape,
            },
        },
    },
    BRICK.ratedCurrentInput: {
        SKOS.definition: Literal("The nominal rated current input of the entity"),
        RDFS.range: BRICK.CurrentShape,
        "subproperties": {
            BRICK.ratedMaximumCurrentInput: {
                SKOS.definition: Literal(
                    "The maximum current that can be input to the entity"
                ),
                RDFS.range: BRICK.CurrentShape,
            },
            BRICK.ratedMinimumCurrentInput: {
                SKOS.definition: Literal(
                    "The minimum current that can be input to the entity"
                ),
                RDFS.range: BRICK.CurrentShape,
            },
        },
    },
    BRICK.ratedCurrentOutput: {
        SKOS.definition: Literal("The nominal rated current output of the entity"),
        RDFS.range: BRICK.CurrentShape,
        "subproperties": {
            BRICK.ratedMaximumCurrentOutput: {
                SKOS.definition: Literal(
                    "The maximum current that can be output by the entity"
                ),
                RDFS.range: BRICK.CurrentShape,
            },
            BRICK.ratedMinimumCurrentOutput: {
                SKOS.definition: Literal(
                    "The minimum current that can be output by the entity"
                ),
                RDFS.range: BRICK.CurrentShape,
            },
        },
    },
    BRICK.temperatureCoefficientofPmax: {
        SKOS.definition: Literal(
            "The % change in power output for every degree celsius that the entity is hotter than 25 degrees celsius"
        ),
        RDFS.range: BRICK.TemperatureCoefficientPerDegreeCelsiusShape,
        RDFS.label: Literal("Temperature coefficient"),
    },
    BRICK.conversionEfficiency: {
        SKOS.definition: Literal(
            "The percent efficiency of the conversion process (usually to power or energy) carried out by the entity"
        ),
        RDFS.range: BRICK.EfficiencyShape,
        RDFS.label: Literal("Conversion efficiency"),
        "subproperties": {
            BRICK.ratedModuleConversionEfficiency: {
                SKOS.definition: Literal(
                    "The *rated* percentage of sunlight that is converted into usable power, as measured using Standard Test Conditions (STC): 1000 W/sqm irradiance, 25 degC panel temperature, no wind"
                ),
                RDFS.domain: BRICK.PV_Panel,
                RDFS.range: BRICK.EfficiencyShape,
                RDFS.label: Literal("Rated module conversion efficiency"),
            },
            BRICK.measuredModuleConversionEfficiency: {
                SKOS.definition: Literal(
                    "The measured percentage of sunlight that is converted into usable power"
                ),
                RDFS.domain: BRICK.PV_Panel,
                RDFS.range: BRICK.EfficiencyShape,
                RDFS.label: Literal("Measured module conversion efficiency"),
            },
        },
    },
    # equipment operation properties
    BRICK.operationalStage: {
        SKOS.definition: Literal("The associated operational stage"),
        RDFS.range: BRICK.StageShape,
        RDFS.label: Literal("Operational stage"),
    },
    BRICK.operationalStageCount: {
        SKOS.definition: Literal(
            "The number of operational stages supported by this eqiupment"
        ),
        RDFS.domain: BRICK.Equipment,
        RDFS.range: BRICK.StageShape,
        RDFS.label: Literal("Operational stage count"),
    },
    BRICK.coolingCapacity: {
        SKOS.definition: Literal(
            "Measurement of a chiller ability to remove heat (adopted from Project Haystack)"
        ),
        RDFS.domain: BRICK.Chiller,
        RDFS.range: BRICK.CoolingCapacityShape,
        RDFS.label: Literal("Cooling capacity"),
        RDFS.seeAlso: Literal("https://project-haystack.org/tag/coolingCapacity"),
    },
    # building properties
    BRICK.buildingPrimaryFunction: {
        SKOS.definition: Literal(
            "Enumerated string applied to a site record to indicate the building's primary function. The list of primary functions is derived from the US Energy Star program (adopted from Project Haystack)"
        ),
        RDFS.seeAlso: Literal("https://project-haystack.org/tag/primaryFunction"),
        RDFS.domain: BRICK.Building,
        RDFS.range: BRICK.BuildingPrimaryFunctionShape,
        RDFS.label: Literal("Building primary function"),
    },
    BRICK.yearBuilt: {
        SKOS.definition: Literal(
            "Four digit year that a building was first built. (adopted from Project Haystack)"
        ),
        RDFS.domain: BRICK.Building,
        RDFS.range: BRICK.YearBuiltShape,
        RDFS.seeAlso: Literal("https://project-haystack.org/tag/yearBuilt"),
        RDFS.label: Literal("Year built"),
    },
    BRICK.thermalTransmittance: {
        SKOS.definition: Literal(
            "The area-weighted average heat transfer coefficient (commonly referred to as a U-value)"
        ),
        RDFS.range: BRICK.ThermalTransmittanceShape,
        RDFS.label: Literal("Thermal transmittance"),
        RDFS.seeAlso: Literal(
            "https://www.iso.org/obp/ui/#iso:std:iso:13789:ed-3:v1:en"
        ),
        "subproperties": {
            BRICK.buildingThermalTransmittance: {
                RDFS.domain: BRICK.Building,
                RDFS.range: BRICK.ThermalTransmittanceShape,
                SKOS.definition: Literal(
                    "The area-weighted average heat transfer coefficient (commonly referred to as a U-value) for a building envelope"
                ),
                RDFS.seeAlso: Literal(
                    "https://www.iso.org/obp/ui/#iso:std:iso:13789:ed-3:v1:en"
                ),
                RDFS.label: Literal("Building thermal transmittance"),
            },
        },
    },
    # special stuff
    BRICK.aggregate: {
        SKOS.definition: Literal(
            "Description of how the dta for this point is aggregated"
        ),
        RDFS.domain: BRICK.Point,
        RDFS.range: BRICK.AggregationShape,
        RDFS.label: Literal("Aggregate"),
    },
}

building_primary_function_values = [
    "Adult Education",
    "Ambulatory Surgical Center",
    "Aquarium",
    "Automobile Dealership",
    "Bank Branch",
    "Bar/Nightclub",
    "Barracks",
    "Bowling Alley",
    "Casino",
    "College/University",
    "Convenience Store with Gas Station",
    "Convenience Store without Gas Station",
    "Convention Center",
    "Courthouse",
    "Data Center",
    "Distribution Center",
    "Drinking Water Treatment & Distribution",
    "Enclosed Mall",
    "Energy/Power Station",
    "Fast Food Restaurant",
    "Financial Office",
    "Fire Station",
    "Fitness Center/Health Club/Gym",
    "Food Sales",
    "Food Service",
    "Hospital (General Medical & Surgical)",
    "Hotel",
    "Ice/Curling Rink",
    "Indoor Arena",
    "K-12 School",
    "Laboratory",
    "Library",
    "Lifestyle Center",
    "Mailing Center/Post Office",
    "Manufacturing/Industrial Plant",
    "Medical Office",
    "Mixed Use Property",
    "Movie Theater",
    "Multifamily Housing",
    "Museum",
    "Non-Refrigerated Warehouse",
    "Office",
    "Other - Education",
    "Other - Entertainment/Public Assembly",
    "Other - Lodging/Residential",
    "Other - Mall",
    "Other - Public Services",
    "Other - Recreation",
    "Other - Restaurant/Bar",
    "Other - Services",
    "Other - Stadium",
    "Other - Technology/Science",
    "Other - Utility",
    "Other",
    "Other/Specialty Hospital",
    "Outpatient Rehabilitation/Physical Therapy",
    "Parking",
    "Performing Arts",
    "Personal Services (Health/Beauty, Dry Cleaning, etc)",
    "Police Station",
    "Pre-school/Daycare",
    "Prison/Incarceration",
    "Race Track",
    "Refrigerated Warehouse",
    "Repair Services (Vehicle, Shoe, Locksmith, etc)",
    "Residence Hall/Dormitory",
    "Restaurant",
    "Retail Store",
    "Roller Rink",
    "Self-Storage Facility",
    "Senior Care Community",
    "Single Family Home",
    "Social/Meeting Hall",
    "Stadium (Closed)",
    "Stadium (Open)",
    "Strip Mall",
    "Supermarket/Grocery Store",
    "Swimming Pool",
    "Transportation Terminal/Station",
    "Urgent Care/Clinic/Other Outpatient",
    "Veterinary Office",
    "Vocational School",
    "Wastewater Treatment Plant",
    "Wholesale Club/Supercenter",
    "Worship Facility",
    "Zoo",
]

# These are the shapes that govern what values of Entity Properties should look like
shape_properties = {
    BRICK.AreaShape: {"units": [UNIT.FT2, UNIT.M2], "datatype": BSH.NumericValue},
    BRICK.VolumeShape: {"units": [UNIT.FT3, UNIT.M3], "datatype": BSH.NumericValue},
    BRICK.PowerComplexityShape: {"values": ["real", "reactive", "apparent"]},
    BRICK.PowerFlowShape: {"values": ["import", "export", "net", "absolute"]},
    BRICK.PhasesShape: {"values": ["A", "B", "C", "AB", "BC", "AC", "ABC"]},
    BRICK.PhaseCountShape: {"values": ["1", "2", "3", "Total"]},
    BRICK.CurrentFlowTypeShape: {"values": ["AC", "DC"]},
    BRICK.StageShape: {"values": [1, 2, 3, 4]},
    BRICK.BuildingPrimaryFunctionShape: {"values": building_primary_function_values},
    BRICK.CoordinateShape: {
        "properties": {
            BRICK.latitude: {"datatype": BSH.NumericValue},
            BRICK.longitude: {"datatype": BSH.NumericValue},
        },
    },
    BRICK.TiltShape: {"unitsFromQuantity": BRICK.Angle, "datatype": BSH.NumericValue},
    BRICK.TemperatureShape: {
        "unitsFromQuantity": BRICK.Temperature,
        "datatype": BSH.NumericValue,
    },
    BRICK.TemperatureCoefficientPerDegreeCelsiusShape: {
        "units": [UNIT.PERCENT],
        "datatype": BSH.NumericValue,
    },
    BRICK.AzimuthShape: {
        "unitsFromQuantity": BRICK.Angle,
        "datatype": BSH.NumericValue,
        "rotationalDirection": {"values": ["clockwise", "counterclockwise"]},
        "referenceDirection": {"values": ["North", "South", "East", "West"]},
        "range": {"minInclusive": 0, "maxInclusive": 360},
    },
    BRICK.YearBuiltShape: {"datatype": XSD.nonNegativeInteger},
    BRICK.ThermalTransmittanceShape: {
        "datatype": BSH.NumericValue,
        "units": [UNIT.BTU_IT, UNIT["W-PER-M2-K"]],
    },
    BRICK.PowerShape: {
        "datatype": BSH.NumericValue,
        "unitsFromQuantity": BRICK.Power,
        "properties": {
            BRICK.ambientTemperatureOfMeasurement: {
                "optional": True,
                SKOS.definition: Literal(
                    "The ambient temperature at which the power input was measured"
                ),
                SH["class"]: BRICK.TemperatureShape,
            },
            BRICK.ratedVoltageInput: {
                "optional": True,
            },
            BRICK.ratedVoltageOutput: {
                "optional": True,
            },
            BRICK.ratedCurrentInput: {
                "optional": True,
            },
            BRICK.ratedCurrentOutput: {
                "optional": True,
            },
        },
    },
    BRICK.VoltageShape: {
        "datatype": BSH.NumericValue,
        "unitsFromQuantity": BRICK.Voltage,
        "properties": {
            BRICK.ambientTemperatureOfMeasurement: {
                "optional": True,
                SKOS.definition: Literal(
                    "The ambient temperature at which the power input was measured"
                ),
                SH["class"]: BRICK.TemperatureShape,
            },
            BRICK.ratedCurrentInput: {
                "optional": True,
            },
            BRICK.ratedCurrentOutput: {
                "optional": True,
            },
        },
    },
    BRICK.CurrentShape: {
        "datatype": BSH.NumericValue,
        "unitsFromQuantity": BRICK.Current,
        "properties": {
            BRICK.ambientTemperatureOfMeasurement: {
                "optional": True,
                SKOS.definition: Literal(
                    "The ambient temperature at which the power input was measured"
                ),
                SH["class"]: BRICK.TemperatureShape,
            },
            BRICK.ratedVoltageInput: {
                "optional": True,
            },
            BRICK.ratedVoltageOutput: {
                "optional": True,
            },
        },
    },
    BRICK.EfficiencyShape: {
        "datatype": BSH.NumericValue,
        "units": [UNIT.PERCENT],
        "range": {"minInclusive": 0},
    },
    BRICK.CoolingCapacityShape: {
        "datatype": BSH.NumericValue,
        "units": [UNIT.TON_FG, UNIT["BTU_IT-PER-HR"], UNIT["BTU_TH-PER-HR"], UNIT.W],
    },
    BRICK.AggregationShape: {
        "properties": {
            BRICK.aggregationFunction: {
                SKOS.definition: Literal(
                    "The aggregation function applied to data in the interval which produces the value"
                ),
                "values": ["max", "min", "count", "mean", "sum", "median", "mode"],
            },
            BRICK.aggregationInterval: {
                SKOS.definition: Literal(
                    "Interval expressed in an ISO 8601 Duration string, e.g. RP1D"
                ),
                "datatype": XSD.string,
            },
        }
    },
}
