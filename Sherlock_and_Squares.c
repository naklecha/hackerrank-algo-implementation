#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

main(a,b){scanf("%d");while(scanf("%d%d",&a,&b)>0)printf("%d\n",(int)(floor(sqrt(b))-ceil(sqrt(a))+1));}
