#include "lists.h"
/**
 * check_cycle - check if there is a cycle in the linked list
 * @list: A pointer to the head of the list
 *
 * Return: 0 if there no cycle, 1 if there is a cycle.
 **/
int check_cycle(listint_t *list)
{
	listint_t *slow = list;
	listint_t *fast = list;

	if (list == NULL)
	{
		return (0);
	}


	while (fast != NULL && fast->next != NULL)
	{
		slow = slow->next;
		fast = fast->next->next;

		if (slow == fast)
		{
			return (1);
		}
	}

	return (0);
}
