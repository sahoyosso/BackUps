
#Use iface to access QGIS API interface or Type help(iface)
#This ^ in Python Concosle on QGIS screen 

layer = qgis.utils.iface.activeLayer()
selected_features = layer.selected_features()
id_List = []
for i in selected_features:
    id_number = i_attribute["The Unique Field Name"]
    id_List.append(id_number)
print(id_List)

""" What this script does: 
    Before running the script -> have an active layer in QGIS
                            --> using the mouse or whatever select certain features of a layer
                            --> then run the script
                            --> this will produce a list of the unique ID's I selected

   Now I can copy and paste that list to make an SQL statement  """

# Taken from https://www.youtube.com/watch?v=coTSHnWvZXA

