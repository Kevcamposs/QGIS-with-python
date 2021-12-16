import processing

parameter = {'INPUT': r'C:\Users\Kevin\Documents\Molde_USGS.shp',
            'TARGET_CRS':'EPSG:4326',
            'OUTPUT':r'C:\Users\Kevin\Documents\GIS_files\SHP\Molde_Lurín_WGS84.shp'}

processing.run('qgis:reprojectlayer', parameter)
