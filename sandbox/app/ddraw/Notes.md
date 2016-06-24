SceneItems 


SceneRenderer 

* SceneWireframeRenderer
* SceneShadedRenderer 


SceneView 

* SceneWireframeView 
* SceneShadedView 


SceneView.draw(scene, 'wireframe') 
    
    items = scene.items() 
    renderer = scene.getRenderer('wireframe') 
    
    for item in items: 
        Renderer.draw(item) 
