# SHADE
**SHADE**: *Shadow Hide Away Delighted Eyes*

**WARNING:Project Ceased**

**Lack of Knowledge, Work of OpenGL Could NOT be Done by Python**

~~This program is aimed to analyze the shadow in the surface among the object.

~~The **INPUT** might include:
- Coordinates of each single Point on the surface of the object.
- Coordinate(s) of the Light source.
The **OUTPUT** might include:
- The light strength of each point on the condition of the light source.

~~The **Functions**:
- calVerticalVetor(pa, pb, pc):
To calculate the vertical vector at the Plane PaPbPc, we solve a linear functions.
- isIntersect(plight, pobject, paobstacle, pbobstacle, pcobstacle) :
*Aim*: Testing if the line between the light and object is through the obstacle(combined with the pa, pb, pc).
~STEP 1~
Calculate the intersect point P0 of the line and the plane(at this time, it is infinite).
~STEP2~
*Some Math First: How to judge the point is inside or outside*:
Let us image a Triangle ABC and a Point P in the 2D plane. Once P is in the ABC, the P is always at your same side( left or right) when walking at the path ABCA.
*How to take the math into reality*: 
We define a function isPointinSameSide(pa, pb, pc, p0) to judge if the point is at the same side of ABC with the Vector.
