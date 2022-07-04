#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * checkpalindrome - recursive function to check list
 * @first: head of the list
 * @last: last list
 * Return: value of the list
 */
int checkpalindrome(listint_t **first, listint_t *last)
{
	int list;

	if (last == NULL)
		return (1);

	list = checkpalindrome(first, last->next);
	if (list == 0)
		return (0);
	
	else
	{
		list = ((*first)->n == last->n);
		*first = (*first)->next;
	}
	return (list);
}

/**
 * is_palindrome - function to check palindrome
 * @head: pointer to the list
 *
 * Return: the integers
 */
int is_palindrome(listint_t **head)
{
	if (!head)
		return (0);

	else
		return (checkpalindrome(head, *head));
}
