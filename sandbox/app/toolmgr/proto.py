from collections import OrderedDict

class _ToolManager(object):
    def __init__(self):
        self.tools = OrderedDict()
    
    def addTool(self, tool):
        self.tools[tool.name] = {'instance': tool, 'history': []}
    
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
        
        self.tools[tool.name]['history'].append(values)
        
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

createSphere = Tool("Create Sphere", "name, radius")
createCylinder = Tool("Create Cylinder", "name, radius, height")

print ToolManager.tools

createSphere.invoke()

createSphere.invoke()

print ToolManager.tools[createSphere.name]['history']

createCylinder.invoke()

print ToolManager.tools[createCylinder.name]['history']

createSphere.execute(('sphere2', 3))

createCylinder.execute(('cylinder20', 3, 6))


"""
OrderedDict([('Create Sphere', {'instance': <__main__.Tool object at 0x00000007E9128E80>, 'history': []}), ('Create Cylinder', {'instance': <__main__.Tool object at 0x00000007E9128F98>, 'history': []})])

User invoked tool 'Create Sphere'
Asking user to input values for tool properties
name,radius
Create Sphere with
	 'name, -> sph1'
	 'radius -> 2'

User invoked tool 'Create Sphere'
Asking user to input values for tool properties
name,radius
Create Sphere with
	 'name, -> sph2'
	 'radius -> 4'
[[u'sph1', u'2'], [u'sph2', u'4']]

User invoked tool 'Create Cylinder'
Asking user to input values for tool properties
name,radius,height
Create Cylinder with
	 'name, -> cyl1'
	 'radius, -> 2'
	 'height -> 3'
[[u'cyl1', u'2', u'3']]

Create Sphere with
	 'name, -> sphere2'
	 'radius -> 3'

Create Cylinder with
	 'name, -> cylinder20'
	 'radius, -> 3'
	 'height -> 6'
"""
