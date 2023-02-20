class Robot {
 int w,h,p=0,per; boolean moved=false;
 public Robot(int width,int height){w=width;h=height;per=2*(w+h)-4;}
 public void step(int num){p=(p+num)%per;moved=true;}
 public int[] getPos(){if(p<=w-1)return new int[]{p,0}; if(p<=w+h-2)return new int[]{w-1,p-(w-1)};if(p<=2*w+h-3)return new int[]{w-1-(p-(w+h-2)),h-1};return new int[]{0,h-1-(p-(2*w+h-3))};}
 public String getDir(){if(p==0)return moved?"South":"East";if(p<=w-1)return "East";if(p<=w+h-2)return "North";if(p<=2*w+h-3)return "West";return "South";}
}