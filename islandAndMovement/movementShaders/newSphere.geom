#version 150 compatibility
#extension GL_EXT_geometry_shader4: enable
#extension GL_ARB_gpu_shader5 : enable

uniform float movePointScale;

uniform int startDay;
uniform int endDay;

uniform int colorBy;
uniform int selectedIndividual;

flat out vec3 vertex_light_position;
flat out vec4 eye_position;
flat out float sphere_radius;

uniform float globalAlpha;

void
main(void)
{
  sphere_radius =  movePointScale * 2.0;
  float halfsize = sphere_radius * 0.5;

  gl_FrontColor = gl_FrontColorIn[0];
  gl_FrontColor.a = globalAlpha;

	int day = int(gl_FrontColor.r);
	int hr = int(gl_FrontColor.g);
	int min = int(gl_FrontColor.b);
  int individualID = int(gl_FrontColor.a);
	  
	//Example using the gl_FrontColor values for filtering!!
	bool drawPoint = true;

  //figure out if this point will be drawn
  //day = 1, startDay =1 endDay =2 -> draw
   //day =2 or 0, startDay = 1 end day = 2 not draw
  if( day < startDay || day >= endDay )
	    drawPoint = false;
	//if( individualID != selectedIndividual )
	//    drawPoint = true;
	    
	if( drawPoint ) {

    gl_FrontColor = vec4( 255.0/255.0 , 0.0, 0.0 , 1.0); 

    if( hr < 4 )
      gl_FrontColor = vec4( 255.0/255.0,255.0/255.0,204.0/255.0, 1.0 );
    if( hr >= 4 && hr < 8 )
      gl_FrontColor = vec4( 199.0/255.0,233.0/255.0,180.0/255.0, 1.0 );
    if( hr >= 8 && hr < 12 )
      gl_FrontColor = vec4(127.0/255.0,205.0/255.0,187.0/255.0, 1.0 );
    if( hr >= 12 && hr < 16 )
      gl_FrontColor = vec4( 65.0/255.0,182.0/255.0,196.0/255.0, 1.0 );
    if( hr >= 16 && hr < 20 )
      gl_FrontColor = vec4( 44.0/255.0,127.0/255.0,184.0/255.0, 1.0 );
    if( hr >= 20 && hr < 24 )
      gl_FrontColor = vec4( 37.0/255.0,52.0/255.0,148.0/255.0, 1.0 );




    eye_position = gl_PositionIn[0];
    vertex_light_position = normalize(gl_LightSource[0].position.xyz - eye_position.xyz);

    gl_TexCoord[0].st = vec2(1.0,-1.0);
    gl_Position = gl_PositionIn[0];
    gl_Position.xy += vec2(halfsize, -halfsize);
    gl_Position = gl_ProjectionMatrix * gl_Position;
    EmitVertex();
      
    gl_TexCoord[0].st = vec2(1.0,1.0);
    gl_Position = gl_PositionIn[0];
    gl_Position.xy += vec2(halfsize, halfsize);
    gl_Position = gl_ProjectionMatrix * gl_Position;
    EmitVertex();

    gl_TexCoord[0].st = vec2(-1.0,-1.0);
    gl_Position = gl_PositionIn[0];
    gl_Position.xy += vec2(-halfsize, -halfsize);
    gl_Position = gl_ProjectionMatrix * gl_Position;
    EmitVertex();

    gl_TexCoord[0].st = vec2(-1.0,1.0);
    gl_Position = gl_PositionIn[0];
    gl_Position.xy += vec2(-halfsize, halfsize);
    gl_Position = gl_ProjectionMatrix * gl_Position;
    EmitVertex();
      
    EndPrimitive();
	}
}
