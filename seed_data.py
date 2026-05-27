"""
Seed script to populate the database with sample data.
Run with: python manage.py shell < seed_data.py
"""
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'grow_sale_site.settings')
django.setup()

from blog.models import BlogPost
from services.models import ServiceCategory

# ── Service Categories ──────────────────────────────────────────────
services_data = [
    {
        'name': 'Garment & Apparel Printing',
        'slug': 'garment-apparel-printing',
        'description': 'Premium screen printing on t-shirts, hoodies, uniforms, and custom apparel. We use plastisol and water-based inks for vibrant, long-lasting prints that withstand repeated washing. Perfect for brand merchandise, team uniforms, and promotional wear.',
        'resolution_dpi': '600 to 1200 DPI',
    },
    {
        'name': 'Industrial Screen Printing',
        'slug': 'industrial-screen-printing',
        'description': 'High-precision industrial printing for electronics, circuit boards, automotive components, and medical devices. Our state-of-the-art equipment delivers consistent results for large-volume production runs with tight tolerances.',
        'resolution_dpi': '800 to 1200 DPI',
    },
    {
        'name': 'Fabric & Textile Printing',
        'slug': 'fabric-textile-printing',
        'description': 'Specialized printing on silk, cotton, polyester, and blended fabrics. From fashion textiles to home furnishings, we deliver rich color reproduction and fine detail on any fabric type. Eco-friendly ink options available.',
        'resolution_dpi': '600 to 1000 DPI',
    },
    {
        'name': 'Signage & Banner Printing',
        'slug': 'signage-banner-printing',
        'description': 'Large-format screen printing for outdoor signage, vinyl banners, POS displays, and exhibition graphics. UV-resistant inks ensure your message stays bold and vibrant in any weather condition.',
        'resolution_dpi': '300 to 600 DPI',
    },
    {
        'name': 'Packaging & Label Printing',
        'slug': 'packaging-label-printing',
        'description': 'Custom packaging solutions including cardboard boxes, plastic containers, glass bottles, and product labels. We offer glossy, matte, and textured finish options to match your brand identity perfectly.',
        'resolution_dpi': '600 to 1200 DPI',
    },
    {
        'name': 'Promotional Products',
        'slug': 'promotional-products',
        'description': 'Screen printing on mugs, pens, bags, notebooks, keychains, and other promotional items. Ideal for corporate gifts, trade show giveaways, and brand awareness campaigns with durable, eye-catching prints.',
        'resolution_dpi': '400 to 800 DPI',
    },
]

for data in services_data:
    ServiceCategory.objects.get_or_create(
        slug=data['slug'],
        defaults=data
    )
print(f"✅ Created {ServiceCategory.objects.count()} service categories")


# ── Blog Posts ───────────────────────────────────────────────────────
blog_data = [
    {
        'title': 'Choosing Between 600 vs 1200 DPI for Silk Textiles',
        'slug': 'choosing-600-vs-1200-dpi-silk-textiles',
        'content': """<h2>Understanding DPI in Textile Printing</h2>
<p>When it comes to screen printing on silk textiles, the DPI (Dots Per Inch) you choose can make or break your final product. At Grow Sale Products, we've spent over 26 years perfecting the art of DPI selection for different fabric types.</p>

<h3>When to Choose 600 DPI</h3>
<p>600 DPI is ideal for designs with bold graphics, large text, and simple color blocks. It offers faster production times and is more cost-effective for bulk orders. If your design doesn't require fine detail work, 600 DPI delivers excellent results on silk with vibrant color saturation.</p>

<h3>When to Choose 1200 DPI</h3>
<p>For photographic reproductions, intricate patterns, or designs with subtle gradients, 1200 DPI is the gold standard. The higher resolution captures fine lines and delicate details that would be lost at lower resolutions. This is especially important for luxury fashion brands and high-end textile products.</p>

<h3>Our Recommendation</h3>
<p>We always recommend starting with a test print at both resolutions. Our team will work with you to find the perfect balance between quality, production speed, and budget for your specific project.</p>""",
        'status': 'published',
    },
    {
        'title': 'The Complete Guide to Screen Printing Ink Types',
        'slug': 'complete-guide-screen-printing-ink-types',
        'content': """<h2>A Deep Dive Into Screen Printing Inks</h2>
<p>The ink you choose is just as important as the printing technique itself. Different substrates and applications demand different ink formulations. Here's our comprehensive guide based on decades of industry experience.</p>

<h3>Plastisol Inks</h3>
<p>The most widely used ink in screen printing. Plastisol sits on top of the fabric rather than soaking in, creating vibrant, opaque prints. It's incredibly versatile, easy to work with, and produces consistent results. Perfect for dark garments and high-opacity requirements.</p>

<h3>Water-Based Inks</h3>
<p>These inks absorb into the fabric, creating a softer hand feel. They're more environmentally friendly and produce a vintage, worn-in look. Ideal for light-colored garments and fashion-forward brands seeking a premium feel.</p>

<h3>UV-Curable Inks</h3>
<p>Used primarily for industrial applications, UV inks cure instantly under ultraviolet light. They offer excellent adhesion to non-porous substrates like plastics, glass, and metals. Essential for outdoor signage and product marking.</p>

<h3>Discharge Inks</h3>
<p>These specialized inks remove the existing dye from fabric and replace it with a new color. The result is an incredibly soft print that feels like it's part of the fabric itself. Premium choice for high-end fashion and retail brands.</p>""",
        'status': 'published',
    },
    {
        'title': '5 Common Screen Printing Mistakes and How to Avoid Them',
        'slug': '5-common-screen-printing-mistakes-avoid',
        'content': """<h2>Learn From the Experts</h2>
<p>After completing over 10,000 projects, we've seen every mistake in the book. Here are the five most common pitfalls and how to ensure your print project goes smoothly.</p>

<h3>1. Incorrect Mesh Count Selection</h3>
<p>Using too fine a mesh for heavy ink deposits or too coarse a mesh for detailed work is a recipe for disaster. The mesh count should match your design complexity and ink type. We carefully select the optimal mesh for every project.</p>

<h3>2. Poor Image Resolution</h3>
<p>Submitting low-resolution artwork is the number one cause of disappointing results. Always provide vector files (AI, EPS, SVG) or high-resolution rasters (minimum 300 DPI at print size). Our design team can help prepare your files if needed.</p>

<h3>3. Skipping the Test Print</h3>
<p>Never go straight to a full production run without a proof print. Colors can look different on screen versus on fabric. A test print catches issues before they become expensive problems.</p>

<h3>4. Ignoring Fabric Pre-Treatment</h3>
<p>Different fabrics require different preparation. Moisture, surface contaminants, or improper tension can all affect print quality. Our facility maintains strict quality control procedures for fabric preparation.</p>

<h3>5. Rushing the Curing Process</h3>
<p>Under-cured ink will crack, peel, or wash out. Over-cured ink can scorch the fabric. We use infrared temperature monitoring to ensure every print is cured to perfection.</p>""",
        'status': 'published',
    },
]

for data in blog_data:
    BlogPost.objects.get_or_create(
        slug=data['slug'],
        defaults=data
    )
print(f"✅ Created {BlogPost.objects.count()} blog posts")

print("\n🎉 Database seeded successfully!")
