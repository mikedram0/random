#include <stdio.h>

//#include <stdlib.h>
//#include <string.h>

int main(){

	FILE *f;
	f=fopen("outc.txt","w");
	long long unsigned int n1,n2,i,j;
	printf("Give starting and ending number");
	scanf("%llu %llu",&n1,&n2);
	char c[50];
	int good= 1;
	for(i=n1;i<n2;i++){

		sprintf(c,"%llu",i);
		good=1;
		for(j=0;j<=21;j++){
			if(c[j]=='0' || c[j]=='5'){
				good=0;
				break;
			}
		}
		if (good>0){
			fputs(c,f);
			fputs("\n",f);
		}
	}


	fclose(f);
	printf("FINISH\n");
	//getch();
	return 0;
}
