from termcolor import colored

class Logger:
    def log(log_time,log_type,log_message):
        log_message_to_print=str(round(log_time*100)/100)
        if log_type == "Log":
            log_message_to_print = log_message_to_print+" [Log]: "+log_message
        elif log_type == "Warning":
            log_message_to_print = colored(log_message_to_print+" [Warning]: "+log_message, 'yellow')
        elif log_type == "Error":
            log_message_to_print = colored(log_message_to_print+" [Error]: "+log_message, 'red', attrs=['reverse'])
        elif log_type == "Separator":
            log_message_to_print="----------------------------------------\n"
        elif log_type == "Info":
            log_message_to_print = colored(log_message_to_print+" [Info]: "+log_message, 'cyan')
        elif log_type == "Validation":
            log_message_to_print = colored(log_message,"green")
        print(log_message_to_print, end = '')
