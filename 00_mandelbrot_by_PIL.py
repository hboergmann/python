from PIL import Image
# drawing area
xa = -2.0
xb = 1.0
ya = -1.5
yb = 1.5
#number of iterations
maxIt = 512
#image size (make y a multible by 4)
imgx = 1024
imgy = 1024
# make a new image in RGB color mode of sizw imgx by imgy
image = Image.new("RGB", (imgx, imgy))
# progress
# progress = 0

# loop through the heights
for y in range(imgy):
    # make the imaganigery part of number by taking y/height * yb-ya + ya
    cy = y * (yb - ya) / (imgy - 1) + ya
    #progress
    progress = (y / imgy * 1000) / 10
    
    print("Percent completed", progress)
    # in each height-loop through the width
    for x in range(imgx):
        cx = x * (xb - xa) / (imgx - 1) + xa
        # combine the two
        c = complex(cx, cy)
        # set initial
        z = 0
        # check the critical point escapes
        for i in range(maxIt):
            if abs(z) > 2.0: break
            z = z * z + c
            #turn the number of iterates to escape into a color
            r = i % 4 * 64
            g = i % 8 * 32
            b = i % 16 * 16
            #color pixel
            image.putpixel((x, y), b * 65536 + g * 256 + r)

# save image
image.save("mandel.png", "PNG")
#image.save("mandel%d.png %maxIt", "PNG")
