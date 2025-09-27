# Step 5: Key Components & Reusable Modules

## Global Header

### Desktop Header
```
┌─────────────────────────────────────────────────────────┐
│ [Secondary Nav]  About | Reviews | FAQs | Blog | Areas  │
│                                 [Phone] (555) 123-4567  │
├─────────────────────────────────────────────────────────┤
│ [Logo]  Home  Services▾  Gallery▾  Process  Pricing     │
│                                         [Book Consult]  │
└─────────────────────────────────────────────────────────┘
```

#### Header Specifications
- **Height**: 120px total (40px secondary nav, 80px main nav)
- **Behavior**: Sticky on scroll with smooth animation
- **Transparency**: Transparent on homepage hero, solid white elsewhere
- **Logo**: SVG format with dark/light versions for different backgrounds
- **Dropdown Menus**: Clean mega-menu style with featured images
- **CTA Button**: Gold background, navy text, subtle hover animation
- **Phone Number**: Emphasized with icon, click-to-call enabled
- **States**:
  - Default: Full height, transparent on homepage
  - Scrolled: Condensed height (80px), white background with shadow
  - Mobile: Hamburger menu, logo centered

### Mobile Header
```
┌─────────────────────────────────────────────────────────┐
│                [Logo]                      [Menu] [Call] │
└─────────────────────────────────────────────────────────┘
```

#### Mobile Header Specifications
- **Height**: 60px
- **Logo**: Centered, slightly reduced size
- **Menu**: Hamburger icon with smooth animation to "X" when open
- **Call Button**: Phone icon with direct click-to-call
- **Expanded Menu**: Full-screen overlay with animated entrance
- **Navigation Structure**: Accordion-style nested menus

## Global Footer

### Desktop Footer
```
┌─────────────────────────────────────────────────────────┐
│ [Logo]                                                  │
│                                                         │
│ [Contact Info]    [Quick Links]    [Service Areas]      │
│ Address           Services         Primary Regions      │
│ Phone             Gallery          Extended Regions     │
│ Email             Process          Service Map          │
│ Hours             Pricing                               │
│                   About                                 │
│                   FAQs                                  │
│                                                         │
│ [Newsletter Signup]                                     │
│ Stay Illuminated: Design tips and early booking access  │
│ [Email Field]                      [Subscribe]          │
│                                                         │
│ [Social Icons]                                          │
│                                                         │
│ © 2025 Premium Holiday Lighting | Privacy | Terms       │
└─────────────────────────────────────────────────────────┘
```

#### Footer Specifications
- **Background**: Deep navy (#0A2342)
- **Text Color**: Winter white (#F7F9FC)
- **Logo**: White version of logo
- **Column Structure**: 3-4 columns on desktop
- **Newsletter**: Simple email capture with privacy note
- **Social Icons**: Gold icons with hover animation
- **Copyright**: Dynamic year with legal links
- **Accessibility**: ARIA labels on all interactive elements

### Mobile Footer
- **Layout**: Stacked sections with accordion-style expandable categories
- **Newsletter**: Full-width input and button
- **Social Icons**: Centered row
- **Legal**: Stacked links with adequate tap targets

## Button System

### Primary Button
```
┌─────────────────────────┐
│     Button Text         │
└─────────────────────────┘
```

#### Primary Button Specifications
- **Background**: Gold (#D4AF37)
- **Text**: Navy (#0A2342), Montserrat Medium, 16px, uppercase, 0.5px letter spacing
- **Padding**: 16px 32px (horizontal padding scales with text length)
- **Border**: None
- **Border Radius**: 2px
- **Shadow**: Subtle drop shadow (0px 2px 4px rgba(0,0,0,0.1))
- **States**:
  - Hover: Darken background by 10%, slight shadow increase
  - Active: Darken background by 15%, shadow inset
  - Focus: Gold outline with 2px offset
  - Disabled: 50% opacity, no hover effects

### Secondary Button
```
┌─────────────────────────┐
│     Button Text         │
└─────────────────────────┘
```

#### Secondary Button Specifications
- **Background**: Transparent
- **Text**: Gold (#D4AF37), Montserrat Medium, 16px, uppercase, 0.5px letter spacing
- **Border**: 1px solid Gold (#D4AF37)
- **Padding**: 15px 31px (accounting for border)
- **Border Radius**: 2px
- **States**:
  - Hover: Light gold background (rgba(212,175,55,0.1))
  - Active: Slightly darker gold background (rgba(212,175,55,0.2))
  - Focus: Gold outline with 2px offset
  - Disabled: 50% opacity, no hover effects

### Tertiary Button / Text Link
```
Button Text →
```

#### Tertiary Button Specifications
- **Background**: None
- **Text**: Gold (#D4AF37), Montserrat Medium, 16px, uppercase, 0.5px letter spacing
- **Underline**: 1px bottom border on hover only
- **Icon**: Right arrow (→) with 8px spacing from text
- **States**:
  - Hover: Underline appears, arrow moves right 4px
  - Active: Darker gold (#B8962F)
  - Focus: Dotted outline
  - Disabled: 50% opacity, no hover effects

### Button Sizes
- **Small**: 32px height, 12px horizontal padding, 14px font
- **Medium** (Default): 48px height, 16px horizontal padding, 16px font
- **Large**: 56px height, 24px horizontal padding, 18px font
- **Full Width**: 100% container width (mobile-specific)

## Quote Request Form

### Desktop Layout
```
┌─────────────────────────────────────────────────────────┐
│                                                         │
│  [Form Headline]                                        │
│  Request Your Custom Lighting Design                    │
│                                                         │
│  [Form Description]                                     │
│  Complete the form below for a personalized quote       │
│  and design consultation.                               │
│                                                         │
│  ┌─────────────────┐  ┌─────────────────┐              │
│  │ First Name      │  │ Last Name       │              │
│  └─────────────────┘  └─────────────────┘              │
│                                                         │
│  ┌─────────────────────────────────────────────────────┐│
│  │ Email Address                                       ││
│  └─────────────────────────────────────────────────────┘│
│                                                         │
│  ┌─────────────────┐  ┌─────────────────┐              │
│  │ Phone Number    │  │ Zip Code        │              │
│  └─────────────────┘  └─────────────────┘              │
│                                                         │
│  ┌─────────────────────────────────────────────────────┐│
│  │ Property Type ▾                                     ││
│  └─────────────────────────────────────────────────────┘│
│                                                         │
│  ┌─────────────────────────────────────────────────────┐│
│  │ Preferred Installation Timeframe ▾                  ││
│  └─────────────────────────────────────────────────────┘│
│                                                         │
│  ┌─────────────────────────────────────────────────────┐│
│  │ Additional Notes (Optional)                         ││
│  │                                                     ││
│  │                                                     ││
│  └─────────────────────────────────────────────────────┘│
│                                                         │
│  □ I agree to receive communications about my project   │
│                                                         │
│  [Submit Button]                                        │
│  Request Consultation                                   │
│                                                         │
└─────────────────────────────────────────────────────────┘
```

### Form Specifications
- **Background**: White with subtle border or light gray background
- **Fields**: Floating labels that animate on focus
- **Validation**: Inline validation with helpful error messages
- **Dropdown Menus**: Custom styled with elegant animation
- **Submit Button**: Primary button style, full width on mobile
- **Success State**: Animated confirmation message
- **Integration**: Connects to CRM with lead tagging
- **Accessibility**: ARIA labels and keyboard navigation support
- **Mobile Adaptation**: Stacked fields, larger touch targets

### Form Field Types
1. **Text Input**: First Name, Last Name
2. **Email Input**: Email Address (with validation)
3. **Phone Input**: Phone Number (with formatting)
4. **Select Dropdown**: Property Type, Installation Timeframe
5. **Textarea**: Additional Notes
6. **Checkbox**: Marketing consent
7. **Hidden Fields**: UTM parameters, referral source

## Pricing Estimator Tool

### Desktop Layout
```
┌─────────────────────────────────────────────────────────┐
│                                                         │
│  [Tool Headline]                                        │
│  Instant Holiday Lighting Estimate                      │
│                                                         │
│  [Tool Description]                                     │
│  Get an approximate price range based on your property  │
│  details. For an exact quote, schedule a consultation.  │
│                                                         │
│  ┌─────────────────────────────────────────────────────┐│
│  │ Step 1: Property Type ▾                             ││
│  └─────────────────────────────────────────────────────┘│
│                                                         │
│  ┌─────────────────────────────────────────────────────┐│
│  │ Step 2: Approximate Square Footage ▾                ││
│  └─────────────────────────────────────────────────────┘│
│                                                         │
│  ┌─────────────────────────────────────────────────────┐│
│  │ Step 3: Desired Coverage Level ▾                    ││
│  └─────────────────────────────────────────────────────┘│
│                                                         │
│  ┌─────────────────────────────────────────────────────┐│
│  │ Step 4: Additional Features                          ││
│  │                                                     ││
│  │ □ Roofline Lighting                                 ││
│  │ □ Tree Lighting                                     ││
│  │ □ Pathway Lighting                                  ││
│  │ □ Custom Features                                   ││
│  │ □ Storage Program                                   ││
│  └─────────────────────────────────────────────────────┘│
│                                                         │
│  [Calculate Button]                                     │
│                                                         │
│  ┌─────────────────────────────────────────────────────┐│
│  │ [Results Section - Initially Hidden]                ││
│  │                                                     ││
│  │ Estimated Price Range:                              ││
│  │ $X,XXX - $X,XXX                                     ││
│  │                                                     ││
│  │ This estimate includes:                             ││
│  │ • Professional design consultation                  ││
│  │ • Custom installation plan                          ││
│  │ • Premium commercial-grade lights                   ││
│  │ • Professional installation                         ││
│  │ • Maintenance throughout season                     ││
│  │ • Complete removal                                  ││
│  │                                                     ││
│  │ [Schedule Consultation Button]                      ││
│  │                                                     ││
│  │ [Refine Estimate Button]                            ││
│  └─────────────────────────────────────────────────────┘│
│                                                         │
└─────────────────────────────────────────────────────────┘
```

### Estimator Specifications
- **Interface**: Step-by-step wizard with progress indication
- **Calculation Logic**: Backend formula based on property size, features, and coverage
- **Results Display**: Animated reveal with price range and included services
- **Visual Elements**: Simple illustrations for coverage levels
- **Mobile Adaptation**: Full-width controls, simplified interface
- **Integration**: Saves estimate to user session for reference in consultation
- **Analytics**: Tracks completion rate and average estimates

### Estimator Logic Parameters
1. **Base Pricing Factors**:
   - Property Type: Residential (1x), Commercial (1.5x), Community (2x)
   - Square Footage: <2,500 (1x), 2,500-5,000 (1.5x), 5,000-10,000 (2x), >10,000 (2.5x+)
   - Coverage Level: Accent (1x), Standard (1.5x), Premium (2x), Ultimate (2.5x)

2. **Additional Features Multipliers**:
   - Roofline Lighting: +15-25% depending on complexity
   - Tree Lighting: +10-20% per tree category
   - Pathway Lighting: +10-15% depending on length
   - Custom Features: +15-30% depending on complexity
   - Storage Program: +10% with multi-year discount options

3. **Result Calculation**:
   - Base Price = (Base Rate × Property Type × Square Footage × Coverage Level)
   - Feature Adjustments = Sum of selected feature percentages
   - Final Range = Base Price ± 15% to account for property-specific factors

## Gallery & Portfolio System

### Desktop Layout
```
┌─────────────────────────────────────────────────────────┐
│                                                         │
│  [Gallery Headline]                                     │
│  Our Portfolio                                          │
│                                                         │
│  [Filter Navigation]                                    │
│  All | Residential | Commercial | Community | Featured  │
│                                                         │
│  [Secondary Filters]                                    │
│  Style: All ▾    Property Type: All ▾    Year: All ▾   │
│                                                         │
│  ┌─────┬─────┬─────┐                                    │
│  │     │     │     │                                    │
│  │  1  │  2  │  3  │                                    │
│  │     │     │     │                                    │
│  ├─────┼─────┼─────┤                                    │
│  │     │     │     │                                    │
│  │  4  │  5  │  6  │                                    │
│  │     │     │     │                                    │
│  ├─────┼─────┼─────┤                                    │
│  │     │     │     │                                    │
│  │  7  │  8  │  9  │                                    │
│  │     │     │     │                                    │
│  └─────┴─────┴─────┘                                    │
│                                                         │
│  [Load More]                                            │
│                                                         │
└─────────────────────────────────────────────────────────┘
```

### Gallery Item Detail View
```
┌─────────────────────────────────────────────────────────┐
│                                                         │
│  [Close Button]                                         │
│                                                         │
│  ┌─────────────────────┐  ┌─────────────────────────────┐│
│  │                     │  │                             ││
│  │                     │  │ [Project Name]              ││
│  │                     │  │ Tudor Estate, Lake Forest   ││
│  │                     │  │                             ││
│  │                     │  │ [Project Details]           ││
│  │   Main Image        │  │ Property Type: Residential  ││
│  │                     │  │ Style: Traditional          ││
│  │                     │  │ Year: 2024                  ││
│  │                     │  │                             ││
│  │                     │  │ [Project Description]       ││
│  │                     │  │ Custom architectural        ││
│  │                     │  │ lighting highlighting the   ││
│  │                     │  │ Tudor features with warm    ││
│  │                     │  │ white lights and custom     ││
│  │                     │  │ accent elements.            ││
│  │                     │  │                             ││
│  └─────────────────────┘  │ [Similar Projects Button]   ││
│                           │                             ││
│  ┌─────┬─────┬─────┬─────┐│ [Request Similar Design]    ││
│  │ T1  │ T2  │ T3  │ T4  ││                             ││
│  └─────┴─────┴─────┴─────┘│                             ││
│                           └─────────────────────────────┘│
│                                                         │
└─────────────────────────────────────────────────────────┘
```

### Gallery Specifications
- **Layout Options**: Grid (default), Masonry, or List view
- **Filtering System**: Primary category tabs with secondary dropdown filters
- **Image Loading**: Lazy loading with blur-up preview
- **Hover Effect**: Subtle zoom with property name overlay
- **Detail View**: Lightbox with project details and thumbnail navigation
- **Image Quality**: High-resolution with optimized loading
- **Mobile Adaptation**: 2-column grid, simplified filters, swipe navigation
- **Accessibility**: Alt text for all images, keyboard navigation support

### Gallery Metadata Structure
1. **Basic Metadata**:
   - Project Name
   - Location
   - Year Completed
   - Property Type
   - Style Category

2. **Extended Metadata**:
   - Services Provided
   - Special Features
   - Client Testimonial (if available)
   - Before/After Available (boolean)
   - Featured Project (boolean)

3. **Technical Metadata**:
   - Image Dimensions
   - Photographer Credit
   - Alt Text
   - Related Projects

## Reviews & Testimonials System

### Desktop Layout
```
┌─────────────────────────────────────────────────────────┐
│                                                         │
│  [Section Headline]                                     │
│  Client Experiences                                     │
│                                                         │
│  [Filter Options]                                       │
│  All | Residential | Commercial | Community             │
│                                                         │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐      │
│  │             │  │             │  │             │      │
│  │ ★★★★★       │  │ ★★★★★       │  │ ★★★★★       │      │
│  │             │  │             │  │             │      │
│  │ "Quote text │  │ "Quote text │  │ "Quote text │      │
│  │ goes here"  │  │ goes here"  │  │ goes here"  │      │
│  │             │  │             │  │             │      │
│  │ - Name      │  │ - Name      │  │ - Name      │      │
│  │   Location  │  │   Location  │  │   Location  │      │
│  │             │  │             │  │             │      │
│  └─────────────┘  └─────────────┘  └─────────────┘      │
│                                                         │
│  [Load More]                                            │
│                                                         │
│  [Leave a Review Button]                                │
│                                                         │
└─────────────────────────────────────────────────────────┘
```

### Video Testimonial Layout
```
┌─────────────────────────────────────────────────────────┐
│                                                         │
│  [Section Headline]                                     │
│  Client Stories                                         │
│                                                         │
│  ┌─────────────────────────────────────────────────────┐│
│  │                                                     ││
│  │                                                     ││
│  │                                                     ││
│  │              [Featured Video Player]                ││
│  │                                                     ││
│  │                                                     ││
│  │                                                     ││
│  └─────────────────────────────────────────────────────┘│
│                                                         │
│  ┌─────┬─────┬─────┬─────┐                              │
│  │ T1  │ T2  │ T3  │ T4  │                              │
│  └─────┴─────┴─────┴─────┘                              │
│                                                         │
└─────────────────────────────────────────────────────────┘
```

### Reviews Specifications
- **Data Sources**: Google Reviews, Houzz, direct testimonials
- **Filtering**: By service type, location, and rating
- **Display Options**: Card view, carousel, or featured highlight
- **Integration**: Embedded review widgets from third-party platforms
- **Submission Form**: Simple form for clients to submit reviews
- **Moderation**: Admin approval workflow for direct submissions
- **Schema Markup**: Structured data for rich search results
- **Video Integration**: Embedded video testimonials with transcript

### Review Collection Process
1. **Automated Requests**: Triggered email 2 weeks after project completion
2. **Review Platforms**: Direct links to Google, Houzz, and direct submission
3. **Incentives**: Photo feature opportunity for detailed reviews
4. **Follow-up**: Gentle reminder if no review after 30 days
5. **Thank You**: Automated thank you note when review is detected

## Availability Calendar

### Desktop Layout
```
┌─────────────────────────────────────────────────────────┐
│                                                         │
│  [Calendar Headline]                                    │
│  Installation Availability                              │
│                                                         │
│  [Month Navigation]                                     │
│  < October 2025 >                                       │
│                                                         │
│  ┌─────┬─────┬─────┬─────┬─────┬─────┬─────┐            │
│  │ Sun │ Mon │ Tue │ Wed │ Thu │ Fri │ Sat │            │
│  ├─────┼─────┼─────┼─────┼─────┼─────┼─────┤            │
│  │     │     │  1  │  2  │  3  │  4  │  5  │            │
│  │     │     │ 🟢  │ 🟢  │ 🟡  │ 🔴  │ 🔴  │            │
│  ├─────┼─────┼─────┼─────┼─────┼─────┼─────┤            │
│  │  6  │  7  │  8  │  9  │ 10  │ 11  │ 12  │            │
│  │ 🔴  │ 🟡  │ 🟡  │ 🟢  │ 🟢  │ 🔴  │ 🔴  │            │
│  ├─────┼─────┼─────┼─────┼─────┼─────┼─────┤            │
│  │ ... │ ... │ ... │ ... │ ... │ ... │ ... │            │
│  └─────┴─────┴─────┴─────┴─────┴─────┴─────┘            │
│                                                         │
│  [Legend]                                               │
│  🟢 Available  🟡 Limited Availability  🔴 Booked        │
│                                                         │
│  [Book Preferred Date]                                  │
│                                                         │
└─────────────────────────────────────────────────────────┘
```

### Calendar Specifications
- **Data Source**: Real-time availability from booking system
- **Color Coding**: Available, Limited Availability, Booked
- **Interaction**: Click date to see available time slots
- **Booking Flow**: Select date → Select time → Complete form
- **Restrictions**: Minimum lead time requirements
- **Special Dates**: Premium dates highlighted (weekends near holidays)
- **Mobile Adaptation**: List view option with date groupings
- **Integration**: Syncs with company scheduling system
- **Notifications**: Email confirmation and calendar invite

### Availability Logic
1. **Capacity Factors**:
   - Installation team availability
   - Equipment availability
   - Geographic zones (limit per area per day)
   - Installation complexity

2. **Booking Rules**:
   - Premium clients get priority booking
   - Minimum 2-week lead time (varies seasonally)
   - Weekend premium pricing
   - Rush installation fees for short notice

3. **Seasonal Adjustments**:
   - Early booking discounts (Jan-Jul)
   - Peak season limited availability (Oct-Nov)
   - Last-minute availability calendar (Nov-Dec)

## FAQ Accordion System

### Desktop Layout
```
┌─────────────────────────────────────────────────────────┐
│                                                         │
│  [FAQ Headline]                                         │
│  Frequently Asked Questions                             │
│                                                         │
│  [Category Navigation]                                  │
│  All | Design | Installation | Maintenance | Pricing    │
│                                                         │
│  ┌─────────────────────────────────────────────────────┐│
│  │ Q: What type of lighting do you use?              ▼ ││
│  └─────────────────────────────────────────────────────┘│
│  ┌─────────────────────────────────────────────────────┐│
│  │ A: We exclusively use commercial-grade LED lights    ││
│  │ with warm white color temperature (2700K-3000K).     ││
│  │ These professional-quality lights offer superior     ││
│  │ durability, energy efficiency, and consistent        ││
│  │ illumination compared to retail options.             ││
│  └─────────────────────────────────────────────────────┘│
│                                                         │
│  ┌─────────────────────────────────────────────────────┐│
│  │ Q: How far in advance should I book?              ▼ ││
│  └─────────────────────────────────────────────────────┘│
│                                                         │
│  ┌─────────────────────────────────────────────────────┐│
│  │ Q: Do you offer removal and storage?              ▼ ││
│  └─────────────────────────────────────────────────────┘│
│                                                         │
│  [More FAQs]                                            │
│                                                         │
│  [Ask a Question]                                       │
│                                                         │
└─────────────────────────────────────────────────────────┘
```

### FAQ Specifications
- **Structure**: Categorized accordion with smooth expand/collapse
- **Search**: Instant filtering as user types
- **Categories**: General, Design, Installation, Maintenance, Pricing
- **Behavior**: Only one question expanded at a time (configurable)
- **Animation**: Smooth height transition with subtle indicator rotation
- **Schema Markup**: FAQPage structured data
- **Related Content**: Links to relevant service pages within answers
- **Mobile Adaptation**: Full-width, touch-optimized accordions
- **Submission**: "Ask a Question" form for questions not covered

### FAQ Management
1. **Content Updates**:
   - Seasonal FAQ updates (pre-season, in-season, post-season)
   - Addition of new questions based on customer inquiries
   - Regular review and refinement of answers

2. **Organization**:
   - Primary categories with clear labels
   - Most common questions prioritized at top
   - Related questions grouped together
   - Clear, concise answers with links to more information

3. **Technical Implementation**:
   - Keyboard accessible (arrow navigation)
   - Screen reader optimized with ARIA attributes
   - Analytics tracking on most viewed/expanded questions
   - URL deep linking to specific questions

## Blog & Content System

### Article Layout
```
┌─────────────────────────────────────────────────────────┐
│                                                         │
│  [Breadcrumbs]                                          │
│  Home > Blog > Category > Article Title                 │
│                                                         │
│  [Article Header]                                       │
│  Article Title                                          │
│                                                         │
│  [Meta Information]                                     │
│  Category | Date | Author | 5 min read                  │
│                                                         │
│  [Featured Image]                                       │
│                                                         │
│  [Article Content]                                      │
│  Introduction paragraph...                              │
│                                                         │
│  [H2 Subheading]                                        │
│  Content paragraphs...                                  │
│                                                         │
│  [Image with Caption]                                   │
│                                                         │
│  [H2 Subheading]                                        │
│  Content paragraphs...                                  │
│                                                         │
│  [Call to Action]                                       │
│  Ready to transform your property?                      │
│  [Schedule Consultation]                                │
│                                                         │
│  [Author Bio]                                           │
│  About the author with photo                            │
│                                                         │
│  [Related Articles]                                     │
│  3 related article cards                                │
│                                                         │
│  [Comments/Discussion]                                  │
│  Optional commenting system                             │
│                                                         │
└─────────────────────────────────────────────────────────┘
```

### Blog Index Layout
```
┌─────────────────────────────────────────────────────────┐
│                                                         │
│  [Blog Header]                                          │
│  Design Insights & Inspiration                          │
│                                                         │
│  [Category Navigation]                                  │
│  All | Design | Trends | Projects | Guides | News       │
│                                                         │
│  [Featured Article]                                     │
│  Large card with image and excerpt                      │
│                                                         │
│  [Article Grid]                                         │
│  ┌─────────┐  ┌─────────┐  ┌─────────┐                  │
│  │ Image   │  │ Image   │  │ Image   │                  │
│  │         │  │         │  │         │                  │
│  │ Title   │  │ Title   │  │ Title   │                  │
│  │ Meta    │  │ Meta    │  │ Meta    │                  │
│  │ Excerpt │  │ Excerpt │  │ Excerpt │                  │
│  └─────────┘  └─────────┘  └─────────┘                  │
│                                                         │
│  [Pagination]                                           │
│  < 1 2 3 ... >                                          │
│                                                         │
│  [Subscribe]                                            │
│  Email signup for blog updates                          │
│                                                         │
└─────────────────────────────────────────────────────────┘
```

### Blog Specifications
- **Content Types**: Articles, Guides, Case Studies, News
- **Media Support**: Images, galleries, videos, downloadable PDFs
- **Categorization**: Primary categories with tags for filtering
- **Author Profiles**: Team member bios and headshots
- **Related Content**: Intelligent suggestion algorithm
- **Social Sharing**: Subtle sharing buttons with share counts
- **SEO Features**: Custom meta data, canonical URLs, schema markup
- **Mobile Adaptation**: Readable typography, optimized images
- **Analytics**: Content performance tracking with goals

### Content Management
1. **Editorial Calendar**:
   - Seasonal content planning
   - Evergreen article development
   - Trending topic coverage
   - Case study publication schedule

2. **Content Types**:
   - Design Inspiration (visual galleries with commentary)
   - Trend Analysis (industry insights and forecasts)
   - Project Spotlights (detailed case studies)
   - How-To Guides (educational content)
   - Company News (team updates, awards, events)

3. **Content Distribution**:
   - Email newsletter integration
   - Social media scheduling
   - Content syndication options
   - Internal linking strategy

## Service Area Map

### Desktop Layout
```
┌─────────────────────────────────────────────────────────┐
│                                                         │
│  [Map Headline]                                         │
│  Our Service Areas                                      │
│                                                         │
│  ┌─────────────────────────┐  ┌─────────────────────────┐│
│  │                         │  │                         ││
│  │                         │  │ Primary Service Areas:  ││
│  │                         │  │                         ││
│  │                         │  │ • North Shore           ││
│  │                         │  │   - Winnetka           ││
│  │      Interactive        │  │   - Lake Forest        ││
│  │         Map             │  │   - Highland Park      ││
│  │                         │  │                         ││
│  │                         │  │ • Northwest Suburbs     ││
│  │                         │  │   - Barrington         ││
│  │                         │  │   - Inverness          ││
│  │                         │  │   - South Barrington   ││
│  │                         │  │                         ││
│  └─────────────────────────┘  └─────────────────────────┘│
│                                                         │
│  [Zip Code Search]                                      │
│  Enter your zip code to check availability              │
│                                                         │
└─────────────────────────────────────────────────────────┘
```

### Map Specifications
- **Map Type**: Interactive with custom styling
- **Regions**: Color-coded service areas (primary, secondary, extended)
- **Interaction**: Hover/click regions for details
- **Search**: Zip code lookup functionality
- **Legend**: Clear explanation of service area types
- **Mobile Adaptation**: Simplified map with expandable area list
- **Integration**: Location-based content personalization
- **Technical**: SVG-based for performance or Google Maps API

### Service Area Logic
1. **Coverage Types**:
   - Primary: Full service area with standard pricing
   - Secondary: Service available with potential travel fee
   - Extended: Limited availability for premium projects

2. **Location Data Structure**:
   - Region name
   - List of cities/towns
   - Zip codes covered
   - Service limitations (if any)
   - Local showcase projects

3. **Personalization**:
   - Location detection (with permission)
   - Custom messaging based on user location
   - Local project examples prioritized in gallery