from .resize_to_visible import Resize_to_visible

# And add the extension to Krita's list of extensions:
app = Krita.instance()
# Instantiate your class:
extension = Resize_to_visible(parent = app)
app.addExtension(extension)
