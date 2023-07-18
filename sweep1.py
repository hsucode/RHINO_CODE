import rhinoscriptsyntax as rs


rail = rs.GetObject("Select rail curve", rs.filter.curve) 
shapes = rs.GetObjects("Select cross-section curves",rs.filter.curve)
if shapes:   
    rs.AddSweep1( rail, shapes )