import gdal
from pathlib import Path
import os

folder_path = r"C:\Users\Kevin\Desktop\UNALM\SextoCiclo\Geo_physics\Lab_1\Input"
BASE_PATH = os.path.dirname(os.path.abspath(folder_path))
folder = Path(folder_path)

l = []

for f in folder.glob('**/*.tif'):
    f_path = f.as_posix()
    l.append(f_path)

vrt_path = os.path.join(BASE_PATH, 'prov_vrt.vrt')
vrt = gdal.BuildVRT(vrt_path, l)

result = os.path.join(BASE_PATH, 'Output\DEM_merge_py.tif')
gdal.Translate(result, vrt, format='GTiff')
