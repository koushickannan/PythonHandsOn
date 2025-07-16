from pptx import Presentation
from pptx.util import Inches
from PIL import Image

# Load the image
image_path = 'willskillmatrix.png'
img = Image.open(image_path)

# Define text for each box
texts = ["Text 1", "Text 2", "Text 3", "Text 4"]

# Create a PowerPoint presentation object
prs = Presentation()

# Add a slide
slide_layout = prs.slide_layouts[5]  # Use a layout with title and content
slide = prs.slides.add_slide(slide_layout)

# Set the dimensions of the image
left = Inches(1)
top = Inches(1)
width = Inches(6)
height = Inches(6)

# Add the image to the slide
pic = slide.shapes.add_picture(image_path, left, top, width=width, height=height)

# Add text boxes
for i, text in enumerate(texts):
    left = Inches(i * 2 + 1)  # Adjust the position of text boxes as needed
    top = Inches(7)
    width = Inches(1.5)
    height = Inches(0.5)
    textbox = slide.shapes.add_textbox(left, top, width, height)
    text_frame = textbox.text_frame
    p = text_frame.add_paragraph()
    p.text = text

# Save the presentation
prs.save('output.pptx')
