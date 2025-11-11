def water_jug():
    jug4 = 0
    jug3 = 0
    print(jug4, jug3)
    jug3 = 3
    print(jug4, jug3)
    jug4 = jug3
    jug3 = 0
    print(jug4, jug3)
    jug3 = 3
    print(jug4, jug3)
    jug3 = jug3 - (4 - jug4)
    jug4 = 4
    print(jug4, jug3)
    jug4 = 0
    print(jug4, jug3)
    jug4 = jug3
    jug3 = 0
    print(jug4, jug3)
    print("\nGoal Achieved: Exactly 2 gallons in 4-gallon jug.")
water_jug()
