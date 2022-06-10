# -*- coding: utf-8 -*-
"""TFL library defines a string class without using loops, lists, arrays, strings.
Uses the tuples for defining strings that are formed in the definition of Kleene-star.
Demonstrats the use of recursion.

Created on Tue Jun  10 12:36:04 2022

@author: okursun@aum.edu

Formal Languages and Automata Theory, Summer 2022
"""

class stfl:

    lambda_str = None
    
    def __init__(self, tupl = lambda_str):
        self.tupl = tupl    #No tuple exists if it is lambda
    
    @staticmethod
    def xdotc(x, c):
        return stfl((x, c))
    
    @staticmethod
    def cdotx(c, x):
        return stfl((c, x))
    
    @staticmethod
    def copy_from_list(lst):        
        temp = stfl()
        for c in lst:
            temp = stfl.xdotc(temp, c)
        return temp    
    
    def __bool__(self):
        return self.tupl is not None
    
    def __len__(self):
        if self:
            if isinstance(self.tupl[0], stfl):
                return 1 + len(self.tupl[0])
            else:
                return 1 + len(self.tupl[1])                
        else:
            return 0

    def __str__(self):
        def rec_str(self):
            if self:
                if isinstance(self.tupl[0], stfl):
                    return rec_str(self.tupl[0]) + str(self.tupl[1])  #x,c
                else:
                    return str(self.tupl[0]) + rec_str(self.tupl[1])  #c,x
            else:
                return ''            
        s = rec_str(self)
        if s=='':
            s='\u03BB'
        return s

    def associativeTupl(self):
        if self:
            if isinstance(self.tupl[0], stfl):
                if self.tupl[0]:
                    return (*self.tupl[0].associativeTupl(), self.tupl[1])
                else:
                    return (self.tupl[1],)                    
            else:
                if self.tupl[1]:
                    return (self.tupl[0], *self.tupl[1].associativeTupl())
                else:
                    return (self.tupl[0],)                    
        else:
            return ('\u03BB')
        
    def __eq__(self, other):
        return self.associativeTupl() == other.associativeTupl()
    
    def __repr__(self):
        if self:
            if isinstance(self.tupl[0], stfl):
                return 'dot({},{})'.format(repr(self.tupl[0]), repr(self.tupl[1]))
            else:
                return 'dot({},{})'.format(repr(self.tupl[0]), repr(self.tupl[1]))
        else:
            return '\u03BB'

    def rev(self):
        if self:
            if isinstance(self.tupl[0], stfl):
                return stfl.cdotx(self.tupl[1], self.tupl[0].rev())  #rev(x+c) = c+rev(x)
            else:
                return stfl.xdotc(self.tupl[1].rev(), self.tupl[0])  #rev(c+x) = rev(x)+c
        else:
            return stfl()           

def main():
    s=stfl()
    print(s)
    print(bool(s))

    stfl.xdotc(s, 1)   #s is immutable, xdotc does not change s
    print(s)
    
    s=stfl.xdotc(s, 1)
    print(s)
    print(bool(s))
    print(len(s))
    
    s=stfl.xdotc(s, 2)
    print(s)
    
    s=stfl.xdotc(s, 3)
    print(s)
    print(repr(s))
    
    x=stfl.copy_from_list('abc')
    print(x)
    
    y=x.rev()
    print(y)
    
    x=stfl.cdotx(5, x)
    print(x)
    print(repr(x))
    
    y=x.rev()
    print(y)    
    print(repr(y))

    y2 = stfl.copy_from_list(['c','b','a',5])
    print(y2)    
    print(repr(y2))
    
    print(y.associativeTupl())
    print(y2.associativeTupl())
    print(y == y2)
    
if __name__ == '__main__':
    main()
