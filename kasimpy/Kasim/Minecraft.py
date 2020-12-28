#Impoting the Minecraft library
from mcpi import minecraft
#Import block library = 4.2(use this library) is another way for 4.1(uses mincraft library)
from mcpi import block

mc = minecraft.Minecraft.create()

#1 Post message
mc.postToChat('Hello world')

#2 Get location
pos = mc.player.getPos()

#2 xyz coordinates
x,y,z = mc.player.getPos()

#2 Post location
mc.postToChat(pos)

#4.1 Plaxe single blocj at location
#Arguments (x,y,z = position And ,id = type of block e.g. 1=stone)
mc.setBlock(x+1,y,z, 2)

#4.2 same as 4.1 using but using block Library
mc.setBlock(x+2,y,z, block.GOLD_ORE.id)
mc.setBlock(x,y,z, block.WOOD_PLANKS.id)

#4.3 using variables
#4.3p1 Integer id
dirt = 3
mc.setBlock(x,y,z-1, dirt)

#4.3p2 Name id
dirt = block.DIRT.id
mc.setBlock(x,y+1,z-1, dirt)

#4.4 extra property blocks eg wools last parameter specifies colour
wool = 35
mc.setBlock(x+1,y,z-1, wool, 1)

#5 place multiple blocks
stone = 1
x,y,z = mc.player.getPos()
# Fill 10*10*10 area of stone
mc.setBlocks(x+3,y+3,z+3, x+13,y+13,z+13)


#3 Teleport
mc.player.setPos(x,y+10,z+2)








