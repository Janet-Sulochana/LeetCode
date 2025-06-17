/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
 struct ListNode *detectCycle(struct ListNode *head) {
    struct ListNode *visited[10000];
    int index=0;
    while(head!=NULL)
    {
        for(int i=0;i<index;i++)
        {
            if(visited[i]==head)
            {
                return head;
            }
        }
        if(index>=10000)break;
        visited[index++]=head;
        head=head->next;
    }
    return NULL;
}