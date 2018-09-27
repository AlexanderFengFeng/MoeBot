/* package whatever; // don't place package name! */

import java.util.*;
import java.lang.*;
import java.io.*;

/* Name of the class has to be "Main" only if the class is public. */
class StackQueues
{
	public static void main(String[] args) throws java.lang.Exception
	{
    Stack<Integer> stack = new Stack<Integer>();
    stack.push(3);
    System.out.println(stack.pop());
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


