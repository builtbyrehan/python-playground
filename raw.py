def large(marks):
    lar = marks[0]
    for i in range(len(marks)):
        if lar < marks[i]:
            lar = marks[i]
            
    return lar


marks = [60,70,90]
result = large(marks)
print(result)