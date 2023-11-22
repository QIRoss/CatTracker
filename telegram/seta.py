from datetime import datetime, timezone, timedelta
import pathlib


def in_downstairs(x_center, y_center):
    if x_center < 0.281711 and y_center > 0.547249: 
        return True
    
    return False


def in_upstairs(x_center, y_center):
    if x_center < 0.473451 and x_center > 0.278024 and y_center < 0.547249\
        or x_center < 0.278024 and y_center < 0.227006:
        return True

    return False


def in_bedroom(x_center, y_center):
    if x_center > 0.532448  and y_center < 0.360878: 
        return True
    
    return False


def verify_where_cat_went(x_center: float, y_center: float):
    arrow = None
    
    # Verify if it is in down
    if in_downstairs(x_center, y_center):
        # Seta para baixo
        arrow = "setaPrimeiroAndar.jpeg"

    elif in_upstairs(x_center, y_center):
        arrow = "setaTerceiroAndar.jpeg"

    elif in_bedroom(x_center, y_center):
        arrow = "setaQuarto.jpeg"

    return arrow


def get_x_center_and_y_center(label_path):
    with open(label_path) as lf:
        text = lf.read()
    line_split = text.split(" ")
    
    x_center = line_split[1]
    y_center = line_split[2]

    return float(x_center), float(y_center)


def get_creation_time(image_path: str):
    return pathlib.Path(image_path).stat().st_ctime


def timeout_last_time_seen(creation_time, timeout=60):
    print("\n\nCreation time =", creation_time)

    # If passed 60 seconds
    if (datetime.now(tz=timezone.utc) - datetime.fromtimestamp(creation_time,tz=timezone.utc)) > timedelta(seconds=timeout):
    # if (datetime.now(tz=timezone.utc) - creation_time) > timedelta(seconds=timeout):
        return True
    
    return False