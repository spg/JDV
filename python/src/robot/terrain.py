class Terrain:
    OBSTACLE_1 = ()
    OBSTACLE_2 = ()

    ORIGIN = (0, 0)

    RED_LINE_NORTH = (79.5, 111.0)
    RED_LINE_SOUTH = (79.5, 0)

    DRAWING_ZONE_CENTER = (174.8, 55.5)

    DRAWING_ZONE_NORTH_WEST_CORNER_OUTER = (141.8, 88.5)
    DRAWING_ZONE_NORTH_EAST_CORNER_OUTER = (207.8, 88.5)
    DRAWING_ZONE_SOUTH_WEST_CORNER_OUTER = (141.8, 22.5)
    DRAWING_ZONE_SOUTH_EAST_CORNER_OUTER = (207.8, 22.5)

    DRAWING_ZONE_NORTH_WEST_CORNER_INNER = (DRAWING_ZONE_NORTH_WEST_CORNER_OUTER[0] + 3.0, DRAWING_ZONE_NORTH_WEST_CORNER_OUTER[1] - 3.0)
    DRAWING_ZONE_NORTH_EAST_CORNER_INNER = (DRAWING_ZONE_NORTH_EAST_CORNER_OUTER[0] - 3.0, DRAWING_ZONE_NORTH_EAST_CORNER_OUTER[1] - 3.0)
    DRAWING_ZONE_SOUTH_WEST_CORNER_INNER = (DRAWING_ZONE_SOUTH_WEST_CORNER_OUTER[0] + 3.0, DRAWING_ZONE_SOUTH_WEST_CORNER_OUTER[1] + 3.0)
    DRAWING_ZONE_SOUTH_EAST_CORNER_INNER = (DRAWING_ZONE_SOUTH_EAST_CORNER_OUTER[0] - 3.0, DRAWING_ZONE_SOUTH_EAST_CORNER_OUTER[1] + 3.0)

    CORNER_ORANGE_WEST_CENTER = (6.0, 6.0)
    CORNER_ORANGE_WEST_LEFT_EDGE = (12.0, 0)
    CORNER_ORANGE_WEST_RIGHT_EDGE = (0, 12.0)

    CORNER_ORANGE_EAST_CENTER = (223.8, 6.0)
    CORNER_ORANGE_EAST_LEFT_EDGE = (229.8, 12.0)
    CORNER_ORANGE_EAST_RIGHT_EDGE = (217.8, 0)

    CORNER_BLUE_WEST_CENTER = (6.0, 105.0)
    CORNER_BLUE_WEST_LEFT_EDGE = (0, 99.0)
    CORNER_BLUE_WEST_RIGHT_EDGE = (12.0, 111.0)

    CORNER_BLUE_EAST_CENTER = (223.8, 105.0)
    CORNER_BLUE_EAST_LEFT_EDGE = (217.8, 111.0)
    CORNER_BLUE_EAST_RIGHT_EDGE = (229.8, 99.0)

    AR_TAG_NORTH = (174.8, 111.0)
    AR_TAG_EAST = (229.8, 55.5)
    AR_TAG_SOUTH = (174.8, 0)

    FIGURE_0_FACE = (56.0, 50.0)
    FIGURE_0_CENTER = (56.0, 0)
    FIGURE_0_LEFT_EDGE = (64.0, 0)
    FIGURE_0_RIGHT_EDGE = (48.0, 0)

    FIGURE_1_FACE = (23.0, 40.0)
    FIGURE_1_CENTER = (23.0, 0)
    FIGURE_1_LEFT_EDGE = (31.0, 0)
    FIGURE_1_RIGHT_EDGE = (15.0, 0)

    FIGURE_2_FACE = (50.0, 16.0)
    FIGURE_2_CENTER = (0, 16.0)
    FIGURE_2_LEFT_EDGE = (0, 80)
    FIGURE_2_RIGHT_EDGE = (0, 24.0)

    FIGURE_3_FACE = (50.0, 42.0)
    FIGURE_3_CENTER = (0, 42.0)
    FIGURE_3_LEFT_EDGE = (0, 34.0)
    FIGURE_3_RIGHT_EDGE = (0, 50.0)

    FIGURE_4_FACE = (50.0, 69.0)
    FIGURE_4_CENTER = (0, 69.0)
    FIGURE_4_LEFT_EDGE = (0, 61.0)
    FIGURE_4_RIGHT_EDGE = (0, 77.0)

    FIGURE_5_FACE = (50, 95)
    FIGURE_5_CENTER = (0, 95.0)
    FIGURE_5_LEFT_EDGE = (0, 87.0)
    FIGURE_5_RIGHT_EDGE = (0, 103.0)

    FIGURE_6_FACE = (23.0, 60.0)
    FIGURE_6_CENTER = (23.0, 111.0)
    FIGURE_6_LEFT_EDGE = (15.0, 111.0)
    FIGURE_6_RIGHT_EDGE = (31.0, 111.0)

    FIGURE_7_FACE = (56.0, 60.0)
    FIGURE_7_CENTER = (56.0, 111.0)
    FIGURE_7_LEFT_EDGE = (64.0, 111.0)
    FIGURE_7_RIGHT_EDGE = (48.0, 111.0)
