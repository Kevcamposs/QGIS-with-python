import gdal
import processing

parameters={"INPUT":"C:/Users/Kevin/Desktop/UNALM/SextoCiclo/Geo_physics/Lab_1/Output/DEM_Lurin_basin.tif",
            "Z_FACTOR":1.0,
            "AZIMUTH":300.0,
            "V_ANGLE":40.0,
            "OUTPUT":"C:/Users/Kevin/Desktop/UNALM/SextoCiclo/Geo_physics/Lab_1/Output/DEM_Lurin_basin_hillshade.tif"}

processing.run("qgis:hillshade",parameters)
