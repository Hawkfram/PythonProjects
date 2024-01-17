import math

GRILLEJEUX = [
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0]
]

couleur = {
    0: '#9E948A',
    2: '#EEE4DA',
    4: '#EDE0C8',
    8: '#F2B179',
    16: '#F59563',
    32: '#F67C60',
    64: '#F65E3B',
    128: '#EDCF73',
    256: '#EDCC62',
    512: '#EDC850',
    1024: '#EDC53F',
    2048: '#EDC22D'
}
FPS = 60
IPS = math.ceil(1000/FPS)