import Rhino
import scriptcontext
import System.Drawing.Color
import rhinoscriptsyntax as rs


def add_group():

    from System.Drawing import Color
    
    #print "New layer:", rs.AddLayer()
    print "New layer:", rs.AddLayer("T001")
    print "New layer:", rs.AddLayer("DWG", Color.DarkSeaGreen,parent="T001")
    print "New layer:", rs.AddLayer("SURFACE", Color.Cornsilk,parent="T001")
    print "New layer:", rs.AddLayer("SOLID",Color.Red,parent="T001")
    
    
def AddChildLayer():
    # Get an existing layer
    default_name = scriptcontext.doc.Layers.CurrentLayer.Name
    # Prompt the user to enter a layer name
    gs = Rhino.Input.Custom.GetString()
    gs.SetCommandPrompt("Name of existing layer")
    gs.SetDefaultString(default_name)
    gs.AcceptNothing(True)
    gs.Get()
    if gs.CommandResult()!=Rhino.Commands.Result.Success:
        return gs.CommandResult()

    # Was a layer named entered?
    layer_name = gs.StringResult().Trim()
    index = scriptcontext.doc.Layers.Find(layer_name, True)
    if index<0: return Rhino.Commands.Result.Cancel

    parent_layer = scriptcontext.doc.Layers[index]

    # Create a child layer
    child_name = parent_layer.Name + "_child"
    childlayer = Rhino.DocObjects.Layer()
    childlayer.ParentLayerId = parent_layer.Id
    childlayer.Name = child_name
    childlayer.Color = System.Drawing.Color.Red

    index = scriptcontext.doc.Layers.Add(childlayer)
    if index<0:
        print "Unable to add", child_name, "layer."
        return Rhino.Commands.Result.Failure
    return Rhino.Commands.Result.Success

if __name__=="__main__":
    # AddChildLayer()
    add_group()