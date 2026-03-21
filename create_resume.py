from reportlab.pdfgen import canvas

c = canvas.Canvas("sample_resume.pdf")
c.setFont("Helvetica-Bold", 16)
c.drawString(100, 800, "Jane Doe")
c.setFont("Helvetica", 12)
c.drawString(100, 780, "Frontend Engineer")

c.setFont("Helvetica-Bold", 14)
c.drawString(100, 740, "Professional Summary")
c.setFont("Helvetica", 12)
c.drawString(100, 720, "Passionate developer with 3 years of experience building modern web applications.")

c.setFont("Helvetica-Bold", 14)
c.drawString(100, 680, "Technical Skills")
c.setFont("Helvetica", 12)
c.drawString(100, 660, "Languages: JavaScript, HTML, CSS, Python")
c.drawString(100, 640, "Frameworks/Libraries: React")
c.drawString(100, 620, "Tools: Git")

c.setFont("Helvetica-Bold", 14)
c.drawString(100, 580, "Experience")
c.setFont("Helvetica-Bold", 12)
c.drawString(100, 560, "Software Developer")
c.setFont("Helvetica", 12)
c.drawString(100, 540, "Built and maintained web apps using React and JavaScript.")
c.drawString(100, 520, "Wrote backend endpoints in Python.")
c.save()

print("sample_resume.pdf created successfully!")
