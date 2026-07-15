h = "Subodh ugile"
first_char = h[0]
print(first_char)

slice_h = h[0:6]
print(slice_h)

print(h[-1])
print(h[-2])

no_list = "0123456789"
print(no_list[:])
print(no_list[3:])
print(no_list[:5])
print(no_list[0:5:2])

print(h.lower())
print(h.upper())

h = "     subodh ugile"
print(h)
print(h.strip())

h = "Vanshika Bhadani"
print(h.replace("Bhadani", "Ugile"))


h = "a, b, c, d, e"
print(h.split())
print(h.split(", "))


h = "subodh Ugile"
print(h.find("Ugile"))
print(h.find("ugile"))

h = "subodh ugile ugile ugile "
print(h.count("ugile"))


chai_type = "Masala"
quantity = 2
order = "I ordered {} cups of {} chai"
print(order)
print(order.format(quantity, chai_type))

h = ["a", "b", "c", "d", "e"]
print(h)
print("".join(h))
print(" ".join(h))
print("-".join(h))
print(", ".join(h))

h = "Subodh"
print(len(h))

for letter in h:
    print(letter)

h = "I said, \"I love you\" "
print(h)

