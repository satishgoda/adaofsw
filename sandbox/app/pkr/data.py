class ItemTransform(object):
    """
    scale, rotation, translation, parent
    """
    def __init__(self):
        self.scale = [1, 1]
        self.rotation = 0.0
        self.translation = [0, 0]
        self.parent = None

class ItemShape(object):
    """
    primitive - box, ellipse, polygon
    image
    """

    def draw(self, color):
        print self.shape, color

class BoxShape(ItemShape):
    def __init__(self):
        self.shape = 'box'

class CircleShape(ItemShape):
    def __init__(self):
        self.shape = 'circle'

class ItemColor(object):
    """
    color
    """
    def __init__(self, color='yellow'):
        self.color = color

class ItemAction(object):
    """
    controls
    script
    """
    def __init__(self):
        pass

class ItemControlsAction(ItemAction):
    def __init__(self):
        super(ItemControlsAction, self).__init__()
        self.setControls([])
    
    def type(cls):
        return "controls"
    
    def setControls(self, controls):
        self.controls = controls
    
    def removeControls(self):
        self.setControls([])
    
    def execute(self):
        if not self.controls:
            print "No controls associated with this item"
            return
        print("Selecting controls ",self.controls)

class ItemScriptAction(ItemAction):
    def __init__(self):
        super(ItemScriptAction, self).__init__()
        self.setScript("")
    
    def setScript(self, script):
        self.script = script
    
    def _validate(self):
        return bool(self.script.strip())
    
    def execute(self):
        if not self._validate():
            print("Error in script")
            return 
        print("Executing script")
        print(self.script)
    
    def type(cls):
        return "script"

class Item(object):
    def __init__(self, id):
        self.id = id
        self.setTransform(ItemTransform())
        self.setShape(BoxShape())
        self.setColor(ItemColor())
        self.setAction(ItemControlsAction())
    
    def setTransform(self, transform):
        self.transform = transform
    
    def setColor(self, color):
        self.color = color
    
    def setShape(self, shape):
        self.shape = shape

    def setAction(self, action):
        self.action = action
    
    def draw(self):
        color = self.getColor()
        self.shape.draw(color)

    def executeAction(self):
        self.action.execute()
    
    def getColor(self):
        return self.color.color
    
    def type(self):
        return self.action.type()

##

item1 = Item('item1')

print item1.type()
item1.draw()
item1.executeAction()
item1.action.setControls(['L_Arm', 'L_Leg', 'L_Ear'])
item1.executeAction()
item1.action.removeControls()
item1.executeAction()
item1.setColor(ItemColor('red'))
item1.draw()

script1 = ItemScriptAction()
script1.execute()
script1.setScript("""pm.select("*_ctrl")""")
script1.execute()

item1.setAction(script1)

item1.executeAction()

item1.draw()
item1.executeAction()

item1.setShape(CircleShape())

item1.draw()
item1.executeAction()
