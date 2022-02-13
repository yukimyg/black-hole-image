from internal.datas import Const as const
#from internal.datas import Image as image


mass_bh = 100 * const.mass_sun

# rs : Schwarzschild radius
rs = 2 * mass_bh * const.newtonian_g / const.c ** 2
distance = 5 * rs

image_width = 4000#image.uhd.width
image_height = 2000#image.uhd.height

input_name = "input.png"
output_name = "output.png"
