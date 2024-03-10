import platform

from util.typedef import Types as T

def get_so():
    so_path = 'lib/libUnitree_motor_SDK_%s.so'

    uname = platform.uname()
    system = uname.system
    machine = uname.machine
    # SOs are named according to (system, bits) tuple.
    if system == 'Windows':
        tup = ('Win', '64')
    elif system == 'Linux':
        # x86_64
        if machine == 'x86_64':
            tup = ('Linux', '64')
        # i?86
        elif machine.endswith('86'):
            tup = ('Linux', '32')
        # aarch32/64
        elif uname.machine.startswith('aarch'):
            tup = ('ARM', machine[:-2])
        # Likely unsupported
        else:
            raise RuntimeError(f'{machine} not supported.')
    else:
        raise RuntimeError(f'{system} not supported.')

    return so_path % ''.join(tup)

def cdll_bare_init(so):
    return T.cdll.LoadLibrary(so)

def cdll_init(so):
    cdll = cdll_bare_init(so)

    # motor_ctrl.h
    cdll.getSystemTime.restype = T.c_longlong

    cdll.modify_data.restype = T.c_int32
    cdll.modify_data.argtypes = (T.POINTER(T.MOTOR_send),)

    cdll.extract_data.restype = T.c_int
    cdll.extract_data.argtypes = (T.POINTER(T.MOTOR_recv),)

    cdll.crc32_core.restype = T.c_uint32
    cdll.crc32_core.argtypes = (T.POINTER(T.c_uint32), T.c_uint32)

    # 此处需要考虑win64平台和linux平台的区别
    # LSerial.h
    cdll.open_set.restype = T.c_int
    cdll.open_set.argtypes = (T.POINTER(T.c_char),)

    cdll.close_serial.restype = T.c_int
    cdll.close_serial.argtypes = (T.c_int,)

    # cdll.broadcast.restype = T.c_int
    # cdll.broadcast.argtypes(T.c_int, T.POINTER(T.MOTOR_send))

    cdll.send_recv.restype = T.c_int
    cdll.send_recv.argtypes = (T.c_int, T.POINTER(T.MOTOR_send), T.POINTER(T.MOTOR_recv))

    return cdll
