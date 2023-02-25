def create_config_file():
    config_file = open('config', 'x')
    config_file.close()

def read_config_file():
    try:
        config_file = open("config", "r")
        config_file_content = config_file.readlines()
        config_file.close()
    except:
        return False
    for i in range(len(config_file_content)):
        config_file_content[i] = [config_file_content[i].replace(' ', '').strip("\n")]
    if len(config_file_content) <= 0:
        return False
    else:
        return config_file_content
    
def add_account(usern,passw,games):
    try:
        if usern == None or passw == None or games == None:
            return False
        config_file = open("config", "a")
        config_file.write(f"{usern}:{passw}:{games}\n")
        config_file.close()
        return True
    except:
        return False

def remove_account():
    #todo
    return