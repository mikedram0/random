#include <stdio.h>
#include <conio.h>
//#include <stdlib.h>
#include <string.h>

int main(){

	FILE *f;
	f=fopen("C:\\Users\\kwnspir\\Desktop\\a.txt","w");
	unsigned long long int n=9999999999,i,j;
	char c[21];
	int good=1;
	for(i=0;i<n;i++){
		printf("%ld\n",i);
		sprintf(c,"%ld",i);
		good=1;
		for(j=0;j<21;j++){
			if(c[j]=='0' || c[j]=='5'){
				good=0;
				break;
			}
		}
		if (good>0){
			fprintf(f,c);
			fprintf(f,"\n");
		}
	}


	fclose(f);
	printf("FINISH\n");
	getch();
	return 0;
}