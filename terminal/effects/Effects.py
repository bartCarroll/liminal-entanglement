#! /usr/bin/env python

import random
import os.path
import time

from PIL import Image, ImageDraw, ImageFont


def rsrc(n):
    return os.path.join(os.path.dirname(__file__), n)


a1 = Image.open(rsrc("images/a1.png"))
a2 = Image.open(rsrc("images/a2.png"))
frames1 = {0: a1, 1: a1, 2: a2, 3: a2}

b1 = Image.open(rsrc("images/b1.png"))
b2 = Image.open(rsrc("images/b2.png"))
frames2 = {0: b1, 1: b1, 2: b2, 3: b2}

p1 = Image.open(rsrc("images/p1.png"))
p2 = Image.open(rsrc("images/p2.png"))
frames3 = {0: p1, 1: p1, 2: p2, 3: p2}

BigFont = ImageFont.truetype(rsrc("fonts/VeraBd.ttf"), 15)
SmallFont = ImageFont.truetype(rsrc("fonts/Roboto-Bold.ttf"), 10)

skull_img = Image.open(rsrc("images/skull2.png"))
death_frame1 = {0: skull_img, 1: skull_img, 2: skull_img, 3: skull_img}

heart_img = Image.open(rsrc("images/heart.png"))
heart_frame1 = {0: heart_img, 1: heart_img, 2: heart_img, 3: heart_img}

crazy_sqr0 = Image.open(rsrc("images/crazy_square_0.png"))
crazy_sqr1 = Image.open(rsrc("images/crazy_square_1.png"))
crazy_sqr2 = Image.open(rsrc("images/crazy_square_2.png"))
crazy_sqr3 = Image.open(rsrc("images/crazy_square_3.png"))
crazy_sqr_frames = {0: crazy_sqr0, 1: crazy_sqr1, 2: crazy_sqr2, 3: crazy_sqr3}

big_hypno0 = Image.open(rsrc("images/big_hypno_1.png"))
big_hypno1 = Image.open(rsrc("images/big_hypno_2.png"))
big_hypno_frames = {0: big_hypno0, 1: big_hypno1, 2: big_hypno0, 3: big_hypno1}

hypno_squares0 = Image.open(rsrc("images/hypno_squares1.png"))
hypno_squares1 = Image.open(rsrc("images/hypno_squares2.png"))
hypno_squares_frames = {0: hypno_squares0, 1: hypno_squares1, 2: hypno_squares0, 3: hypno_squares1}

# STATIC IMAGES
big_heart_img = Image.open(rsrc("images/heart_big.png"))
big_skull_img = Image.open(rsrc("images/skull_big.png"))
cross_over_img = Image.open(rsrc("images/cross_over.png"))
enter_here_img = Image.open(rsrc("images/enter_here.png"))


def scroll_text(d, text, font=BigFont):
    draw = ImageDraw.Draw(d.im)
    tw, th = draw.textsize(text, font=font)
    shift = 0 if font == BigFont else -2
    for x in range(28, 0 - tw, -1):
        d.reset()
        draw.text((x, 14 - th + shift), text, font=font)
        d.send()
        time.sleep(0.06)
    del draw


def display_text(d, text, font=SmallFont):
    draw = ImageDraw.Draw(d.im)
    tw, th = draw.textsize(text, font=font)
    shift = -1 if font == BigFont else -3
    d.reset()
    draw.text((14 - (tw / 2), 14 - th + shift), text, font=font)
    d.send()
    del draw


def blink_text(d, text, n=3, font=SmallFont):
    for i in range(n):
        display_text(d, text, font)
        time.sleep(0.5)
        d.reset()
        d.send()
        time.sleep(0.5)


def animate(disp, i, w, d=1):
    l, h = -w, 29
    if d < 0:
        l, h = h, l
    for x in range(l, h, d):
        im = i[abs(x % len(i))]
        disp.reset()
        disp.im.paste(im, (x, 0))
        disp.send()
        time.sleep(0.1)


def heart(d):
    animate(d, heart_frame1, 19, 1)


def skull(d):
    animate(d, death_frame1, 19, 1)


def alien_1(d):
    animate(d, frames1, 19, 1)


def alien_2(d):
    animate(d, frames2, 14, -1)


def gobble(d):
    animate(d, frames3, 14, 1)


def dot(d):
    draw = ImageDraw.Draw(d.im)
    w, h = d.im.size
    mw = w / 2
    mh = h / 2
    for i in range(0, 14):
        d.reset()
        draw.ellipse([(mw - i, mh - i), (mw + i, mh + i)], fill=(255, 255, 255))
        d.send()
        time.sleep(0.6 / (i + 1))
    del draw


def wipe_right(d):
    w, h = d.im.size
    d.reset(white=True)
    d.send()
    time.sleep(0.5)
    for x in range(1, w + 1):
        draw = ImageDraw.Draw(d.im)
        xy = (0, 0)
        sz = (x, h)
        draw.rectangle([xy, sz], fill=(0, 0, 0))
        del draw
        d.send()
        time.sleep(0.07)


def wipe_down(d):
    w, h = d.im.size
    d.reset()
    d.send()
    time.sleep(0.5)
    for y in range(1, h + 1):
        draw = ImageDraw.Draw(d.im)
        xy = (0, 0)
        sz = (28, y)
        draw.rectangle([xy, sz], fill=(255, 255, 255))
        del draw
        d.send()
        time.sleep(0.1)


def curtain(d):
    w, h = d.im.size
    for x in range(1, w + 1):
        draw = ImageDraw.Draw(d.im)
        xy = (w - x, 0)
        sz = (x, h)
        draw.rectangle([(0, 0), (w, h)], fill=(255, 255, 255))
        draw.rectangle([xy, sz], fill=(0, 0, 0))
        del draw
        d.send()
        time.sleep(0.1)

def animate_14x28(disp,frames):
    for frame in frames.values():
        display_image(disp, frame)
        time.sleep(0.3)

def crazy_blocks(disp):
    for i in range(10):
        animate_14x28(disp, crazy_sqr_frames)

def big_hypno(disp):
    for i in range(10):
        animate_14x28(disp, big_hypno_frames)

def hypno_squares(disp):
    for i in range(10):
        animate_14x28(disp, hypno_squares_frames)

transitions = [
    dot,
    alien_1,
    alien_2,
    curtain,
    wipe_right,
    wipe_down,
    gobble,
    crazy_blocks,
    big_hypno,
    hypno_squares,
    heart,
    skull,
]
random.shuffle(transitions)
t_idx = 0


def rand(d):
    global t_idx
    f = transitions[t_idx]
    t_idx = (t_idx + 1) % len(transitions)
    f(d)


# STATIC IMAGES
def display_image(disp, img):
    disp.reset()
    disp.im.paste(img, (0, 0))
    disp.send()


def display_skull(disp):
    display_image(disp, big_skull_img)


def display_heart(disp):
    display_image(disp, big_heart_img)


def display_enter_here(disp):
    display_image(disp, enter_here_img)


def display_cross_over(disp):
    display_image(disp, cross_over_img)


static_images = [
    display_skull,
    display_heart,
    display_enter_here,
    display_cross_over,
]