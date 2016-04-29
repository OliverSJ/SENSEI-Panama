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
# plane.setEffect("textured -v emissive -d 50Island.png")


#-----------------------------------------------------------------------------
#PointCloud code
scene = getSceneManager()
scene.addLoader(BinaryPointsLoader())

setNearFarZ(0.1, 1000000)

# pointProgram = ProgramAsset()
# pointProgram.name = "points"
# pointProgram.vertexShaderName = "islandShaders/Sphere.vert"
# pointProgram.fragmentShaderName = "islandShaders/Sphere.frag"
# pointProgram.geometryShaderName = "islandShaders/Sphere.geom"
# pointProgram.geometryOutVertices = 4
# pointProgram.geometryInput = PrimitiveType.Points
# pointProgram.geometryOutput = PrimitiveType.TriangleStrip
# scene.addProgram(pointProgram)

# pointScale = Uniform.create('pointScale', UniformType.Float, 1)
# pointScale.setFloat(1)
# globalAlpha = Uniform.create('globalAlpha', UniformType.Float, 2)
# globalAlpha.setFloat(1)

# pointCloudModel = ModelInfo()
# pointCloudModel.name = 'pointCloud'
# pointCloudModel.path = 'hmColorHigh.xyzb'
# #pointCloudModel.options = "10000 100:1000000:5 20:100:4 6:20:2 0:5:1"
# pointCloudModel.options = "10000 100:1000000:20 20:100:10 6:20:5 0:5:5"
# #pointCloudModel.options = "10000 0:1000000:1"
# scene.loadModel(pointCloudModel)

# pointCloud = StaticObject.create(pointCloudModel.name)
# # attach shader uniforms
# mat = pointCloud.getMaterial()
# mat.setProgram(pointProgram.name)
# mat.attachUniform(pointScale)
# mat.attachUniform(globalAlpha)
# getDefaultCamera().setPosition(imgResRatioX*10260/2, imgResRatioY*9850/2, 2500)

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

selectedIndividual1 = Uniform.create('selectedIndividual1', UniformType.Int, 1) #if 1, shaders turn on.  If 0, shaders turn off
selectedIndividual1.setInt(4693)

selectedIndividual2 = Uniform.create('selectedIndividual2', UniformType.Int, 1) #if 1, shaders turn on.  If 0, shaders turn off
selectedIndividual2.setInt(4693)

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
moveMat.attachUniform(selectedIndividual1)
moveMat.attachUniform(selectedIndividual2)
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
ss2 = mm.getMainMenu().addSubMenu("Step Through Options")
btnOneUp = ss2.addButton("Forward a day", "oneDayStepUp(1)")
btnOneDown = ss2.addButton("Backward a day", "oneDayStepDown(1)")
btnSvnUp = ss.addButton("7 Days", "sevenDayStepUp(1)")
btnSvnUp = ss.addButton("7 Days", "sevenDayStepDown(1)")

#SUBMENU COLOR
ss3 = mm.getMainMenu().addSubMenu("Color Options")
btnGrad1 = ss3.addButton("Hour Gradient 1", "setColorBy(0)")
btnGrad2 = ss3.addButton("Hour Gradient 2", "setColorBy(1)")
btnGrad3 = ss3.addButton("Hour Gradient 3", "setColorBy(2)")
btnGrad4 = ss3.addButton("Day Gradient 1", "setColorBy(3)")
btnGrad5 = ss3.addButton("Day Gradient 2", "setColorBy(4)")
btnGrad6 = ss3.addButton("Color by individual", "setColorBy(5)")

ss4 = mm.getMainMenu().addSubMenu("selected Individual 1")
ss4.setStyleValue('fill', '#954FEA')
btn1 = ss3.addButton("Veruca 4690", "setSelInd1(4690)")
btn2 = ss3.addButton("Chibi 4693", "setSelInd1(4693)")
btn3 = ss3.addButton("Abby 4652", "setSelInd1(4652)")
btn4 = ss3.addButton("Ben Bob 4653", "setSelInd1(4653)")
btn5 = ss3.addButton("Bonnie 4658", "setSelInd1(4658)")
btn6 = ss3.addButton("Chloe 4052", "setSelInd1(4052)")
btn7 = ss3.addButton("Clementina 4672", "setSelInd1(4672)")
btn8 = ss3.addButton("Ellie 4668", "setSelInd1(4668)")
btn9 = ss3.addButton("Gillian 4671", "setSelInd1(4671)")
btn10 = ss3.addButton("Ornette 4669", "setSelInd1(4669)")
btn11 = ss3.addButton("Pliny 4675", "setSelInd1(4675)")
btn12 = ss3.addButton("Ripley 4650", "setSelInd1(4650)")
btn13 = ss3.addButton("Serge 4670", "setSelInd1(4670)")
btn14 = ss3.addButton("Sofie 4674", "setSelInd1(4674)")
btn15 = ss3.addButton("Greg 4689", "setSelInd1(4689)")
btn16 = ss3.addButton("Ibeth 4654", "setSelInd1(4654)")
btn17 = ss3.addButton("Olga 4657", "setSelInd1(4657)")
btn18 = ss3.addButton("Mimi 4660", "setSelInd1(4660)")
btn19 = ss3.addButton("Kyle 4692", "setSelInd1(4692)")
btn20 = ss3.addButton("Atlas 4673", "setSelInd1(4673)")
btn21 = ss3.addButton("Vielle 4670", "setSelInd1(4670)")
btn22 = ss3.addButton("Judy 4656", "setSelInd1(4656)")
btn23 = ss3.addButton("Merk 4665", "setSelInd1(4665)")

ss5 = mm.getMainMenu().addSubMenu("selected Individual 2")
ss5.setStyleValue('fill', '#5588F4')
btn1 = ss5.addButton("Veruca 4690", "setSelInd2(4690)")
btn2 = ss5.addButton("Chibi 4693", "setSelInd2(4693)")
btn3 = ss5.addButton("Abby 4652", "setSelInd2(4652)")
btn4 = ss5.addButton("Ben Bob 4653", "setSelInd2(4653)")
btn5 = ss5.addButton("Bonnie 4658", "setSelInd2(4658)")
btn6 = ss5.addButton("Chloe 4052", "setSelInd2(4052)")
btn7 = ss5.addButton("Clementina 4672", "setSelInd2(4672)")
btn8 = ss5.addButton("Ellie 4668", "setSelInd2(4668)")
btn9 = ss5.addButton("Gillian 4671", "setSelInd2(4671)")
btn10 = ss5.addButton("Ornette 4669", "setSelInd2(4669)")
btn11 = ss5.addButton("Pliny 4675", "setSelInd2(4675)")
btn12 = ss5.addButton("Ripley 4650", "setSelInd2(4650)")
btn13 = ss5.addButton("Serge 4670", "setSelInd2(4670)")
btn14 = ss5.addButton("Sofie 4674", "setSelInd2(4674)")
btn15 = ss5.addButton("Greg 4689", "setSelInd2(4689)")
btn16 = ss5.addButton("Ibeth 4654", "setSelInd2(4654)")
btn17 = ss5.addButton("Olga 4657", "setSelInd2(4657)")
btn18 = ss5.addButton("Mimi 4660", "setSelInd2(4660)")
btn19 = ss5.addButton("Kyle 4692", "setSelInd2(4692)")
btn20 = ss5.addButton("Atlas 4673", "setSelInd2(4673)")
btn21 = ss5.addButton("Vielle 4670", "setSelInd2(4670)")
btn22 = ss5.addButton("Judy 4656", "setSelInd2(4656)")
btn23 = ss5.addButton("Merk 4665", "setSelInd2(4665)")


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

	print( "one day step up" + myStartDay)

def oneDayStepDown(value):
    global myStartDay
    global myEndDay
    global numberOfDays

    myStartDay = myStartDay - 1
    if myStartDay < 0:
        myStartDay = numberOfDays-1
    myEndDay = myStartDay + 1
    endDay.setInt(myEndDay)
    startDay.setInt(myStartDay)

    print( "one day step down " + myStartDay)

def sevenDayStepUp(value):
    global myStartDay
    global myEndDay
    global numberOfDays

    myStartDay = myStartDay + 7
    if myStartDay > numberOfDays:
        myStartDay = 0
    myEndDay = myStartDay + 7
    endDay.setInt(myEndDay)
    startDay.setInt(myStartDay)

    print( "seven day step up" + myStartDay)

def sevenDayStepDown(value):
    global myStartDay
    global myEndDay
    global numberOfDays

    myStartDay = myStartDay - 7
    if myStartDay < 0:
        myStartDay = numberOfDays-7
    myEndDay = myStartDay + 7
    endDay.setInt(myEndDay)
    startDay.setInt(myStartDay)

    print( "seven day step down " + myStartDay)

def allDay(value):
	global numberOfDays
	endDay.setInt(numberOfDays)
	startDay.setInt(0)

	print( "one day step " + myStartDay)

def setColorBy(value):
    colorBy.setInt(value)

    print( "set color by " + value)

def setSelIn1(value):
    colorBy.setInt(value)

    print( "set color by " + value)

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
