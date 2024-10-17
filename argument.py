def ask_ok(prompt, retries=4, reminder='Please try again!'):
    while True:
        reply = input(prompt).strip().lower()  # Normalize the input
        if reply in {'y', 'ye', 'yes'}:
            return True
        if reply in {'n', 'no', 'nop', 'nope'}:
            return False
        retries -= 1
        if retries < 0:
            raise ValueError('Invalid user response')
        print(reminder)
