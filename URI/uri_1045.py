x = False

while not(x):
    A, B, C = map(float, input().split())
    if A > 0 and B > 0 and C > 0:
        x = True
        nums = sorted([A, B, C], reverse=True)

if nums[0] >=nums[1] + nums[2]:
    print('NAO FORMA TRIANGULO')
else:
    if nums[0]**2 == (B**2 + nums[2]**2):
        print('TRIANGULO RETANGULO')
    if nums[0]**2 > (B**2 + nums[2]**2):
        print('TRIANGULO OBTUSANGULO')
    if nums[0]**2 < (B**2 + nums[2]**2):
        print('TRIANGULO ACUTANGULO')
    if nums[0] ==nums[1] and nums[1] == nums[2]:
        print('TRIANGULO EQUILATERO')
    if (nums[0] ==nums[1] and nums[1] != nums[2] and nums[0] != nums[2]) or (nums[2] == nums[0] and nums[1] != nums[2] and nums[0] !=nums[1]) or (nums[2] == nums[1] and nums[0] != nums[2] and nums[0] !=nums[1]):
        print('TRIANGULO ISOSCELES')