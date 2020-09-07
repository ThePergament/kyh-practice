
def is_it_too_long(name, max_length):
    return len(name) > max_length
def main():
        #students ="anna beatrice cecilia doris esmeralda frida gunilla".split()
        try:
            max_length = int(input("Ange maxlängd"))
        except ValueError:
            max_length = 5
        students =input ("Ange studenternas namn med komma emellan: ").split(",")
        for name in students:
            fixed_name = name.strip()
            if is_it_too_long(fixed_name,max_length):
                print(f"{name.title()} är för långt!")


if __name__ == '__main__':
    main()