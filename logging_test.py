import logging

logger = logging.getLogger(__name__)
logging.basicConfig(filename='logFile.log', filemode='w', format='%(message)s', encoding='utf-8', level=logging.DEBUG)

def log_to_file(user_in):
    log_number = user_in.split(" ")[1]
    log_dict = {
        '10': 'Debug test',
        '20': 'Program successful!',
        '30': 'Warning, there could be errors',
        '40': 'Program encountered an error!',
        '50': 'The program has stopped working!'
    }
    
    if log_number in log_dict:
        message = log_dict[log_number]
        logging.log(int(log_number), message)
    else:
        logging.error('Invalid log number.')


if __name__ == '__main__':
    user_in = input()
    log_to_file(user_in)

    with open("logFile.log", 'r') as f:
        for line in f:
            print(line)
