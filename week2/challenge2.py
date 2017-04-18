def multiply(a,b):
    print("Multiplying %d x %d" % (a,b))
    answer = a*b
    return answer

def divide(a,b):
    print("Multiplying %d / %d" % (a,b))
    answer = a/b
    return answer

num1 = 10
num2 = 20
num3 = multiply(num1,num2)
num4 = divide(num1,num2)

print(num1, " and ", num2)

def u_and_r(text):
    u_r = text.upper()[::-1]
    return u_r

text = "Do not go gentle into that good night"
new_text = u_and_r(text)
print(new_text)
