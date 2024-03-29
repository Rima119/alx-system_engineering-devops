#include <stdlib.h>
#include <stdio.h>
#include <sys/types.h>
#include <sys/wait.h>
#include <unistd.h>

/**
 * infinite_while - functions that runs an infinite while loop
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

/**
 * main - Entry point
 * Return: 0
 */
int main(void)
{
	int n;
	pid_t p;

	for (n = 0; n < 5; n++)
	{
		p = fork();
		if (p > 0)
		{
			printf("Zombie process created, PID: %d\n", p);
			sleep(1);
		}
		else
			exit(0);
	}
	infinite_while();
	return (0);
}
