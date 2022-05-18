print("module start")
print("__name_test.py name:", __name__)

def add(a, b):
    print(f"{a} + {b} = {a+b} is computed from " + __name__)


if __name__ == "__main__":
    add(1, 2)

print("module ends")