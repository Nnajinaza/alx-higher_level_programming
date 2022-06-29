#include "lists.h"
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

/**
 * insert_node - inserts a number into a sorted singly linked list.
 * @head: the head.
 * @number: the number.
 * Return: the new node.
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *a = *head;
	listint_t *b = *head;
	listint_t *new;

	if (*head == NULL)
		return (add_nodeint_end(head, number));

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	if (number < a->n)
	{
		new->n = number;
		new->next = b;
		*head = new;
		return (*head);
	}
	while (a->next != NULL)
	{
		a = a->next;
		if ((b->n <= number) && (a->n >= number))
		{
			new->n = number;
			new->next = a;
			b->next = new;
			return (new);
		}
		b = b->next;
	}
	free(new);
	return (add_nodeint_end(head, number));
}
