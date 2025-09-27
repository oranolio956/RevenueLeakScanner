# Step 15: Developer Tokens & Example CSS

## Design Token System

### Color Tokens

```css
:root {
  /* Primary Colors */
  --color-navy: #0A2342;
  --color-winter-white: #F7F9FC;
  --color-gold: #D4AF37;
  
  /* Secondary Colors */
  --color-charcoal: #2D3142;
  --color-soft-silver: #E0E2E6;
  --color-midnight-blue: #14395B;
  
  /* Tertiary/Accent Colors */
  --color-evergreen: #1D3C34;
  --color-warm-glow: #E8C872;
  --color-deep-burgundy: #5E1914;
  
  /* Functional Colors */
  --color-success: #2E7D32;
  --color-warning: #F9A825;
  --color-error: #C62828;
  --color-info: #1565C0;
  
  /* Text Colors */
  --text-primary: var(--color-navy);
  --text-secondary: var(--color-charcoal);
  --text-tertiary: rgba(45, 49, 66, 0.7);
  --text-inverse: var(--color-winter-white);
  --text-accent: var(--color-gold);
  
  /* Background Colors */
  --bg-primary: var(--color-winter-white);
  --bg-secondary: var(--color-soft-silver);
  --bg-tertiary: #F0F2F5;
  --bg-accent: var(--color-navy);
  --bg-gold: var(--color-gold);
  
  /* Border Colors */
  --border-light: rgba(224, 226, 230, 0.5);
  --border-medium: var(--color-soft-silver);
  --border-dark: rgba(45, 49, 66, 0.2);
  --border-accent: var(--color-gold);
  
  /* Shadow Colors */
  --shadow-soft: rgba(10, 35, 66, 0.05);
  --shadow-medium: rgba(10, 35, 66, 0.1);
  --shadow-hard: rgba(10, 35, 66, 0.2);
}
```

### Typography Tokens

```css
:root {
  /* Font Families */
  --font-primary: 'Playfair Display', Georgia, serif;
  --font-secondary: 'Montserrat', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;
  
  /* Font Weights */
  --font-weight-regular: 400;
  --font-weight-medium: 500;
  --font-weight-semibold: 600;
  --font-weight-bold: 700;
  
  /* Font Sizes */
  --text-xs: 0.75rem;   /* 12px */
  --text-sm: 0.875rem;  /* 14px */
  --text-base: 1rem;    /* 16px */
  --text-lg: 1.125rem;  /* 18px */
  --text-xl: 1.25rem;   /* 20px */
  --text-2xl: 1.5rem;   /* 24px */
  --text-3xl: 1.75rem;  /* 28px */
  --text-4xl: 2rem;     /* 32px */
  --text-5xl: 2.25rem;  /* 36px */
  --text-6xl: 3rem;     /* 48px */
  
  /* Line Heights */
  --leading-none: 1;
  --leading-tight: 1.1;
  --leading-snug: 1.2;
  --leading-normal: 1.5;
  --leading-relaxed: 1.625;
  --leading-loose: 2;
  
  /* Letter Spacing */
  --tracking-tighter: -0.05em;
  --tracking-tight: -0.025em;
  --tracking-normal: 0;
  --tracking-wide: 0.025em;
  --tracking-wider: 0.05em;
  --tracking-widest: 0.1em;
}
```

### Spacing Tokens

```css
:root {
  /* Base Spacing Unit: 8px */
  --space-2xs: 0.25rem;  /* 4px - 0.5x base */
  --space-xs: 0.5rem;    /* 8px - 1x base */
  --space-sm: 1rem;      /* 16px - 2x base */
  --space-md: 1.5rem;    /* 24px - 3x base */
  --space-lg: 2rem;      /* 32px - 4x base */
  --space-xl: 3rem;      /* 48px - 6x base */
  --space-2xl: 4rem;     /* 64px - 8x base */
  --space-3xl: 6rem;     /* 96px - 12x base */
  
  /* Component Specific Spacing */
  --space-button-x: 1.5rem;  /* 24px horizontal padding for buttons */
  --space-button-y: 0.75rem; /* 12px vertical padding for buttons */
  --space-card: 2rem;        /* 32px padding for cards */
  --space-section: 6rem;     /* 96px padding for sections */
  --space-container: 5%;     /* Container side padding */
  
  /* Grid Gaps */
  --gap-xs: 0.5rem;    /* 8px */
  --gap-sm: 1rem;      /* 16px */
  --gap-md: 1.5rem;    /* 24px */
  --gap-lg: 2rem;      /* 32px */
  --gap-xl: 3rem;      /* 48px */
}
```

### Border & Radius Tokens

```css
:root {
  /* Border Widths */
  --border-width-thin: 1px;
  --border-width-medium: 2px;
  --border-width-thick: 4px;
  
  /* Border Radii */
  --radius-none: 0;
  --radius-sm: 0.125rem;   /* 2px */
  --radius-md: 0.25rem;    /* 4px */
  --radius-lg: 0.5rem;     /* 8px */
  --radius-xl: 1rem;       /* 16px */
  --radius-full: 9999px;   /* Fully rounded (circles, pills) */
}
```

### Shadow Tokens

```css
:root {
  /* Box Shadows */
  --shadow-xs: 0 1px 2px var(--shadow-soft);
  --shadow-sm: 0 1px 3px var(--shadow-soft), 0 1px 2px var(--shadow-medium);
  --shadow-md: 0 4px 6px var(--shadow-soft), 0 2px 4px var(--shadow-medium);
  --shadow-lg: 0 10px 15px var(--shadow-soft), 0 4px 6px var(--shadow-medium);
  --shadow-xl: 0 20px 25px var(--shadow-soft), 0 10px 10px var(--shadow-medium);
  --shadow-inner: inset 0 2px 4px var(--shadow-soft);
  
  /* Focus Shadows */
  --shadow-focus: 0 0 0 3px rgba(212, 175, 55, 0.4);
  --shadow-focus-error: 0 0 0 3px rgba(198, 40, 40, 0.4);
}
```

### Animation Tokens

```css
:root {
  /* Transition Durations */
  --duration-fast: 150ms;
  --duration-normal: 250ms;
  --duration-slow: 350ms;
  
  /* Transition Timing Functions */
  --ease-default: cubic-bezier(0.4, 0, 0.2, 1);
  --ease-in: cubic-bezier(0.4, 0, 1, 1);
  --ease-out: cubic-bezier(0, 0, 0.2, 1);
  --ease-in-out: cubic-bezier(0.4, 0, 0.2, 1);
  
  /* Animation Presets */
  --transition-button: var(--duration-normal) var(--ease-default);
  --transition-transform: transform var(--duration-normal) var(--ease-default);
  --transition-opacity: opacity var(--duration-normal) var(--ease-default);
  --transition-colors: background-color var(--duration-normal) var(--ease-default), 
                       border-color var(--duration-normal) var(--ease-default), 
                       color var(--duration-normal) var(--ease-default);
}
```

### Breakpoint Tokens

```css
:root {
  /* Breakpoints */
  --breakpoint-xs: 480px;   /* Extra small devices */
  --breakpoint-sm: 640px;   /* Small devices */
  --breakpoint-md: 768px;   /* Medium devices */
  --breakpoint-lg: 1024px;  /* Large devices */
  --breakpoint-xl: 1280px;  /* Extra large devices */
  --breakpoint-2xl: 1536px; /* 2X large devices */
  
  /* Container Max Widths */
  --container-max-width: 1280px;
  --container-narrow-max-width: 1024px;
}
```

### Z-Index Tokens

```css
:root {
  /* Z-Index Scale */
  --z-negative: -1;       /* Below normal flow */
  --z-base: 0;            /* Default stacking context */
  --z-raised: 10;         /* Raised elements (cards, etc.) */
  --z-dropdown: 1000;     /* Dropdowns */
  --z-sticky: 1100;       /* Sticky elements */
  --z-fixed: 1200;        /* Fixed elements (navbar, etc.) */
  --z-modal: 1300;        /* Modal dialogs */
  --z-popover: 1400;      /* Popovers and tooltips */
  --z-toast: 1500;        /* Toast notifications */
  --z-overlay: 1600;      /* Full-screen overlays */
}
```

## Component CSS Examples

### Button Component

```css
/* Base Button Styles */
.btn {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  font-family: var(--font-secondary);
  font-weight: var(--font-weight-medium);
  font-size: var(--text-base);
  letter-spacing: var(--tracking-wide);
  text-transform: uppercase;
  padding: var(--space-button-y) var(--space-button-x);
  border-radius: var(--radius-sm);
  border: var(--border-width-thin) solid transparent;
  transition: var(--transition-colors), var(--transition-transform), box-shadow var(--duration-normal) var(--ease-default);
  cursor: pointer;
  white-space: nowrap;
  text-decoration: none;
}

.btn:focus {
  outline: none;
  box-shadow: var(--shadow-focus);
}

/* Primary Button */
.btn-primary {
  background-color: var(--color-gold);
  color: var(--color-navy);
  border-color: var(--color-gold);
  box-shadow: var(--shadow-sm);
}

.btn-primary:hover {
  background-color: #C9A633; /* Slightly darker gold */
  border-color: #C9A633;
  transform: translateY(-1px);
  box-shadow: var(--shadow-md);
}

.btn-primary:active {
  background-color: #B8962F; /* Even darker gold */
  border-color: #B8962F;
  transform: translateY(0);
  box-shadow: var(--shadow-sm);
}

/* Secondary Button */
.btn-secondary {
  background-color: transparent;
  color: var(--color-gold);
  border-color: var(--color-gold);
}

.btn-secondary:hover {
  background-color: rgba(212, 175, 55, 0.1);
  transform: translateY(-1px);
  box-shadow: var(--shadow-sm);
}

.btn-secondary:active {
  background-color: rgba(212, 175, 55, 0.2);
  transform: translateY(0);
  box-shadow: none;
}

/* Tertiary Button / Text Link */
.btn-tertiary {
  background-color: transparent;
  color: var(--color-gold);
  border-color: transparent;
  padding: var(--space-xs) var(--space-sm);
  text-decoration: none;
  position: relative;
}

.btn-tertiary::after {
  content: '→';
  margin-left: var(--space-xs);
  transition: transform var(--duration-normal) var(--ease-default);
}

.btn-tertiary:hover {
  background-color: transparent;
  border-color: transparent;
}

.btn-tertiary:hover::after {
  transform: translateX(4px);
}

.btn-tertiary:active {
  color: #B8962F; /* Darker gold */
}

/* Button Sizes */
.btn-sm {
  font-size: var(--text-sm);
  padding: calc(var(--space-button-y) * 0.75) calc(var(--space-button-x) * 0.75);
  height: 32px;
}

.btn-md {
  /* Default size */
  height: 48px;
}

.btn-lg {
  font-size: var(--text-lg);
  padding: calc(var(--space-button-y) * 1.25) calc(var(--space-button-x) * 1.25);
  height: 56px;
}

/* Full Width Button */
.btn-full {
  width: 100%;
}

/* Disabled State */
.btn:disabled,
.btn.disabled {
  opacity: 0.5;
  cursor: not-allowed;
  pointer-events: none;
}
```

### Card Component

```css
/* Base Card Styles */
.card {
  background-color: var(--color-winter-white);
  border-radius: var(--radius-md);
  box-shadow: var(--shadow-md);
  overflow: hidden;
  transition: transform var(--duration-normal) var(--ease-default), 
              box-shadow var(--duration-normal) var(--ease-default);
}

.card:hover {
  transform: translateY(-4px);
  box-shadow: var(--shadow-lg);
}

/* Card Content */
.card-content {
  padding: var(--space-card);
}

/* Card with Border Accent */
.card-accent {
  border-top: var(--border-width-medium) solid var(--color-gold);
}

/* Service Card */
.service-card {
  display: flex;
  flex-direction: column;
  height: 100%;
}

.service-card-image {
  width: 100%;
  height: 240px;
  object-fit: cover;
}

.service-card-content {
  padding: var(--space-card);
  flex-grow: 1;
  display: flex;
  flex-direction: column;
}

.service-card-title {
  font-family: var(--font-primary);
  font-weight: var(--font-weight-bold);
  font-size: var(--text-2xl);
  color: var(--text-primary);
  margin-bottom: var(--space-sm);
}

.service-card-description {
  font-family: var(--font-secondary);
  font-size: var(--text-base);
  color: var(--text-secondary);
  margin-bottom: var(--space-md);
  flex-grow: 1;
}

.service-card-footer {
  margin-top: auto;
}

/* Testimonial Card */
.testimonial-card {
  background-color: var(--bg-tertiary);
  padding: var(--space-card);
  border-radius: var(--radius-md);
  position: relative;
}

.testimonial-card::before {
  content: '"';
  position: absolute;
  top: var(--space-md);
  left: var(--space-md);
  font-family: var(--font-primary);
  font-size: 4rem;
  line-height: 1;
  color: var(--color-gold);
  opacity: 0.2;
}

.testimonial-quote {
  font-family: var(--font-primary);
  font-style: italic;
  font-size: var(--text-lg);
  color: var(--text-primary);
  margin-bottom: var(--space-md);
  position: relative;
  z-index: 1;
}

.testimonial-author {
  display: flex;
  align-items: center;
}

.testimonial-author-image {
  width: 48px;
  height: 48px;
  border-radius: var(--radius-full);
  object-fit: cover;
  margin-right: var(--space-sm);
}

.testimonial-author-name {
  font-family: var(--font-secondary);
  font-weight: var(--font-weight-medium);
  font-size: var(--text-base);
  color: var(--text-primary);
}

.testimonial-author-location {
  font-family: var(--font-secondary);
  font-size: var(--text-sm);
  color: var(--text-tertiary);
}
```

### Navigation Component

```css
/* Main Navigation */
.main-nav {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  z-index: var(--z-fixed);
  transition: background-color var(--duration-normal) var(--ease-default),
              box-shadow var(--duration-normal) var(--ease-default);
}

/* Transparent state (initial) */
.main-nav-transparent {
  background-color: transparent;
  box-shadow: none;
}

/* Solid state (after scroll) */
.main-nav-solid {
  background-color: var(--color-winter-white);
  box-shadow: var(--shadow-md);
}

.nav-container {
  display: flex;
  align-items: center;
  justify-content: space-between;
  max-width: var(--container-max-width);
  margin: 0 auto;
  padding: var(--space-md) var(--space-container);
  height: 80px;
}

/* Logo */
.nav-logo {
  display: flex;
  align-items: center;
}

.nav-logo img {
  height: 40px;
  width: auto;
}

/* Primary Navigation Links */
.nav-links {
  display: flex;
  align-items: center;
  list-style: none;
  margin: 0;
  padding: 0;
}

.nav-link {
  margin: 0 var(--space-md);
  position: relative;
}

.nav-link a {
  font-family: var(--font-secondary);
  font-weight: var(--font-weight-medium);
  font-size: var(--text-sm);
  text-transform: uppercase;
  letter-spacing: var(--tracking-wide);
  color: var(--text-primary);
  text-decoration: none;
  padding: var(--space-xs) 0;
  transition: color var(--duration-normal) var(--ease-default);
}

.nav-link a:hover {
  color: var(--color-gold);
}

/* Active link indicator */
.nav-link.active a::after {
  content: '';
  position: absolute;
  bottom: 0;
  left: 0;
  width: 100%;
  height: 2px;
  background-color: var(--color-gold);
  transform: scaleX(1);
  transform-origin: left;
}

.nav-link a::after {
  content: '';
  position: absolute;
  bottom: 0;
  left: 0;
  width: 100%;
  height: 2px;
  background-color: var(--color-gold);
  transform: scaleX(0);
  transform-origin: left;
  transition: transform var(--duration-normal) var(--ease-default);
}

.nav-link a:hover::after {
  transform: scaleX(1);
}

/* Navigation CTA */
.nav-cta {
  margin-left: var(--space-lg);
}

/* Mobile Navigation */
.mobile-nav-toggle {
  display: none;
  background: none;
  border: none;
  cursor: pointer;
  padding: var(--space-xs);
}

.mobile-nav-toggle span {
  display: block;
  width: 24px;
  height: 2px;
  background-color: var(--text-primary);
  margin: 5px 0;
  transition: transform var(--duration-normal) var(--ease-default),
              opacity var(--duration-normal) var(--ease-default);
}

/* Mobile menu open state */
.mobile-nav-toggle.open span:nth-child(1) {
  transform: translateY(7px) rotate(45deg);
}

.mobile-nav-toggle.open span:nth-child(2) {
  opacity: 0;
}

.mobile-nav-toggle.open span:nth-child(3) {
  transform: translateY(-7px) rotate(-45deg);
}

/* Mobile menu */
.mobile-menu {
  position: fixed;
  top: 80px;
  left: 0;
  right: 0;
  bottom: 0;
  background-color: var(--color-winter-white);
  padding: var(--space-lg);
  transform: translateX(100%);
  transition: transform var(--duration-normal) var(--ease-default);
  z-index: var(--z-fixed);
  overflow-y: auto;
}

.mobile-menu.open {
  transform: translateX(0);
}

.mobile-menu-links {
  list-style: none;
  margin: 0;
  padding: 0;
}

.mobile-menu-link {
  margin: var(--space-md) 0;
}

.mobile-menu-link a {
  font-family: var(--font-secondary);
  font-weight: var(--font-weight-medium);
  font-size: var(--text-lg);
  color: var(--text-primary);
  text-decoration: none;
  display: block;
  padding: var(--space-xs) 0;
}

.mobile-menu-cta {
  margin-top: var(--space-xl);
}

/* Media queries */
@media (max-width: 1024px) {
  .nav-links {
    display: none;
  }
  
  .nav-cta {
    display: none;
  }
  
  .mobile-nav-toggle {
    display: block;
  }
}
```

### Form Component

```css
/* Form Container */
.form-container {
  max-width: 640px;
  margin: 0 auto;
}

/* Form Group */
.form-group {
  margin-bottom: var(--space-md);
}

/* Form Label */
.form-label {
  display: block;
  font-family: var(--font-secondary);
  font-weight: var(--font-weight-medium);
  font-size: var(--text-sm);
  color: var(--text-secondary);
  margin-bottom: var(--space-xs);
}

/* Form Input */
.form-input {
  display: block;
  width: 100%;
  height: 48px;
  padding: 0 var(--space-sm);
  font-family: var(--font-secondary);
  font-size: var(--text-base);
  color: var(--text-primary);
  background-color: var(--color-winter-white);
  border: var(--border-width-thin) solid var(--border-medium);
  border-radius: var(--radius-sm);
  transition: border-color var(--duration-normal) var(--ease-default),
              box-shadow var(--duration-normal) var(--ease-default);
}

.form-input:focus {
  outline: none;
  border-color: var(--color-gold);
  box-shadow: var(--shadow-focus);
}

.form-input::placeholder {
  color: var(--text-tertiary);
}

/* Form Textarea */
.form-textarea {
  display: block;
  width: 100%;
  min-height: 120px;
  padding: var(--space-sm);
  font-family: var(--font-secondary);
  font-size: var(--text-base);
  color: var(--text-primary);
  background-color: var(--color-winter-white);
  border: var(--border-width-thin) solid var(--border-medium);
  border-radius: var(--radius-sm);
  resize: vertical;
  transition: border-color var(--duration-normal) var(--ease-default),
              box-shadow var(--duration-normal) var(--ease-default);
}

.form-textarea:focus {
  outline: none;
  border-color: var(--color-gold);
  box-shadow: var(--shadow-focus);
}

/* Form Select */
.form-select-container {
  position: relative;
}

.form-select {
  display: block;
  width: 100%;
  height: 48px;
  padding: 0 var(--space-sm);
  font-family: var(--font-secondary);
  font-size: var(--text-base);
  color: var(--text-primary);
  background-color: var(--color-winter-white);
  border: var(--border-width-thin) solid var(--border-medium);
  border-radius: var(--radius-sm);
  appearance: none;
  cursor: pointer;
  transition: border-color var(--duration-normal) var(--ease-default),
              box-shadow var(--duration-normal) var(--ease-default);
}

.form-select:focus {
  outline: none;
  border-color: var(--color-gold);
  box-shadow: var(--shadow-focus);
}

.form-select-arrow {
  position: absolute;
  top: 50%;
  right: var(--space-sm);
  transform: translateY(-50%);
  pointer-events: none;
}

/* Form Checkbox */
.form-checkbox-container {
  display: flex;
  align-items: flex-start;
  margin-bottom: var(--space-sm);
}

.form-checkbox {
  position: absolute;
  opacity: 0;
  width: 0;
  height: 0;
}

.form-checkbox-label {
  position: relative;
  padding-left: 32px;
  cursor: pointer;
  font-family: var(--font-secondary);
  font-size: var(--text-base);
  color: var(--text-secondary);
  user-select: none;
}

.form-checkbox-label::before {
  content: '';
  position: absolute;
  left: 0;
  top: 2px;
  width: 20px;
  height: 20px;
  border: var(--border-width-thin) solid var(--border-medium);
  border-radius: var(--radius-sm);
  background-color: var(--color-winter-white);
  transition: background-color var(--duration-normal) var(--ease-default),
              border-color var(--duration-normal) var(--ease-default);
}

.form-checkbox:checked + .form-checkbox-label::before {
  background-color: var(--color-gold);
  border-color: var(--color-gold);
}

.form-checkbox:checked + .form-checkbox-label::after {
  content: '';
  position: absolute;
  left: 7px;
  top: 7px;
  width: 6px;
  height: 10px;
  border: solid var(--color-winter-white);
  border-width: 0 2px 2px 0;
  transform: rotate(45deg);
}

.form-checkbox:focus + .form-checkbox-label::before {
  box-shadow: var(--shadow-focus);
}

/* Form Validation */
.form-input.error,
.form-textarea.error,
.form-select.error {
  border-color: var(--color-error);
}

.form-input.error:focus,
.form-textarea.error:focus,
.form-select.error:focus {
  box-shadow: var(--shadow-focus-error);
}

.form-error-message {
  font-family: var(--font-secondary);
  font-size: var(--text-sm);
  color: var(--color-error);
  margin-top: var(--space-2xs);
}

/* Form Row (for side-by-side fields) */
.form-row {
  display: flex;
  gap: var(--space-md);
  margin-bottom: var(--space-md);
}

.form-row .form-group {
  flex: 1;
  margin-bottom: 0;
}

/* Form Actions */
.form-actions {
  display: flex;
  justify-content: flex-end;
  margin-top: var(--space-lg);
}

.form-actions .btn + .btn {
  margin-left: var(--space-sm);
}

/* Responsive adjustments */
@media (max-width: 640px) {
  .form-row {
    flex-direction: column;
    gap: var(--space-md);
  }
}
```

### Hero Section Component

```css
/* Hero Section */
.hero {
  position: relative;
  height: 80vh;
  min-height: 600px;
  display: flex;
  align-items: center;
  overflow: hidden;
}

/* Hero Background */
.hero-bg {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  z-index: -1;
}

.hero-bg-image {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.hero-bg-overlay {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: linear-gradient(to right, rgba(10, 35, 66, 0.8) 0%, rgba(10, 35, 66, 0.4) 100%);
}

/* Hero Content */
.hero-content {
  max-width: var(--container-max-width);
  margin: 0 auto;
  padding: 0 var(--space-container);
  width: 100%;
}

.hero-content-inner {
  max-width: 600px;
}

.hero-title {
  font-family: var(--font-primary);
  font-weight: var(--font-weight-bold);
  font-size: var(--text-6xl);
  line-height: var(--leading-tight);
  color: var(--color-winter-white);
  margin-bottom: var(--space-md);
}

.hero-subtitle {
  font-family: var(--font-secondary);
  font-weight: var(--font-weight-regular);
  font-size: var(--text-xl);
  line-height: var(--leading-relaxed);
  color: var(--color-winter-white);
  margin-bottom: var(--space-lg);
  opacity: 0.9;
}

.hero-actions {
  display: flex;
  gap: var(--space-md);
}

/* Hero with Video Background */
.hero-video {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  object-fit: cover;
  z-index: -2;
}

/* Hero Variations */
.hero-centered {
  text-align: center;
}

.hero-centered .hero-content-inner {
  margin: 0 auto;
}

.hero-centered .hero-actions {
  justify-content: center;
}

/* Responsive adjustments */
@media (max-width: 768px) {
  .hero {
    height: auto;
    min-height: 500px;
    padding: var(--space-3xl) 0;
  }
  
  .hero-title {
    font-size: var(--text-5xl);
  }
  
  .hero-subtitle {
    font-size: var(--text-lg);
  }
  
  .hero-actions {
    flex-direction: column;
  }
  
  .hero-actions .btn {
    width: 100%;
  }
}
```

### Gallery Component

```css
/* Gallery Container */
.gallery {
  position: relative;
}

/* Gallery Filters */
.gallery-filters {
  display: flex;
  justify-content: center;
  margin-bottom: var(--space-xl);
}

.gallery-filter {
  font-family: var(--font-secondary);
  font-weight: var(--font-weight-medium);
  font-size: var(--text-sm);
  text-transform: uppercase;
  letter-spacing: var(--tracking-wide);
  color: var(--text-secondary);
  background: none;
  border: none;
  padding: var(--space-xs) var(--space-sm);
  cursor: pointer;
  transition: color var(--duration-normal) var(--ease-default);
  position: relative;
}

.gallery-filter:hover {
  color: var(--text-primary);
}

.gallery-filter.active {
  color: var(--color-gold);
}

.gallery-filter.active::after {
  content: '';
  position: absolute;
  bottom: 0;
  left: var(--space-sm);
  right: var(--space-sm);
  height: 2px;
  background-color: var(--color-gold);
}

/* Gallery Grid */
.gallery-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: var(--space-md);
}

/* Gallery Item */
.gallery-item {
  position: relative;
  overflow: hidden;
  border-radius: var(--radius-md);
  cursor: pointer;
  height: 0;
  padding-bottom: 66.67%; /* 3:2 aspect ratio */
}

.gallery-item-image {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  object-fit: cover;
  transition: transform var(--duration-normal) var(--ease-default);
}

.gallery-item:hover .gallery-item-image {
  transform: scale(1.05);
}

.gallery-item-overlay {
  position: absolute;
  bottom: 0;
  left: 0;
  right: 0;
  padding: var(--space-md);
  background: linear-gradient(to top, rgba(10, 35, 66, 0.8) 0%, rgba(10, 35, 66, 0) 100%);
  opacity: 0;
  transition: opacity var(--duration-normal) var(--ease-default);
}

.gallery-item:hover .gallery-item-overlay {
  opacity: 1;
}

.gallery-item-title {
  font-family: var(--font-primary);
  font-weight: var(--font-weight-semibold);
  font-size: var(--text-lg);
  color: var(--color-winter-white);
  margin-bottom: var(--space-2xs);
}

.gallery-item-subtitle {
  font-family: var(--font-secondary);
  font-size: var(--text-sm);
  color: var(--color-winter-white);
  opacity: 0.8;
}

/* Gallery Lightbox */
.gallery-lightbox {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(10, 35, 66, 0.95);
  z-index: var(--z-modal);
  display: flex;
  align-items: center;
  justify-content: center;
  opacity: 0;
  pointer-events: none;
  transition: opacity var(--duration-normal) var(--ease-default);
}

.gallery-lightbox.open {
  opacity: 1;
  pointer-events: auto;
}

.gallery-lightbox-content {
  position: relative;
  max-width: 90%;
  max-height: 90%;
}

.gallery-lightbox-image {
  max-width: 100%;
  max-height: 90vh;
  border-radius: var(--radius-md);
}

.gallery-lightbox-close {
  position: absolute;
  top: -40px;
  right: 0;
  width: 32px;
  height: 32px;
  background: none;
  border: none;
  color: var(--color-winter-white);
  font-size: 24px;
  cursor: pointer;
}

.gallery-lightbox-nav {
  position: absolute;
  top: 50%;
  transform: translateY(-50%);
  width: 48px;
  height: 48px;
  background: rgba(10, 35, 66, 0.5);
  border: none;
  border-radius: var(--radius-full);
  color: var(--color-winter-white);
  font-size: 24px;
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
  transition: background-color var(--duration-normal) var(--ease-default);
}

.gallery-lightbox-nav:hover {
  background-color: rgba(10, 35, 66, 0.8);
}

.gallery-lightbox-prev {
  left: -60px;
}

.gallery-lightbox-next {
  right: -60px;
}

.gallery-lightbox-caption {
  position: absolute;
  bottom: -40px;
  left: 0;
  right: 0;
  text-align: center;
  color: var(--color-winter-white);
  font-family: var(--font-secondary);
  font-size: var(--text-sm);
}

/* Responsive adjustments */
@media (max-width: 1024px) {
  .gallery-grid {
    grid-template-columns: repeat(2, 1fr);
  }
}

@media (max-width: 640px) {
  .gallery-grid {
    grid-template-columns: 1fr;
  }
  
  .gallery-filters {
    flex-wrap: wrap;
    justify-content: center;
  }
  
  .gallery-lightbox-nav {
    width: 40px;
    height: 40px;
  }
  
  .gallery-lightbox-prev {
    left: 16px;
  }
  
  .gallery-lightbox-next {
    right: 16px;
  }
}
```

## Example HTML Section

### Hero Section with Call-to-Action

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Premium Holiday Lighting</title>
  <link href="https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;600;700&family=Montserrat:wght@400;500;600;700&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="css/tokens.css">
  <link rel="stylesheet" href="css/global.css">
  <link rel="stylesheet" href="css/components.css">
</head>
<body>
  <!-- Header/Navigation -->
  <header class="main-nav main-nav-transparent" id="main-nav">
    <div class="nav-container">
      <div class="nav-logo">
        <a href="/">
          <img src="images/logo-light.svg" alt="Illuminate Distinction" class="logo-light">
          <img src="images/logo-dark.svg" alt="Illuminate Distinction" class="logo-dark">
        </a>
      </div>
      
      <nav>
        <ul class="nav-links">
          <li class="nav-link"><a href="/">Home</a></li>
          <li class="nav-link"><a href="/services">Services</a></li>
          <li class="nav-link"><a href="/gallery">Gallery</a></li>
          <li class="nav-link"><a href="/process">Process</a></li>
          <li class="nav-link"><a href="/pricing">Pricing</a></li>
          <li class="nav-link"><a href="/contact">Contact</a></li>
        </ul>
      </nav>
      
      <div class="nav-cta">
        <a href="/consultation" class="btn btn-primary">Schedule Consultation</a>
      </div>
      
      <button class="mobile-nav-toggle" id="mobile-nav-toggle">
        <span></span>
        <span></span>
        <span></span>
      </button>
    </div>
    
    <div class="mobile-menu" id="mobile-menu">
      <ul class="mobile-menu-links">
        <li class="mobile-menu-link"><a href="/">Home</a></li>
        <li class="mobile-menu-link"><a href="/services">Services</a></li>
        <li class="mobile-menu-link"><a href="/gallery">Gallery</a></li>
        <li class="mobile-menu-link"><a href="/process">Process</a></li>
        <li class="mobile-menu-link"><a href="/pricing">Pricing</a></li>
        <li class="mobile-menu-link"><a href="/contact">Contact</a></li>
      </ul>
      
      <div class="mobile-menu-cta">
        <a href="/consultation" class="btn btn-primary btn-full">Schedule Consultation</a>
      </div>
    </div>
  </header>

  <!-- Hero Section -->
  <section class="hero">
    <div class="hero-bg">
      <img src="images/hero-image.jpg" alt="Architectural Holiday Lighting" class="hero-bg-image">
      <div class="hero-bg-overlay"></div>
    </div>
    
    <div class="hero-content">
      <div class="hero-content-inner">
        <h1 class="hero-title">Architectural Holiday Lighting for Discerning Properties</h1>
        <p class="hero-subtitle">Custom design, flawless installation, and proactive maintenance for a truly distinctive holiday display.</p>
        <div class="hero-actions">
          <a href="/consultation" class="btn btn-primary btn-lg">Schedule Consultation</a>
          <a href="/gallery" class="btn btn-secondary btn-lg">View Gallery</a>
        </div>
      </div>
    </div>
  </section>

  <!-- Trust Indicators Section -->
  <section class="trust-indicators">
    <div class="container">
      <div class="trust-indicators-grid">
        <div class="trust-indicator">
          <div class="trust-indicator-icon">
            <img src="images/icons/shield.svg" alt="Warranty Icon">
          </div>
          <div class="trust-indicator-content">
            <h3 class="trust-indicator-title">5-Year Warranty</h3>
            <p class="trust-indicator-text">Premium components backed by comprehensive coverage</p>
          </div>
        </div>
        
        <div class="trust-indicator">
          <div class="trust-indicator-icon">
            <img src="images/icons/certificate.svg" alt="Certification Icon">
          </div>
          <div class="trust-indicator-content">
            <h3 class="trust-indicator-title">Certified Designers</h3>
            <p class="trust-indicator-text">Architectural expertise for distinguished properties</p>
          </div>
        </div>
        
        <div class="trust-indicator">
          <div class="trust-indicator-icon">
            <img src="images/icons/clock.svg" alt="Response Icon">
          </div>
          <div class="trust-indicator-content">
            <h3 class="trust-indicator-title">24-Hour Response</h3>
            <p class="trust-indicator-text">Guaranteed service throughout the season</p>
          </div>
        </div>
        
        <div class="trust-indicator">
          <div class="trust-indicator-icon">
            <img src="images/icons/return.svg" alt="Return Rate Icon">
          </div>
          <div class="trust-indicator-content">
            <h3 class="trust-indicator-title">92% Client Return Rate</h3>
            <p class="trust-indicator-text">Exceptional satisfaction year after year</p>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- JavaScript for Navigation -->
  <script>
    // Navigation scroll behavior
    const mainNav = document.getElementById('main-nav');
    const mobileNavToggle = document.getElementById('mobile-nav-toggle');
    const mobileMenu = document.getElementById('mobile-menu');
    
    // Handle scroll events
    window.addEventListener('scroll', () => {
      if (window.scrollY > 50) {
        mainNav.classList.remove('main-nav-transparent');
        mainNav.classList.add('main-nav-solid');
      } else {
        mainNav.classList.add('main-nav-transparent');
        mainNav.classList.remove('main-nav-solid');
      }
    });
    
    // Mobile menu toggle
    mobileNavToggle.addEventListener('click', () => {
      mobileNavToggle.classList.toggle('open');
      mobileMenu.classList.toggle('open');
    });
  </script>
</body>
</html>
```

## Responsive Design Implementation

### Breakpoint System

```css
/* Base styles apply to all screen sizes */

/* Small screens (640px and up) */
@media (min-width: 640px) {
  /* Small screen styles */
}

/* Medium screens (768px and up) */
@media (min-width: 768px) {
  /* Medium screen styles */
}

/* Large screens (1024px and up) */
@media (min-width: 1024px) {
  /* Large screen styles */
}

/* Extra large screens (1280px and up) */
@media (min-width: 1280px) {
  /* Extra large screen styles */
}

/* 2XL screens (1536px and up) */
@media (min-width: 1536px) {
  /* 2XL screen styles */
}
```

### Container Classes

```css
/* Container */
.container {
  width: 100%;
  margin-left: auto;
  margin-right: auto;
  padding-left: var(--space-container);
  padding-right: var(--space-container);
}

/* Container with maximum width */
@media (min-width: 640px) {
  .container {
    max-width: 640px;
  }
}

@media (min-width: 768px) {
  .container {
    max-width: 768px;
  }
}

@media (min-width: 1024px) {
  .container {
    max-width: 1024px;
  }
}

@media (min-width: 1280px) {
  .container {
    max-width: var(--container-max-width);
  }
}

/* Narrow container */
.container-narrow {
  width: 100%;
  margin-left: auto;
  margin-right: auto;
  padding-left: var(--space-container);
  padding-right: var(--space-container);
}

@media (min-width: 640px) {
  .container-narrow {
    max-width: 640px;
  }
}

@media (min-width: 768px) {
  .container-narrow {
    max-width: 768px;
  }
}

@media (min-width: 1024px) {
  .container-narrow {
    max-width: var(--container-narrow-max-width);
  }
}
```

### Responsive Grid System

```css
/* Grid Container */
.grid {
  display: grid;
  gap: var(--gap-md);
}

/* Grid columns for different breakpoints */
.grid-cols-1 {
  grid-template-columns: repeat(1, minmax(0, 1fr));
}

.grid-cols-2 {
  grid-template-columns: repeat(2, minmax(0, 1fr));
}

.grid-cols-3 {
  grid-template-columns: repeat(3, minmax(0, 1fr));
}

.grid-cols-4 {
  grid-template-columns: repeat(4, minmax(0, 1fr));
}

/* Responsive grid columns */
@media (min-width: 640px) {
  .sm\:grid-cols-1 {
    grid-template-columns: repeat(1, minmax(0, 1fr));
  }
  
  .sm\:grid-cols-2 {
    grid-template-columns: repeat(2, minmax(0, 1fr));
  }
  
  .sm\:grid-cols-3 {
    grid-template-columns: repeat(3, minmax(0, 1fr));
  }
  
  .sm\:grid-cols-4 {
    grid-template-columns: repeat(4, minmax(0, 1fr));
  }
}

@media (min-width: 768px) {
  .md\:grid-cols-1 {
    grid-template-columns: repeat(1, minmax(0, 1fr));
  }
  
  .md\:grid-cols-2 {
    grid-template-columns: repeat(2, minmax(0, 1fr));
  }
  
  .md\:grid-cols-3 {
    grid-template-columns: repeat(3, minmax(0, 1fr));
  }
  
  .md\:grid-cols-4 {
    grid-template-columns: repeat(4, minmax(0, 1fr));
  }
}

@media (min-width: 1024px) {
  .lg\:grid-cols-1 {
    grid-template-columns: repeat(1, minmax(0, 1fr));
  }
  
  .lg\:grid-cols-2 {
    grid-template-columns: repeat(2, minmax(0, 1fr));
  }
  
  .lg\:grid-cols-3 {
    grid-template-columns: repeat(3, minmax(0, 1fr));
  }
  
  .lg\:grid-cols-4 {
    grid-template-columns: repeat(4, minmax(0, 1fr));
  }
}

/* Grid gaps */
.gap-xs {
  gap: var(--gap-xs);
}

.gap-sm {
  gap: var(--gap-sm);
}

.gap-md {
  gap: var(--gap-md);
}

.gap-lg {
  gap: var(--gap-lg);
}

.gap-xl {
  gap: var(--gap-xl);
}
```

### Responsive Typography

```css
/* Base typography */
html {
  font-size: 16px;
}

body {
  font-family: var(--font-secondary);
  font-weight: var(--font-weight-regular);
  line-height: var(--leading-normal);
  color: var(--text-primary);
}

/* Headings */
h1, .h1 {
  font-family: var(--font-primary);
  font-weight: var(--font-weight-bold);
  font-size: var(--text-4xl);
  line-height: var(--leading-tight);
  letter-spacing: var(--tracking-tight);
  margin-bottom: var(--space-md);
}

h2, .h2 {
  font-family: var(--font-primary);
  font-weight: var(--font-weight-bold);
  font-size: var(--text-3xl);
  line-height: var(--leading-snug);
  letter-spacing: var(--tracking-tight);
  margin-bottom: var(--space-sm);
}

h3, .h3 {
  font-family: var(--font-primary);
  font-weight: var(--font-weight-semibold);
  font-size: var(--text-2xl);
  line-height: var(--leading-snug);
  letter-spacing: var(--tracking-normal);
  margin-bottom: var(--space-sm);
}

h4, .h4 {
  font-family: var(--font-primary);
  font-weight: var(--font-weight-semibold);
  font-size: var(--text-xl);
  line-height: var(--leading-normal);
  letter-spacing: var(--tracking-normal);
  margin-bottom: var(--space-xs);
}

/* Responsive typography */
@media (min-width: 768px) {
  h1, .h1 {
    font-size: var(--text-5xl);
  }
  
  h2, .h2 {
    font-size: var(--text-4xl);
  }
  
  h3, .h3 {
    font-size: var(--text-3xl);
  }
  
  h4, .h4 {
    font-size: var(--text-2xl);
  }
}

@media (min-width: 1024px) {
  h1, .h1 {
    font-size: var(--text-6xl);
  }
  
  h2, .h2 {
    font-size: var(--text-5xl);
  }
  
  h3, .h3 {
    font-size: var(--text-4xl);
  }
  
  h4, .h4 {
    font-size: var(--text-3xl);
  }
}

/* Fluid typography for specific elements */
.hero-title {
  font-size: clamp(2rem, 5vw, 3rem);
}

.section-title {
  font-size: clamp(1.5rem, 4vw, 2.25rem);
}
```

### Responsive Spacing Utilities

```css
/* Margin utilities */
.m-0 { margin: 0; }
.m-xs { margin: var(--space-xs); }
.m-sm { margin: var(--space-sm); }
.m-md { margin: var(--space-md); }
.m-lg { margin: var(--space-lg); }
.m-xl { margin: var(--space-xl); }

.mx-0 { margin-left: 0; margin-right: 0; }
.mx-xs { margin-left: var(--space-xs); margin-right: var(--space-xs); }
.mx-sm { margin-left: var(--space-sm); margin-right: var(--space-sm); }
.mx-md { margin-left: var(--space-md); margin-right: var(--space-md); }
.mx-lg { margin-left: var(--space-lg); margin-right: var(--space-lg); }
.mx-xl { margin-left: var(--space-xl); margin-right: var(--space-xl); }
.mx-auto { margin-left: auto; margin-right: auto; }

.my-0 { margin-top: 0; margin-bottom: 0; }
.my-xs { margin-top: var(--space-xs); margin-bottom: var(--space-xs); }
.my-sm { margin-top: var(--space-sm); margin-bottom: var(--space-sm); }
.my-md { margin-top: var(--space-md); margin-bottom: var(--space-md); }
.my-lg { margin-top: var(--space-lg); margin-bottom: var(--space-lg); }
.my-xl { margin-top: var(--space-xl); margin-bottom: var(--space-xl); }

.mt-0 { margin-top: 0; }
.mt-xs { margin-top: var(--space-xs); }
.mt-sm { margin-top: var(--space-sm); }
.mt-md { margin-top: var(--space-md); }
.mt-lg { margin-top: var(--space-lg); }
.mt-xl { margin-top: var(--space-xl); }

.mb-0 { margin-bottom: 0; }
.mb-xs { margin-bottom: var(--space-xs); }
.mb-sm { margin-bottom: var(--space-sm); }
.mb-md { margin-bottom: var(--space-md); }
.mb-lg { margin-bottom: var(--space-lg); }
.mb-xl { margin-bottom: var(--space-xl); }

/* Padding utilities */
.p-0 { padding: 0; }
.p-xs { padding: var(--space-xs); }
.p-sm { padding: var(--space-sm); }
.p-md { padding: var(--space-md); }
.p-lg { padding: var(--space-lg); }
.p-xl { padding: var(--space-xl); }

.px-0 { padding-left: 0; padding-right: 0; }
.px-xs { padding-left: var(--space-xs); padding-right: var(--space-xs); }
.px-sm { padding-left: var(--space-sm); padding-right: var(--space-sm); }
.px-md { padding-left: var(--space-md); padding-right: var(--space-md); }
.px-lg { padding-left: var(--space-lg); padding-right: var(--space-lg); }
.px-xl { padding-left: var(--space-xl); padding-right: var(--space-xl); }

.py-0 { padding-top: 0; padding-bottom: 0; }
.py-xs { padding-top: var(--space-xs); padding-bottom: var(--space-xs); }
.py-sm { padding-top: var(--space-sm); padding-bottom: var(--space-sm); }
.py-md { padding-top: var(--space-md); padding-bottom: var(--space-md); }
.py-lg { padding-top: var(--space-lg); padding-bottom: var(--space-lg); }
.py-xl { padding-top: var(--space-xl); padding-bottom: var(--space-xl); }

.pt-0 { padding-top: 0; }
.pt-xs { padding-top: var(--space-xs); }
.pt-sm { padding-top: var(--space-sm); }
.pt-md { padding-top: var(--space-md); }
.pt-lg { padding-top: var(--space-lg); }
.pt-xl { padding-top: var(--space-xl); }

.pb-0 { padding-bottom: 0; }
.pb-xs { padding-bottom: var(--space-xs); }
.pb-sm { padding-bottom: var(--space-sm); }
.pb-md { padding-bottom: var(--space-md); }
.pb-lg { padding-bottom: var(--space-lg); }
.pb-xl { padding-bottom: var(--space-xl); }

/* Responsive spacing utilities */
@media (min-width: 768px) {
  .md\:m-0 { margin: 0; }
  .md\:m-xs { margin: var(--space-xs); }
  .md\:m-sm { margin: var(--space-sm); }
  .md\:m-md { margin: var(--space-md); }
  .md\:m-lg { margin: var(--space-lg); }
  .md\:m-xl { margin: var(--space-xl); }
  
  /* Additional responsive margin utilities... */
  
  .md\:p-0 { padding: 0; }
  .md\:p-xs { padding: var(--space-xs); }
  .md\:p-sm { padding: var(--space-sm); }
  .md\:p-md { padding: var(--space-md); }
  .md\:p-lg { padding: var(--space-lg); }
  .md\:p-xl { padding: var(--space-xl); }
  
  /* Additional responsive padding utilities... */
}

@media (min-width: 1024px) {
  .lg\:m-0 { margin: 0; }
  .lg\:m-xs { margin: var(--space-xs); }
  .lg\:m-sm { margin: var(--space-sm); }
  .lg\:m-md { margin: var(--space-md); }
  .lg\:m-lg { margin: var(--space-lg); }
  .lg\:m-xl { margin: var(--space-xl); }
  
  /* Additional responsive margin utilities... */
  
  .lg\:p-0 { padding: 0; }
  .lg\:p-xs { padding: var(--space-xs); }
  .lg\:p-sm { padding: var(--space-sm); }
  .lg\:p-md { padding: var(--space-md); }
  .lg\:p-lg { padding: var(--space-lg); }
  .lg\:p-xl { padding: var(--space-xl); }
  
  /* Additional responsive padding utilities... */
}
```

## Accessibility Enhancements

### Focus Styles

```css
/* Global focus styles */
:focus {
  outline: none;
}

:focus-visible {
  outline: 2px solid var(--color-gold);
  outline-offset: 2px;
}

/* Button focus styles */
.btn:focus-visible {
  outline: 2px solid var(--color-gold);
  outline-offset: 2px;
  box-shadow: var(--shadow-focus);
}

/* Form input focus styles */
.form-input:focus-visible,
.form-textarea:focus-visible,
.form-select:focus-visible {
  outline: 2px solid var(--color-gold);
  outline-offset: 0;
  border-color: var(--color-gold);
  box-shadow: var(--shadow-focus);
}

/* Interactive element focus styles */
a:focus-visible,
button:focus-visible,
[role="button"]:focus-visible,
input[type="checkbox"]:focus-visible + label::before,
input[type="radio"]:focus-visible + label::before {
  outline: 2px solid var(--color-gold);
  outline-offset: 2px;
}
```

### Skip Link

```css
/* Skip to main content link */
.skip-link {
  position: absolute;
  top: -40px;
  left: 0;
  background: var(--color-navy);
  color: var(--color-winter-white);
  padding: var(--space-xs) var(--space-sm);
  z-index: var(--z-overlay);
  transition: top var(--duration-normal) var(--ease-default);
}

.skip-link:focus {
  top: 0;
}
```

```html
<!-- Skip link implementation -->
<a href="#main-content" class="skip-link">Skip to main content</a>
<main id="main-content">
  <!-- Main content here -->
</main>
```

### ARIA Attributes

```html
<!-- Navigation with ARIA attributes -->
<nav aria-label="Main navigation">
  <ul role="menubar">
    <li role="none">
      <a href="/" role="menuitem">Home</a>
    </li>
    <li role="none">
      <a href="/services" role="menuitem" aria-haspopup="true" aria-expanded="false">Services</a>
      <ul role="menu" aria-label="Services submenu">
        <li role="none">
          <a href="/services/residential" role="menuitem">Residential</a>
        </li>
        <li role="none">
          <a href="/services/commercial" role="menuitem">Commercial</a>
        </li>
      </ul>
    </li>
  </ul>
</nav>

<!-- Form with ARIA attributes -->
<form aria-labelledby="form-title">
  <h2 id="form-title">Contact Us</h2>
  
  <div class="form-group">
    <label for="name" id="name-label">Name</label>
    <input type="text" id="name" class="form-input" aria-labelledby="name-label" aria-required="true">
  </div>
  
  <div class="form-group">
    <label for="email" id="email-label">Email</label>
    <input type="email" id="email" class="form-input" aria-labelledby="email-label" aria-required="true">
    <div class="form-error-message" id="email-error" aria-live="polite"></div>
  </div>
  
  <button type="submit" aria-label="Submit form">Submit</button>
</form>

<!-- Modal with ARIA attributes -->
<div role="dialog" aria-labelledby="modal-title" aria-describedby="modal-description" aria-modal="true">
  <h2 id="modal-title">Schedule Consultation</h2>
  <p id="modal-description">Select your preferred date and time for a consultation.</p>
  
  <!-- Modal content -->
  
  <button aria-label="Close modal" class="modal-close">×</button>
</div>
```

### Reduced Motion

```css
/* Respect user preference for reduced motion */
@media (prefers-reduced-motion: reduce) {
  *,
  *::before,
  *::after {
    animation-duration: 0.01ms !important;
    animation-iteration-count: 1 !important;
    transition-duration: 0.01ms !important;
    scroll-behavior: auto !important;
  }
  
  .hero-bg-video {
    display: none;
  }
  
  .hero-bg-image {
    display: block;
  }
}
```

## Animation & Interaction Examples

### Button Hover Animation

```css
.btn {
  position: relative;
  overflow: hidden;
  transition: transform var(--duration-normal) var(--ease-default),
              box-shadow var(--duration-normal) var(--ease-default);
}

.btn::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(255, 255, 255, 0.1);
  transform: translateX(-100%);
  transition: transform var(--duration-normal) var(--ease-default);
}

.btn:hover {
  transform: translateY(-2px);
  box-shadow: var(--shadow-md);
}

.btn:hover::before {
  transform: translateX(0);
}

.btn:active {
  transform: translateY(0);
  box-shadow: var(--shadow-sm);
}
```

### Scroll Animation

```css
.fade-in {
  opacity: 0;
  transform: translateY(20px);
  transition: opacity var(--duration-slow) var(--ease-default),
              transform var(--duration-slow) var(--ease-default);
}

.fade-in.visible {
  opacity: 1;
  transform: translateY(0);
}
```

```javascript
// Intersection Observer for scroll animations
document.addEventListener('DOMContentLoaded', () => {
  const fadeElements = document.querySelectorAll('.fade-in');
  
  const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add('visible');
        observer.unobserve(entry.target);
      }
    });
  }, {
    threshold: 0.1,
    rootMargin: '0px 0px -50px 0px'
  });
  
  fadeElements.forEach(element => {
    observer.observe(element);
  });
});
```

### Gallery Hover Effect

```css
.gallery-item {
  position: relative;
  overflow: hidden;
  border-radius: var(--radius-md);
}

.gallery-item-image {
  width: 100%;
  height: 100%;
  object-fit: cover;
  transition: transform var(--duration-normal) var(--ease-default);
}

.gallery-item-overlay {
  position: absolute;
  bottom: 0;
  left: 0;
  right: 0;
  padding: var(--space-md);
  background: linear-gradient(to top, rgba(10, 35, 66, 0.8) 0%, rgba(10, 35, 66, 0) 100%);
  transform: translateY(100%);
  transition: transform var(--duration-normal) var(--ease-default);
}

.gallery-item:hover .gallery-item-image {
  transform: scale(1.05);
}

.gallery-item:hover .gallery-item-overlay {
  transform: translateY(0);
}
```

### Smooth Accordion

```css
.accordion-item {
  border-bottom: 1px solid var(--border-medium);
}

.accordion-header {
  padding: var(--space-md);
  cursor: pointer;
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.accordion-icon {
  transition: transform var(--duration-normal) var(--ease-default);
}

.accordion-content {
  max-height: 0;
  overflow: hidden;
  transition: max-height var(--duration-normal) var(--ease-default);
}

.accordion-item.active .accordion-icon {
  transform: rotate(180deg);
}

.accordion-item.active .accordion-content {
  max-height: 500px; /* Adjust based on content */
}
```

```javascript
// Accordion functionality
document.addEventListener('DOMContentLoaded', () => {
  const accordionHeaders = document.querySelectorAll('.accordion-header');
  
  accordionHeaders.forEach(header => {
    header.addEventListener('click', () => {
      const item = header.parentElement;
      const isActive = item.classList.contains('active');
      
      // Close all accordions
      document.querySelectorAll('.accordion-item').forEach(accordionItem => {
        accordionItem.classList.remove('active');
      });
      
      // If the clicked item wasn't active, open it
      if (!isActive) {
        item.classList.add('active');
      }
    });
  });
});
```