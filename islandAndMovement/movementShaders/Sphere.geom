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
    sphere_radius =  pointScale * 2.0;
    float halfsize = sphere_radius * 0.5;

    gl_FrontColor = gl_FrontColorIn[0];
    //gl_FrontColor.a = globalAlpha;

	int individualID = int(gl_FrontColor.a);
	int day = int(gl_FrontColor.r);
	int hr = int(gl_FrontColor.g);
	int min = int(gl_FrontColor.b);
	  
	//Example using the gl_FrontColor values for filtering!!
	bool drawPoint = true;

    //figure out if this point will be drawn
    //day = 1, startDay =1 endDay =2 -> draw
    //day =2 or 0, startDay = 1 end day = 2 not draw
    if( day < startDay || day >= endDay )
	    drawPoint = true;
	if( individualID != selectedIndividual )
	    drawPoint = true;

    drawPoint = true;
	    
	if( drawPoint ) {
        //where to put it?
	    vec3 in_gl_Position = gl_PositionIn[0];

	    float utmE = in_gl_Position.x;
	    float utmN = in_gl_Position.y;
	    float ht = in_gl_Position.z;

	    //convert utm to x, y
        float utmE1 = 624030.0137255481; //0.18/(float(10260)/32064) * 10260
        float utmN1 = 1015207.0834458455; //.18/(float(9850)/30780) * 9850
        float utmE2 = 629801.5337255481;//624030.0137255481 + 32064.0 * .18
        float utmN2 = 1009666.6834458455;//1015207.0834458455 - 30780.0 * .18

        float totalW = 5771.52; 
        float totalH = 5540.4;

        vec3 my_gl_Position;
        my_gl_Position.x =  in_gl_Position.x; //0.0; //(utmE1-utmE)/(utmE2-utmE1) *totalW;
        my_gl_Position.y =  in_gl_Position.y; //0.0; //(utmN2-utmN)/(utmN2-utmN1) *totalH;
        my_gl_Position.z = .5; 

/*
	    //set color
	    if( colorBy == 0 ){ //color by time of day
	    	if( hr < 4 )
		      gl_FrontColor = vec4(	254.0/255.0 , 235.0/255.0 , 226.0/255.0 , 1.0);
            if( hr >= 4 && hr < 8 )
                gl_FrontColor = vec4( 252.0/255.0 , 197.0/255.0, 192.0/255.0 , 1.0);    	    
            if( hr >= 8 && hr < 12 )
                gl_FrontColor = vec4( 250.0/255.0 , 159.0/255.0 , 181.0/255.0  , 1.0);
            if( hr >= 12 && hr < 16 )
                gl_FrontColor = vec4( 247.0/255.0, , , 1.0);  
            if( hr >= 16 && hr < 20 )
                gl_FrontColor = vec4( 252.0/255.0 , 197.0/255.0, 192.0/255.0 , 1.0); 
            if( hr >= 20 && hr < 24 )
                gl_FrontColor = vec4( 252.0/255.0 , 197.0/255.0, 192.0/255.0 , 1.0); 
	    }

*/
        gl_FrontColor = vec4( 255.0/255.0 , 0.0, 0.0 , 1.0); 

    	    eye_position = my_gl_Position;//gl_PositionIn[0];
    	    vertex_light_position = normalize(gl_LightSource[0].position.xyz - eye_position.xyz);

    	    gl_TexCoord[0].st = vec2(1.0,-1.0);
    	    gl_Position = my_gl_Position;//gl_PositionIn[0];
    	    gl_Position.xy += vec2(halfsize, -halfsize);
    	    gl_Position = gl_ProjectionMatrix * gl_Position;
    	    EmitVertex();
    
	    gl_TexCoord[0].st = vec2(1.0,1.0);
    	    //gl_Position = gl_PositionIn[0];
            gl_Position = my_gl_Position;
    	    gl_Position.xy += vec2(halfsize, halfsize);
    	    gl_Position = gl_ProjectionMatrix * gl_Position;
    	    EmitVertex();

    	    gl_TexCoord[0].st = vec2(-1.0,-1.0);
    	    //gl_Position = gl_PositionIn[0];
            gl_Position = my_gl_Position;
    	    gl_Position.xy += vec2(-halfsize, -halfsize);
    	    gl_Position = gl_ProjectionMatrix * gl_Position;
    	    EmitVertex();

    	    gl_TexCoord[0].st = vec2(-1.0,1.0);
    	    //gl_Position = gl_PositionIn[0];
            gl_Position = my_gl_Position;
    	    gl_Position.xy += vec2(-halfsize, halfsize);
    	    gl_Position = gl_ProjectionMatrix * gl_Position;
    	    EmitVertex();
    
	    EndPrimitive();
	}
}
