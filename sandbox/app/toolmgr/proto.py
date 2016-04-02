from collections import OrderedDict


class _ToolManager(object):
    def __init__(self):
        self.tools = OrderedDict()
    
    def addTool(self, tool):
        self.tools[tool.name] = tool
    
    def invokeTool(self, tool):
        print("\nUser invoked tool '{0}'\nAsking user to input values for tool properties".format(tool.name))
        values = []
        for prop in tool.properties:
            try:
                prop_value = raw_input(prop)
            except EOFError as e:
                print("\nIncorrect input for tool. Aborting..")
                return
            else:
                values.append(prop_value)
        
        self.executeTool(tool, values)
    
    def executeTool(self, tool, values):
        tool.execute(values)

ToolManager = _ToolManager()

class Tool(object):
    manager = ToolManager

    def __init__(self, name, properties):
        self.name = name
        self.properties = properties.split()
        self.manager.addTool(self)
    
    def invoke(self):
        """
        The tool is invoked from the user interface
        """
        self.manager.invokeTool(self)

    def execute(self, values):
        print ("\n{0} with".format(self.name))
        for prop, value in zip(self.properties, values):
            print("\t '{0} -> {1}'".format(prop, value))

tool1 = Tool("Create Sphere", "name, radius")
tool2 = Tool("Create Cylinder", "name, radius, height")

print ToolManager.tools

tool1.invoke()

tool2.invoke()

tool1.execute(('sphere2', 3))

"""
OrderedDict([('Create Sphere', <__main__.Tool object at 0x00000007B07A3EB8>), ('Create Cylinder', <__main__.Tool object at 0x00000007B07A3E80>)])

User invoked tool 'Create Sphere'
Asking user to input values for tool properties
name,radius
Create Sphere with
	 'name, -> sphere1'
	 'radius -> 3'

User invoked tool 'Create Cylinder'
Asking user to input values for tool properties
name,radius,height
Create Cylinder with
	 'name, -> cyl1'
	 'radius, -> 2'
	 'height -> 4'

Create Sphere with
	 'name, -> sphere2'
	 'radius -> 3'
"""
