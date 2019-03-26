#include <stdio.h>
#include <pthread.h>

void *fir(long long unsigned int n1,long long unsigned int n2);
void *sec(long long unsigned int n1,long long unsigned int n2);

int main(){
	long long unsigned int n1,n2;
	printf("Give starting and ending number");
	scanf("%llu %llu",&n1,&n2);
	pthread_t thread_id1,thread_id2;
    	pthread_create(&thread_id1, NULL, fir(n1,n2), NULL);
    	pthread_create(&thread_id2, NULL, sec(n1,n2), NULL); 
    	pthread_join(thread_id1, NULL);  
    	pthread_join(thread_id2, NULL);
	return 0;
}

void *fir(long long unsigned int n1,long long unsigned int n2){
	FILE *f;
	f=fopen("fout.txt","w");
	long long unsigned int i,j;
	char c[50];
	int good= 1;
	for(i=n1;i<n2;i=i+2){

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
}

void *sec(long long unsigned int n1,long long unsigned int n2){
	FILE *f2;
	f2=fopen("sout.txt","w");
	long long unsigned int i,j;
	char c2[50];
	int good2= 1;
	for(i=n1+1;i<n2;i=i+2){

		sprintf(c2,"%llu",i);
		good2=1;
		for(j=0;j<=21;j++){
			if(c2[j]=='0' || c2[j]=='5'){
				good2=0;
				break;
			}
		}
		if (good2>0){
			fputs(c2,f2);
			fputs("\n",f2);
		}
	}


	fclose(f2);
	printf("FINISH\n");
}
