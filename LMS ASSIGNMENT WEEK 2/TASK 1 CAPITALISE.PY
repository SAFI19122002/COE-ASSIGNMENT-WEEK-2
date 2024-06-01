def capitalize_full_name(full_name):
    return full_name.title()

if __name__ == "__main__":
    import sys
    input = input().strip()
    capitalized_name = capitalize_full_name(input)
    print(capitalized_name)