#include <stdio.h>
#include <string.h>
#define MAXLINE 1000

int mygetline(char line[], int max){

	int c;
	int i = 0;
	while( (c = getchar()) != EOF && c != '\n' &&  --max > 0 ){
		line[i++] = c;
	}
	if (c == '\n')
		line[i++] = c ;
	line[i] = '\0';
	return i;
}


int main( int argc, char* argv[]){

	if (argc != 2 ){
		printf("Usage: [stdin] | ./mygrep [pattern]\n ");
		return 0; 
	}
	char line[MAXLINE];
	while(mygetline(line,MAXLINE) > 0){
		if( strstr(line,argv[1]) != NULL )
			printf("%s",line);
	}
	return 0;

}
