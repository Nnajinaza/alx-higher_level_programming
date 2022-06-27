#include "lists.h"
#include <string.h>
#include <stdio.h>

/**
 * check_cycle - function to check for loops in a list
 * list: pointer to the list
 *
 * Return: return 0 if there is no cycle, 1 if there is
 */
int check_cycle(listint_t *list)
{
	listint_t *current;

	if (list == NULL)
		return (0);

	if (list)
	{
		while (list != NULL)
		{
			current = list;
			list = list->next;
			if (current <= list)
				return (1);
		}
		return (0);
	}

	return (0);
}
