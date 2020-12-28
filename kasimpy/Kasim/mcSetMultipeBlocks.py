#set multiple blocks: works
from mcpi.minecraft import Minecraft
from mcpi import block

mc = Minecraft.create()

stone = 1
x, y, z = mc.player.getPos()
mc.setBlocks(x+1, y+1, z+1, x+5, y+5, z+5, stone)
