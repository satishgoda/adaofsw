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
    def __init__(self, name, properties):
        self.name = name
        self.properties = properties.split()

    def execute(self, values):
        print ("\n{0} with".format(self.name))
        for prop, value in zip(self.properties, values):
            print("\t '{0} -> {1}'".format(prop, value))

def test():
    createSphere = Tool("Create Sphere", "name radius")
    createCylinder = Tool("Create Cylinder", "name radius height")
    
    ToolManager.addTool(createSphere)
    ToolManager.addTool(createCylinder)
    
    print ToolManager.tools
    
    ToolManager.invokeTool(createSphere)
    
    print ToolManager.tools[createSphere.name]['history']
    
    createSphere.execute(ToolManager.tools[createSphere.name]['history'][-1])
    
    ToolManager.invokeTool(createCylinder)
    
    print ToolManager.tools[createCylinder.name]['history']
    
    createCylinder.execute(ToolManager.tools[createCylinder.name]['history'][0])
