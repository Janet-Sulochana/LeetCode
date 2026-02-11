/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    ListNode reverse(ListNode head){
        ListNode temp=head;
        ListNode prev=null;
        ListNode newHead;
        while(temp != null){
            ListNode fut = temp.next;
            temp.next=prev;
            prev= temp;
            temp=fut;
        }
        return prev;
    }
    public boolean isPalindrome(ListNode head) {

        if(head == null) return true;
        ListNode temp=head;
        ListNode copyHead=new ListNode(temp.val);
        ListNode copyTemp=copyHead;
        temp=temp.next;
        while(temp != null){
            copyTemp.next=new ListNode(temp.val);
            copyTemp=copyTemp.next;
            temp=temp.next;
        }

        ListNode newHead=reverse(copyHead);
        temp=head;
        
        while(temp != null){
            if(temp.val != newHead.val){return false;}
            temp=temp.next;
            newHead=newHead.next;
        }return true;
    }
}