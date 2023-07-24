import Log
# https://github.com/OpsecGuy/PersonalCollection/blob/main/log.py


def verify_int_range(param: str, value: int, a: int, b: int) -> int:
    if isinstance(a, int) and isinstance(b, int):
        if isinstance(value, int) and value >= a and value <= b:
            return value
        else:
            Log().error(' - ', verify_int_range, f'Parmeter {param} value {value} is out of range! Min: {a} | Max: {b}')
    else:
        Log().error(' - ', verify_int_range, f'Parameter {value} type does not match!')
        
def verify_float_range(param: str, value: float, a: float, b: float) -> float:
    if isinstance(a, float) and isinstance(b, float):
        if isinstance(value, float) and value >= a and value <= b:
            return value
        else:
            Log().error(' - ', verify_float_range, f'Parmeter {param} value {value} is out of range! Min: {a} | Max: {b}')
    else:
        Log().error(' - ', verify_float_range, f'Parameter {value} type does not match!')

def verify_mode_range(param: str, value: str, options: list):
    if isinstance(value, str) and value in options:
        return value
    else:
        Log().error(' - ', verify_mode_range, f'Parmeter {param} value {value} is out of range! Available options: {options}')

def verify_file_name(param: str, value: str, format: str):
    if isinstance(value, str) and value.endswith(format):
        return value
    else:
        Log().error(' - ', verify_mode_range, f'Parmeter {param} value {value} is incorrect!')
        
### Examples
def showcase():
    my_int = 1
    my_float = 1.0
    my_mode = '1'
    my_file = 'file.txt'

    verify_int_range('my_int', my_int, 0, 2)
    verify_float_range('my_float', my_float, 0.0, 2.0)
    verify_mode_range('my_modes', my_mode, ['1', '2', '3'])
    verify_file_name('my_file', my_file, '.txt')
    # Error example
    bad_int = 3
    verify_int_range('bad_int', bad_int, 0, 2)
    # ... [verify_int_range] -> Parmeter bad_int value 3 is out of range! Min: 0 | Max: 2

showcase()

    