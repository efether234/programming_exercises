'''
Akash and Vishal are quite fond of travelling. They mostly travel by railways. They were travelling in a train one day and they got interested in the seating arrangement of their compartment. The compartment looked something like 

 
So they got interested to know the seat number facing them and the seat type facing them. The seats are denoted as follows : 

Window Seat : WS
Middle Seat : MS
Aisle Seat : AS

You will be given a seat number, find out the seat number facing you and the seat type, i.e. WS, MS or AS.

INPUT
First line of input will consist of a single integer T denoting number of test-cases. Each test-case consists of a single integer N denoting the seat-number.

OUTPUT
For each test case, print the facing seat-number and the seat-type, separated by a single space in a new line.

CONSTRAINTS
1<=T<=105
1<=N<=108
'''

t = int(input())
for i in range(t):
    seat = int(input())
    opp_seat = seat + 2 * (6 - (seat - 1) % 12) - 1
    res = str(opp_seat)
    if opp_seat % 12 in (1, 6, 7, 0):
        res += ' WS'
    if opp_seat % 12 in (3, 4, 9, 10):
        res += ' AS'
    if opp_seat % 12 in (2, 5, 8, 11):
        res += ' MS'
    print(res)