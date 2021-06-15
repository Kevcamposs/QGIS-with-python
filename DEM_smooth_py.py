import gdal
import processing

parameters={"INPUT":"C:/Users/Kevin/Desktop/UNALM/SextoCiclo/Geo_physics/Lab_1/Output/SHP_cuenca.shp",
            "ITERATIONS":1,
            "OFFSET":0.5,
            "MAX_ANGLE":180.0,
            "OUTPUT":"C:/Users/Kevin/Desktop/UNALM/SextoCiclo/Geo_physics/Lab_1/Output/SHP_smoothed.shp"}

processing.run("qgis:smoothgeometry",parameters)
