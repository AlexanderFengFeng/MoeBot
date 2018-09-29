/* package whatever; // don't place package name! */

import java.util.*;
import java.lang.*;
import java.io.*;

/* Name of the class has to be "Main" only if the class is public. */
class StackQueues
{
  private static void sort(Stack<Integer> s) {
    Stack<Integer> r = new Stack<Integer>();
    
    while (!s.isEmpty()) { //Will loop until s is empty
      int temp = s.pop();
      while (!r.isEmpty() && r.peek() > temp) {
        s.push(r.pop());
      }
       r.push(temp);
    }

    //Reverse r onto s
    while (!r.isEmpty()) {
      s.push(r.pop());
    }
  }

	public static void main(String[] args) throws java.lang.Exception
	{
    //MyQueue q = new MyQueue();
    SortedStack s = new SortedStack();
    s.push(6);
    s.push(1);
    s.push(4);
    s.push(3);
    s.push(2);
    s.push(5);
    while (s.isEmpty() == false) {
      System.out.println(s.pop());
    }
	}
}

class MyQueue
{
  Stack<Integer> first = new Stack<Integer>();
  int firstLen = 0;

  Stack<Integer> second = new Stack<Integer>();
  int secondLen = 0;

  public void push(int v) {
    first.push(v);
    firstLen++;
  }

  public int pop() {
    if (secondLen == 0)
      if (firstLen == 0)
        throw new EmptyStackException();
      else
        reverse();
    int v = second.pop();
    secondLen--;
    return v;
  }

  public int peek() {
    if (secondLen == 0)
      if (firstLen == 0)
        throw new EmptyStackException();
      else
        reverse();
    int v = second.peek();
    return v;
  }

  private void reverse() {
    int iter = firstLen;
    for (int i=0; i<iter; i++) {
      second.push(first.pop());
      firstLen--;
      secondLen++;
    }
  }
}

class SortedStack
{
  Stack<Integer> smallest = new Stack<Integer>();
  Stack<Integer> largest = new Stack<Integer>();

  public void push(int v) {
    if (smallest.empty() && largest.empty())
      smallest.push(v);
    else {
      // If we need to reorder
      if (smallest.peek() < v) {
        int restack = 0;
        while (smallest.peek() < v) {
          largest.push(smallest.pop());
          restack++;
        }
        largest.push(v);
        for (int i=0; i<restack+1; i++) {
          smallest.push(largest.pop());
        }
      // Else if we can just plop it on
      } else {
        smallest.push(v);
      }
    }
  }

  public int pop() {
    if (smallest.empty())
      throw new EmptyStackException();
    int v = smallest.pop();
    return v;
  }

  public int peek() {
    if (smallest.empty())
      throw new EmptyStackException();
    int v = smallest.peek();
    return v;
  }

  public boolean isEmpty() {
    return smallest.empty();
  }
}

class Animal {
  private int order;
  protected String name;

  //Constructor
  public Animal(String n) {name = n;}

  public void setOrder(int ord) {order = order;}
  public int getOrder() {return order;}

  public boolean isOlderThan(Animal a) {
    return this.order < a.getOrder();
  }
}

class AnimalQueue {
  LinkedList<Dog> dogs = new LinkedList<Dog>();
  LinkedList<Cat> cats = new LinkedList<Cat>();
  private int order = 0;
  
  public void enqueue(Animal a) {
    a.setOrder(order);
    order++;

    if (a instanceof Dog) dogs.addLast((Dog) a);
    else if (a instanceof Cat) cats.addLast((Cat) a);
  }
  
  public Animal dequeueAny() {
    if (dogs.size() == 0) return dequeueCats();
    if (cats.size() == 0) return dequeueDogs();
    Dog dog = dogs.peek();
    Cat cat = cats.peek();
    if (dog.isOlderThan(cat)) return dequeueDogs();
    else return dequeueCats();
  }

  public Dog dequeueDogs() { return dogs.poll(); }

  public Cat dequeueCats() { return cats.poll(); }
}

class Dog extends Animal {
  public Dog(String n) { super(n); }
}

class Cat extends Animal {
  public Cat(String n) { super(n); }
}
































