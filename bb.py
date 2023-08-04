

import rhinoinside
rhinoinside.load()
import System
import Rhino

# for now, you need to explicitly use floating point
# numbers in Point3d constructor
pts = System.Collections.Generic.List[Rhino.Geometry.Point3d]()
pts.Add(Rhino.Geometry.Point3d(0.0,0.0,0.0))
pts.Add(Rhino.Geometry.Point3d(1.0,0.0,0.0))
pts.Add(Rhino.Geometry.Point3d(1.5,2.0,0.0))

crv = Rhino.Geometry.Curve.CreateInterpolatedCurve(pts,3)
print (crv.GetLength())