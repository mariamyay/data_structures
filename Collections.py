# -*- coding: utf-8 -*-
"""
Created on Wed Sep 21 18:59:57 2022

@author: Mariam
"""

from abc import ABC, abstractmethod

class Collection(ABC):
    @abstractmethod
    def is_empty(self):
        pass
    @abstractmethod
    def empty(self):
        pass
    @abstractmethod
    def print(self):
        pass
    
class List(Collection):
    @abstractmethod
    def addFirst(self,e):
        pass
    @abstractmethod
    def removeFirst(self):
        pass
    @abstractmethod
    def addLast(self,e):
        pass
    @abstractmethod
    def removeLast(self):
        pass
    @abstractmethod
    def first(self):
        pass
    @abstractmethod
    def last(self):
        pass
    @abstractmethod
    def replace(self,e,r):
        pass

class Stack(Collection):
    @abstractmethod
    def push(self,e):
        pass
    @abstractmethod
    def pop(self):
        pass
    @abstractmethod
    def top(self):
        pass


class LinkedList(List):
    class Node:
        def __init__(self, d, n=None):
            self._data=d
            self._next=n
            
    def __init__(self):
        self._first=None
        self._last=None
        self._length=0
    
    def is_empty(self):
        return self._length==0
    
    def empty(self):
        self._first=None
        self._length=0
    
    def print(self):
        current=self._first
        while(current):
            print(current._data)
            current=current._next
            
    def addFirst(self, e):
        n = self.Node(e, self._first)
        self._first=n
        if self.is_empty():
            self._last=n
        self._length+=1
        
    def removeFirst(self):
        if self.is_empty():
            return False
        if self._length==1:
            self._first=None
            self._last=None
            self._length=0
            return True
        else:
            n=self._first
            self._first=self._first._next
            n._next=None
            self._length-=1
        return True
        
    def addLast(self, e):
        n=self.Node(e, None)
        if self._last==None:
            self._last=n
        else:
            self._last._next=n
            self._last=n
        if self.is_empty():
            self._first=n
        self._length+=1
        
    def removeLast(self):
        if self.is_empty():
            return False
        n=self._first
        if n==self._last:
            self._first=None
        else:
            while n._next!=self._last:
                n=n._next
            self._last=n
            self._last._next=None
        self._length-=1
        return True
        
    def first(self):
        if self.is_empty():
            return "The list is empty."
        return self._first._data
    
    def last(self):
        if self.is_empty():
            return "The list is empty."
        return self._last._data
    
    def replace(self, e, r):
        n=self._first
        if n._data==e:
            self.removeFirst()
            self.addFirst(r)
            return True
        while n._next and n._next._data!=e:
            n=n._next
        if n._next==None:
            return False
        n._next=self.Node(r, n._next._next)
        return True
    def __private_reverse_rec(self, first):
        if first==None or first._next==None:
            return first
        rest = self.__private_reverse_rec(first._next)
        first._next._next = first
        first._next = None
        return rest
    def reverse(self):
        self._first=self.__private_reverse_rec(self._first)
        n=self._first
        while n._next:
            n=n._next
        self._last=n

    class Iterator:
        def __init__(self, lls):
            self._current=lls._first
        
        def __next__(self):
            if self._current==None:
                raise StopIteration
            n=self._current._data
            self._current=self._current._next
            return n
    def __iter__(self):
        return self.Iterator(self)
    
    class OddIterator:
        def __init__(self, lls):
            if lls._first:
                self._current=lls._first._next
            else:
                self._current=None

        def __next__(self):
            if self._current==None:
                raise StopIteration
            n=self._current._data
            self._current=self._current._next
            if self._current:
                self._current=self._current._next
            return n
        def __iter__(self):
            return self 
    
    def odd_iter(self):
        return self.OddIterator(self)  
    
    class IteratorType:
        def __init__(self, lls, type):
            if type=="odd":
                self._type=1
            else:
                self._type=0
            c=lls._first
            i= 0
            while c!=None:
                if c._data%2==self._type:
                    self._current=c
                    break
                i+=1
                c=c._next
            if i == lls._length:
                self._current=None


        def __next__(self):
            if self._current==None:
                raise StopIteration
            x=self._current._data
            self._current=self._current._next
            while self._current!=None:
                if self._current._data%2==self._type:
                    break
                self._current=self._current._next
            return x
        def __iter__(self):
            return self
    def type_iter(self,type):
        return self.IteratorType(self,type)
                    
            
        
class DoubleLinkedList(List):
    class Node:
        def __init__(self, d, n=None, p=None):
            self._data=d
            self._next=n
            self._previous=p
            
    def __init__(self):
        self._first=None
        self._last=None
        self._length=0
    def is_empty(self):
        return self._length==0
    
    def empty(self):
        self._first=None
        self._last=None
        self._length=0
    
    def print(self):
        current=self._first
        while(current):
            print(current._data)
            current=current._next
    
    def addFirst(self, e):
        n = self.Node(e, self._first, None)
        if self._first==None:
            self._first=n
        else:
            self._first._previous=n
            self._first=n
        if self.is_empty():
            self._last=n
        self._length+=1
    
    def removeFirst(self):
        if self.is_empty():
            return False
        n=self._first
        if n==self._last:
            self._first=None
            self._last=None
        else:
            self._first=self._first._next
            self._first._previous=None
            n._next=None
        self._length-=1
        return True
    
    def addLast(self, e):
        n=self.Node(e,n=None,p=self._last)
        if self.is_empty():
            self._first=n
            self._last=n
        else:
            self._last._next=n
            self._last=n
        self._length+=1
        
    def removeLast(self):
        if self.is_empty():
            return False
        if self._first==self._last:
            self._first=None
            self._last=None
        else:
            self._last=self._last._previous
            self._last._next=None
        self._length-=1
        return True
    
    def first(self):
        if self.is_empty():
            return "The list is empty."
        return self._first._data
    
    def last(self):
        if self.is_empty():
            return "The list is empty."
        return self._last._data
    
    def replace(self, e, r):
        n=self._first
        if n._data==e:
            self.removeFirst()
            self.addFirst(r)
        else:
            while n and n._data!=e:
                n=n._next
            if n==self._last and n._data==e:
                self.removeLast()
                self.addLast(r)
                return True
            elif  n==None:
                return False
            elif n!=self._last: 
                new=self.Node(r, n._next, n._previous)
                n._previous._next=new
                n._next._previous=new
                n=new
        return True
    def printrev(self):
        n=self._last
        while n:
            print(n._data)
            n=n._previous
        
def reverse(l):
    if l.is_empty():
       return l
    f=l.first()
    l.removeFirst()
    reverse(l)
    l.addLast(f)


class LinkedStack(Stack, LinkedList):
    def __init__(self):
        Stack.__init__(self)
        LinkedList.__init__(self)
    def push(self, e):
        self.addFirst(e)
    def pop(self):
        if self.is_empty():
            return None
        l=self._first
        self.removeFirst()
        return l._data
    def top(self):
        return self.first()
    def size(self):
        return self._length
    
        
def rev(stack, s1, s2):
    if stack.is_empty():
        return stack
    # size1=stack.length
    # for i in range(size1/2):
    p1=stack.pop()
    s1.push(p1)
    # size2=stack.length
    # for i in range(size2):
    p2=stack.pop()
    s2.push(p2)
    rev(stack, s1, s2)
    p3=s1
    
        
           
    
    
s=LinkedStack()
s.push(1)
s.push(2)
s.push(3)
s.pop()
s.pop()
s.pop()
s.pop()
rev(s)
s.print()
# l=LinkedList()
# l.addFirst(1)
# l.addFirst(2)
# l.addFirst(3)
# l.addFirst(4)
# l.addFirst(5)
# for i in l.type_iter("even"):
#     print(i)
# l=LinkedList()
# l.addLast(10)
# l.addLast(20)
# l.addLast(30)
# l.addLast(40)
# l.addLast(50)
# for i in l.odd_iter():
#     print(i)

# for i in l.odd_iter():
#     print(i)
    
# for i in l.odd_iter():
#     print(i)

# def a(list_class):
#     l=list_class()
#     l.addFirst(1)
#     l.addFirst(2)
#     l.print()
    
    
#  a(LinkedList)


# d=DoubleLinkedList()
# d.removeFirst()
# d.removeLast()
# d.addLast(5)
# print(d.first())
# print(d.last())
# d.removeFirst()
# print(d._last._data)


    
    
    
    
# def add_before_rec(stack: StudentsLinkedStack, a: Student, e: Student):
#     if stack.is_empty():
#         return stack
#     if stack.top()==a:
#         el = stack.pop()
#         stack.push(e)
#         stack.push(el)
#     else:
#         t = stack.pop()
#         add_before_rec(stack, a, e)
#         stack.push(t)