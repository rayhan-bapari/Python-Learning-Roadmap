year = 2024

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print(f"{year} is a leap year")
        else:
            print(f"{year} is not a leap year")
    else:
        print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year")


# | শর্ত                              | Leap Year? |
# | ------------------------------- | ---------- |
# | ৪ দিয়ে বিভাজ্য নয়                | না         |
# | ৪ দিয়ে বিভাজ্য, ১০০ নয়          | হ্যাঁ         |
# | ১০০ দিয়ে বিভাজ্য, কিন্তু ৪০০ নয়   | না         |
# | ৪০০ দিয়ে বিভাজ্য                | হ্যাঁ        |

# 2020 → leap year ✅

# 1900 → divisible by 100 but not 400 → not leap year ❌

# 2000 → divisible by 400 → leap year ✅

# 2023 → not divisible by 4 → not leap year ❌
