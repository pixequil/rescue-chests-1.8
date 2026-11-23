# After many hours I found the fucking mcedit documentation.
# https://github.com/codewarrior0/pymclevel/blob/master/mclevel.py

displayName = "Rescue old chests for 1.8"

inputs = (
    ("Quick and dirty thing that preserves chest contents for converting worlds from 1.7 or older to 1.8.\n", "label"),
    ("Chests created in very early versions of minecraft didn't have data on which way they faced, so, left unchanged, they retained the block id 54:0 going into the anvil format. This caused them to be deleted upon opening a world in release 1.8 or later, and was only solved in 1.15.", "label"),
    ("This script changes them all to face east, which will at least let you keep your items. I don't understand why MCEdit won't just let me find/replace 54:0 with 54:5 but this script works so here it is.", "label"),
)

def perform(level, box, options):
    for (chunk, slices, point) in level.getChunkSlices(box):

        chestBlocks = ( chunk.Blocks==level.materials.Chest.ID )
        chestBlocks &= ( chunk.Data==0 )
        # adapted from the active ingredient in this c# script:
        # https://gist.github.com/Gargaj/2891b8fc558e01b8ddf2

        chunk.Data[chestBlocks] = 5;
        chunk.chunkChanged(False)