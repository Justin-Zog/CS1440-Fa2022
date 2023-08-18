from Ocean import Ocean
from Sunset import Sunset
from Forest import Forest


def makePalette(iterations, palette_type="ocean"):
    if palette_type == 'ocean':
        return Ocean(iterations)
    elif palette_type == 'sunset':
        return Sunset(iterations)
    elif palette_type == 'forest':
        return Forest(iterations)
    else:
        raise NotImplementedError(f"Cannot create a '{palette_type}' palette.")
