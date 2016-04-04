import maya.cmds as cmds

from toolmgr import ToolManager

class ToolManagerWindow(object):
    def __init__(self, toolmgr):
        self.mgr = toolmgr
        self.window = TreeListWindow()
        self.propsWindow = None
        self.propsUI = []
        self.propValues = {}
        self.initializeTools()
    
    def show(self):
        self.window.show()
    
    def initializeTools(self):
        for toolName in self.mgr.tools:
            self.addToolWidget(self.mgr.tools[toolName]['instance'])
    
    def addToolWidget(self, tool):
        self.window.treeLister.addItem = (tool.name, '', partial(self.invokeTool, tool))

    def invokeTool(self, tool):        
        self.invokePropsWindow(tool)
    
    def invokePropsWindow(self, tool):
        self.propsWindow = cmds.window(title=tool.name)
        cmds.rowColumnLayout( numberOfColumns=2, columnAttach=(1, 'right', 0), columnWidth=[(1, 100), (2, 250)] )

        for prop in tool.properties:
            cmds.text(label=prop.capitalize())
            tf = cmds.textField()
            self.propsUI.append(tf)
        self.execButton = cmds.button(label='execute', command=partial(self.executeTool, tool))
        
        cmds.showWindow(self.propsWindow)
    
    def executeTool(self, tool, incoming):
        values = []

        for propUI in self.propsUI:
            values.append(cmds.textField(propUI, query=True, text=True))
        
        tool.execute(values)
        cmds.deleteUI(self.propsWindow)
        
        self.propsWindow = None
        self.propsUI = []

def testUI():
    createSphere = Tool("Create Sphere", "name radius")
    createCylinder = Tool("Create Cylinder", "name radius height")
    
    ToolManager.addTool(createSphere)
    ToolManager.addTool(createCylinder)
    
    tmw = ToolManagerWindow(ToolManager)
    
    tmw.show()

testUI()
