
import rhinoscriptsyntax as rs

def sweep_one():
    "Calculate the length of one or more curves"
    # Get the curve objects

    rail = rs.GetObject("Select rail curve", rs.filter.curve)
    if rail:
        arrObjects = rs.GetObjects("Select Objects", rs.filter.curve)
        if( arrObjects==None ): return
        rs.UnselectObjects(arrObjects)
        for object in arrObjects:
            if object:
                rs.AddSweep1( rail, object )

# Check to see if this file is being executed as the "main" python
# script instead of being used as a module by some other python script
# This allows us to use the module which ever way we want.
if( __name__ == "__main__" ):
    sweep_one()