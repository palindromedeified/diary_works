from PIL import Image, ImageDraw


def window(a, frame='#d6d6d6', sky='#3075b6', tree='#963', sun='#ecec20', bird='#0070c0'):
    im = Image.new("RGB", (int(a) * 20, int(a) * 24))
    drawer = ImageDraw.Draw(im)
    drawer.rectangle(((0, 0), ((a * 20), (a * 24))), frame)
    drawer.rectangle(((a * 2, a * 2), ((a * 9), (a * 11))), sky)
    drawer.rectangle(((a * 11, a * 2), ((a * 18), (a * 11))), sky)
    drawer.rectangle(((a * 2, a * 13), ((a * 9), (a * 22))), sky)
    drawer.rectangle(((a * 11, a * 13), ((a * 18), (a * 22))), sky)
    drawer.ellipse(((13 * a, 3 * a), (18 * a, 8 * a)), sun)
    drawer.polygon(((a * 11, a * 13), (a * 12.5, a * 13), (a * 18, a * 21), (a * 18, a * 22), (a * 16, a * 22)), tree)
    drawer.polygon(((a * 5, a * 2), (a * 9, a * 8), (a * 9, a * 9)), tree)
    drawer.line(((7 * a), 3 * a, (7 * a), 5 * a), tree, width=int(0.2 * a))
    drawer.line(((5 * a), 6 * a, (9 * a), 8 * a), tree, width=int(0.2 * a))
    drawer.ellipse(((3 * a, 17 * a), (5 * a, 19 * a)), bird)
    drawer.ellipse(((5 * a, 17 * a), (7 * a, 19 * a)), bird)
    drawer.ellipse((int(3.2 * a), int(17.2 * a), (int(4.8 * a), int(18.8 * a))), sky)
    drawer.ellipse((int(5.2 * a), int(17.2 * a), (int(6.8 * a), int(18.8 * a))), sky)
    drawer.rectangle((((a * 3), (a * 18)), ((a * 7), (a * 20))), sky)
    im.save('window.png')


window(20)
# def picture(file_name, width, height, sky_color='#87CEEB', ocean_color="#017B92", boat_color="#874535",
#             sail_color="#FFFFFF", sun_color="#FFCF40"):
#     im = Image.new("RGB", (width, height))
#     drawer = ImageDraw.Draw(im)
#     drawer.rectangle(((0, 0), (width, int(height * 0.8))), sky_color)
#     drawer.rectangle(((0, int(height * 0.8)), (width, height)), ocean_color)
#     drawer.ellipse(((int(0.8 * width), -int(0.2 * height)), (int(1.2 * width), int(0.2 * height))), sun_color)
#     drawer.polygon(((int(width * 0.51), int(height * 0.3)), (int(width * 0.66), int(height * 0.45)),
#                     (int(width * 0.51), int(height * 0.6))), sail_color)
#     drawer.rectangle(((int(width * 0.49), int(height * 0.3)), (int(width * 0.51), int(height * 0.65))), boat_color)
#     drawer.polygon(((int(width * 0.25), int(height * 0.65)), (int(width * 0.75), int(height * 0.65)),
#                     (int(width * 0.7), int(height * 0.85)), (int(width * 0.3), int(height * 0.85))), boat_color)
#     im.save(file_name)
