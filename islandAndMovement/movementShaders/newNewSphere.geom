#version 150 compatibility
#extension GL_EXT_geometry_shader4: enable
#extension GL_ARB_gpu_shader5 : enable

uniform float movePointScale;

uniform int startDay;
uniform int endDay;

uniform int colorBy;
uniform int selectedIndividual1;
uniform int selectedIndividual2;


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
	bool drawPoint = false;

  //figure out if this point will be drawn
  //day = 1, startDay =1 endDay =2 -> draw
   //day =2 or 0, startDay = 1 end day = 2 not draw
  if( individualID == selectedIndividual1 || individualID == selectedIndividual2 )
      drawPoint = true; 
  if( drawPoint && (day < startDay || day >= endDay) )
	    drawPoint = false;
	    
	if( drawPoint ) {

    gl_FrontColor = vec4( 255.0/255.0 , 0.0, 0.0 , 1.0); 

    if( colorBy == 0 ){ //one color palette
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
    }
    if( colorBy == 1 ){
      if( hr < 3 )
        gl_FrontColor = vec4( 69.0/255.0,117.0/255.0,180.0/255.0, 1.0 );
      if( hr >= 3 && hr < 6 )
        gl_FrontColor = vec4( 116.0/255.0,173.0/255.0,209.0/255.0, 1.0 );
      if( hr >= 6 && hr < 9 )
        gl_FrontColor = vec4(171.0/255.0,217.0/255.0,233.0/255.0, 1.0 );
      if( hr >= 9 && hr < 12 )
        gl_FrontColor = vec4( 224.0/255.0,243.0/255.0,248.0/255.0, 1.0 );
      if( hr >= 12 && hr < 15 )
        gl_FrontColor = vec4( 254.0/255.0,224.0/255.0,144.0/255.0, 1.0 );
      if( hr >= 15 && hr < 18 )
        gl_FrontColor = vec4( 253.0/255.0,174.0/255.0,97.0/255.0, 1.0 );
      if( hr >= 18 && hr < 21 )
        gl_FrontColor = vec4( 244.0/255.0,109.0/255.0,67.0/255.0, 1.0 );
      if( hr >= 21 && hr < 24 )
        gl_FrontColor = vec4( 215.0/255.0,48.0/255.0,39.0/255.0, 1.0 );
    }
    if( colorBy == 2){
      if( hr < 3 )
        gl_FrontColor = vec4( 104.0/255.0,79.0/255.0,227.0/255.0, 1.0 );
      if( hr >= 3 && hr < 6 )
        gl_FrontColor = vec4( 78.0/255.0,181.0/255.0,226.0/255.0, 1.0 );
      if( hr >= 6 && hr < 9 )
        gl_FrontColor = vec4( 138.0/255.0,227.0/255.0,244.0/255.0, 1.0 );
      if( hr >= 9 && hr < 12 )
        gl_FrontColor = vec4( 253.0/255.0,247.0/255.0,155.0/255.0, 1.0 );
      if( hr >= 12 && hr < 15 )
        gl_FrontColor = vec4( 253.0/255.0,222.0/255.0,115.0/255.0, 1.0 );//
      if( hr >= 15 && hr < 18 )
        gl_FrontColor = vec4( 253.0/255.0,247.0/255.0,155.0/255.0, 1.0 );
      if( hr >= 18 && hr < 21 )
        gl_FrontColor = vec4( 138.0/255.0,227.0/255.0,244.0/255.0, 1.0 );
      if( hr >= 21 && hr < 24 )
        gl_FrontColor = vec4( 78.0/255.0,181.0/255.0,226.0/255.0, 1.0 );
    }
    if( colorBy == 3){
      if( day < 10 )
        gl_FrontColor = vec4( 247.0/255.0,251.0/255.0,255.0/255.0, 1.0 );
      if( day >= 10 && day < 20 )
        gl_FrontColor = vec4( 222.0/255.0,235.0/255.0,247.0/255.0, 1.0 );
      if( day >= 20 && day < 30 )
        gl_FrontColor = vec4( 198.0/255.0,219.0/255.0,239.0/255.0, 1.0 );
      if( day >= 30 && day < 40 )
        gl_FrontColor = vec4( 158.0/255.0,202.0/255.0,225.0/255.0, 1.0 );
      if( day >= 40 && day < 50 )
        gl_FrontColor = vec4( 107.0/255.0,174.0/255.0,214.0/255.0, 1.0 );
      if( day >= 50 && day < 60 )
        gl_FrontColor = vec4( 66.0/255.0,146.0/255.0,198.0/255.0, 1.0 );
      if( day >= 60 && day < 70 )
        gl_FrontColor = vec4( 33.0/255.0,113.0/255.0,181.0/255.0, 1.0 );
      if( day >= 70 && day < 84 )
        gl_FrontColor = vec4( 8.0/255.0,81.0/255.0,156.0/255.0, 1.0 );
    }
    if( colorBy == 4){
      if( day < 10 )
        gl_FrontColor = vec4( 255.0/255.0,247.0/255.0,243.0/255.0, 1.0 );
      if( day >= 10 && day < 20 )
        gl_FrontColor = vec4( 253.0/255.0,224.0/255.0,221.0/255.0, 1.0 );
      if( day >= 20 && day < 30 )
        gl_FrontColor = vec4( 252.0/255.0,197.0/255.0,192.0/255.0, 1.0 );
      if( day >= 30 && day < 40 )
        gl_FrontColor = vec4( 250.0/255.0,159.0/255.0,181.0/255.0, 1.0 );
      if( day >= 40 && day < 50 )
        gl_FrontColor = vec4( 247.0/255.0,104.0/255.0,161.0/255.0, 1.0 );
      if( day >= 50 && day < 60 )
        gl_FrontColor = vec4( 221.0/255.0,52.0/255.0,151.0/255.0, 1.0 );
      if( day >= 60 && day < 70 )
        gl_FrontColor = vec4( 174.0/255.0,1.0/255.0,126.0/255.0, 1.0 );
      if( day >= 70 && day < 84 )
        gl_FrontColor = vec4( 122.0/255.0,1.0/255.0,119.0/255.0, 1.0 );
    }
    if( colorBy == 5 ){
      if( individualID == selectedIndividual1 )
        gl_FrontColor = vec4( 149.0/255.0,79.0/255.0,234.0/255.0, 1.0 );
      if( individualID == selectedIndividual2 )
        gl_FrontColor = vec4( 85.0/255.0,136.0/255.0,244.0/255.0, 1.0 );
    }



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
