import cv2
import numpy as np
import argparse


def main():
    parser = argparse.ArgumentParser(
        description='Parse a Danganronpa V3 Treasure Hunter Monolith screenshot and output a CSV file representing the board. For mean difficulty boards (22x11)')
    parser.add_argument('image', type=str,
                        help='Screenshot file in 16:9 aspect ratio, without black bars (jpg, png, bmp...)')
    parser.add_argument('-o', '--out', type=str, default='out.csv',
                        help='Output file name (default out.csv)')

    args = parser.parse_args()

    # Dominant colors, in BGR order
    colors = np.array([
        [0xc7, 0xc6, 0xc8],  # 1 - gray
        [0xc6, 0x9a, 0xf1],  # 2 - pink
        [0x6e, 0xb7, 0xdd],  # 3 - orange
        [0xc3, 0xb1, 0x5f],  # 4 - blue
    ])

    image = cv2.imread(args.image)
    if image is None:
        raise Exception('Could not read image ' + args.image)

    # THM mean grid is 22x11, and screenshot roughly 1 extra cell of padding on each side
    # Resize so each cell is about 32 px
    cSize = 32
    downsampled = image_resize(image, width=(22+2) * cSize)

    # DEBUG
    # gridVisualization = downsampled.copy()

    csvMap = np.zeros((11, 22))

    for y in range(11):
        for x in range(22):
            px = int((x + 1) * cSize + cSize / 6)
            py = int((y + 1) * cSize + cSize / 6)
            w = int(cSize * 4 / 6)
            cell = downsampled[py:py+w, px:px+w]

            # DEBUG
            # cv2.rectangle(gridVisualization, (px, py), (px+w, py+w), (255, 0, 0))

            pixels = np.float32(cell.reshape(-1, 3))

            # Get dominant color
            criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 200, .1)
            flags = cv2.KMEANS_RANDOM_CENTERS
            _, labels, palette = cv2.kmeans(pixels, 1, None, criteria, 10, flags)
            _, counts = np.unique(labels, return_counts=True)
            dominant = palette[np.argmax(counts)]

            # Quantize into known colors
            diffs = np.linalg.norm(dominant - colors, axis=1)
            nearest = np.argmin(diffs)
            if diffs[nearest] < 50:
                csvMap[y, x] = nearest + 1  # colors are 1,2,3,4

    # DEBUG
    # cv2.imwrite('gridVisualization.png', grid)

    np.savetxt(args.out, csvMap, fmt='%d', delimiter=',')


def image_resize(image, width=None, height=None, inter=cv2.INTER_AREA):
    '''
    Resize image and keep aspect ratio
    Ref: https://stackoverflow.com/a/44659589
    '''
    # initialize the dimensions of the image to be resized and
    # grab the image size
    dim = None
    (h, w) = image.shape[:2]

    # if both the width and height are None, then return the
    # original image
    if width is None and height is None:
        return image

    # check to see if the width is None
    if width is None:
        # calculate the ratio of the height and construct the
        # dimensions
        r = height / float(h)
        dim = (int(w * r), height)

    # otherwise, the height is None
    else:
        # calculate the ratio of the width and construct the
        # dimensions
        r = width / float(w)
        dim = (width, int(h * r))

    # resize the image
    resized = cv2.resize(image, dim, interpolation=inter)

    # return the resized image
    return resized


if __name__ == '__main__':
    main()
