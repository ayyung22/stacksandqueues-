#CIS 103 XY Fundamentals of Programming
#Homework Assignment 8: Stacks and Queues
#Author: Annie Yung
#Date: 11/21/24

from collections import deque

print("Part 1: Stacks")
class Stack:
    def __init__(self):
        self.stack = []

    def push(self, value):
        #Add an element to the stack
        self.stack.append(value)

    def pop(self):
        #Remove and returns the top element
        if not self.is_empty():
            return self.stack.pop()
        else:
            raise IndexError("pop from an empty stack")

    def peek(self):
        #Return the top element without removing it
        if not self.is_empty():
            return self.stack[-1]
        else:
            raise IndexError("peek from an empty stack")

    def is_empty(self):
        #Checks if the stack is empty
        return len(self.stack) == 0


#Example
if __name__ == "__main__":
    # Create a stack and perform the operations
    s = Stack()

    # Pushing three elements
    s.push(0)
    s.push(10)
    s.push(20)

    # Pop one element
    popped = s.pop()

    # Peek at the top element
    top = s.peek()

    # Output results
    print(f"Popped element: {popped}")
    print(f"Top element after popping: {top}")

print()
print()

print("Part 2: Matching Parentheses")

def is_balanced(expression):
    # Create an empty stack
    stack = []
    matching_bracket = {')': '(', '}': '{', ']': '['}

    for char in expression:
        # If the character is an opening bracket, then it will push it onto the stack
        if char in matching_bracket.values():
            stack.append(char)
        elif char in matching_bracket:
            if not stack or stack[-1] != matching_bracket[char]:
                return False
            #Pops the top of the stack
            stack.pop()

    # If the stack is empty, all opening brackets had matching closing brackets
    return len(stack) == 0


#Examples
print(is_balanced("{[()]}"))
print(is_balanced("{[(])}"))
print(is_balanced("{[}"))
print(is_balanced("()"))
print(is_balanced("({[()]})"))
print(is_balanced("{[}"))
print(is_balanced("()[]{}"))
print(is_balanced("[({})]"))

print("Question 3: Converting Infix to Postfix")
print()
print()

def infix_to_postfix(expression):
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
    left_associative = {'+': True, '-': True, '*': True, '/': True, '^': False}  # '^' is right associative

    # Stack to hold the operators and parentheses
    stack = []
    # List to store the output
    output = []

    # Iterate through each character in the input expression
    for char in expression:
        if char.isalnum():
            output.append(char)
        elif char == '(':
            stack.append(char)
        elif char == ')':
            while stack and stack[-1] != '(':
                output.append(stack.pop())
            stack.pop()
        else:
            while (stack and stack[-1] != '(' and
                   (precedence[char] < precedence.get(stack[-1], 0) or
                    (precedence[char] == precedence.get(stack[-1], 0) and left_associative.get(char, True)))):
                output.append(stack.pop())
            stack.append(char)

    while stack:
        output.append(stack.pop())

    return ''.join(output)

# Test cases
print(infix_to_postfix("A*(B+C)"))
print(infix_to_postfix("A+B*C"))
print(infix_to_postfix("(A+B)*(C-D)"))
print(infix_to_postfix("A+B*(C-D)"))
print(infix_to_postfix("A^B^C"))
print(infix_to_postfix("A+(B*C-(D/E^F)*G)*H"))

print("Part 2: Queues")
print()
class Queue:
    def __init__(self):
        # Initialize an empty deque
        self.queue = deque()

    def enqueue(self, element):
        # Add an element to the rear of the queue
        self.queue.append(element)

    def dequeue(self):
        # Remove and return the front element of the queue
        if not self.is_empty():
            return self.queue.popleft()  # Removes and returns from the front of the queue
        else:
            raise IndexError("dequeue from an empty queue")  #Raises an error if the queue is empty

    def peek(self):
        # Returns the front element without removing it
        if not self.is_empty():
            return self.queue[0]
        else:
            raise IndexError("peek from an empty queue")  # Raises an error if the queue is empty

    def is_empty(self):
        # Check if the queue is empty
        return len(self.queue) == 0

#Example
def test_queue():
    q = Queue()
    q.enqueue(10)
    q.enqueue(20)
    q.enqueue(30)  #
    print(f"Peek front element: {q.peek()}")

    q.dequeue()  # Dequeue 10
    print(f"Peek front element after dequeue: {q.peek()}")

test_queue()

print()
print()
print("Question 5: Customer Checkout Simulation")

class CheckoutQueue:
    def __init__(self, service_time):
        self.queue = deque()  # Creates the queue of customers
        self.service_time = service_time  # Shows the time taken to serve each customer

    def add_customer(self, customer_name):
        self.queue.append(customer_name)

    def serve_customer(self):
        if not self.is_empty():
            customer = self.queue.popleft()
            return customer
        else:
            return None

    def is_empty(self):
        return len(self.queue) == 0

    def calculate_total_wait_time(self):
        total_wait_time = 0
        customers_served = 0

        while not self.is_empty():
            customer = self.serve_customer()
            if customer:
                wait_time = customers_served * self.service_time
                print(f"Customer {customer} is being served. Wait time: {wait_time} minutes.")
                total_wait_time += wait_time
                customers_served += 1

        return total_wait_time

def checkout_simulation(customers, service_time_per_customer):
    queue = CheckoutQueue(service_time_per_customer)

    # Adds all customers to the queue
    for customer in customers:
        queue.add_customer(customer)

    # Calculatse the total wait time for all customers
    total_wait_time = queue.calculate_total_wait_time()

    print(f"\nTotal wait time for all customers: {total_wait_time} minutes.")

# Test the program
customers = ["James", "Sarah", "Raul", "Hootie"]
service_time_per_customer = 5  # 5 minutes per customer

checkout_simulation(customers, service_time_per_customer)
