# Step 2: Visual Direction (Art Direction)

## Color Palette

### Primary Colors
- **Deep Navy**: #0A2342 - Used for primary text, headers, and key UI elements
- **Winter White**: #F7F9FC - Used for backgrounds and negative space
- **Gold Accent**: #D4AF37 - Used sparingly for highlights and call-to-action elements

### Secondary Colors
- **Charcoal**: #2D3142 - Used for secondary text and UI elements
- **Soft Silver**: #E0E2E6 - Used for borders, dividers, and subtle backgrounds
- **Midnight Blue**: #14395B - Used for hover states and secondary buttons

### Tertiary/Accent Colors
- **Evergreen**: #1D3C34 - Used for seasonal accents and secondary elements
- **Warm Glow**: #E8C872 - Used to represent warm white lighting in graphics
- **Deep Burgundy**: #5E1914 - Used very sparingly for seasonal contrast elements

## Typography

### Primary Font Family: Playfair Display
- **Headings**: Playfair Display, 700 weight (Bold)
  - H1: 48px/56px, letter-spacing: -0.5px, line-height: 1.1
  - H2: 36px/44px, letter-spacing: -0.3px, line-height: 1.2
  - H3: 28px/36px, letter-spacing: -0.2px, line-height: 1.3
  - H4: 22px/30px, letter-spacing: -0.1px, line-height: 1.4
- **Display Text**: Playfair Display, 600 weight (Semi-Bold)
  - Large quotes: 32px/40px, letter-spacing: -0.2px, line-height: 1.3
  - Featured text: 24px/32px, letter-spacing: -0.1px, line-height: 1.4

### Secondary Font Family: Montserrat
- **Body Text**: Montserrat, 400 weight (Regular)
  - Body: 16px/24px, letter-spacing: 0, line-height: 1.6
  - Small: 14px/20px, letter-spacing: 0, line-height: 1.5
- **UI Elements**: Montserrat, 500 weight (Medium)
  - Buttons: 16px/24px, letter-spacing: 0.5px, line-height: 1.5, uppercase
  - Navigation: 14px/20px, letter-spacing: 0.5px, line-height: 1.5, uppercase
- **Captions/Small Text**: Montserrat, 400 weight (Regular)
  - Caption: 12px/16px, letter-spacing: 0.2px, line-height: 1.4

## Grid System & Spacing

### Grid System
- **Base**: 12-column grid system
- **Container Width**: 1280px maximum (80% of viewport width on smaller screens)
- **Gutter Width**: 24px between columns
- **Breakpoints**:
  - Mobile: 0-767px (4-column grid)
  - Tablet: 768px-1023px (8-column grid)
  - Desktop: 1024px+ (12-column grid)
  - Large Desktop: 1440px+ (12-column grid with increased margins)

### Spacing Scale
- **Base Unit**: 8px
- **Scale**:
  - 2XS: 4px (0.5x base) - Minimal separation between related elements
  - XS: 8px (1x base) - Tight spacing between closely related elements
  - S: 16px (2x base) - Standard spacing between related elements
  - M: 24px (3x base) - Spacing between distinct elements
  - L: 32px (4x base) - Spacing between groups of elements
  - XL: 48px (6x base) - Section padding
  - 2XL: 64px (8x base) - Major section separation
  - 3XL: 96px (12x base) - Hero and feature section padding

### Negative Space Usage
- Maintain minimum 48px (XL) padding around all content sections
- Use asymmetrical spacing to create visual interest (e.g., larger right margin than left)
- Increase negative space around premium elements to enhance perceived value
- Maintain consistent vertical rhythm using the spacing scale
- Use negative space strategically to direct attention to key elements (CTAs, testimonials)

## Imagery Style

### Photography Direction
- **Style**: Editorial and architectural
- **Lighting**: Natural light with warm evening ambiance
- **Color Treatment**: Rich, slightly desaturated with emphasis on contrast
- **Subject Matter**:
  - Actual completed projects (never stock photography)
  - Real installation crews in branded uniforms (clean, professional)
  - Close-up detail shots of premium light fixtures and installation quality
  - Wide architectural shots showing full property transformation
  - Before/after comparisons with consistent framing

### Photography Guidelines
- Shoot during "blue hour" (15-30 minutes after sunset) for optimal lighting contrast
- Include human elements for scale and emotional connection
- Capture multiple angles of the same property (wide establishing shot, medium architectural details, close-up craftsmanship)
- Show variety of property types (traditional, modern, commercial, estates)
- Maintain consistent horizon line and perspective across gallery images
- Avoid overly saturated or HDR-style processing

### Image Specifications
- **Hero Images**: 2560px × 1440px minimum, 16:9 aspect ratio
- **Gallery Images**: 1920px × 1080px minimum, 16:9 aspect ratio
- **Detail Shots**: 1200px × 1200px minimum, 1:1 aspect ratio
- **Team/Process Photos**: 1200px × 800px minimum, 3:2 aspect ratio
- **File Format**: WebP with JPEG fallback, 85% quality
- **File Size**: Maximum 250KB for mobile optimization

## Motion Rules

### Animation Principles
- **Subtle**: All animations should be understated and purposeful
- **Smooth**: Use ease-in-out timing functions (cubic-bezier(0.4, 0, 0.2, 1))
- **Swift**: Keep animations between 200-300ms for optimal perception
- **Purposeful**: Only animate elements that provide user feedback or enhance understanding

### Specific Animation Guidelines
- **Hover States**: Subtle scale (1.02-1.05x) and shadow increases
- **Page Transitions**: Fade transitions (200ms) between pages
- **Scroll Animations**: Gentle fade-in and slight upward movement (20px)
- **Button Interactions**: Subtle background color shifts and minimal scale changes
- **Gallery Transitions**: Crossfade between images (300ms)
- **Menu Animations**: Smooth dropdown with slight fade and expansion

### Video Guidelines
- **Length**: 30-90 seconds maximum for homepage videos
- **Style**: Cinematic, slow-moving establishing shots
- **Content**: Installation process, finished results, client reactions
- **Audio**: Optional soft instrumental background only (must be muted by default)
- **Captions**: Always include for accessibility
- **Autoplay**: Only when muted and visible in viewport
- **Controls**: Always provide play/pause and mute controls

## UI Elements

### Button Styles
- **Primary**: Gold (#D4AF37) background, navy (#0A2342) text, subtle shadow
- **Secondary**: Transparent background, gold border, gold text
- **Tertiary**: No background/border, gold text with subtle underline
- **Button Sizes**:
  - Small: 32px height, 16px horizontal padding
  - Medium: 48px height, 24px horizontal padding
  - Large: 56px height, 32px horizontal padding
- **Button States**:
  - Hover: Darken background by 10%, add subtle shadow
  - Active: Darken background by 15%, reduce shadow
  - Disabled: 50% opacity, no hover effects

### Card Styles
- **Service Cards**: White background, subtle shadow, 2px gold top border
- **Testimonial Cards**: Light gray background, no border, subtle shadow
- **Feature Cards**: White background, medium shadow, rounded corners
- **Card Padding**: 32px (L) consistent internal padding

### Form Elements
- **Input Fields**: White background, 1px charcoal border, 48px height
- **Dropdown Menus**: Custom styling with subtle animation
- **Checkboxes/Radio Buttons**: Custom styling with gold accents
- **Form Labels**: Above input fields, Montserrat Medium, 14px
- **Form Validation**: Inline validation with subtle animations

## Iconography
- **Style**: Simple, outlined icons with 2px stroke weight
- **Color**: Primary navy or gold depending on context
- **Size**: 24px × 24px standard (scale proportionally as needed)
- **Usage**: Use icons sparingly and only when they enhance understanding
- **Animation**: Subtle animations on hover/interaction where appropriate