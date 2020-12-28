#drop block

from mcpi.minecraft import Minecraft
from time import sleep

mc = Minecraft.create()

grass = 2
flower = 38

while True:
    x, y, z = mc.player.getPos()   # player position
    block_beneath = mc.getBlock(x,y-1,z)  # block id

    if block_beneath == grass:
        mc.setBlock(x,y,z, flower)
    else:
        mc.setBlock(x, y-1, z, grass)

    sleep(0.1)    
