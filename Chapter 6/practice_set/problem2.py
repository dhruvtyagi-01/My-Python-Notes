m1 = int(input("Enter marks:"))
m2 = int(input("Enter marks:"))
m3 = int(input("Enter marks:"))

if((m1 < 0 or m1 > 100) or (m2 < 0 or m2 > 100) or (m3 < 0 or m3 > 100)):
    print("Marks should range from 0-100")

elif((m1 + m2 + m3) < 120):
    print("You have FAILED!")

elif(m1 < 33 or m2 < 33 or m3< 33):
    print("You have FAILED!")

else:
    print("You have PASSED!")