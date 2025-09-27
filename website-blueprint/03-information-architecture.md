# Step 3: Information Architecture (Sitemap)

## Complete Website Structure

```
Home
├── Services
│   ├── Residential Lighting
│   │   ├── Custom Design Process
│   │   ├── Installation Services
│   │   ├── Maintenance & Support
│   │   └── Removal & Storage
│   ├── Commercial Lighting
│   │   ├── Retail & Storefront
│   │   ├── Office Buildings
│   │   ├── Hotels & Hospitality
│   │   └── Commercial Case Studies
│   ├── Community & HOA Lighting
│   │   ├── Entrance & Common Areas
│   │   ├── Community-wide Programs
│   │   └── HOA Case Studies
│   └── Special Event Lighting
│       ├── Weddings & Celebrations
│       ├── Corporate Events
│       └── Event Gallery
├── Gallery
│   ├── Residential Projects
│   │   ├── Traditional Homes
│   │   ├── Modern & Contemporary
│   │   ├── Estates & Large Properties
│   │   └── Before & After
│   ├── Commercial Projects
│   │   ├── Retail & Restaurants
│   │   ├── Office Buildings
│   │   ├── Hotels & Venues
│   │   └── Before & After
│   ├── Community Projects
│   │   ├── Neighborhood Entrances
│   │   ├── Clubhouses & Amenities
│   │   ├── Street Displays
│   │   └── Before & After
│   └── Featured Projects (Spotlight gallery)
├── Our Process
│   ├── Design Consultation
│   ├── Custom Planning
│   ├── Professional Installation
│   ├── Proactive Maintenance
│   ├── Post-Season Removal
│   └── Optional Storage Program
├── Pricing
│   ├── Residential Pricing Guide
│   │   ├── Factors That Affect Pricing
│   │   ├── Package Options
│   │   └── Custom Quote Process
│   ├── Commercial Pricing Guide
│   │   ├── Commercial Factors
│   │   ├── ROI Calculator
│   │   └── Multi-Year Contracts
│   ├── Instant Estimator Tool
│   └── Request Custom Quote
├── About Us
│   ├── Our Story
│   ├── Our Team
│   │   ├── Design Team
│   │   ├── Installation Experts
│   │   └── Support Staff
│   ├── Our Standards
│   │   ├── Quality Materials
│   │   ├── Installation Excellence
│   │   └── Safety Protocols
│   ├── Certifications & Insurance
│   └── Careers
├── Reviews & Testimonials
│   ├── Residential Client Stories
│   ├── Commercial Client Stories
│   ├── Video Testimonials
│   └── Leave a Review
├── FAQs
│   ├── General Questions
│   ├── Design Process
│   ├── Installation & Safety
│   ├── Maintenance & Support
│   ├── Removal & Storage
│   └── Pricing & Packages
├── Blog
│   ├── Design Inspiration
│   ├── Lighting Trends
│   ├── Project Spotlights
│   ├── Holiday Entertaining
│   ├── Commercial Insights
│   └── Company News
├── Service Areas
│   ├── Primary Service Region
│   │   ├── [City/Area 1]
│   │   ├── [City/Area 2]
│   │   └── [Additional Cities/Areas]
│   ├── Extended Service Region
│   │   ├── [City/Area 1]
│   │   ├── [City/Area 2]
│   │   └── [Additional Cities/Areas]
│   └── Service Area Map
└── Contact & Booking
    ├── Schedule Consultation
    ├── Request Quote
    ├── Customer Support
    └── Contact Information
```

## Seasonal Elements & Special Features

### Global Seasonal Banner
- **Position**: Sticky banner at top of all pages
- **Content**: "Now Booking for 2025 Holiday Season" with countdown to installation start dates
- **CTA**: "Reserve Your Installation Date" button
- **Behavior**: Dismissible but reappears after 3 days if not converted
- **Seasonal Variation**: Updates automatically based on current date:
  - Jan-Mar: "Early Booking Special: Save 15% on 2025 Holiday Lighting"
  - Apr-Jul: "2025 Holiday Lighting Design Consultations Now Available"
  - Aug-Oct: "Limited Installation Slots Remaining for 2025 Season"
  - Nov-Dec: "Now Booking for Last-Minute 2025 Installations"
  - Dec 26-31: "Reserve Your Spot for 2026 Holiday Season"

### Homepage Seasonal Modules
- **Hero Section**: Updates seasonally with current-season photography
- **Availability Calendar**: Shows available installation dates (dynamically updated)
- **Seasonal Promotions**: Dedicated section that updates based on time of year
- **Countdown Timer**: Days remaining until full booking (creates urgency)

### Service Page Seasonal Elements
- **Seasonal Package Highlights**: Featured packages based on current date
- **Installation Calendar**: Visual calendar showing available dates
- **Weather-Triggered Content**: Special content for snow events or severe weather
- **Seasonal FAQ Expansion**: Additional FAQs appear during peak season

### Gallery Seasonal Features
- **Current Projects**: Live feed of this season's installations (Nov-Dec)
- **Design Preview Tool**: Available Jan-Oct for next season planning
- **Seasonal Filtering**: Filter gallery by season/year
- **New Installation Badges**: Highlight newly completed projects

### Blog & Content Seasonal Strategy
- **Content Calendar**: Predetermined seasonal content that publishes automatically
- **Seasonal Guides**: Downloadable PDFs with seasonal tips and ideas
- **Holiday Entertaining Series**: Special content series during Nov-Dec
- **Year in Review**: Annual gallery of best projects (publishes each January)

## Navigation Structure

### Primary Navigation
- **Main Menu Items**: Home, Services, Gallery, Process, Pricing, Contact
- **Behavior**: Sticky on scroll, transparent on homepage hero
- **Mobile**: Hamburger menu with animated expansion
- **Dropdown Style**: Clean mega-menu for Services and Gallery sections

### Secondary Navigation
- **Location**: Top right above main navigation
- **Items**: About Us, Reviews, FAQs, Blog, Service Areas
- **Style**: Smaller text, separated from main navigation

### Utility Navigation
- **Location**: Far right of secondary navigation
- **Items**: Client Login, Support, Phone Number
- **Style**: Emphasized phone number with icon

### Footer Navigation
- **Primary Sections**: Mirrors main navigation categories
- **Secondary Links**: Privacy Policy, Terms of Service, Accessibility Statement
- **Contact Information**: Address, phone, email, hours
- **Social Media**: Subtle icon links to all platforms
- **Newsletter Signup**: Simple email capture with seasonal promotion

### Mobile-Specific Navigation
- **Bottom Action Bar**: Quick access to Call, Quote, Book buttons
- **Simplified Menu Structure**: Condensed version of desktop navigation
- **Location Detection**: Automatically shows nearest service area information

## User Journeys & Conversion Paths

### Primary Journey: Residential Client
1. Homepage → Gallery → Residential Projects
2. Residential Projects → Service Details
3. Service Details → Pricing Guide
4. Pricing Guide → Instant Estimator
5. Instant Estimator → Schedule Consultation

### Secondary Journey: Commercial Client
1. Homepage → Commercial Services
2. Commercial Services → Commercial Case Studies
3. Commercial Case Studies → Commercial Pricing
4. Commercial Pricing → ROI Calculator
5. ROI Calculator → Request Custom Quote

### Tertiary Journey: Returning Client
1. Homepage → Client Login
2. Client Login → Previous Installation Details
3. Previous Installation Details → Renewal Options
4. Renewal Options → Confirm Booking

### Micro-Conversions
- Newsletter signup
- Gallery browsing (3+ minutes)
- Blog article completion
- Video testimonial views
- Before/after comparison interactions

## Technical Sitemap Specifications

### URL Structure
- Use clean, hierarchical URLs (e.g., `/services/residential/custom-design/`)
- Include target keywords in URLs
- Keep URLs under 60 characters
- Use hyphens as word separators
- Avoid URL parameters when possible

### Canonical Tags
- Implement canonical tags on all pages
- Address pagination and filtering variations
- Handle seasonal duplicate content appropriately

### XML Sitemap
- Generate dynamic XML sitemap
- Include lastmod dates
- Set appropriate priority values
- Submit to Google Search Console

### Internal Linking Structure
- Hub and spoke model centered on service pages
- Cross-link related services and gallery examples
- Implement breadcrumb navigation
- Use descriptive anchor text for internal links

### Structured Data Implementation
- LocalBusiness schema for company information
- Service schema for service pages
- FAQPage schema for FAQ sections
- Review schema for testimonials
- BreadcrumbList schema for navigation paths