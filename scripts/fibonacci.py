import time

def fibonacci_seq(n1, n2, max):
    num = [n1, n2]
    nth = 0
    for nth in range(max - 2):
        nth = n1 + n2
        num.append(nth)
        n1 = n2
        n2 = nth
    return str(num)

def fibonacci_nth(n1, n2, max):
    nth = 0
    for nth in range(max - 2):
        nth = n1 + n2
        n1 = n2
        n2 = nth
    return str(nth)

def main():
    n1 = int(input("First fibonacci term: "))
    n2 = int(input("Second fibonacci term: "))
    max = int(input("Maximum value of the row: "))
    print("----------------------------")
    global start_time
    start_time = time.time()
    #print("The whole sequence: " + fibonacci_seq(n1, n2, max))
    print("The maximum term: " + fibonacci_nth(n1, n2, max))
    
main()
print("Fun fact: this program took " + str(time.time() - start_time) + " seconds to run!")