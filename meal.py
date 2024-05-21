def main():
    time = input("What time is it? ")
    hour = convert(time)

    if 6 <= hour < 9:
        print("breakfast time")
    elif 12 <= hour < 14:
        print("lunch time")
    elif 18 <= hour < 20:
        print("dinner time")

def convert(time):
    hours, minutes = map(int,time.split(":"))
    return hours + minutes / 60

if __name__ == "__main__":
    main()
