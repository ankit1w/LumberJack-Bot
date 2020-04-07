import time

import pyautogui
import win32gui


def get_pixel_colour():
	color_dat = list()
	i_desktop_window_id = win32gui.GetDesktopWindow()
	i_desktop_window_dc = win32gui.GetWindowDC(i_desktop_window_id)
	for height in branch_heights:
		long_colour = win32gui.GetPixel(i_desktop_window_dc, ref_branch_x, height)
		i_colour = int(long_colour)
		color_dat.append(((i_colour & 0xff), ((i_colour >> 8) & 0xff), ((i_colour >> 16) & 0xff)))
	for color in color_dat:
		yield color


def start():
	while True:
		time.sleep(batch_sleep)
		for i in get_pixel_colour():
			if i == branch_color:
				pyautogui.press('left', presses=2, interval=double_press_interval)
			else:
				pyautogui.press('right', presses=2, interval=double_press_interval)


if __name__ == '__main__':
	branch_color = (162, 116, 56)
	# Color of the pixel used to determine presence of a branch, when a branch is present.

	ref_branch_x = 1030
	# X-coordinate of branches on the right side of the tree.

	branch_heights = (570, 445, 320, 195, 70)
	# Y-coordinates of the branches ordered from bottom to top.

	batch_sleep = 0.07
	# Time in seconds before going to the next "batch" of branches.

	double_press_interval = 0.02
	# Time in seconds between two presses of a the same key.

	start()
