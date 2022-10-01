# Coded by SpiderX360

string = input("")
list_str = list(string)

try:
    # cheking input
    if len(string) == 10:
        format24 = ""

        # Part 12 AM/PM
        if string[-2:] == "PM" and string[:2] == "12":
            format24 = f"{string[:2]}"


        elif string[-2:] == "AM" and string[:2] == "12":
            format24 = f"{'00'}"

        # Part PM

        elif string[-2:] == "PM" and string[:2] < "12":
            format24 = f"{(12 + int(string[:2]))}"

        elif string[-2:] == "PM" and string[:2] > "12":
            format24 = f"{string[:2]}"

        # Part AM

        elif string[-2:] == "AM" and string[:2] < "12":
            format24 = f"{string[:2]}"


        else:
            exit()



    else:
        exit()

    print(f"{format24}{string[2:8]}")

except:
    exit()