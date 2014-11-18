import bpy
from animation_nodes.mn_execution import nodePropertyChanged
from animation_nodes.mn_node_base import *

class mn_IntegerSocket(mn_BaseSocket, mn_SocketProperties):
	bl_idname = "mn_IntegerSocket"
	bl_label = "Integer Socket"
	dataType = "Integer"
	allowedInputTypes = ["Integer"]
	drawColor = (0.2, 0.2, 1, 1)
	
	number = bpy.props.IntProperty(default = 0, update = nodePropertyChanged)
	
	def drawInput(self, layout, node, text):
		layout.prop(self, "number", text = text)
		
	def getValue(self):
		return self.number
		
	def setStoreableValue(self, data):
		self.number = data
	def getStoreableValue(self):
		return self.number

classes = [
	mn_IntegerSocket
]
    
def register():
    for cls in classes:
        bpy.utils.register_class(cls)
 
 
def unregister():
    for cls in classes:
        bpy.utils.unregister_class(cls)
