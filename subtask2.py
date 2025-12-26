def solve_task_8_2():
    n = 0
    s = 0
    m = -1
    a = -1
    
    x = int(input("Enter number (or -1 to stop): "))
    
    while x != -1:
        if n == 0 or x < m:
            m = x
        
        n = n + 1
        s = s + x
        
        x = int(input("Enter next number: "))
    
    if n > 0:
        a = s / n
        
    print(f"n={n}, s={s}, m={m}, a={a}")

solve_task_8_2()

# it looks like I learned how to use
git today