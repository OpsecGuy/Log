import os

from datetime import datetime
from typing import Optional, Any


class Log:
    def __init__(self) -> None:
        self.now = datetime.now()
        self.curr_time = self.now.strftime('%H:%M:%S')

    def info(self, id, function, message, exit_with_code: Optional[int]=0) -> None:
        print(f'| {self.curr_time} INF | {id} | [{function.__name__}] -> {message}')
        if exit_with_code:
            os._exit(exit_with_code)

    def warn(self, id, function, message, exit_with_code: Optional[int]=0) -> None:
        print(f'| {self.curr_time} WRN | {id} | [{function.__name__}] -> {message}')
        if exit_with_code:
            os._exit(exit_with_code)

    def error(self, id, function, message, exit_with_code: Optional[int]=0) -> None:
        print(f'| {self.curr_time} ERR | {id} | [{function.__name__}] -> {message}')
        os._exit(exit_with_code)

### Examples
def showcase():
    Log().info('0', showcase, 'This is info message')
    Log().warn('0', showcase, 'This is warn message')
    Log().error('0', showcase, 'This is error message', 1)

showcase()