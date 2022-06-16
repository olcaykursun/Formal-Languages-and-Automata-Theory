# -*- coding: utf-8 -*-
"""
Checks DFA string for validityof its format (it does not check if it accepts the correct language)
See Week-3 notes
Created on Thu Jun 16 18:33:01 2022

@author: Dr. Olcay Kursun, okursun@aum.edu
"""



#dfa_str = input('Enter a DFA string')

#Here is one from the Week-3 notes:
dfa_str = '({1,2,3,4,5},{a,b},{((1,a),2),((1,b),3),((2,a),2),((2,b),4),((3,a),5),((3,b),3),((4,a),2),((4,b),4),((5,a),5),((5,b),3)},1,{2,3})'

#We don't want to enter characters as 'a', 'b','c' so let us allow a,b,c by declaring them as followsas input alphabet characters, or simply use any integers 0,1,2,3... 
a='a'
b='b'
c='c'
#or simply use integers 0,1,2,3... as the alphabet symbols, which is more flexible, 26 may represent Z of English alphabet for example

class MyException(Exception):
    pass

try:
    dfa = eval(dfa_str)
    if len(dfa) != 5:
        raise MyException("The input string must correspond to a 5-tuple")
except BaseException:
    print("The input string must correspond to a tuple")
    raise

Q,S,T,i,A = dfa
if not isinstance(Q,set):
    raise MyException("Q is not a set")
if not isinstance(S,set):
    raise MyException("S is not a set")
if not isinstance(T,set):
    raise MyException("T is not a set")
if i not in Q:
    raise MyException("i is not a state")
if not isinstance(A,set):
    raise MyException("A is not a set")
    if A.difference(Q):
        raise MyException("A is not a subset of Q")
if len(T) != len(Q)*len(S):
    raise MyException("Invalid number of transitions")

all_pairs = {(q, ch) for q in Q for ch in S}

try:
    given_pairs = set()
    for (cur_state, ch), next_state in T:
        assert(next_state in Q)
        given_pairs.add((cur_state, ch))
    assert(all_pairs == given_pairs)
except AssertionError:
    print('Transitions function part of the string does not represent a valid total function')

