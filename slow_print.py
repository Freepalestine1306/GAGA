import time

def slow_print(text, delay=0.03):
    for char in text:
        print(char, end="", flush=True)
        time.sleep(delay)
    print()

def slow_input(prompt, delay=0.03):
    for char in prompt:
        print(char, end="", flush=True)
        time.sleep(delay)
    return input()
