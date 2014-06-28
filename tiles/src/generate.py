from PIL import Image
import os
import json

def main():
    pack = {
        "meta": {
            "app": "https://github.com/piesome/mahjonki-graphics/tiles/src/generate.py",
            "version": "1.0",
            "image": "tiles.png",
            "format": "RGBA8888",
            "size": {"w": 288, "h": 240},
            "scale": "1"
        },
        "frames": {

        }
    }

    out = Image.new("RGBA", (288, 240), 0x00000000)

    each = (32, 48)
    im = Image.open("tiles.png")
    background = im.crop((each[0] * 6, 
                          each[1] * 4, 
                          each[0] * 6 + each[0], 
                          each[1] * 4 + each[1]))
    foreground = im.crop((each[0] * 7, 
                          each[1] * 4, 
                          each[0] * 7 + each[0], 
                          each[1] * 4 + each[1]))

    tiles = []
    for value_index, value in enumerate(["I", "Ryan", "San", "Su", "U", "Ryu", "Chi", "Pa", "Chu"]):
        for suite_index, suite in enumerate(["pin", "sou", "man"]):
            tiles.append(((value_index, suite_index), value + suite))


    tiles.append(((0, 3), "Ton"))
    tiles.append(((1, 3), "Nan"))
    tiles.append(((2, 3), "Sha"))
    tiles.append(((3, 3), "Pei"))

    tiles.append(((4, 3), "Haku"))
    tiles.append(((5, 3), "Hatsu"))
    tiles.append(((6, 3), "Chun"))

    tiles.append(((0, 4), "Upin-Dora"))
    tiles.append(((1, 4), "Usou-Dora"))
    tiles.append(((2, 4), "Uman-Dora"))

    tiles.append(((8, 4), "Backside"))

    for tile in tiles:
        new = Image.new("RGBA", each, color=0x00000000)
        new.paste(background, (0,0), background)
        pos = {"x": each[0] * (tile[0][0]),
               "y": each[1] * (tile[0][1]),
               "w": each[0] * (tile[0][0] + 1),
               "h": each[1] * (tile[0][1] + 1)}
        gfx = im.crop((pos["x"], pos["y"], pos["w"], pos["h"]))
        new.paste(gfx, (0,0), gfx)
        new.paste(foreground, (0,0), foreground)
        pack["frames"][tile[1]+".png"] = {
            "frame": {"x": pos["x"], "y": pos["y"], "w": each[0], "h": each[1]},
            "rotated": False,
            "trimmed": False,
            "spriteSourceSize": {"x": 0, "y": 0, "w": each[0], "h": each[1]},
            "sourceSize": {"w": each[0], "h": each[1]}
        }
        out.paste(new, (pos["x"], pos["y"]), new)
        # new.save("../tmp/"+tile[1]+".png", "PNG")

    out.save("../tiles.png", "PNG")
    with open("../tiles.json", "w") as fp:
        fp.write(json.dumps(pack, sort_keys=True, indent=4, separators=(',', ': ')))

if __name__ == "__main__":
    main()