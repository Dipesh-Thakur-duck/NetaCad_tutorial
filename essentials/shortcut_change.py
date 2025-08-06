var1 = 1
var2 = 2

# way 1
var3 = var1
var1 = var2
var2 = var3

print(var1, var2)

# way 2

var1, var2 = var2, var1
print(var1, var2)