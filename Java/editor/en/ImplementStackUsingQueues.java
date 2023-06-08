  /**
Implement a last-in-first-out (LIFO) stack using only two queues. The 
implemented stack should support all the functions of a normal stack (push, top, pop, and 
empty). 

 Implement the MyStack class: 

 
 void push(int x) Pushes element x to the top of the stack. 
 int pop() Removes the element on the top of the stack and returns it. 
 int top() Returns the element on the top of the stack. 
 boolean empty() Returns true if the stack is empty, false otherwise. 
 

 Notes: 

 
 You must use only standard operations of a queue, which means that only push 
to back, peek/pop from front, size and is empty operations are valid. 
 Depending on your language, the queue may not be supported natively. You may 
simulate a queue using a list or deque (double-ended queue) as long as you use 
only a queue's standard operations. 
 

 
 Example 1: 

 
Input
["MyStack", "push", "push", "top", "pop", "empty"]
[[], [1], [2], [], [], []]
Output
[null, null, null, 2, 2, false]

Explanation
MyStack myStack = new MyStack();
myStack.push(1);
myStack.push(2);
myStack.top(); // return 2
myStack.pop(); // return 2
myStack.empty(); // return False
 

 
 Constraints: 

 
 1 <= x <= 9 
 At most 100 calls will be made to push, pop, top, and empty. 
 All the calls to pop and top are valid. 
 

 
 Follow-up: Can you implement the stack using only one queue? 

 Related Topics Stack Design Queue 👍 3556 👎 916

*/
  
  package com.shuzijun.leetcode.editor.en;

  import java.util.LinkedList;
  import java.util.Queue;

  public class ImplementStackUsingQueues{
      public static void main(String[] args) {
          MyStack solution = new ImplementStackUsingQueues().new MyStack();
      }
      //leetcode submit region begin(Prohibit modification and deletion)
class MyStack {
    private Queue<Integer> queue1;
    private Queue<Integer> queue2;

    public MyStack() {
        this.queue1 = new LinkedList<>();
        this.queue2 = new LinkedList<>();
    }
    
    public void push(int x) {
        if (this.empty() || !this.queue1.isEmpty()) this.queue1.add(x);
        else this.queue2.add(x);
    }
    
    public int pop() {
        int res = 0;
        if (!this.queue1.isEmpty()) {
            while (!this.queue1.isEmpty()) {
                res = this.queue1.poll();
                if (this.queue1.isEmpty()) return res;
                this.queue2.add(res);
            }
        }
        while (!this.queue2.isEmpty()) {
            res = this.queue2.poll();
            if (this.queue2.isEmpty()) return res;
            this.queue1.add(res);
        }
        return res;
    }
    
    public int top() {
        int res = 0;
        if (!this.queue1.isEmpty()) {
            while (!this.queue1.isEmpty()) {
                res = this.queue1.poll();
                this.queue2.add(res);
            }
        } else {
            while (!this.queue2.isEmpty()) {
                res = this.queue2.poll();
                this.queue1.add(res);
            }
        }
        return res;
    }
    
    public boolean empty() {
        return this.queue1.isEmpty() && this.queue2.isEmpty();
    }
}

/**
 * Your MyStack object will be instantiated and called as such:
 * MyStack obj = new MyStack();
 * obj.push(x);
 * int param_2 = obj.pop();
 * int param_3 = obj.top();
 * boolean param_4 = obj.empty();
 */
//leetcode submit region end(Prohibit modification and deletion)

  }