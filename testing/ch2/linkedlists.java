/* package whatever; // don't place package name! */

import java.util.*;
import java.lang.*;
import java.io.*;

/* Name of the class has to be "Main" only if the class is public. */
class LinkedLists
{
	public int add(int a, int b) {
		return a+b;
	}

/*	private static void delDupes(Node n) {
		Node curr = n;
		while (curr != null) {
			Node runner = curr;
			while (runner.next != null) {
				System.out.print(curr.data);
				System.out.print(runner.next.data);
				System.out.println();
				if (runner.next.data == curr.data) {
					runner.next = runner.next.next;
				} else {
					runner = runner.next;
				}
			}
			curr = curr.next;
		}
	}
	
	private static Node kthNode (int k, Node n) {
		Node m = n;
		int length = 1;
		while (n.next != null) {
			n = n.next;
			length++;
		}
		for (int i = 0; i < length-k; i++) {
			m = m.next;
		}
		return m;
	}
	
	private static Node partition (int k, Node n) {
		Node lesser = null;
		Node greater = null;
		Node lesserHead = null;
		Node greaterHead = null;
		
		while (n != null) {
			n.next = null;
			if (n.data < k) {
				if (lesser == null)
					lesserHead = n;
				else
					lesser.next = n;
				lesser = n;
			} else {
				if (greater == null)
					greaterHead = n;
				else 
					greater.next = n;
				greater = n;
			}
			n = n.next;
		}
		if (greater == null) {
			lesser.next = null;
			return lesser;
		}
		greater.next = null;
		if (lesser == null)
			return greaterHead;
		lesser.next = greaterHead;
		return lesserHead;
	}
*/	
	private static void printList(Node n) {
		while (n != null) {
			System.out.print(n.data);
			n = n.next;
		}
		System.out.println();
	}
	
	private static boolean palindrome (Node n) {
		Node m = reverse(n);
		while (n != null) {
			if (m.data != n.data)
				return false;
			n = n.next;
			m = m.next;
		}
		return true;
	}
	
	private static Node reverse (Node n) {
		Node head = null;
		while (n != null) {
			Node m = new Node(n.data);
			m.next = head;
			head = m;
			n = n.next;
		}
		return head;
	}
	
	private static Node reverseOverwrite(Node n) {
		Node head = null;
		Node next;
		while (n != null) {
			next = n.next;
			n.next = head;
			head = n;
			n = next;
		}
		return head;
	}
	
	private static boolean doesIntersect (Node n, Node m) {
		while (n.next != null ) {
			n = n.next;
		}
		while (m.next != null) {
			m = m.next;
		}
		if (n == m)
			return true;
		else
			return false;
	}
	
	private static Node intersect (Node n, Node m) {
		if (n == null || m == null)
			return null;
		if (doesIntersect(n, m) == false)
			return null;
		int diff = length(n) - length(m);
		if (diff < 0) { // m has greater length
			for (int i = 0; i > diff; i--)
				m = m.next;
		} else if (diff > 0) {
			for (int i = 0; i < diff; i++)
				n = n.next;
		}
		while (n != null && m != null) {
			if (n == m)
				return n;
			n = n.next;
			m = m.next;
		}
		return null;
	}
	
	private static int length(Node n) {
		int len = 0;
		while (n != null) {
			len++;
			n = n.next;
		}
		return len;
	}
	
/*	private static Node sum (Node n, Node m) {
		int over = 0, sum, a, b;
		Node head = null, tail = null;
		while (n!= null || m!= null) {
			if (n == null)
				a = 0;
			else {
				a = n.data;
				n = n.next;
			}
			if (m == null)
				b = 0;
			else {
				b = m.data;
				m = m.next;
			}
			sum = a+b+over;
			if (sum >= 10) {
				sum = sum % 10;
				over = 1;
			} else {
				over = 0;
			}
			Node node = new Node(sum);
			if (head == null) {
				head = node;
				tail = head;
			} else {
				tail.next = node;
				tail = node;
			}
		}
		if (over != 0) {
			Node node = new Node(over);
			tail.next = node;
		}
		return head;
	}
*/
  private static Node loopNode(Node n)
  {
    Node curr = n;
    Node runner = n;
    while (runner.next != null) {
      if (curr.next == runner.next.next) {
        return curr.next;
      } else {
        curr = curr.next;
        runner = runner.next.next;
      }
      if (runner == null) {
        return null;
      }
    }
    return null;
  }

  private static Node loop(Node n)
  {
    Node curr = n;
    Node loop = loopNode(n);
    if (loop == null)
      return null;
    while (curr != loop) {
      curr = curr.next;
      loop = loop.next;
    }
    return curr;
  }

	public static void main(String[] args) throws java.lang.Exception
	{
		Node a = new Node('a');
		Node b = new Node('b');
		Node c = new Node('c');
		Node d = new Node('d');
		Node e = new Node('e');
		Node f = new Node('f');
		Node g = new Node('g');
		a.next = b;
		b.next = c;
		c.next = d;
		d.next = e;
		e.next = f; 
		f.next = d;
		System.out.println("Inital linked list");
		System.out.println("Next");
		Node head = loop(a);
    if (head != null)
		  System.out.println(head.data);
    else
      System.out.println("Head is null");
	}
}

class Node
{
	char data;
	Node next;
	public Node(char data) {
		this.data = data;
		this.next = null;
	}
}
