#include <stdio.h>
#include<ctype.h>
/**
 * main - prints the alphabet in lowercase, and then in uppercase,
 * followed by a new line
 * Return: Always 0 (Success)
 */
int main(void)
{
	char ch,cap;

	for (ch = 'a'; ch <= 'z'; ch++)
	{
		putchar(ch);
		cap=toupper(ch);
		putchar(cap);
		putchar('\n');
	}
	for (ch = 'A'; ch <= 'Z'; ch++)
		putchar(ch);
	putchar('\n');
	return (0);
}
