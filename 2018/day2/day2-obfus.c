#include <stdio.h>
int main(void){char b[100];char k[500][100]={0};int q=0;for(int i=0;fgets(b,100,stdin)!=NULL;i++,q++){memcpy(k[i],b,strlen(b));}for(int i=0;i<q;i++){for(int z=0;z<q;z++){int f=0;char p[100]={0};int r=0;for(int c=0;k[i][c]!=10;c++){if(k[i][c]==k[z][c]){p[r++]=k[i][c];}else{f++;}}p[r]=0;if(f==1){printf("%s\n",p);return 0;}}}}
