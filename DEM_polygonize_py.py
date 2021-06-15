import gdal
import processing

parameters={"INPUT":"C:/Users/Kevin/Desktop/UNALM/SextoCiclo/Geo_physics/Lab_1/Output/DEM_cuenca.tif",
            "BAND":1,
            "FIELD":"ND",
            "EIGHT_CONNECTEDNESS":False,
            "OUTPUT":"C:/Users/Kevin/Desktop/UNALM/SextoCiclo/Geo_physics/Lab_1/Output/SHP_cuenca.shp"}

processing.run("gdal:polygonize",parameters)
