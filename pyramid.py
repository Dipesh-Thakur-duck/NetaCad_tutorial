blocks = int(input("Enter the number of blocks: "))
for_result = blocks
pyramid_layer = 0
deductor = 0
while blocks >= 0:
    deductor += 1
    blocks -= deductor
    if blocks >= 0:
        pyramid_layer += 1
print(f'Height of pyramid with {for_result} is {pyramid_layer}')

"""
Optimized code:

blocks = int(input("Enter the number of blocks: "))
pyramid_layer = 0
layer_blocks = 1

while blocks >= layer_blocks:
    blocks -= layer_blocks
    pyramid_layer += 1
    print(pyramid_layer)
    layer_blocks += 1

print(f'Height of pyramid with {blocks + sum(range(1, pyramid_layer + 1))} blocks is {pyramid_layer}')

say pyramid_layer = 4

range(1,4) = [1,2,3]
sum([1,2,3]) = 6

blocks + 6 helps find the actual number of blocks given since blocks variable is reduced in the process
"""