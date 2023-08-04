

from rhino3dm import *
center = Point3d(1,2,3)
arc = Arc(center, 10, 1)
nc = arc.ToNurbsCurve()
start = nc.PointAtStart
print(start)