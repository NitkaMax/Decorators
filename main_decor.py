import time

def logger(input_function):
    def new_function(*args, **kwargs):
        output_function = input_function(*args, **kwargs)
        time_now = time.strftime('%d/%m/%Y*%X', time.localtime(time.time()))
        log = f'{time_now}  <<<name_function: {input_function.__name__}>>>  ' \
              f'    <<<arguments: {args}{kwargs}>>>   <<<function output: {output_function}>>>  '
        with open('Logs/functionsfromtask1.log', 'a', encoding='utf-8') as file_log:
            file_log.write(log + '\n')
        return output_function
    return new_function
