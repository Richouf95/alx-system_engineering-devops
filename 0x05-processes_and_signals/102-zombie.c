#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/wait.h>


int infinite_while(void);

/**
 * main - main function
 * Return: 0
*/

int main(void)
{
	pid_t pid;
	int i;

	for (i = 0; i < 5; i++)
	{
		pid = fork();
		if (pid > 0)
		{
			printf("Zombie process created, PID: %d\n", pid);
			sleep(1);
		}
		else
			exit(0);
	}

	infinite_while();

	return (0);
}


/**
 * infinite_while - infinite while
 * Return: 0
*/

int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}
