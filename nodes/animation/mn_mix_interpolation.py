import bpy
from bpy.types import Node
from animation_nodes.mn_node_base import AnimationNode
from animation_nodes.mn_execution import nodePropertyChanged, allowCompiling, forbidCompiling
from animation_nodes.utils.mn_interpolation_utils import *

class mn_MixInterpolation(Node, AnimationNode):
	bl_idname = "mn_MixInterpolation"
	bl_label = "Mix Interpolation"
	isDetermined = True
	
	def init(self, context):
		forbidCompiling()
		self.inputs.new("mn_FloatSocket", "Factor").setMinMax(0, 1)
		self.inputs.new("mn_InterpolationSocket", "Interpolation 1").showName = False
		self.inputs.new("mn_InterpolationSocket", "Interpolation 2").showName = False
		self.outputs.new("mn_InterpolationSocket", "Interpolation")
		allowCompiling()
		
	def getInputSocketNames(self):
		return {"Factor" : "factor", "Interpolation 1" : "a", "Interpolation 2" : "b"}
	def getOutputSocketNames(self):
		return {"Interpolation" : "interpolation"}
		
	def execute(self, factor, a, b):
		return (mixedInterpolation, (a, b, factor))

classes = [
	mn_MixInterpolation
]
    
def register():
    for cls in classes:
        bpy.utils.register_class(cls)
 
 
def unregister():
    for cls in classes:
        bpy.utils.unregister_class(cls)
