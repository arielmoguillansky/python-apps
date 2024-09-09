# This program will ask the user for the current time and then tell the user what meal they should have based on the time of day.
def main():
    time = input("What time is it? ").strip()
    parsedTime = convert(time)

    if parsedTime is not None:
        match(parsedTime):
            case parsedTime if 7 <= parsedTime <= 8:
                print("breakfast time")
            case parsedTime if 12 <= parsedTime <= 13:
                print("lunch time")
            case parsedTime if 18 <= parsedTime <= 19:
                print("dinner time")
            case _:
                return
    else:
        print("Invalid time format.")


def convert(time):
    try:
        hour,minutes = time.split(":")
        hour = int(hour)
        minutes = int(minutes)

        return hour + round(minutes / 60,2)
    except (ValueError, IndexError):
        return None


if __name__ == "__main__":
    main()
