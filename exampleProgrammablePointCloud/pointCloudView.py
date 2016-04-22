from cyclops import *
from pointCloud import *

scene = getSceneManager()
scene.addLoader(BinaryPointsLoader())

#***FILTERS CREATED HERE
blackOn = Uniform.create('blackOn', UniformType.Int, 1) #if 1, shaders turn on.  If 0, shaders turn off
blackToBlue = Uniform.create('blackToBlue', UniformType.Int, 1)#if 1, shaders turn on.  If 0, shaders turn off   
blackOn.setInt(1)
blackToBlue.setInt(0)

#Point cloud created here- makes sure it is different name from James point cloud
pointProgram = ProgramAsset()
pointProgram.name = "points"
pointProgram.vertexShaderName = "myShaders/Sphere.vert" #here are our shaders
pointProgram.fragmentShaderName = "myShaders/Sphere.frag"
pointProgram.geometryShaderName = "myShaders/Sphere.geom"#this is the one we will modify to filter and color points
pointProgram.geometryOutVertices = 4
pointProgram.geometryInput = PrimitiveType.Points
pointProgram.geometryOutput = PrimitiveType.TriangleStrip
scene.addProgram(pointProgram)

pointScale = Uniform.create('pointScale', UniformType.Float, 1)
pointScale.setFloat(5.0)#can change point size here, as needed

pointCloudModel = ModelInfo()
pointCloudModel.name = 'pointCloud'
pointCloudModel.path = 'newpng.xyzb'
#pointCloudModel.options = "10000 100:1000000:5 20:100:4 6:20:2 0:5:1"
pointCloudModel.options = "10000 100:1000000:20 20:100:10 6:20:5 0:5:5"
#pointCloudModel.options = "10000 0:1000000:1"
scene.loadModel(pointCloudModel)

pointCloud = StaticObject.create(pointCloudModel.name)
# attach shader uniforms
mat = pointCloud.getMaterial()
mat.setProgram(pointProgram.name)
mat.attachUniform(pointScale)

#****ASSOCIATE FILTERS WITH THE POINT CLOUD
mat.attachUniform(blackOn)
mat.attachUniform(blackToBlue)

getDefaultCamera().setPosition(0, 10, 50)
getDefaultCamera().lookAt(pointCloud.getBoundCenter(), Vector3(0,1,0))


    
#  EVENT HANDLERS
## here is where we will get the wand events, and toggle through days and individuals
## for now, i am using it to turn on and off the black points, and change the black points to blue
def handleEvent():
    e = getEvent()
    
    if(e.isButtonDown(EventFlags.ButtonLeft)): 
        print("Left button pressed turning off black")
        blackOn.setInt(0)
    if(e.isButtonDown(EventFlags.ButtonUp)): 
        print("Up button pressed turning off black to blue")
        blackToBlue.setInt(0)
    if(e.isButtonDown(EventFlags.ButtonRight)):
        print("Left button pressed turning on black")
        blackOn.setInt(1)
    if(e.isButtonDown(EventFlags.ButtonDown)):
        print("Up button pressed turning on black to blue")
        blackToBlue.setInt(1)

setEventFunction(handleEvent)

## to see how the shaders handle these changes, go to the myShaders/Sphere.geom file
