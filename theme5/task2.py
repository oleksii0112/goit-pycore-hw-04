def get_cats_info(path):
    try:
        with open(path, "r", encoding="utf-8") as file:
            cats_info = []
            for line_number, line in enumerate(file, start=1):
                line = line.strip()
                if not line:
                    continue
                try:
                    id_cat, name_cat, age_cat = line.split(",")
                    cats_info.append({"id":id_cat,
                                "name": name_cat,
                                "age": int(age_cat)})
                except:
                    print("Неправильний формат запису!")
                    continue
                
            return cats_info
    except:
        print ("ФАйл не знайдено")
        return None 

cats_info = get_cats_info("theme5/cats.txt")
for cat in cats_info:
    print(cat)
