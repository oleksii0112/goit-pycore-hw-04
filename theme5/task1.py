
def total_salary(path):
    try:
        with open(path, mode="r", encoding="utf-8") as file:
            total = 0
            avg = 0
            count = 0 
            for line in file:
                line = line.strip()
                if not line:
                    continue
                name, salary = line.split(",")
                salary = float(salary)
                total = total + salary
                count = count + 1
            avg = total/count if count > 0 else 0 
            return total, avg
    except:
        print(f"Сталася помилка")
        return (0,0)

total, avg = total_salary("theme5/salary.txt")
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {avg}")



