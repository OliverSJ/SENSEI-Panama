from omega import *
from cyclops import *
from pointCloud import *

#Directions
#Point Cloud should be the same size as the plane

#----------------------------------------------------------------------------
#Planeview code
imgResRatioX = 0.18/(float(10260)/32064)
imgResRatioY = 0.18/(float(9850)/30780)
plane = PlaneShape.create(imgResRatioX*10260, imgResRatioY*9850)
plane.setPosition(Vector3(imgResRatioX*10260/2, imgResRatioY*9850/2, 0))
plane.setEffect("textured -v emissive -d 50Island.png")


#-----------------------------------------------------------------------------
#PointCloud code
scene = getSceneManager()
scene.addLoader(BinaryPointsLoader())

setNearFarZ(0.1, 1000000)

pointProgram = ProgramAsset()
pointProgram.name = "points"
pointProgram.vertexShaderName = "islandShaders/Sphere.vert"
pointProgram.fragmentShaderName = "islandShaders/Sphere.frag"
pointProgram.geometryShaderName = "islandShaders/Sphere.geom"
pointProgram.geometryOutVertices = 4
pointProgram.geometryInput = PrimitiveType.Points
pointProgram.geometryOutput = PrimitiveType.TriangleStrip
scene.addProgram(pointProgram)

pointScale = Uniform.create('pointScale', UniformType.Float, 1)
pointScale.setFloat(1)
globalAlpha = Uniform.create('globalAlpha', UniformType.Float, 2)
globalAlpha.setFloat(1)

pointCloudModel = ModelInfo()
pointCloudModel.name = 'pointCloud'
pointCloudModel.path = 'hmColorHigh.xyzb'
#pointCloudModel.options = "10000 100:1000000:5 20:100:4 6:20:2 0:5:1"
pointCloudModel.options = "10000 100:1000000:20 20:100:10 6:20:5 0:5:5"
#pointCloudModel.options = "10000 0:1000000:1"
scene.loadModel(pointCloudModel)

pointCloud = StaticObject.create(pointCloudModel.name)
# attach shader uniforms
mat = pointCloud.getMaterial()
mat.setProgram(pointProgram.name)
mat.attachUniform(pointScale)
mat.attachUniform(globalAlpha)
getDefaultCamera().setPosition(imgResRatioX*10260/2, imgResRatioY*9850/2, 2500)

#---------------------------------------------------------------------------
# Movement point cloud code

#filters
startDay = Uniform.create('startDay', UniformType.Int, 1)
endDay = Uniform.create('endDay', UniformType.Int, 1)

myStartDay = 0
myEndDay = 1
dayIncrement = 1
numberOfDays = 84

startDay.setInt(myStartDay)
endDay.setInt(myEndDay)

colorBy = Uniform.create('colorBy', UniformType.Int, 1) #if 1, shaders turn on.  If 0, shaders turn off
colorBy.setInt(0)

selectedIndividual = Uniform.create('selectedIndividual', UniformType.Int, 1) #if 1, shaders turn on.  If 0, shaders turn off
selectedIndividual.setInt(4693)

movePointScale = Uniform.create('movePointScale', UniformType.Float, 1)
movePointScale.setFloat(8.0)

#Point cloud created here- makes sure it is different name from James point cloud
movePointProgram = ProgramAsset()
movePointProgram.name = "movePoints"
movePointProgram.vertexShaderName = "movementShaders/Sphere.vert" #here are our shaders
movePointProgram.fragmentShaderName = "movementShaders/Sphere.frag"
movePointProgram.geometryShaderName = "movementShaders/newSphere.geom"
movePointProgram.geometryOutVertices = 4
movePointProgram.geometryInput = PrimitiveType.Points
movePointProgram.geometryOutput = PrimitiveType.TriangleStrip
scene.addProgram(movePointProgram)

movePointCloudModel = ModelInfo()
movePointCloudModel.name = 'movePointCloud'
movePointCloudModel.path = 'allChibi.xyzb'#'XY_Chibi_Christmas_Parsed.xyzb'#'Chibi_Christmas_Parsed.xyzb' #'newpng.xyzb'
#movePointCloudModel.options = "10000 100:1000000:5 20:100:4 6:20:2 0:5:1"
movePointCloudModel.options = "10000 100:1000000:20 20:100:10 6:20:5 0:5:5"
#movePointCloudModel.options = "10000 0:1000000:1"
scene.loadModel(movePointCloudModel)

movePointCloud = StaticObject.create(movePointCloudModel.name)
# attach shader uniforms
moveMat = movePointCloud.getMaterial()
moveMat.setProgram(movePointProgram.name)

moveMat.attachUniform(movePointScale)
moveMat.attachUniform(startDay)
moveMat.attachUniform(endDay)
moveMat.attachUniform(selectedIndividual)
moveMat.attachUniform(colorBy)

#---------------------------------------------------------------------------
#Menu items
#PointSize slider created by: Alessandro
mm = MenuManager.createAndInitialize()
mm.getMainMenu().addLabel("Point Size")
pointss = mm.getMainMenu().addSlider(40, "onPointSizeSliderValueChanged(%value%)")
pointSlider = pointss.getSlider()
pointSlider.setValue(1)

#Controls alpha values of points created by: Alessandro
mm.getMainMenu().addLabel("Point Transparency")
alphass = mm.getMainMenu().addSlider(11, "onAlphaSliderValueChanged(%value%)")
alphaSlider = alphass.getSlider()
alphaSlider.setValue(10)

#SUBMENU CAMERA
ss = mm.getMainMenu().addSubMenu("Camera Options")
vbtn = ss.addButton("Vertical View", "viewVertical(1)")
hbtn = ss.addButton("Horizontal View", "viewHorizontal(1)")

#SUBMENU STEPTHRO
ss = mm.getMainMenu().addSubMenu("Step Through Options")
btnOneUp = ss.addButton("Forward a day", "oneDayStepUp(1)")
btnOneDown = ss.addButton("Backward a day", "oneDayStepDown(1)")

#btnOne.getButton().setRadio(True)
btnSvnUp = ss.addButton("7 Days", "sevenDayStepUp(1)")
btnSvnUp = ss.addButton("7 Days", "sevenDayStepDown(1)")
#btnSvn.setRadio(True)
ss.addLabel("--------------------")
btnAll = ss.addButton("All Days", "allDay(1)")
#btnAll.setRadio(True)



#--------------------------------------------------------------------------------------
#Functions
def oneDayStepUp(value):
	global myStartDay
	global myEndDay
	global numberOfDays

	myStartDay = myStartDay + 1
	if myStartDay > numberOfDays:
		myStartDay = 0
	myEndDay = myStartDay + 1
	endDay.setInt(myEndDay)
	startDay.setInt(myStartDay)

	print( "one day step " + myStartDay)


def sevenDayStep(value):
	print( "seven day step")
	# if (value == 1):
 #        a = value

def allDay(value):
	global numberOfDays
	endDay.setInt(numberOfDays)
	startDay.setInt(0)

	print( "one day step " + myStartDay)


def onPointSizeSliderValueChanged(value):
    if (value != 0):
        size = .95 + value * .05
    else:
        size = 0.0
    pointScale.setFloat(size)

def onAlphaSliderValueChanged(value):
    if (value != 0):
        a = value/10.0
    else:
        a = 0.0
    #globalAlpha.setFloat(a)
    pointCloud.getMaterial().setAlpha(a)

# def handleEvent():
#     e = getEvent()
#     print(getDefaultCamera().getPosition())         #prints location of camera
#     if (e.isButtonDown(EventFlags.ButtonDown)):
#         viewVertical(1)
#     if (e.isButtonDown(EventFlags.ButtonUp)):
#         viewHorizontal(1)
# setEventFunction(handleEvent)

def viewVertical(value):
    if (value == 1):
        getDefaultCamera().setPosition(Vector3(imgResRatioX*10260/2, imgResRatioY*9850/2, 2500))
        getDefaultCamera().setPitchYawRoll(Vector3(0,0,0))

def viewHorizontal(value):
    if (value == 1):
        getDefaultCamera().setPitchYawRoll(Vector3(45,0,0))
        getDefaultCamera().setPosition(Vector3(imgResRatioX*10260/2, 0, 500))



#--Event handler
#  EVENT HANDLERS
def handleEvent():
    e = getEvent()
    if(e.isButtonDown(EventFlags.ButtonLeft)): 
        print("Left button pressed ")
    #     myStartDay = myStartDay + dayIncrement
    #     myEndDay = myEndDay + dayIncrement
    #     if( myStartDay > numberOfDays ):
    #         myStartDay = 0
    #         myEndDay = dayIncrement
    #     endDay.setInt(myEndDay)
    #     startDay.setInt(myStartDay)
    # if(e.isButtonDown(EventFlags.ButtonRight)):
    #     myStartDay = myStartDay - dayIncrement
    #     myEndDay = myEndDay - dayIncrement
    #     if( myStartDay < 0 ):
    #         myStartDay = numberOfDays - dayIncrement
    #         myEndDay = numberOfDays
    #     endDay.setInt(myEndDay)
    #     startDay.setInt(myStartDay)
    # if(e.isButtonDown(EventFlags.ButtonUp)): 
    #     print("Up button pressed turning off white")
    # if(e.isButtonDown(EventFlags.ButtonDown)):
    #     print("Up button pressed turning on white")

setEventFunction(handleEvent)
