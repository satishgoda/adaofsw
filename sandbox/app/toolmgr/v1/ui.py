import maya.cmds as cmds

from toolmgr import ToolManager

class ToolPropertiesWindow(object):
    def __init__(self, parent):
        self.parent = parent
        self.propsLayout = None
        self.propsUI = []
        self.propValues = {}
    
    def initialize(self, tool, executionCallback):
        if not self.propsLayout is None:
            self.cleanup()
        
        self.propsLayout = cmds.rowColumnLayout(parent=self.parent, numberOfColumns=2, columnAttach=(1, 'right', 0), columnWidth=[(1, 100), (2, 250)] )

        for prop in tool.properties:
            cmds.text(label=prop.capitalize())
            tf = cmds.textField()
            self.propsUI.append(tf)
        
        self.execButton = cmds.button(label='execute', command=partial(executionCallback, tool))

    def values(self):
        values = []
        for propUI in self.propsUI:
            value = cmds.textField(propUI, query=True, text=True)
            values.append(value)
        return values
    
    def cleanup(self):
        cmds.deleteUI(self.propsLayout)
        self.propsLayout = None
        self.propsUI = []
    
class ToolBoxWindow(object):
    def __init__(self, toolmgr):
        self.mgr = toolmgr
        self.window = cmds.window()
        self.pl = cmds.paneLayout( configuration='horizontal2')
        self.tl = cmds.treeLister()
        self.toolPropsWindow = ToolPropertiesWindow(self.pl)
    
    def show(self):
        cmds.dockControl(content=self.window, area='left', allowedArea=('left', 'right'))
    
    def initializeTools(self):
        for toolName in self.mgr.tools:
            tool = self.mgr.tools[toolName]['instance']
            cmds.treeLister(self.tl, edit=True, addItem = (tool.name, '', partial(self.invokeTool, tool)))

    def invokeTool(self, tool):        
        self.invokePropsWindow(tool)
    
    def invokePropsWindow(self, tool):
        self.toolPropsWindow.initialize(tool, self.executeTool)
        
    def executeTool(self, tool, incoming):
        values = self.toolPropsWindow.values()
        
        self.mgr.executeTool(tool, values)
        
        self.toolPropsWindow.cleanup()

createSphere = Tool("Create/Sphere", "name radius")
createCylinder = Tool("Create/Cylinder", "name radius height")

ToolManager.addTool(createSphere)
ToolManager.addTool(createCylinder)

tbw = ToolBoxWindow(ToolManager)

tbw.show()

tbw.initializeTools()
