#version 150 compatibility
#extension GL_EXT_geometry_shader4: enable
#extension GL_ARB_gpu_shader5 : enable

uniform float pointScale;
uniform int blackOn; //FILTER 1
uniform int blackToBlue; //CHANGE COLOR

flat out vec3 vertex_light_position;
flat out vec4 eye_position;
flat out float sphere_radius;

uniform float globalAlpha;

void
main(void)
{
    	sphere_radius =  pointScale * 2.0;
    	float halfsize = sphere_radius * 0.5;

    	gl_FrontColor = gl_FrontColorIn[0];
    	gl_FrontColor.a = globalAlpha;

	//Example using the gl_FrontColor values for filtering!!
	//now these hold colors.  in our case they will store r=day, g=hr, b=min, a=individualId

	bool drawPoint = true;
	
	//turn off if the r value is 0 (black) and main program tells us to turn off black
	if( gl_FrontColor.r == 0.0 && blackOn == 0 ) 
	    drawPoint = false;

	//change points where r = 0 to blue and main program tells us to do this
	if( gl_FrontColor.r == 0.0 && blackToBlue == 1 )
	    gl_FrontColor.b = 1.0; 

	    
	if( drawPoint ) {
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
