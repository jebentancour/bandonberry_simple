#!/usr/bin/python

from BDN_MCP23S17 import MCP23S17
import time

COLUMS = 6
ROWS = 8
NUM_OF_READS = 2
DEBOUNCE_DELAY = 0.001

right_notes_matrix = [[[0, 0] for x in range(ROWS)] for y in range(COLUMS)]
# Mano Derecha
# 0 = Abriendo, 1 = Cerrando
right_notes_matrix[0][0] = [81, 80]
right_notes_matrix[0][1] = [85, 88]
right_notes_matrix[0][2] = [79, 75]
right_notes_matrix[0][3] = [78, 80]
right_notes_matrix[0][4] = [75, 76]
right_notes_matrix[0][5] = [77, 77]
right_notes_matrix[0][6] = [63, 63]
right_notes_matrix[0][7] = [57, 58]
right_notes_matrix[1][0] = [74, 76]
right_notes_matrix[1][1] = [80, 81]
right_notes_matrix[1][2] = [83, 85]
right_notes_matrix[1][3] = [71, 73]
right_notes_matrix[1][4] = [68, 69]
right_notes_matrix[1][5] = [70, 64]
right_notes_matrix[1][6] = [65, 65]
right_notes_matrix[1][7] = [57, 57]
right_notes_matrix[2][0] = [69, 71]
right_notes_matrix[2][1] = [72, 74]
right_notes_matrix[2][2] = [76, 79]
right_notes_matrix[2][3] = [66, 67]
right_notes_matrix[2][4] = [73, 78]
right_notes_matrix[2][5] = [64, 66]
right_notes_matrix[2][6] = [59, 59]
right_notes_matrix[3][0] = [82, 70]
right_notes_matrix[3][1] = [84, 72]
right_notes_matrix[3][2] = [86, 87]
right_notes_matrix[3][3] = [67, 68]
right_notes_matrix[3][4] = [62, 61]
right_notes_matrix[3][5] = [60, 62]
right_notes_matrix[4][0] = [90, 82]
right_notes_matrix[4][1] = [88, 84]
right_notes_matrix[4][2] = [87, 86]
right_notes_matrix[4][3] = [93, 91]
right_notes_matrix[4][4] = [61, 60]
right_notes_matrix[5][0] = [92, 92]
right_notes_matrix[5][1] = [91, 90]
right_notes_matrix[5][2] = [89, 89]
right_notes_matrix[5][3] = [94, 93]

left_notes_matrix = [[[0, 0] for x in range(ROWS)] for y in range(COLUMS)]
# Mano Izquierda
# 0 = Abriendo, 1 = Cerrando
left_notes_matrix[0][0] = [ 54, 53]
left_notes_matrix[0][1] = [ 39, 37]
left_notes_matrix[0][2] = [ 36, 41]
left_notes_matrix[0][3] = [ 63, 71]
left_notes_matrix[0][4] = [ 69, 68]
left_notes_matrix[0][5] = [ 67, 66]
left_notes_matrix[0][6] = [ 47, 52]
left_notes_matrix[0][7] = [ 38, 40]
left_notes_matrix[1][0] = [ 66, 64]
left_notes_matrix[1][1] = [ 61, 56]
left_notes_matrix[1][2] = [ 42, 47]
left_notes_matrix[1][3] = [ 62, 61]
left_notes_matrix[1][4] = [ 59, 57]
left_notes_matrix[1][5] = [ 56, 52]
left_notes_matrix[1][6] = [ 52, 45]
left_notes_matrix[2][0] = [ 48, 65]
left_notes_matrix[2][1] = [ 43, 54]
left_notes_matrix[2][2] = [ 41, 42]
left_notes_matrix[2][3] = [ 64, 62]
left_notes_matrix[2][4] = [ 60, 59]
left_notes_matrix[2][5] = [ 57, 55]
left_notes_matrix[2][6] = [ 50, 43]
left_notes_matrix[3][0] = [ 51, 60]
left_notes_matrix[3][1] = [ 65, 49]
left_notes_matrix[3][2] = [ 58, 48]
left_notes_matrix[3][3] = [ 55, 58]
left_notes_matrix[3][4] = [ 45, 50]
left_notes_matrix[3][5] = [ 40, 38]
left_notes_matrix[4][0] = [ 49, 51]
left_notes_matrix[4][1] = [ 53, 63]
left_notes_matrix[4][2] = [ 68, 67]
left_notes_matrix[4][3] = [ 46, 46]
left_notes_matrix[4][4] = [ 44, 44]

right_prev_data = [0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF]
left_prev_data = [0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF]

try:
    # MCP23S17 izquierdo
    mcp1 = MCP23S17(ce=1)
    mcp1.open()
    mcp1.setDirPORTA(0xFF)
    mcp1.setDirPORTB(0xC0)
    mcp1.setPullupPORTA(0xFF)
    mcp1.setPullupPORTB(0xC0)

    # MCP23S17 derecho
    mcp0 = MCP23S17(ce=0)
    mcp0.open()
    mcp0.setDirPORTA(0xFF)
    mcp0.setDirPORTB(0xC0)
    mcp0.setPullupPORTA(0xFF)
    mcp0.setPullupPORTB(0xC0)

    while (True):

        left_new_data = [0x00, 0x00, 0x00, 0x00, 0x00, 0x00]
        right_new_data = [0x00, 0x00, 0x00, 0x00, 0x00, 0x00]
        valve_new_data = 0x00
        for current_col in range(COLUMS):
            mcp1.writePORTB(~(0x01 << current_col))
            mcp0.writePORTB(~(0x01 << current_col))
            for i in range(NUM_OF_READS):
                left_new_data[current_col] |= mcp1.readPORTA()
                time.sleep(DEBOUNCE_DELAY)
                right_new_data[current_col] |= mcp0.readPORTA()
                time.sleep(DEBOUNCE_DELAY)
            if left_prev_data[current_col] != left_new_data[current_col]:
                for current_row in range(ROWS):
                    new_bit = (left_new_data[current_col] >> current_row) & 0x01
                    prev_bit = (left_prev_data[current_col] >> current_row) & 0x01
                    if new_bit != prev_bit:
                        if new_bit:
                            note = left_notes_matrix[current_col][current_row]
                            print 'left_Off  [{0}][{1}] {2}'.format(current_col, current_row, note)
                        else:
                            note = left_notes_matrix[current_col][current_row]
                            print 'left_on   [{0}][{1}] {2}'.format(current_col, current_row, note)
            if right_prev_data[current_col] != right_new_data[current_col]:
                for current_row in range(ROWS):
                    new_bit = (right_new_data[current_col] >> current_row) & 0x01
                    prev_bit = (right_prev_data[current_col] >> current_row) & 0x01
                    if new_bit != prev_bit:
                        if new_bit:
                            note = right_notes_matrix[current_col][current_row]
                            print 'right_off [{0}][{1}] {2}'.format(current_col, current_row, note)
                        else:
                            note = right_notes_matrix[current_col][current_row]
                            print 'right_on  [{0}][{1}] {2}'.format(current_col, current_row, note)

        left_prev_data = left_new_data
        right_prev_data = right_new_data

finally:
    mcp1.close()
    mcp0.close()
