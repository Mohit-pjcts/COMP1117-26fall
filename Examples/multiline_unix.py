from oneline_unix import ls, mkdir, touch, unix_filter, process_command_unix

def user_interface(sys_state):
    while True:
        full_command = input("$ ").strip()
        sub_commands = full_command.split("&&")
        output = list(map(lambda c: process_command_unix(sys_state, c), sub_commands))
        print(output)

if __name__ == "__main__":
    init_state = ['/Desktop', '/Documents', '/home', 'test.txt']
    user_interface(init_state)
