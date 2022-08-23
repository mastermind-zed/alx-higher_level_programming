#include "lists.h"
/**
 * insert_node - function that insert a number into a sorted singly linked list
 * @head: pointer to the first element of the list.
 * @number: integer
 * Return: address of the new node, or NULL if it failed
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *prior; 
	listint_t *node = *head;

	prior = malloc(sizeof(listint_t));
	if (prior == NULL)
		return (NULL);
	prior->n = number;

	if (node == NULL || node->n >= number)
	{
		prior->next = node;
		*head = prior;
		return (prior);
	}

	while (node && node->next && node->next->n < number)
		node = node->next;

	prior->next = node->next;
	node->next = prior;

	return (prior);
}
