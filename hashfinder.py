import random
 

def replace_with_numbers(string, dictionary):  
    new_string = ""  
    number_string = ""  # برای ذخیره اعداد جایگزین  
    for char in string:  
        if char in dictionary:  
            new_string += str(dictionary[char])  # جایگزینی با عدد  
            number_string += str(dictionary[char])  # عدد را ذخیره کن  
        else:  
            new_string += char  
            if char.isdigit():  # اگر خودش عدد بود، در عدد نهایی ذخیره شود  
                number_string += char  
    return new_string, int(number_string) if number_string else 0  

# دیکشنری جایگزینی حروف با اعداد  
replacement_dict = {  
    "a": 1,  "b": 2,  "c": 3,  "d": 4,  "e": 5,  
    "f": 6,  "g": 7,  "h": 8,  "i": 9,  "j": 10,  
    "k": 11,  "l": 12,  "m": 13,  "n": 14,  "o": 15,  
    "p": 16,  "q": 17,  "r": 18,  "s": 19,  "t": 20,  
    "u": 21,  "v": 22,  "w": 23,  "x": 24,  "y": 25,  "z": 26  
}  

# دریافت مسیر فایل از کاربر
file_path = input("Enter the path to your .txt file: ")
try:
    with open(file_path, 'r') as file:
        user_input = file.read().strip()  # خواندن محتوای فایل و حذف فضای خالی اضافی
        print("Content of file:", user_input)

        # جایگزینی و دریافت عدد نهایی  
        modified_string, final_number = replace_with_numbers(user_input, replacement_dict)  

        print("Hash of content:", modified_string)  
        print("Final hash:", final_number)  

        # انجام یک عملیات روی عدد (مثلاً ضرب بر 676 و تقسیم بر 2)  
        result = final_number * 676  
        print("Hash after change:", result)  

        result_backup = result // 2   
        print("Hash after change 2:", result_backup)

except FileNotFoundError:
    print("Error: File not found. Please check the file path and try again.")


with open("hashlog.txt", "w") as output_file:
    output_file.write(f"{file_path} : {result_backup}\n")
print("Result successfully saved in hashlog.txt")