import bpy, random
from animation_nodes.utils.mn_math_utils import perlinNoise
from bpy.types import Node
from animation_nodes.mn_node_base import AnimationNode
from animation_nodes.mn_execution import nodePropertyChanged, allowCompiling, forbidCompiling


class mn_FloatWiggle(Node, AnimationNode):
	bl_idname = "mn_FloatWiggle"
	bl_label = "Number Wiggle"
	isDetermined = True
	
	additionalSeed = bpy.props.IntProperty(update = nodePropertyChanged)
	
	def init(self, context):
		forbidCompiling()
		self.inputs.new("mn_FloatSocket", "Seed")
		self.inputs.new("mn_FloatSocket", "Evolution")
		self.inputs.new("mn_FloatSocket", "Speed").number = 15.0
		self.inputs.new("mn_FloatSocket", "Amplitude").number = 1
		self.inputs.new("mn_FloatSocket", "Persistance").number = 0.3
		self.inputs.new("mn_IntegerSocket", "Octaves").number = 2.0
		self.outputs.new("mn_FloatSocket", "Noise")
		allowCompiling()
		
	def draw_buttons(self, context, layout):
		layout.prop(self, "additionalSeed", text = "Additional Seed")
		
	def getInputSocketNames(self):
		return {"Seed" : "seed",
				"Evolution" : "x",
				"Speed" : "speed",
				"Amplitude" : "amplitude",
				"Persistance" : "persistance",
				"Octaves" : "octaves"}
	def getOutputSocketNames(self):
		return {"Noise" : "noise"}
		
	def execute(self, seed, x, speed, amplitude, persistance, octaves):
		x = x / speed + 2673 * seed + 823 * self.additionalSeed
		total = perlinNoise(x, persistance, octaves)
		return total * amplitude
		


classes = [
	mn_FloatWiggle
]
    
def register():
    for cls in classes:
        bpy.utils.register_class(cls)
 
 
def unregister():
    for cls in classes:
        bpy.utils.unregister_class(cls)
