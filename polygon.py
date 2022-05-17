class Triangle:
    def get_shape(a, b, c):
        if a+b<=c or b+c<=a or c+a<=b:
            return -1
        if a==b and b==c:
            return 3
        if a==b or b==c or c==a:
            return 2
        return 1