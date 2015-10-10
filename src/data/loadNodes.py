import arcpy, sys

# load the standard OpenStreetMap bpx as it references the core OSM tools
arcpy.ImportToolbox(r'C:\Users\Thomas.AVWORLD\AppData\Roaming\ESRI\Desktop10.3\ArcToolbox\My Toolboxes\Toolbox.tbx')
arcpy.env.overwriteOutput = True

arcpy.OSMGPNodeLoader(sys.argv[1], sys.argv[2])