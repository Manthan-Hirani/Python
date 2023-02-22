from word2number import w2n

def marksheet(m1, m2, m3, m4):
    if (m1 > 100 or m1 < 0 or m2 > 100 or m2 < 0 or m3 > 100 or m3 < 0 or m4 > 100 or m4 < 0):
        print("Please Enter Valid Marks")
    else:
        total = m1 + m2 + m3 + m4
        avg = (total)/4
        if (avg >= 80):
            print(f"Grade:A, Total={total}, Percentage={avg}")
        elif (avg < 80 and avg >= 70):
            print(f"Grade:B, Total={total}, Percentage={avg}")
        elif (avg < 70 and avg >= 60):
            print(f"Grade:C, Total={total}, Percentage={avg}")
        elif (avg < 60 and avg >= 50):
            print(f"Grade:D, Total={total}, Percentage={avg}")
        elif (avg < 50 and avg >= 40):
            print(f"Grade:E, Total={total}, Percentage={avg}")
        else:
            print(f"Grade:F, Total={total}, Percentage={avg}")


m1 = w2n.word_to_num(input("Enter marks of subject 1: "))
m2 = w2n.word_to_num(input("Enter marks of subject 2: "))
m3 = w2n.word_to_num(input("Enter marks of subject 3: "))
m4 = w2n.word_to_num(input("Enter marks of subject 4: "))

grade = marksheet(m1, m2, m3, m4)