import mcrcon
import config
import sys
import math

command_fill = "fill {x1} {y1} {z1} {x2} {y2} {z2} {block_name} replace"
command_setblock = "setblock {x} {y} {z} {block_name} replace"

rcon = mcrcon.MCRcon()

def piramyd(args):
    if len(args) < 5:
        print("usage: piramyd smallest x, smallest y, smallest z, baseSize, blockName")
        return

    height = math.floor(int(args[3]) / 2)
    size = int(args[3])
    x = int(args[0])
    y = int(args[1])
    z = int(args[2])
    yDelta = 1
    if len(args) > 5:
        yDelta = int(args[5])
    for i in range(height):
        response = rcon.command(command_fill.format(x1=x, y1=y, z1=z, x2=x + size, y2 = y, z2 = z + size, block_name=args[4]))
        if response:
            print("  %s" % response)

        x +=1 
        y +=yDelta
        z +=1
        size -= 2

def piramydCrater(args):
    if len(args) < 4:
        print("usage: crater smallest x, heighest y, smallest z, baseSize, blockName")
        return

    return piramyd([args[0], args[1], args[2], args[3], "air", -1])


def degToRad(degrees):
    return degrees * math.pi / 180


def circle(args):
    if len(args) < 6:
        print("usage: circle center_x, center_y, center_z, raduis, horizontal / vertical, blockName")
        return

    centerX = int(args[0])
    centerY = int(args[1])
    centerZ = int(args[2])
    radius = int(args[3])

    horizontal = (args[4].lower() == "horizontal")
    vertical = (args[4].lower() == "vertical")
    for deg in range (360):
        rad = degToRad(deg)
        cos = math.cos(rad)
        sin = math.sin(rad)
        if horizontal:
            response = rcon.command(command_setblock.format(x=centerX + math.floor(radius * cos), y=centerY, z=centerZ  + math.floor(radius * sin), block_name=args[5]))
            if response:
                print("  %s" % response)
        elif vertical:
            response = rcon.command(command_setblock.format(x=centerX + math.floor(radius * cos), y=centerY + math.floor(radius * sin), z=centerZ, block_name=args[5]))
            if response:
                print("  %s" % response)
    

def cylinder(args):
    if len(args) < 7:
        print("usage: cylinder center_x, center_y, center_z, raduis, horizontal / vertical, blockName, length")
        return

    horizontal = (args[4].lower() == "horizontal")
    vertical = (args[4].lower() == "vertical")
    length = int(args[6])

    for i in range(length):
        if horizontal:
            centerX = int(args[0])
            circle([centerX + i, args[1], args[2], args[3], "vertical", args[5]])
        elif vertical:
            centerY = int(args[1])
            circle([args[0], centerY + i, args[2], args[3], "horizontal", args[5]])

def main():
    conf = config.Config()
    
    print("# connecting to %s:%i..." % (conf.Host(), conf.Port()))
    rcon.connect(conf.Host(), conf.Port(), conf.Password())
    print("# ready")
    
    try:
        while True:
            cmd = input("@: ").lower()
            if len(cmd) == 0:
                continue
                
            parts = cmd.split()
            if parts[0] == "piramyd":
                piramyd(parts[1:])
            elif parts[0] == "crater":
                piramydCrater(parts[1:])
            elif parts[0] == "circle":
                circle(parts[1:])
            elif parts[0] == "cylinder":
                cylinder(parts[1:])
        
    except KeyboardInterrupt:
        print("\n# disconnecting...")
        rcon.disconnect()

main()

