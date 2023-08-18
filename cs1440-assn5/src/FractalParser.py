'''
Reads .frac files named on the commandline and converts its contents into a dictionary.
'''


def parse(file, image_name):
    file_dict = {}
    complete_dict = {}
    isJuliaFractal = False
    isPhoenixFractal = False

    for line in file:
        # We want to ignore any lines that start with '#' or ''. We also want to ignore any line without a ':'.
        if line[0] == '#' or line[0] == '':
            continue
        elif ':' not in line:
            continue
        # Add all items to a dictionary
        # **NOTE** this will also add bogus items, the program will simply ignore them in the future.
        line = line.replace("\n", "").replace(" ", "").lower()
        line_array = line.split(':')
        file_dict[line_array[0]] = line_array[1]

    # &&&&&&&&&&&& ERROR HANDLING SECTION BEGINS &&&&&&&&&&&& #
    # Checks to see if the required data fields were in the file and if they are the correct type.
    if 'type' not in file_dict:
        raise RuntimeError("ERROR: The file did not provide the 'type' data field.\nExiting Program...")
    elif file_dict['type'] == "phoenix" or file_dict['type'] == "julia" or file_dict['type'] == "burningshipjulia":
        if file_dict['type']  == "phoenix":
            if 'preal' not in file_dict:
                raise RuntimeError("ERROR: The file did not provide the 'preal' data field.\nExiting Program...")
            if 'pimag' not in file_dict:
                raise RuntimeError("ERROR: The file did not provide the 'pimag' data field.\nExiting Program...")

            try:
                float(file_dict['preal'])
                float(file_dict['pimag'])
            except Exception:
                raise RuntimeError("ERROR: The 'preal' or 'pimag' data fields were invalid.\nExiting Program...")

            isPhoenixFractal = True

        if 'creal' not in file_dict:
            raise RuntimeError("ERROR: The file did not provide the 'creal' data field.\nExiting Program...")
        if 'cimag' not in file_dict:
            raise RuntimeError("ERROR: The file did not provide the 'cimag' data field.\nExiting Program...")

        try:
            float(file_dict['creal'])
            float(file_dict['cimag'])
        except Exception:
            raise RuntimeError("ERROR: The 'creal' or 'cimag' data fields were invalid.\nExiting Program...")

        isJuliaFractal = True

    if 'centerx' not in file_dict:
        raise RuntimeError("ERROR: The file did not provide the 'centerX' data field.\nExiting Program...")
    if 'centery' not in file_dict:
        raise RuntimeError("ERROR: The file did not provide the 'centerY' data field.\nExiting Program...")
    if 'axislength' not in file_dict:
        raise RuntimeError("ERROR: The file did not provide the 'axisLength' data field.\nExiting Program...")
    if 'pixels' not in file_dict:
        raise RuntimeError("ERROR: The file did not provide the 'pixels' data field.\nExiting Program...")
    if 'iterations' not in file_dict:
        raise RuntimeError("ERROR: The file did not provide the 'iterations' data field.\nExiting Program...")

    # Checks types
    try:
        float(file_dict['centerx'])
        float(file_dict['centery'])
        float(file_dict['axislength'])
        int(file_dict['pixels'])
        int(file_dict['iterations'])
    except Exception:
        raise RuntimeError("ERROR: One or more of the data fields contained invalid values.\nExiting Program...")

    # &&&&&&&&&&&& LIST CREATION BEGINS &&&&&&&&&&&& #
    # Creates the list
    complete_dict['type'] = file_dict['type']
    complete_dict['pixels'] = int(file_dict['pixels'])
    complete_dict['iterations'] = int(file_dict['iterations'])
    complete_dict['axislength'] = float(file_dict['axislength'])
    complete_dict['min'] = {
        'x': float(file_dict['centerx']) - (float(complete_dict['axislength']) / 2),
        'y': float(file_dict['centery']) - (float(complete_dict['axislength']) / 2)
    }
    complete_dict['max'] = {
        'x': float(file_dict['centerx']) + (float(complete_dict['axislength']) / 2),
        'y': float(file_dict['centery']) + (float(complete_dict['axislength']) / 2)
    }
    complete_dict['pixelsize'] = float((complete_dict['max']['x'] - complete_dict['min']['x']) / complete_dict['pixels'])

    if isJuliaFractal:
        complete_dict['creal'] = float(file_dict['creal'])
        complete_dict['cimag'] = float(file_dict['cimag'])

    if isPhoenixFractal:
        complete_dict['preal'] = float(file_dict['preal'])
        complete_dict['pimag'] = float(file_dict['pimag'])

    # Gets the correct image_name
    image_name = image_name.split("/")
    for item in image_name:
        if '.frac' in item:
            image_name = item.replace(".frac", "")
    complete_dict['imagename'] = image_name

    return complete_dict
