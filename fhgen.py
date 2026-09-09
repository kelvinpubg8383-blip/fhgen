import sys

def generate_password(ssid_input):
    suffix = ssid_input.split('_')[-1].strip().lower()
    if len(suffix) != 6:
        return "Error: length must be 6"
    part1 = suffix[0:2]
    part2 = suffix[2:4]
    part3 = suffix[4:6]
    return f"wlan{part3}{part1}{part2}"

if __name__ == "__main__":
    if len(sys.argv) > 1:
        target = sys.argv
    else:
        target = input("SSID: ")
    print(generate_password(target))
