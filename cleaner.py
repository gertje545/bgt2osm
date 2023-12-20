from osgeo import gdal, ogr

gdal.SetConfigOption('GML_SKIP_CORRUPTED_FEATURES', 'YES')

infile = './bgt_begroeidterreindeel.gml'
outfile = './source.geojson'

driver = ogr.GetDriverByName('GML')
dataSource = driver.Open(infile)
dataLayer = dataSource.GetLayer()

for feature in dataLayer:
    featureGeometryRef = feature.GetGeometryRef()

    if 'CURVEPOLYGON' in str(featureGeometryRef):
        polygon_geometry = ogr.CreateGeometryFromWkt(featureGeometryRef.ExportToWkt()).GetLinearGeometry()
        feature.SetGeometryDirectly(polygon_geometry)
    with open(outfile, 'a') as f:
        f.write(feature.ExportToJson() + '\n')