# No animation

## 1

1. Open Krita
2. Run script

A. Should be greyed or at least not error.

**Note**: Greyed menu can be set through `.action` file.


## 2

1. Make two layers, draw a circle in each, one on the left, one on the right
2. Turn off visibility of left circle.
3. Run script

A. Should have resize to right circle boundaries.

4. Turn on visibility of left circle.
5. Run script

B. Should have resized to boundaries of both circle combined.

**Note**: A is Basic behavior. B is making sure nothing is cropped. Because when using crop, it will delete whatever is outside, in visible or invisible layers. 


## 3

1. Make two layers, draw a circle in each, one on the left, one on the right
2. Put both layers in a group.
3. Turn off visibility of left circle.
4. Run script

A. Should have resize to right circle boundaries.

4. Turn on visibility of left circle.
5. Run script

B. Should have resized to boundaries of both circle combined.

**Note**: When using group boundaries instead of Leaf node boundaries, it fail at B.


# Animation

Test with:
- 2 frames in one layer.
- 2 frames in one layer + 1 layer no frame
- 2 frames in one layer + 1 frame in another layer
- 2 frames in one layer + 2 frames in another layer

Test:
- Make 3 frames or more in one layer. Spam the script / ctrl+z, every 3 or 4 you get one frame ignored, mostly the middle one, sometimes the last one.
  To fix that you need to use `waitForDone` after changing frame.