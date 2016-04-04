import maya.cmds as cmds

from toolmgr import ToolManager

class ToolManagerWindow(object):
    def __init__(self, toolmgr):
        self.mgr = toolmgr
        self.window = cmds.window()
        self.pl = cmds.paneLayout( configuration='horizontal2')
        self.tl = cmds.treeLister()
        self.propsLayout = None
        self.propsUI = []
        self.propValues = {}
        self.initializeTools()
    
    def show(self):
        cmds.showWindow(self.window)
    
    def initializeTools(self):
        for toolName in self.mgr.tools:
            self.addToolWidget(self.mgr.tools[toolName]['instance'])
    
    def addToolWidget(self, tool):
        cmds.treeLister(self.tl, edit=True, addItem = (tool.name, '', partial(self.invokeTool, tool)))

    def invokeTool(self, tool):        
        self.invokePropsWindow(tool)
    
    def invokePropsWindow(self, tool):
        if not self.propsLayout is None:
            self.cleanupPropsWindow()
        
        self.createPropsWindow(tool)
        
    def createPropsWindow(self, tool):
        self.propsLayout = cmds.rowColumnLayout(parent=self.pl, numberOfColumns=2, columnAttach=(1, 'right', 0), columnWidth=[(1, 100), (2, 250)] )

        for prop in tool.properties:
            cmds.text(label=prop.capitalize())
            tf = cmds.textField()
            self.propsUI.append(tf)
        self.execButton = cmds.button(label='execute', command=partial(self.executeTool, tool))
    
    def cleanupPropsWindow(self):
        cmds.deleteUI(self.propsLayout)
        self.propsLayout = None
        self.propsUI = []
    
    def executeTool(self, tool, incoming):
        values = []

        for propUI in self.propsUI:
            values.append(cmds.textField(propUI, query=True, text=True))
        
        self.mgr.executeTool(tool, values)
        
        self.cleanupPropsWindow()

def testUI():
    createSphere = Tool("Create Sphere", "name radius")
    createCylinder = Tool("Create Cylinder", "name radius height")
    
    ToolManager.addTool(createSphere)
    ToolManager.addTool(createCylinder)
    
    tmw = ToolManagerWindow(ToolManager)
    
    tmw.show()

testUI()
