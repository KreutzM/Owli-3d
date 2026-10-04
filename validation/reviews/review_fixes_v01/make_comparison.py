"""Pixel-only fixed-camera before/after board; no new scene camera or geometry."""
from pathlib import Path
from PIL import Image, ImageDraw

folder = Path(__file__).resolve().parent
views = ('VAL_FRONT','VAL_LEFT','VAL_BACK','VAL_3Q')
tile, heading = 512,32
board = Image.new('RGB',(tile*2,(tile+heading)*4),(245,245,240))
draw = ImageDraw.Draw(board)
for row,view in enumerate(views):
    for col,(label,path) in enumerate((('#5 accepted baseline',folder/'evidence/baseline'/(view+'.png')),
                                       ('#37 saved candidate',folder/(view+'.png')))):
        with Image.open(path) as image:
            board.paste(image.convert('RGB').resize((tile,tile),Image.Resampling.LANCZOS),(col*tile,row*(tile+heading)+heading))
        draw.text((col*tile+8,row*(tile+heading)+9),view+' | '+label,fill=(30,30,30))
board.save(folder/'baseline_vs_corrected.png')
