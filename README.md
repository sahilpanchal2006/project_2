# 🖨️ Grow Sale — Premium Screen Printing Services

> A professional Django web application for a screen printing business — showcasing services, products, quote requests, and industry blog posts.

---

## 🌟 Features

### 🏠 Home Page
- Animated hero section with company stats (Years, Projects, Clients, Max DPI)
- **Fully clickable service cards** — click anywhere (icon, text, image) to navigate
- **Fully clickable product cards** — click anywhere including product image to get a quote
- **Fully clickable blog cards** — click anywhere including featured image to read the post
- Animated counters for key statistics
- Featured products showcase with category badges
- Industry blog preview section
- Call-to-action banners with quote and phone links

### 🛠️ Services
- Dynamic service listing page with all printing categories
- Service cards with resolution DPI, quality badges, fast delivery tags
- Each card fully clickable — links directly to the quote form with material pre-selected
- Smooth scroll anchor linking (`#service-slug`) for direct service navigation
- "How We Work" 4-step process section

### 📦 Products
- Product catalog with category filtering
- Product images with hover zoom effect
- Category badge overlays on product images
- Featured products highlighted on the homepage
- Supports: Fabric, Silk, Plastics, Cardboard categories

### 📋 Quote Request System
- Multi-field quote form with:
  - Client name, email, phone
  - Material selection (Fabric, Silk, Plastics, Cardboard)
  - Finish type (Glossy, Matte, Textured)
  - Design file upload (PDF, AI, PSD, PNG, JPG)
  - Project details message
- URL parameter pre-filling (`?material=fabric`) from service/product links
- All submissions stored in the Django admin panel

### 📝 Blog
- Blog post listing with featured images, dates, and excerpts
- Individual blog detail pages with full content
- Draft / Published status system
- Admin-managed blog posts with rich content support

### ⚙️ Django Admin Panel
- Full CRUD for: Services, Products, Quotes, Blog Posts
- Quote requests viewable and manageable from `/admin/`
- Image upload support for products and blog posts

### 🎨 Design & UI
- Modern, premium dark/light design system
- Custom CSS design tokens (colors, spacing, typography)
- Google Fonts — **Outfit** typeface throughout
- Smooth reveal animations on scroll
- Hover effects, micro-animations, and card lift effects
- Glassmorphism elements and gradient accents
- Fully responsive — mobile, tablet, and desktop
- SEO-ready with meta descriptions and semantic HTML

---

## 🧰 Tech Stack

| Layer | Technology |
|---|---|
| **Backend** | Python 3.x, Django 4.2 |
| **Database** | SQLite (development) |
| **Frontend** | HTML5, Vanilla CSS, JavaScript |
| **CSS Framework** | Tailwind CSS (via CDN) |
| **Forms** | django-crispy-forms + crispy-tailwind |
| **Images** | Pillow |
| **Font** | Google Fonts — Outfit |

---

## 📁 Project Structure

```
grow_sale/
├── blog/                   # Blog app (posts, listing, detail)
│   ├── models.py
│   ├── views.py
│   └── urls.py
├── services/               # Services, Products & Quote app
│   ├── models.py           # ServiceCategory, Quote, Product
│   ├── views.py
│   ├── forms.py            # Quote request form
│   └── templatetags/       # Custom template filters
├── grow_sale_site/         # Project settings & URLs
│   ├── settings.py
│   ├── urls.py
│   └── context_processors.py
├── templates/              # All HTML templates
│   ├── base.html
│   ├── home.html
│   ├── blog/
│   └── services/
├── static/
│   ├── css/styles.css      # Global design system
│   └── js/main.js          # Animations & interactions
├── requirements.txt
├── manage.py
└── seed_data.py            # Demo data seeder script
```

---

## 🚀 Getting Started

### Prerequisites
- Python 3.10+
- pip

### 1. Clone the repository
```bash
git clone https://github.com/sahilpanchal2006/project_2.git
cd project_2
```

### 2. Create & activate virtual environment
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python -m venv venv
source venv/bin/activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Apply database migrations
```bash
python manage.py migrate
```

### 5. Create a superuser (for admin access)
```bash
python manage.py createsuperuser
```

### 6. (Optional) Seed demo data
```bash
python seed_data.py
```

### 7. Run the development server
```bash
python manage.py runserver
```

Visit: **http://127.0.0.1:8000/**
Admin: **http://127.0.0.1:8000/admin/**

---

## 📸 Pages Overview

| Page | URL |
|---|---|
| Home | `/` |
| Services | `/services/` |
| Products | `/products/` |
| Quote Form | `/quote/` |
| Blog List | `/blog/` |
| Blog Post | `/blog/<slug>/` |
| Admin Panel | `/admin/` |

---

## 🔒 Important Notes

> ⚠️ Before deploying to production:
> - Change `SECRET_KEY` in `settings.py` to a strong random key
> - Set `DEBUG = False`
> - Configure a production database (PostgreSQL recommended)
> - Set up proper `ALLOWED_HOSTS`
> - Use environment variables for sensitive settings

---

## 📄 License

This project is for educational and business use by **Grow Sale Products**.

---

<p align="center">Made with ❤️ using Django</p>
