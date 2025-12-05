stack = [] 
s = "Hello" 
for ch in s: 
 stack.append(ch) 
rev = "" 
while stack: 
 rev += stack.pop() 
print("Original:", s) 
print("Reversed:", rev) 
