# BBD's Krita Script Starter Feb 2018

from krita import Extension

EXTENSION_ID = 'pykrita_resize_to_visible'
MENU_ENTRY = 'Resize to visible'


class Resize_to_visible(Extension):

    def __init__(self, parent):
        # Always initialise the superclass.
        # This is necessary to create the underlying C++ object
        super().__init__(parent)

    def setup(self):
        pass

    def createActions(self, window):
        action = window.createAction(EXTENSION_ID, MENU_ENTRY, "tools/scripts")
        # parameter 1 = the name that Krita uses to identify the action
        # parameter 2 = the text to be added to the menu entry for this script
        # parameter 3 = location of menu entry
        action.triggered.connect(self.action_triggered)

    def action_triggered(self):
        root_node_childs = Krita.instance().activeDocument().rootNode().childNodes()
        first = True

        stack = root_node_childs

        while stack:
            node = stack.pop()
            is_leaf = len(node.childNodes()) == 0

            if is_leaf:
                if not node.visible():
                    continue

                nb = node.bounds()

                if first:
                    left = nb.left()
                    top = nb.top()
                    right = nb.right()
                    bottom = nb.bottom()
                    first = False
                else:
                    left = min(nb.left(), left)
                    top = min(nb.top(), top)
                    right = max(nb.right(), right)
                    bottom = max(nb.bottom(), bottom)
            else:
                for c in node.childNodes():
                    stack.append(c)

        # Avoid using
        # Krita.instance().activeDocument().crop()
        # because it delete the part that it outside the calculated zone in non-visible layers.
        # This may be unexpected to the user.

        Krita.instance().activeDocument().resizeImage(
            left,
            top,
            right - left,
            bottom - top
        );
