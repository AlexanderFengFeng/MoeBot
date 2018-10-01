/* package whatever; // don't place package name! */

import java.util.*;
import java.lang.*;
import java.io.*;

/* Name of the class has to be "Main" only if the class is public. */
class TreeGraphs
{
  // Here we are assuming that the array is filled
  private static Node createMinBST(int array[]) {
    return createMinBST(array, 0, array.length-1);
  }

  private static Node createMinBST(int array[], int start, int end) {
    int middle = (start+end)/2;
    if (start == end) {
      Node n = new Node(array[start]);
      return n;
    } else if (end < start) return null;

    Node center = new Node(array[middle]);
    center.left = createMinBST(array, start, middle-1);
    center.right = createMinBST(array, middle+1, end);
    return center;
  }

  private static void preOrder(Node n) {
    if (n == null) return;

    System.out.println(n.data);
    preOrder(n.left);
    preOrder(n.right);
  }

  private static ArrayList<LinkedListNode> treeToLinkedList(Node n) {
    if (n == null) return null;

    ArrayList<LinkedListNode> linkedLists = new ArrayList<LinkedListNode>();

    //List of nodes at one depth
    ArrayList<Node> nodes = new ArrayList<Node>();

    //Children of nodes at a depth. Replaces nodes
    ArrayList<Node> newNodes = new ArrayList<Node>();

    LinkedListNode curr = null;

    nodes.add(n);
    // Loops through each level
    while (!nodes.isEmpty()) {
      // Loops through the nodes at a level
      for (int i = 0; i < nodes.size(); i++) {
        Node currNode = nodes.get(i);
        LinkedListNode node = new LinkedListNode(currNode.data);
        if (i == 0) {
          linkedLists.add(node);
        } else {
          curr.next = node;
        }
        curr = node;
        // Adds the children for each node at a level
        if (currNode.left != null) newNodes.add(currNode.left);
        if (currNode.right != null) newNodes.add(currNode.right);
      }
      nodes.clear();
      for (int i = 0; i<newNodes.size(); i++) {
        nodes.add(newNodes.get(i));
      }
      newNodes.clear();
    }
    return linkedLists;
  }

  private static ArrayList<LinkedList<Node>> createLevelLinkedList(Node root) {
    ArrayList<LinkedList<Node>> res = new ArrayList<LinkedList<Node>>();
    LinkedList<Node> current = new LinkedList<Node>();
    if (root != null) current.add(root);

    while (current.size() > 0) {
      res.add(current);
      // Start a new linked list
      LinkedList<Node> parents = current;
      current = new LinkedList<Node>();
      for (Node parent : parents) {
        if (parent.left != null) current.add(parent.left);
        if (parent.right != null) current.add(parent.right);
      }
    }
    return res;
  }

  private static int getBalance(Node n) {
    int l, r;
    if (n.left == null) l = -1;
    else l = getBalance(n.left);
    if (n.right == null) r = -1;
    else r = getBalance(n.right);

    int balance = Math.abs(l-r);
    System.out.println(n.data + " " + balance);
    if (Math.abs(balance) > 1)
      balance = Integer.MAX_VALUE;
    return balance;
  }

  private static int checkHeight(Node n) {
    if (n == null) return -1;

    int left = checkHeight(n.left);
    if (left == Integer.MIN_VALUE) return left;
    int right = checkHeight(n.right);
    if (right == Integer.MIN_VALUE) return right;

    int balance = left - right;
    if (Math.abs(balance) > 1) return Integer.MIN_VALUE;
    else return Math.max(left, right) + 1;
  }
  
  private static void inOrder(Node n) {
    if (n == null) return;

    inOrder(n.left);
    System.out.println(n.data);
    inOrder(n.right);
  }

  private static boolean isBST(Node n) {
    if (n == null) return true;
    ArrayList<Node> list = new ArrayList<Node>();
    getInOrder(n, list);
    int greatest = Integer.MIN_VALUE;
    for (int i = 0; i < list.size(); i++) {
      int value = list.get(i).data;
      System.out.println(value);
      if (value <= greatest) return false;
      else {
        greatest = value; 
      }
    }
    return true;
  }

  private static void getInOrder(Node n, ArrayList<Node> list) {
    if (n == null) return;

    getInOrder(n.left, list);
    list.add(n);
    getInOrder(n.right, list);
  }

  private static boolean checkBST(Node n) {
    return checkBST(n, null, null);
  }
  
  private static boolean checkBST(Node n, Integer min, Integer max) {
    if (n == null) return true;

    // If n is not null and the values fall out of bounds
    if ((min != null && n.data <= min) || (max != null && n.data > max))
      return false;
    if ((!checkBST(n.left, min, n.data)) || !checkBST(n.right, n.data, max))
      return false;

    return true;
  }

  private static Node successor(Node n) {
    // No right children (must go to parent)
    if (n.right == null) {
      // Loops parent until a larger one is found or no parent is found 
      while (n.parent != null && n.parent.data < n.data)
        n = n.parent;
      if (n.parent == null) return null;
      else return n.parent;
    // If node has right child
    } else {
      // Goes to right child
      Node curr = n.right;
      // then looks all the way left
      while (curr.left != null)
        curr = curr.left;
      return curr;
    }
  }

  private static Node ancestorParents(Node n, Node m) {
    if (!doesIntersect(n, m)) return null;
    int a = depth(n);
    int b = depth(m);
    int diff = a - b;
    if (diff > 0) {
      for (int i = 0; i < diff; i++)
        n = n.parent;
    } else if (diff < 0) {
      for (int i = 0; i > diff; i--)
        m = m.parent;
    }
    while (n != null || m != null) {
      if (n == m) return n;
      n = n.parent;
      m = m.parent;
    }
    return n;
  }

  private static int depth(Node n) {
    int depth = 0;
    while (n != null) {
      n = n.parent;
      depth++;
    }
    return depth;
  }
  
  private static boolean doesIntersect(Node n, Node m) {
    if (n == null || m == null) return false;
    while (n.parent != null) n = n.parent;
    while (m.parent != null) m = m.parent;
    if (n == m) return true;
    else return false;
  }

  private static Node ancestor(Node n, Node a, Node b) {
    // If node a or b is not in the tree
    if (!find(n, a) || !find(n, b)) return null;
    return ancestorRec(n, a, b);
  }
  
  private static Node ancestorRec(Node n, Node a, Node b) {
    if (n == null || n == a || n == b) return n;

    boolean aOnLeft = find(n.left, a);
    boolean bOnLeft = find(n.left, b);

    if (aOnLeft != bOnLeft) return n;
    
    // Both on left
    if (aOnLeft) {
      return ancestorRec(n.left, a, b);
    // Both on right
    } else  {
      return ancestorRec(n.right, a, b);
    }
  }
  
  private static ArrayList<LinkedList<Integer>> sequences(Node n) {
    ArrayList<LinkedList<Integer>> list = ArrayList<LinkedList<Integer>>();
    
    if (n == null) {
      lists.add(new LinkedList<Integer>());
      return list;
    }

    LinkedList<Integer> prefix = new LinkedList<Integer>();
    prefix.add(n.data);

    ArrayList<LinkedList<Integer>> leftSeq = sequences(n.left);
    ArrayList<LinkedList<Integer>> rightSeq = sequences(n.right);

    for (LinkedList<Integer> left : leftSeq) {
      for (LinkedList<Integer> right : rightSeq) {
        ArrayList<LinkedList<Integer>> weaved = new ArrayList<LinkedList<Integer>>();
        weaveLists(left, right, weaved, prefix);
        result.addAll(weaved);
      }
    }
    return result;
  }

  private static void weaveLists(LinkedList<Integer> first, LinkedList<Integer> second,
      ArrayList<LinkedList<Integer>> results, LinkedList<Integer> prefix) {
    if (first.size() == 0 || second.size() == 0) {
      LinkedList<Integer> result = (LinkedList<Integer>) prefix.clone();
      result.addAll(first);
      result.addAll(second);
      results.add(result);
      return;
    }

  }

  private static boolean find(Node n, Node target) {
    if (n == null) return false;
    if (n == target) return true;
    return (find(n.left, target) || find(n.right, target));
  }

	public static void main(String[] args) throws java.lang.Exception
	{
    //4.2
    /*int[] array = new int[8];
    for (int i = 0; i<array.length; i++) {
      array[i] = i;
    }
    Node root = createMinBST(array);
    preOrder(root);
    
    System.out.println("Additional testing");
    Node curr = root;
    while (curr != null) {
      System.out.println(curr.data);
      curr = curr.right;
    }*/

    //4.3
    Node a = new Node(6);
    Node b = new Node(3);
    Node c = new Node(1);
    Node d = new Node(5);
    Node e = new Node(25);
    Node f = new Node(10);
    Node g = new Node(8);
    Node h = new Node(15);
    Node i = new Node(30);
    Node j = new Node(28);
    Node k = new Node(40);

    a.setLeft(b);
    a.setRight(e);
    b.setLeft(c);
    b.setRight(d);
    e.setLeft(f);
    e.setRight(i);
    f.setLeft(g);
    f.setRight(h);
    i.setLeft(j);
    i.setRight(k);

    System.out.println(ancestorParents(d, i).data);



    /*ArrayList<LinkedListNode> list = treeToLinkedList(a);
    System.out.println("Size: "+ list.size());
    for (int i = 0; i < list.size(); i++) {
      LinkedListNode n = list.get(i);
      System.out.println("List: "+ i);
      while (n != null) {
        System.out.println(n.data);
        n = n.next;
      }
    }*/
	}
}

class Node
{
  int data;
	Node left;
	Node right;
  Node parent = null;

	public Node(int data) {
    this.data = data;
		this.left = null;
    this.right = null;
	}
  public void setLeft(Node left) {
    this.left = left;
    left.parent = this;
  }
  public void setRight(Node right) {
    this.right = right;
    right.parent = this;
  }
}

class LinkedListNode
{
  int data;
  LinkedListNode next;
  public LinkedListNode(int data) {
    this.data = data;
    this.next = null;
  }
}
