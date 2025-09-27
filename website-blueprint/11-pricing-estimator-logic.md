# Step 11: Pricing & Estimator Logic

## Pricing Strategy Framework

### Pricing Philosophy

1. **Value-Based Pricing Approach**
   - Pricing based on perceived value and outcomes rather than cost-plus
   - Emphasis on premium quality, expertise, and comprehensive service
   - Clear differentiation from commodity pricing of competitors
   - Transparent communication of value components
   - Avoidance of discount-driven promotions

2. **Strategic Positioning**
   - Positioned as premium service provider (top 10-15% of market)
   - Price point reflects architectural expertise and design quality
   - Higher than average market rates justified by superior results
   - Pricing reinforces brand perception of exclusivity and quality
   - Avoidance of price competition with standard installation services

3. **Client Investment Framing**
   - Language of "investment" rather than "cost" or "price"
   - Focus on property enhancement and experience value
   - Emphasis on long-term relationship and multi-year benefits
   - Clear articulation of ROI for commercial clients
   - Transparent explanation of quality differences

### Pricing Structure

1. **Base Pricing Factors**
   - Property type (residential, commercial, community)
   - Property size (square footage or linear footage)
   - Design complexity (standard, custom, signature)
   - Installation difficulty (architectural features, access challenges)
   - Geographic location (primary vs. extended service areas)

2. **Service Tiers**

   | Tier | Name | Description | Target Client | Price Point |
   |------|------|-------------|--------------|-------------|
   | **1** | **Signature Design** | Fully custom architectural lighting design with premium features, dedicated designer, and enhanced service package | Luxury estates, high-end commercial | $$$$$ |
   | **2** | **Custom Design** | Tailored lighting design with property-specific planning and quality components | Upscale homes, quality-focused businesses | $$$$ |
   | **3** | **Classic Design** | Pre-designed lighting packages with limited customization options | Standard homes, budget-conscious clients | $$$ |

3. **Add-On Services**

   | Service | Description | Price Structure |
   |---------|-------------|----------------|
   | **Storage Program** | Professional removal, cleaning, testing, and storage of lighting components | Annual fee (15-20% of installation) |
   | **Mid-Season Check** | Proactive maintenance visit to ensure optimal display | Fixed fee ($150-250) |
   | **Extended Display** | Additional weeks beyond standard season | Weekly fee (10-15% of base price) |
   | **Design Preview** | 3D visualization of property with lighting design | Complimentary with Signature, fee for others |
   | **Smart Controls** | App-controlled lighting with scheduling and effects | Component cost plus programming fee |
   | **Event Lighting** | Special occasion temporary enhancement | Hourly rate plus equipment rental |
   | **Storm Response** | Priority service after weather events | Included in Signature, fee for others |

4. **Package Options**

   | Package | Included Elements | Target Client | Price Range |
   |---------|-------------------|--------------|-------------|
   | **Complete Estate** | Full property lighting (roofline, landscape, pathways, trees, architectural features) | Luxury estates | $3,500-15,000+ |
   | **Architectural Highlight** | Roofline, key architectural features, and focal point trees | Upscale homes | $2,500-6,000 |
   | **Classic Elegance** | Roofline and limited accent lighting | Standard homes | $1,500-3,500 |
   | **Commercial Storefront** | Facade, windows, entrance, and signage | Retail businesses | $2,000-7,500 |
   | **Commercial Property** | Building exterior, parking areas, landscape features | Office/commercial buildings | $5,000-20,000+ |
   | **Community Entrance** | Gateway features, signage, and landscape elements | HOAs, neighborhoods | $3,500-10,000 |

### Pricing Communication Strategy

1. **Transparency Approach**
   - Clear explanation of pricing factors
   - Upfront communication about investment ranges
   - No hidden fees or unexpected charges
   - Detailed line-item proposals
   - Value justification for each component

2. **Price Presentation**
   - Range-based pricing on website and marketing materials
   - Specific pricing only after property assessment
   - Emphasis on value and outcomes in all pricing discussions
   - Comparison tools highlighting included services
   - Visual examples of different investment levels

3. **Objection Handling Framework**
   - Prepared responses to common price objections
   - Value comparison tools for competitive situations
   - ROI calculators for commercial clients
   - Financing options for larger installations
   - Tiered options to accommodate different budgets

## Pricing Formula Specifications

### Residential Pricing Formula

```
Base Price = (Linear Footage × Rate Factor) + (Design Complexity Multiplier)

Where:
- Linear Footage = Total linear feet of installation areas
- Rate Factor = Base rate per linear foot based on service tier
  * Signature: $18-25 per linear foot
  * Custom: $14-18 per linear foot
  * Classic: $10-14 per linear foot
- Design Complexity Multiplier:
  * Standard: 1.0x
  * Moderate: 1.2x
  * Complex: 1.5x
  * Highly Complex: 2.0x
```

#### Adjustment Factors

1. **Property Type Adjustment**
   - Single-story home: 1.0x
   - Two-story home: 1.2x
   - Three+ story home: 1.5x
   - Estate property: 1.8x

2. **Architectural Complexity**
   - Simple rooflines: 1.0x
   - Moderate complexity: 1.2x
   - High complexity: 1.5x
   - Custom architectural features: 1.8x

3. **Installation Difficulty**
   - Standard access: 1.0x
   - Moderate difficulty: 1.15x
   - Challenging access: 1.3x
   - Extreme difficulty: 1.5x

4. **Geographic Location**
   - Primary service area: 1.0x
   - Secondary service area: 1.1x
   - Extended service area: 1.25x

5. **Seasonal Timing**
   - Early booking (Jan-Jul): 0.9x
   - Standard booking (Aug-Oct): 1.0x
   - Late booking (Nov): 1.15x
   - Rush installation (Dec): 1.25x

### Commercial Pricing Formula

```
Base Price = (Square Footage × Base Rate) × (Property Type Factor) × (Complexity Factor)

Where:
- Square Footage = Total exterior square footage
- Base Rate = Starting rate per square foot
  * Standard: $0.75-1.25 per sq ft
  * Premium: $1.25-2.00 per sq ft
  * Signature: $2.00-3.50 per sq ft
- Property Type Factor:
  * Retail/Storefront: 1.2x
  * Office Building: 1.0x
  * Restaurant: 1.3x
  * Hotel/Hospitality: 1.4x
  * Industrial: 0.8x
- Complexity Factor:
  * Basic: 1.0x
  * Standard: 1.2x
  * Complex: 1.5x
  * Custom Design: 2.0x
```

#### Commercial Adjustment Factors

1. **Visibility Factor**
   - Low visibility location: 0.9x
   - Standard visibility: 1.0x
   - High visibility/corner: 1.2x
   - Landmark location: 1.5x

2. **Contract Length**
   - Single season: 1.0x
   - Two-year contract: 0.9x
   - Three-year contract: 0.85x
   - Five-year contract: 0.8x

3. **Installation Timing**
   - Off-peak installation: 0.9x
   - Standard timing: 1.0x
   - Peak season rush: 1.2x
   - Last-minute installation: 1.3x

4. **Additional Services**
   - Basic package: 1.0x
   - With storage program: 1.15x
   - With maintenance plan: 1.2x
   - All-inclusive package: 1.3x

### Community/HOA Pricing Formula

```
Base Price = (Entrance Linear Footage × Rate) + (Common Area Square Footage × Area Rate) + (Feature Lighting Cost)

Where:
- Entrance Linear Footage = Linear feet of entrance areas
- Rate = Per linear foot rate ($15-30)
- Common Area Square Footage = Square footage of common areas
- Area Rate = Per square foot rate ($0.50-1.50)
- Feature Lighting Cost = Sum of special feature lighting costs
```

#### Community Adjustment Factors

1. **Community Size**
   - Small (under 50 homes): 1.0x
   - Medium (50-200 homes): 1.2x
   - Large (200+ homes): 1.5x

2. **Design Exclusivity**
   - Standard design: 1.0x
   - Custom community design: 1.3x
   - Signature exclusive design: 1.8x

3. **Contract Structure**
   - Single season: 1.0x
   - Multi-year contract: 0.85-0.95x
   - Community-wide program: 0.8-0.9x

4. **Installation Complexity**
   - Standard installation: 1.0x
   - Complex installation: 1.2x
   - Phased installation: 1.15x

## Online Estimator Tool Logic

### Estimator Interface Design

```
┌─────────────────────────────────────────────────────────┐
│                                                         │
│  [Tool Headline]                                        │
│  Holiday Lighting Investment Estimator                  │
│                                                         │
│  [Tool Description]                                     │
│  Get an approximate investment range based on your      │
│  property details. For an exact quote, schedule a       │
│  consultation.                                          │
│                                                         │
│  ┌─────────────────────────────────────────────────────┐│
│  │ Step 1: Property Type ▾                             ││
│  └─────────────────────────────────────────────────────┘│
│                                                         │
│  ┌─────────────────────────────────────────────────────┐│
│  │ Step 2: Property Size ▾                             ││
│  └─────────────────────────────────────────────────────┘│
│                                                         │
│  ┌─────────────────────────────────────────────────────┐│
│  │ Step 3: Design Level ▾                              ││
│  └─────────────────────────────────────────────────────┘│
│                                                         │
│  ┌─────────────────────────────────────────────────────┐│
│  │ Step 4: Select Areas to Illuminate                   ││
│  │                                                     ││
│  │ □ Roofline                                          ││
│  │ □ Windows & Doors                                   ││
│  │ □ Trees & Landscaping                               ││
│  │ □ Pathways & Driveways                              ││
│  │ □ Architectural Features                            ││
│  │ □ Yard Displays                                     ││
│  └─────────────────────────────────────────────────────┘│
│                                                         │
│  ┌─────────────────────────────────────────────────────┐│
│  │ Step 5: Additional Services                          ││
│  │                                                     ││
│  │ □ Professional Storage Program                      ││
│  │ □ Mid-Season Maintenance Check                      ││
│  │ □ Extended Display Period                           ││
│  │ □ Smart Control System                              ││
│  └─────────────────────────────────────────────────────┘│
│                                                         │
│  [Calculate Button]                                     │
│                                                         │
│  ┌─────────────────────────────────────────────────────┐│
│  │ [Results Section - Initially Hidden]                ││
│  │                                                     ││
│  │ Estimated Investment Range:                         ││
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

### Estimator Input Options

1. **Property Type**
   - Single-Family Home
   - Estate/Large Property
   - Townhome/Condo
   - Retail/Storefront
   - Office Building
   - Restaurant/Hospitality
   - Community/HOA

2. **Property Size**
   - **Residential**:
     * Small (under 2,500 sq ft)
     * Medium (2,500-4,000 sq ft)
     * Large (4,000-6,000 sq ft)
     * Estate (6,000+ sq ft)
   - **Commercial**:
     * Small (under 5,000 sq ft)
     * Medium (5,000-15,000 sq ft)
     * Large (15,000-30,000 sq ft)
     * Campus (30,000+ sq ft)
   - **Community**:
     * Small (single entrance)
     * Medium (2-3 features)
     * Large (multiple entrances/areas)

3. **Design Level**
   - Classic (standard designs)
   - Custom (tailored to property)
   - Signature (fully custom architectural design)

4. **Areas to Illuminate**
   - Roofline
   - Windows & Doors
   - Trees & Landscaping
   - Pathways & Driveways
   - Architectural Features
   - Yard Displays

5. **Additional Services**
   - Professional Storage Program
   - Mid-Season Maintenance Check
   - Extended Display Period
   - Smart Control System

### Estimator Calculation Logic

```javascript
function calculateEstimate(inputs) {
  // Initialize base price
  let basePrice = 0;
  let minMultiplier = 0.85; // For lower range
  let maxMultiplier = 1.15; // For upper range
  
  // Step 1: Calculate base price by property type and size
  if (inputs.propertyType === 'single-family') {
    switch (inputs.propertySize) {
      case 'small':
        basePrice = 1500;
        break;
      case 'medium':
        basePrice = 2500;
        break;
      case 'large':
        basePrice = 4000;
        break;
      case 'estate':
        basePrice = 7500;
        break;
    }
  } else if (inputs.propertyType === 'commercial') {
    switch (inputs.propertySize) {
      case 'small':
        basePrice = 2000;
        break;
      case 'medium':
        basePrice = 5000;
        break;
      case 'large':
        basePrice = 10000;
        break;
      case 'campus':
        basePrice = 20000;
        break;
    }
  } else if (inputs.propertyType === 'community') {
    switch (inputs.propertySize) {
      case 'small':
        basePrice = 3500;
        break;
      case 'medium':
        basePrice = 7500;
        break;
      case 'large':
        basePrice = 15000;
        break;
    }
  }
  
  // Step 2: Apply design level multiplier
  let designMultiplier = 1.0;
  switch (inputs.designLevel) {
    case 'classic':
      designMultiplier = 1.0;
      break;
    case 'custom':
      designMultiplier = 1.3;
      break;
    case 'signature':
      designMultiplier = 1.8;
      break;
  }
  basePrice *= designMultiplier;
  
  // Step 3: Add costs for selected areas
  let areaMultiplier = 1.0;
  let selectedAreas = inputs.areasToIlluminate;
  
  if (selectedAreas.includes('roofline')) {
    areaMultiplier += 0.3;
  }
  if (selectedAreas.includes('windows-doors')) {
    areaMultiplier += 0.2;
  }
  if (selectedAreas.includes('trees-landscaping')) {
    areaMultiplier += 0.25;
  }
  if (selectedAreas.includes('pathways-driveways')) {
    areaMultiplier += 0.15;
  }
  if (selectedAreas.includes('architectural-features')) {
    areaMultiplier += 0.25;
  }
  if (selectedAreas.includes('yard-displays')) {
    areaMultiplier += 0.2;
  }
  
  basePrice *= areaMultiplier;
  
  // Step 4: Add costs for additional services
  let additionalServices = inputs.additionalServices;
  let additionalCost = 0;
  
  if (additionalServices.includes('storage-program')) {
    additionalCost += basePrice * 0.15;
  }
  if (additionalServices.includes('maintenance-check')) {
    additionalCost += 200;
  }
  if (additionalServices.includes('extended-display')) {
    additionalCost += basePrice * 0.1;
  }
  if (additionalServices.includes('smart-control')) {
    additionalCost += 500;
  }
  
  basePrice += additionalCost;
  
  // Step 5: Calculate range
  let minPrice = Math.round(basePrice * minMultiplier / 100) * 100;
  let maxPrice = Math.round(basePrice * maxMultiplier / 100) * 100;
  
  return {
    minPrice: minPrice,
    maxPrice: maxPrice,
    includedServices: getIncludedServices(inputs)
  };
}

function getIncludedServices(inputs) {
  let services = [
    'Professional design consultation',
    'Custom installation plan',
    'Premium commercial-grade lights',
    'Professional installation',
    'Maintenance throughout season',
    'Complete removal'
  ];
  
  let additionalServices = inputs.additionalServices;
  
  if (additionalServices.includes('storage-program')) {
    services.push('Off-season professional storage');
  }
  if (additionalServices.includes('maintenance-check')) {
    services.push('Mid-season maintenance check');
  }
  if (additionalServices.includes('extended-display')) {
    services.push('Extended display period');
  }
  if (additionalServices.includes('smart-control')) {
    services.push('Smart control system');
  }
  
  return services;
}
```

### Estimator Results Presentation

1. **Price Range Display**
   - Clear investment range (minimum to maximum)
   - Prominent, easy-to-read format
   - Context for the estimate (what factors influence it)
   - Explanation that final quote may vary based on site assessment

2. **Included Services List**
   - Bulleted list of all included services
   - Emphasis on comprehensive nature of service
   - Highlighting of premium elements
   - Clear differentiation from DIY or basic services

3. **Next Steps Guidance**
   - Primary CTA: Schedule consultation
   - Secondary CTA: Refine estimate
   - Explanation of consultation process
   - Timeline expectations for installation

4. **Additional Information**
   - Financing options if available
   - Early booking incentives
   - Availability information
   - Testimonials from similar projects

## Exact Quote vs. Range Explanation

### Distinction Communication

1. **Estimator Purpose Statement**
   - Clear explanation that online tool provides approximate range
   - Transparency about factors that affect final pricing
   - Explanation of why in-person assessment is necessary
   - Value proposition of the consultation process

2. **Consultation Value Proposition**
   - Detailed property assessment
   - Professional design recommendations
   - Precise measurements
   - Customized lighting plan
   - Exact investment amount
   - Timeline and logistics planning

3. **Range vs. Exact Quote Messaging**

   **Website Copy Example**:
   
   > "Our online estimator provides an approximate investment range based on typical properties with similar characteristics. For an exact quote tailored to your specific property's architecture, access requirements, and design preferences, we recommend a complimentary on-site consultation with our lighting design specialist.
   > 
   > During your consultation, our designer will:
   > 
   > - Assess your property's unique architectural features
   > - Take precise measurements for accurate pricing
   > - Discuss your aesthetic preferences and goals
   > - Identify any special installation considerations
   > - Create a custom lighting design concept
   > - Provide an exact investment amount with no obligation
   > 
   > This personalized approach ensures you receive an accurate quote and a lighting design that perfectly complements your property's distinctive character."

### Quote Process Workflow

1. **Initial Estimate** (Online Tool)
   - Customer inputs basic property information
   - System calculates approximate range
   - Range presented with included services
   - Consultation scheduling option provided

2. **Design Consultation** (In-Person)
   - Designer visits property
   - Detailed measurements taken
   - Client preferences discussed
   - Architectural features assessed
   - Installation challenges identified
   - Preliminary design concepts presented

3. **Custom Proposal** (Post-Consultation)
   - Detailed lighting design created
   - Precise measurements incorporated
   - Exact pricing calculated
   - Line-item proposal prepared
   - Optional enhancements included
   - Installation timeline proposed

4. **Proposal Presentation** (In-Person or Virtual)
   - Walkthrough of design concept
   - Explanation of investment breakdown
   - Discussion of options and alternatives
   - Addressing of questions and concerns
   - Contract and deposit process explained

5. **Booking Confirmation** (Final Step)
   - Contract signing
   - Installation date selection
   - Deposit payment
   - Pre-installation preparation instructions
   - Introduction to installation team

## Upsell Path Strategy

### Core Upsell Opportunities

1. **Storage Program**
   - **Value Proposition**: Professional removal, cleaning, testing, and climate-controlled storage of lighting components
   - **Timing**: Present during initial consultation and proposal
   - **Pricing**: 15-20% of installation cost annually
   - **Messaging Focus**: Convenience, extended product life, guaranteed availability

2. **Storm Check Service**
   - **Value Proposition**: Priority service after severe weather events
   - **Timing**: Present during proposal and installation
   - **Pricing**: $150-250 per visit or included in premium packages
   - **Messaging Focus**: Peace of mind, rapid response, display integrity

3. **Extended Display Period**
   - **Value Proposition**: Additional weeks of display beyond standard period
   - **Timing**: Present during proposal and mid-season
   - **Pricing**: 10-15% of installation cost per additional week
   - **Messaging Focus**: Extended enjoyment, special occasions, maximum value

4. **Smart Control Upgrade**
   - **Value Proposition**: App-controlled lighting with scheduling and effects
   - **Timing**: Present during design consultation
   - **Pricing**: $500-1,500 depending on system complexity
   - **Messaging Focus**: Convenience, customization, modern technology

5. **Mid-Season Refresh**
   - **Value Proposition**: Mid-season maintenance visit to ensure optimal display
   - **Timing**: Present during installation and follow-up
   - **Pricing**: $150-300 depending on property size
   - **Messaging Focus**: Maintained perfection, weather resilience, professional care

### Upsell Presentation Strategy

1. **Tiered Package Structure**
   - Present good-better-best options
   - Include progressively more services at each tier
   - Highlight most popular option
   - Show value comparison between tiers
   - Make recommendations based on property needs

2. **Bundling Approach**
   - Create logical service bundles with price advantage
   - Example: "Complete Care Package" (installation, mid-season check, removal, storage)
   - Example: "Multi-Year Program" (guaranteed pricing for 3 years)
   - Example: "Smart Lighting Bundle" (smart controls, app setup, training)
   - Demonstrate savings versus à la carte pricing

3. **Timing-Based Incentives**
   - Early booking discounts (10-15% for booking by July)
   - Multi-year contract discounts (5-10% per year)
   - Last-minute add-on specials
   - Renewal incentives for returning clients
   - Referral bonuses for existing clients

### Upsell Implementation Points

1. **Website Integration**
   - Featured add-ons in estimator tool
   - Comparison charts showing package differences
   - Testimonials specific to premium services
   - Visual examples of standard vs. enhanced options
   - Clear value propositions for each upgrade

2. **Consultation Process**
   - Needs assessment questions to identify upgrade opportunities
   - Visual aids showing difference between standard and premium options
   - Property-specific recommendations for enhancements
   - ROI discussion for commercial clients
   - "Good investment" framing for residential clients

3. **Proposal Presentation**
   - Tiered options in all proposals
   - Visual highlighting of recommended tier
   - Clear explanation of differences between tiers
   - Easy upgrade path from base proposal
   - Limited-time incentives when appropriate

4. **Post-Installation Opportunities**
   - Follow-up contact for additional services
   - Mid-season enhancement options
   - Next-season early booking incentives
   - Referral program introduction
   - Loyalty program for returning clients

## Pricing Page Design

### Pricing Page Structure

```
┌─────────────────────────────────────────────────────────┐
│                                                         │
│  [Page Headline]                                        │
│  Investment in Architectural Holiday Lighting           │
│                                                         │
│  [Page Introduction]                                    │
│  Understanding the value and factors that determine     │
│  your holiday lighting investment.                      │
│                                                         │
│  ┌─────────────────────────────────────────────────────┐│
│  │                                                     ││
│  │  [Section: Our Approach to Pricing]                 ││
│  │  Explanation of value-based pricing philosophy      ││
│  │  and quality differentiation                        ││
│  │                                                     ││
│  └─────────────────────────────────────────────────────┘│
│                                                         │
│  ┌─────────────────────────────────────────────────────┐│
│  │                                                     ││
│  │  [Section: Service Tiers]                           ││
│  │                                                     ││
│  │  ┌─────────┐    ┌─────────┐    ┌─────────┐         ││
│  │  │         │    │         │    │         │         ││
│  │  │ Classic │    │ Custom  │    │Signature│         ││
│  │  │ Design  │    │ Design  │    │ Design  │         ││
│  │  │         │    │         │    │         │         ││
│  │  │ $$$     │    │ $$$$    │    │ $$$$$   │         ││
│  │  │         │    │         │    │         │         ││
│  │  │[Features]    │[Features]    │[Features]         ││
│  │  │         │    │         │    │         │         ││
│  │  │[Learn More]  │[Learn More]  │[Learn More]       ││
│  │  └─────────┘    └─────────┘    └─────────┘         ││
│  │                                                     ││
│  └─────────────────────────────────────────────────────┘│
│                                                         │
│  ┌─────────────────────────────────────────────────────┐│
│  │                                                     ││
│  │  [Section: Investment Ranges]                       ││
│  │                                                     ││
│  │  Residential Properties:                            ││
│  │  • Small Home: $1,500-3,500                         ││
│  │  • Medium Home: $2,500-5,000                        ││
│  │  • Large Home: $4,000-8,000                         ││
│  │  • Estate: $7,500-15,000+                           ││
│  │                                                     ││
│  │  Commercial Properties:                             ││
│  │  • Retail/Storefront: $2,000-7,500                  ││
│  │  • Office Building: $5,000-20,000+                  ││
│  │  • Restaurant/Hospitality: $3,000-10,000            ││
│  │                                                     ││
│  │  Community/HOA:                                     ││
│  │  • Entrance Features: $3,500-10,000                 ││
│  │  • Common Areas: $5,000-15,000                      ││
│  │  • Complete Community: Custom Pricing               ││
│  │                                                     ││
│  └─────────────────────────────────────────────────────┘│
│                                                         │
│  ┌─────────────────────────────────────────────────────┐│
│  │                                                     ││
│  │  [Section: Factors That Affect Pricing]             ││
│  │                                                     ││
│  │  [Icon] Property Size & Type                        ││
│  │  [Description]                                      ││
│  │                                                     ││
│  │  [Icon] Design Complexity                           ││
│  │  [Description]                                      ││
│  │                                                     ││
│  │  [Icon] Installation Challenges                     ││
│  │  [Description]                                      ││
│  │                                                     ││
│  │  [Icon] Selected Features                           ││
│  │  [Description]                                      ││
│  │                                                     ││
│  │  [Icon] Additional Services                         ││
│  │  [Description]                                      ││
│  │                                                     ││
│  └─────────────────────────────────────────────────────┘│
│                                                         │
│  ┌─────────────────────────────────────────────────────┐│
│  │                                                     ││
│  │  [Section: Estimator Tool]                          ││
│  │  Get an approximate investment range for your       ││
│  │  property with our online estimator tool.           ││
│  │                                                     ││
│  │  [Try Estimator Tool Button]                        ││
│  │                                                     ││
│  └─────────────────────────────────────────────────────┘│
│                                                         │
│  ┌─────────────────────────────────────────────────────┐│
│  │                                                     ││
│  │  [Section: Financing Options]                       ││
│  │  Information about available payment plans and      ││
│  │  financing options.                                 ││
│  │                                                     ││
│  └─────────────────────────────────────────────────────┘│
│                                                         │
│  ┌─────────────────────────────────────────────────────┐│
│  │                                                     ││
│  │  [Section: FAQ About Pricing]                       ││
│  │  Common questions about pricing, packages, and      ││
│  │  payment options.                                   ││
│  │                                                     ││
│  └─────────────────────────────────────────────────────┘│
│                                                         │
│  ┌─────────────────────────────────────────────────────┐│
│  │                                                     ││
│  │  [Section: CTA]                                     ││
│  │  Ready for an exact quote? Schedule your            ││
│  │  complimentary design consultation.                 ││
│  │                                                     ││
│  │  [Schedule Consultation Button]                     ││
│  │                                                     ││
│  └─────────────────────────────────────────────────────┘│
│                                                         │
└─────────────────────────────────────────────────────────┘
```

### Pricing Page Content

1. **Page Introduction**

   > "At [Company Name], we believe in transparent, value-based pricing that reflects the premium quality, expert design, and exceptional service we provide. Unlike standard holiday lighting companies that offer one-size-fits-all solutions, our architectural approach requires a customized investment based on your property's unique characteristics and your specific design goals.
   >
   > The investment ranges below provide general guidance, while our online estimator tool offers a more tailored approximation. For an exact quote, we recommend scheduling a complimentary design consultation with our lighting specialists."

2. **Our Approach to Pricing**

   > "Our pricing philosophy centers on delivering exceptional value through:
   >
   > - **Architectural Design Expertise**: Custom lighting plans that enhance your property's unique features
   > - **Premium Materials**: Commercial-grade components with superior durability and appearance
   > - **Professional Installation**: Meticulous attention to detail and proper installation techniques
   > - **Comprehensive Service**: From initial design through maintenance and removal
   > - **Peace of Mind**: Full warranty coverage and responsive support throughout the season
   >
   > Rather than competing on price with companies using retail-grade products and seasonal labor, we focus on delivering a superior experience and result that justifies a premium investment."

3. **Service Tiers**

   **Classic Design**
   > "Our Classic Design tier offers elegant, traditional holiday lighting with quality components and professional installation. Ideal for clients seeking a beautiful display with proven design elements.
   >
   > **Starting at $1,500 for residential properties**
   >
   > **Includes:**
   > - Professional consultation
   > - Quality commercial-grade lighting
   > - Standard design templates
   > - Professional installation
   > - Basic maintenance
   > - Post-season removal
   >
   > **Ideal for:** Standard homes and properties seeking traditional holiday elegance."

   **Custom Design**
   > "Our Custom Design tier provides tailored lighting solutions that highlight your property's unique architectural features with distinctive design elements and premium components.
   >
   > **Starting at $2,500 for residential properties**
   >
   > **Includes:**
   > - Detailed design consultation
   > - Premium commercial-grade lighting
   > - Property-specific custom design
   > - Professional installation
   > - Proactive maintenance
   > - Post-season removal
   > - Basic smart controls
   >
   > **Ideal for:** Distinctive homes and businesses seeking a customized lighting experience."

   **Signature Design**
   > "Our Signature Design tier delivers the ultimate in architectural holiday lighting with fully bespoke designs, the highest quality components, and white-glove service throughout the season.
   >
   > **Starting at $5,000 for residential properties**
   >
   > **Includes:**
   > - Comprehensive design process
   > - Highest-grade architectural lighting
   > - Fully custom design with 3D preview
   > - White-glove installation
   > - Priority maintenance with weekly checks
   > - Careful removal and storage
   > - Advanced smart control system
   >
   > **Ideal for:** Luxury estates and premium commercial properties seeking an unparalleled lighting experience."

4. **Factors That Affect Pricing**

   **Property Size & Type**
   > "Larger properties and those with multiple structures require more materials and installation time. Commercial properties often have different requirements than residential ones, affecting overall investment."

   **Design Complexity**
   > "Custom designs with multiple lighting techniques and special features require more planning, specialized components, and installation expertise than standard designs."

   **Installation Challenges**
   > "Properties with steep rooflines, limited access points, or unusual architectural features may require specialized equipment and additional installation time."

   **Selected Features**
   > "The specific areas you choose to illuminate—rooflines, trees, pathways, architectural features—each contribute to the overall investment."

   **Additional Services**
   > "Optional services such as our storage program, smart control systems, or extended display periods will affect your total investment."

5. **FAQ About Pricing**

   **Q: Why is there a range rather than an exact price?**
   > "Every property is unique in terms of size, architectural features, access challenges, and design requirements. These factors significantly impact the materials, time, and expertise required. We provide exact pricing after a professional assessment of your specific property."

   **Q: What's included in my investment?**
   > "Your investment covers the entire experience: professional design consultation, premium commercial-grade lighting components, expert installation, proactive maintenance throughout the season, responsive service if issues arise, and complete removal after the season. Unlike DIY solutions or budget providers, there are no hidden costs or additional work required on your part."

   **Q: Do you offer any discounts?**
   > "We offer early booking incentives for clients who secure their installation date before August. We also provide multi-year contract options for commercial clients and returning customer benefits. However, we don't discount our standard pricing as it would compromise our ability to deliver the premium experience our clients expect."

   **Q: How does your pricing compare to competitors?**
   > "Our investment ranges are higher than budget providers who use retail-grade products and seasonal labor. However, clients choose us for our architectural design approach, premium materials, installation expertise, and comprehensive service—delivering superior results and long-term value that justify the investment difference."

   **Q: Do you offer payment plans?**
   > "Yes, we offer flexible payment options including installment plans and financing for larger projects. Typically, we require a 50% deposit to secure your installation date, with the balance due upon completion."