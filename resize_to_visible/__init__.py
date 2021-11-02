from .resize_to_visible import Resize_to_visible
from .resize_to_visible_animation import Resize_to_visible_animation

# And add the extension to Krita's list of extensions:
app = Krita.instance()
# Instantiate your class:
extension = Resize_to_visible(parent = app)
app.addExtension(extension)

extension2 = Resize_to_visible_animation(parent = app)
app.addExtension(extension2)
