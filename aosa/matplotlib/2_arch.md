
One Figure, Multiple Backends/Output Devices

* Stack

 * Layer 3 - scripting - (knows about 2)
 * Layer 2 - artist  - (knows about 1)
 * Layer 1 - backend - (itself)

* Layer 1 (backend) - Implements the abstract interfaces of 

 * FigureCanvas - Encapsulates the concept of a surface to draw into (Paper)
 * Renderer - Does the rendering (Paintbrush)
 * Event - Handles user inputs such as keyboard and mouse events

