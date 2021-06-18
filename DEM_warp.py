import gdal
import processing

parameters={"INPUT":"C:/Users/Kevin/Desktop/UNALM/SextoCiclo/Geo_physics/Lab_1/Output/DEM_merge_py.tif",
            "SOURCE_CRS":"EPSG:4326",
            "TARGET_CRS":"EPSG:5387",
            "OUTPUT":"C:/Users/Kevin/Desktop/UNALM/SextoCiclo/Geo_physics/Lab_1/Output/DEM_warp_py.tif"}

processing.run("gdal:warpreproject",parameters)