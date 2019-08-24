
a = dict()

a = {
    "css": {
        "border-color": "red",
        "color": "white"
    }
}

b = """
    max-height: 100px;
"""
c = str("")

for item in a:
    # print(a[item])
    for _ in a[item]:
        print(_)
        b += _ + ":" + a[item][_] + ";"

print(b)
