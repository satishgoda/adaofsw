
One Figure, Multiple Backends/Output Devices

## Stack

* Layer 3 - scripting - (knows about 2)
* Layer 2 - artist  - (knows about 1)
* Layer 1 - backend - (itself)

## Layer 1 (backend)

Implements the abstract interfaces of 

* FigureCanvas - Encapsulates the concept of a surface to draw into (Paper)
  * QtFigureCanvas knows how to insert itself into a native Qt window

* Renderer - Does the rendering (Paintbrush)
  * Transfer the matplotlib Renderer commands onto the canvas (QtGui.QPainter)

* Event - Handles user inputs such as keyboard and mouse events
  * Translate native Qt events into the matplotlib Event framework
  * This signals the event dispatcher to generate events so upstream listeners can handle them

