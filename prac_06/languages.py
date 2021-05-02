from prac_06.programming_language import ProgrammingLanguage


def main():
    ruby = ProgrammingLanguage('Ruby', 'Dynamic', True, 1995)
    python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
    visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)
    print(ruby, python, visual_basic, sep='', end='')
    code_programming = [ruby, python, visual_basic]
    print('The dynamically typed languages are:', end='')
    for each in code_programming:
        if ProgrammingLanguage.is_dynamic(each):
            print(each.field)


main()