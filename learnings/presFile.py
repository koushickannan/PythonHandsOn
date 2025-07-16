from pptx import Presentation

# Create a new PowerPoint presentation
prs = Presentation()

# Slide 1: Title Slide
slide = prs.slides.add_slide(prs.slide_layouts[0])
title = slide.shapes.title
subtitle = slide.placeholders[1]
title.text = "Ariella Ferrera: A Glimpse into the Life of an Instagram Star"
subtitle.text = "Presented by: Your Name"

# Slide 2 to Slide 9
slides_content = [
    ("Introduction", ["Name: Ariella Ferrera", "Birthdate: January 15, 1979", "Age: 44 years",
                     "Birthplace: Colombia", "Profession: Instagram Star", "Zodiac Sign: Capricorn"]),
    ("Ariella Ferrera's Biography", ["Instagram star, model, and adult actress.",
                                    "Worked with prominent companies like Brazzers, Mile High, and Digital Playground.",
                                    "1.4 million followers on ariellaferreraofficial account."]),
    ("Family Life of Ariella Ferrera", ["Adopted a rescue dog named Bella."]),
    ("Ariella Ferrera's Net Worth", ["Estimated net worth: $5 million (Forbes & Business Insider sources)."]),
    ("Ariella Ferrera's Career Success", ["Instagram Star: Primary source of income.",
                                         "Respected as a highly skilled professional.",
                                         "Notable financial gains and exciting opportunities."]),
    ("Income & Lifestyle", ["Income: Under review.", "Lives a low-key lifestyle in a private residence."]),
    ("Physical Measurements", ["Striking looks and dynamic personality.",
                              "Svelte physique, wonderful body proportions.",
                              "Unique charm enhanced by captivating eyes."]),
    ("Social Media Presence", ["Wide popularity across social media platforms.",
                              "Active engagement on Instagram, Twitter, and Facebook.",
                              "Shares updates on projects and ventures."]),
]

for title_text, content_list in slides_content:
    slide = prs.slides.add_slide(prs.slide_layouts[1])
    title = slide.shapes.title
    content_box = slide.placeholders[1]

    title.text = title_text
    content_box.text = content_list[0]
    for content in content_list[1:]:
        content_box.text += "\n" + content

# Slide 10: Fun Facts & Trivia
slide = prs.slides.add_slide(prs.slide_layouts[1])
title = slide.shapes.title
content_box = slide.placeholders[1]

title.text = "Fun Facts & Trivia"
content = content_box.text = "In June 2020, she posted a picture with MMA fighter Randy Couture."

# Save the PowerPoint presentation
prs.save("Ariella_Ferrera_Presentation.pptx")
