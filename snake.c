#include <stdio.h>
#include <stdlib.h>
#include <ncurses.h>
#include <time.h>

#define WIDTH 50
#define HEIGHT 15


int main(){
	srand(time(NULL)); 	
	initscr();
	curs_set(0);
	noecho();
	timeout(0);	

	WINDOW* win = newwin(HEIGHT, WIDTH, 0 , 0 );


	struct piece {
	
		int x;
		int y;
		char dir;

	};

	struct food {
		
		int x;
		int y;
	
	} food = {1 + rand() % (WIDTH -2),1+ rand() % (HEIGHT -2)} ;


	int N = 5;
	char snake_char = 'o';
	char food_char = '#';
	struct piece* snake = malloc(N*sizeof(struct piece));
	for (int i = N-1; i >= 0 ; --i){
	
		snake[i].x = N-i;
	       	snake[i].y = 1;
		snake[i].dir = 'r';

	}
	bool isRunning = TRUE;
	bool grow = FALSE;
	while (isRunning){
	
		mvwaddch(win,food.y,food.x,food_char);
		for(int i = N-1 ; i >= 0 ; --i ){
			mvwaddch(win,snake[i].y,snake[i].x,snake_char);
		
			if( i != 0 && (snake[i].x == snake[0].x && snake[i].y == snake[0].y))
				isRunning = FALSE;
			switch(snake[i].dir){
			
				case 'u':
					--snake[i].y;
					break;
				case 'd':
					++snake[i].y;
					break;
				case 'l':
					--snake[i].x;
					break;
				case 'r':
					++snake[i].x;
					break;
			}
			if (i != 0 )
				snake[i].dir = snake[i-1].dir;
	
		}
		if (snake[0].x <= 0 || snake[0].x >= (WIDTH-1) || snake[0].y >= (HEIGHT-1)  || snake[0].y <= 0 )
			isRunning = FALSE;
		if ((snake[0].x == food.x && snake[0].y == food.y) || grow){
			food.x = 1 + rand() % (WIDTH-2);
			food.y = 1 + rand() % (HEIGHT-2);
			snake = realloc(snake,(N+1)*sizeof(struct piece) );
			switch(snake[N-1].dir){
			
				case 'u':
					snake[N].x = snake[N-1].x ;
					snake[N].y = snake[N-1].y + 1;
					break;
				case 'd':
					snake[N].x = snake[N-1].x ;
					snake[N].y = snake[N-1].y - 1;
					break;
				case 'l':
					snake[N].x = snake[N-1].x +1 ;
					snake[N].y = snake[N-1].y;
					break;
				case 'r':
					snake[N].x = snake[N-1].x - 1 ;
					snake[N].y = snake[N-1].y;
					break;

				}
			snake[N].dir = snake[N-1].dir;
			N++;
			grow = FALSE;
		}
		int c;
		c = getch();
		switch(c){
			case 'g':
				grow = TRUE;
				break;
			case 'q':
				isRunning = FALSE;
				break;	
			case 'w':
				if (snake[0].dir != 'd')
					snake[0].dir = 'u';
				break;
			case 's':
				if (snake[0].dir != 'u')
					snake[0].dir = 'd';
				break;
			case 'a':
				if (snake[0].dir != 'r')
					snake[0].dir = 'l';
				break;
			case 'd':
				if (snake[0].dir != 'l')
					snake[0].dir = 'r';
				break;
		
		}
		mvprintw(0.2*HEIGHT,1.2*WIDTH,"Score: %d, %d",food.x,food.y);
		box(win,0,0);
		wrefresh(win);
		napms(100);	
		wclear(win);
	}


	endwin();

	return 0;

}
