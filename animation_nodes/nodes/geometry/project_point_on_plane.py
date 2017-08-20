import bpy
from mathutils import Vector
from ... data_structures import VirtualVector3DList
from ... base_types import AnimationNode, VectorizedSocket
from . c_utils import projectPointOnPlaneList, projectPointOnPlaneSingle

class ProjectPointOnPlaneNode(bpy.types.Node, AnimationNode):
    bl_idname = "an_ProjectPointOnPlaneNode"
    bl_label = "Project Point on Plane"
    bl_width_default = 170
    searchTags = ["Distance Point to Plane", "Closest Point on Plane"]

    usePlanePointList = VectorizedSocket.newProperty()
    usePlaneNormalList = VectorizedSocket.newProperty()
    usePointList = VectorizedSocket.newProperty()

    def create(self):
        self.newInput(VectorizedSocket("Vector", "usePlanePointList",
            ("Plane Point", "planePoint", dict(value = (0, 0, 0))),
            ("Plane Points", "planePoints"),
            codeProperties = dict(default = (0, 0, 0))))
        self.newInput(VectorizedSocket("Vector", "usePlaneNormalList",
            ("Plane Point", "planeNormal", dict(value = (0, 0, 1))),
            ("Plane Points", "planeNormals"),
            codeProperties = dict(default = (0, 0, 1))))

        self.newInput(VectorizedSocket("Vector", "usePointList",
            ("Point", "point", dict(value = (0, 0, 1))),
            ("Points", "points"),
            codeProperties = dict(default = (0, 0, 1))))

        props = ["usePlanePointList", "usePlaneNormalList", "usePointList"]

        self.newOutput(VectorizedSocket("Vector", props,
            ("Projection", "projection"),
            ("Projections", "projections")))
        self.newOutput(VectorizedSocket("Float", props,
            ("Signed Distance", "distance"),
            ("Signed Distances", "distances")))

    def getExecutionFunctionName(self):
        useList = any((self.usePlanePointList, self.usePlaneNormalList,
        self.usePointList))
        if useList:
            return "execute_List"
        else:
            return "execute_Single"

    def execute_List(self, planePoints, planeNormals, points):
        planePoints = VirtualVector3DList.fromListOrElement(planePoints, Vector((0, 0, 0)))
        planeNormals = VirtualVector3DList.fromListOrElement(planeNormals, Vector((0, 0, 1)))
        points = VirtualVector3DList.fromListOrElement(points, Vector((0, 0, 1)))
        amount = VirtualVector3DList.getMaxRealLength(planePoints, planeNormals, points)
        return projectPointOnPlaneList(amount, planePoints, planeNormals, points)

    def execute_Single(self, planePoint, planeNormal, point):
        return projectPointOnPlaneSingle(planePoint, planeNormal, point)
