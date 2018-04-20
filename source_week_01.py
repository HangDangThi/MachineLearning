#Date: 04/20/2018
#Create by: Hang Dang

#Exercise 01: https://www.practicepython.org/exercise/2014/05/21/15-reverse-word-order.html
def PrintBackward(str):
    return ' '.join(str.split()[::-1])


#Exercise 02: https://www.practicepython.org/exercise/2014/03/05/05-list-overlap.html
def GetCommonElements(_lst1, _lst2):
   #way 1:
   # _lst_cmn = list()
   # for ele in _lst1:
   #     if(ele in _lst2):
    #      if(not (ele in _lst_cmn)):
    #          _lst_cmn.append(ele)

    #way 2:
   _lst_cmn = list(set([ele for ele in _lst1 if ele in _lst2]))
   return _lst_cmn


#Exercise 03: https://www.practicepython.org/exercise/2014/03/19/07-list-comprehensions.html
def GetEvenElements(_lst):
    #way 1:
    # _lst_even = list()
    # for ele in _lst:
    #     if(ele % 2 == 0):
    #         _lst_even.append(ele)

    #way 2:
    _lst_even = [ele for ele in _lst if ele%2 == 0]
    return _lst_even


#Exercise 04: https://www.practicepython.org/exercise/2014/04/10/10-list-overlap-comprehensions.html
import random as rd

def GetOverlapEle_Random():
    _lst1 = rd.sample(range(0,85),12)
    _lst2 = rd.sample(range(0,72),16)

    print '\t\tList 1:', _lst1
    print '\t\tList 2:', _lst2

    _lst_ovlp = list(set([ele for ele in _lst1 if ele in _lst2]))

    return _lst_ovlp

#Exercise 05: https://www.practicepython.org/exercise/2014/04/30/13-fibonacci.html

def GenFibonacci(n):
    if n == 0:
        fibo = []
    elif n == 1:
        fibo = [1]
    elif n == 2:
        fibo = [1, 2]
    elif n > 2:
        fibo = [1, 1]
        i = 1
        while i < (n - 1):
            fibo.append(fibo[i] + fibo[i-1])
            i = i+1

    return fibo


#Main function
def main():
    print("\nExercise 01: functions with string")
    myself = 'My name is HangDang - Hang Dang is a bear'
    print '\t\t\t', myself
    str_rever = PrintBackward(myself)
    print 'Reversed: ', str_rever


    print("\nExercise 02: list comprehension")
    _lst1 = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    _lst2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    _lst_cmn = GetCommonElements(_lst1, _lst2)
    print(_lst_cmn)


    print("\nExercise 03: list comprehensions")
    _lst3 = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
    _lst_even = GetEvenElements(_lst3)
    print "List even elements: ", _lst_even


    print("\nExercise 04: Random list and comprehensions")
    _lst_ovlp = GetOverlapEle_Random()
    print 'Result: ', _lst_ovlp

    print("\nExercise 05: Generate Fibonacci")
    print '\tInput numbers that you would like to generate: '
    n = int(input())
    fibo = GenFibonacci(n)
    print '\t\t', fibo

if __name__ == "__main__":
    main()

print("Done!")

