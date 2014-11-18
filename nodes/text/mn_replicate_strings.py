import bpy
from bpy.types import Node
from animation_nodes.mn_node_base import AnimationNode
from animation_nodes.mn_execution import nodePropertyChanged, allowCompiling, forbidCompiling

class mn_ReplicateStringsNode(Node, AnimationNode):
	bl_idname = "mn_ReplicateStringsNode"
	bl_label = "Replicate Strings"
	
	def init(self, context):
		forbidCompiling()
		self.inputs.new("mn_StringSocket", "Text")
		self.inputs.new("mn_IntegerSocket", "Amount")
		self.outputs.new("mn_StringSocket", "Text")
		allowCompiling()
		
	def execute(self, input):
		output = {}
		output["Text"] = input["Text"] * input["Amount"]
		return output

classes = [
	mn_ReplicateStringsNode
]
    
def register():
    for cls in classes:
        bpy.utils.register_class(cls)
 
 
def unregister():
    for cls in classes:
        bpy.utils.unregister_class(cls)
