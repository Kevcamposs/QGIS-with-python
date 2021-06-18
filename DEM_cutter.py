import gdal
import processing

parameters={"INPUT":"C:/Users/Kevin/Desktop/UNALM/SextoCiclo/Geo_physics/Lab_1/Output/transmission_segments.tif",
            "MASK":"C:/Users/Kevin/Desktop/UNALM/SextoCiclo/Geo_physics/Lab_1/Output/SHP_smoothed.shp",
            "TARGET_CRS":"EPSG:5387",
            "NODATA":None,
            "MULTIHREADIN":False,
            "OPTIONS":"",
            "DATA_TYPE":0,
            "OUTPUT":"C:/Users/Kevin/Desktop/UNALM/SextoCiclo/Geo_physics/Lab_1/Output/transmission_segments_Lurin_basin.tif"}

processing.run("gdal:cliprasterbymasklayer",parameters)
