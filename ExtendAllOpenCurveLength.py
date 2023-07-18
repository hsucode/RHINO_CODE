
import rhinoscriptsyntax as rs

def GetObjArea():
    "Calculate the length of one or more curves"
    # Get the curve objects
    arrObjects = rs.GetObjects("Select Objects", rs.filter.curve, True, True)
    if( arrObjects==None ): return
    rs.UnselectObjects(arrObjects)
    objArea = 0.0 
    count  = 0
    for object in arrObjects:
        if rs.IsCurve(object):
            
            if rs.IsCurveClosed(object):
                print "The object is a closed curve."
            else:
                print "The object is not a closed curve."
                #Get the curve objArea
                length =5.0 # = rs.GetReal("Length to extend", 30.0)
                if length: rs.ExtendCurveLength( object, 2, 2, length )
    
    if (count>0):
        print "Surface selected:", count, " Total Area:", objArea
    
# Check to see if this file is being executed as the "main" python
# script instead of being used as a module by some other python script
# This allows us to use the module which ever way we want.
if( __name__ == "__main__" ):
    GetObjArea()