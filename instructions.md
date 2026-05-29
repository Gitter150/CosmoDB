# Teammate A: Master Interface, Grid Architecture & Global Controls Manual

This document provides absolute, mouse-click by mouse-click UI navigation blueprints for Teammate A. Your role is to construct the foundational application framework, establish global design parameters, build out the left control slicer panel, and engineer the top-level high-impact executive KPI metrics cards on **Page 1**.

---

## SECTION 1: GLOBAL VISUAL RE-ENGINEERING

Before adding new assets, you must optimize the canvas and apply high-contrast dark theme properties.

### Action 1.1: Canvas Inversion to High-Contrast Cosmic Black
1. Left-click any completely blank space on the white canvas area.
2. Navigate to the **Visualizations Pane** located on the right side of the screen.
3. Click the **Format page** sub-tab (the icon resembling a paint roller/paintbrush over a blank sheet of paper).
4. Expand the **Canvas background** chevron card.
5. Click the **Color** dropdown bucket and select **Pure Black** (`#000000`).
6. Drag the **Transparency** slider from its default 100% down to exactly **0%**.

### Action 1.2: Precision Layout Grid Initialization
1. Move your mouse to the main top ribbon menu and click on the **View** tab.
2. Locate the **Page options** configuration block.
3. Check the box for **Gridlines** to render architectural alignment layout dots across your canvas.
4. Check the box for **Snap to grid** to automate layout standardization.

---

## SECTION 2: THE LEFT CONTROL FILTER COLUMN

You will now construct a floating modular sidebar menu container housing your interactive macro-level slicers.

### Action 2.1: Designing the Structural Sidebar Container
1. Click on the **Insert** tab in the main top ribbon menu.
2. In the **Elements** group, click the **Shapes** dropdown menu arrow.
3. Select the **Rounded Rectangle** shape. A blue block will appear on your canvas.
4. With this new shape selected, look at the **Visualizations Pane** on the right side of your screen and click the **Format** tab (the paintbrush/page icon).
5. Choose the **General** sub-tab at the top of that section and expand the **Properties** card:
   * Set **Height** to `700`
   * Set **Width** to `250`
6. Expand the **Position** sub-card:
   * Set **Horizontal (X)** to `0`
   * Set **Vertical (Y)** to `0`
7. Now click back onto the **Shape** sub-tab next to *General*, and expand the **Style** card:
   * Under **Fill**, click the Color bucket and set it to a deep slate grey (`#161B26`).
   * Under **Border**, change the Color to a subtle grey line (`#2D323F`).
   * Under **Rounded Corners**, ensure the slider is dialed to **10px**.

### Action 2.2: Engineering Slicer 1 (Discovery Year Slider Track)
1. In the **Visualizations Pane**, locate the visual template grid and select the **Slicer** icon (represented by an interactive funnel next to a table layout).
2. Move your newly generated slicer element over the top portion of your left panel.
3. Navigate to the **Data Pane** on the absolute far-right margin. Expand the `cleaned_exoplanets` table.
4. Locate the **`Discovery_Year`** column and check its box (or drag-and-drop it into the **Field** bucket under the visual selector).
5. Click the **Format visual** tab (the paintbrush icon) on the Visualizations pane.
6. Under the **Visual** sub-tab, expand **Slicer settings** and look at the **Style** dropdown. Select **Between**.
7. Expand the **Values** card (controls the text input boxes):
   * Change **Font color** to **Pure White** (`#FFFFFF`) and select **Bold**.
   * Change the input box background color to a dark charcoal or leave as no fill.
8. Expand the **Slider** card:
   * Click the Color selector for the line track and handles and select your primary **Electric Cyan** (`#00F0FF`).
9. Expand the **Slicer header** card at the top:
   * Set **Font color** to your high-contrast **Electric Cyan** (`#00F0FF`), font weight to **Bold**.
10. Switch to the **General** sub-tab of this slicer's formatting options:
    * Expand **Effects** -> Toggle the **Background** switch to **OFF** (completely removing the clunky white background rectangle).
    * Expand **Properties** -> Set **Height** to `130` and **Width** to `220`. Move it via mouse to sit centered at the top of your sidebar.

### Action 2.3: Engineering Slicer 2 (Host Star Type Selection Buttons)
1. Click on a blank black space on the canvas to clear selection states.
2. Click the **Slicer** icon again in the Visualizations pane.
3. Move this second box inside your left sidebar container panel, dropping it directly below your `Discovery_Year` slider track.
4. From the far-right **Data Pane**, drag the engineered categorical column **`Host_Star_Type`** and drop it into the visual’s **Field** well.
5. Click the **Format visual** tab (the paintbrush icon) and select the **Visual** sub-tab.
6. Expand **Slicer settings**, click the **Style** dropdown, and change it from *Vertical List* to **Tile**. The checkboxes will instantly convert to flat application button tiles.
7. Expand the **Slices** or **Values** sub-card:
   * Set the text **Font color** to **Pure White** (`#FFFFFF`).
   * Set the tile **Background color** to a subtle contrast grey (`#2D323F`) or leave transparent to adopt the panel tone.
   * Set the selected/active tile border state to your neon **Electric Cyan** (`#00F0FF`).
8. Switch over to the **General** sub-tab:
   * Expand **Effects** -> Toggle the **Background** switch to **OFF**.
   * Expand **Properties** -> Set **Width** to `220`. Adjust the height to frame the five stellar class selection buttons cleanly.

---

## SECTION 3: THE STRATEGIC EXECUTIVE KPI HEADER BANNER

You will now construct high-visibility, big-number metrics running along the top header row of the dashboard, giving your visualization teacher an immediate sense of dataset scale.

### Action 3.1: KPI Card 1 (Total Confirmed Worlds Cataloged)
1. Click the **Card** visual icon inside the Visualizations pane (the rectangle containing a prominent `123` symbol).
2. Look at the **Data Pane** on the right, grab the **`Planet_Name`** column, and drop it directly into the **Fields** well.
3. Click the small down-arrow chevron next to `Planet_Name` inside your fields well and make sure it is explicitly checked as **Count** (not Count Distinct).
4. Click the **Format visual** tab (the paintbrush icon) and navigate to the **Visual** sub-tab:
   * Expand **Callout value**: Set font size to **32 pt**, weight to **Bold**, and select your primary **Electric Cyan** (`#00F0FF`) color selector.
   * Expand **Category label**: Turn it **OFF** (we will use a custom structured title card for cleaner presentation).
5. Switch to the **General** sub-tab of this card visual:
   * Expand **Title**: Toggle the switch to **ON**. Type `"TOTAL CONFIRMED EXOPLANETS"` in the Text box. Set its font family to *Segoe UI Semibold*, font color to **Pure White** (`#FFFFFF`), and size to **10 pt**.
   * Expand **Effects**: Ensure **Background** is **ON**. Set its fill color to your dark panel grey (`#161B26`). Toggle **Visual border** to **ON**, select a subtle grey color (`#2D323F`), and set **Rounded corners** to **10px**.
   * Expand **Properties**: Set **Height** to `85` and **Width** to `220`.
6. Position this card row horizontally at the top banner area, right next to your left control column.

### Action 3.2: KPI Card 2 (Unique Explored Star Systems)
1. Right-click your newly constructed Planet Count KPI card and select **Copy -> Copy visual**.
2. Click on any blank black space on the canvas and press **Ctrl + V** to paste a perfect duplicate.
3. With this duplicate selected, go to the fields well, click the **X** on `Planet_Name` to evict it.
4. From your **Data Pane**, drag the **`Host_Star_Name`** column and drop it into that empty field bucket.
5. Click the down-arrow chevron next to `Host_Star_Name` inside the well and change the math aggregation to **Count (Distinct)**. 
6. Switch to the **General** sub-tab -> expand **Title** -> update the Text block to read: `"UNIQUE HOST STAR SYSTEMS"`.
7. Move this card horizontally next to Card 1, ensuring a clean spatial gap between them.

### Action 3.3: KPI Card 3 (High-Probability Habitable Targets Found)
1. Copy Card 2 and press **Ctrl + V** to generate your third metric card.
2. Evict `Host_Star_Name` from its fields well.
3. From your **Data Pane**, drag your feature-engineered **`Habitability_Index`** column and drop it into the empty fields well. Set its aggregation to **Count**.
4. Look at the **Filters Pane** running vertically between your canvas and visual selectors. Locate the entry labeled **Filters on this visual**.
5. Click to expand the **`Habitability_Index`** visual filter card:
   * Change filter type to **Basic filtering**.
   * Check the boxes explicitly for **`Extremely Habitable`** and **`Moderately Habitable`** (leave the rest unchecked).
6. Switch to the **General** sub-tab -> expand **Title** -> update the text box to read: `"POTENTIALLY HABITABLE WORLDS"`.
7. Go to **Format Visual -> Visual -> Callout value** -> change the font color selector to your vibrant highlight tone: **Neon Gold/Amber** (`#FFB800`).
8. Place this card horizontally next to Card 2.

---

## SECTION 4: THE PIXEL-PERFECT LAYOUT ALIGNMENT SEQUENCE

To lock in an elite layout grid structure, use Power BI's structural math instead of trying to arrange objects by eye:

1. Hold down the **Ctrl** key on your computer keyboard and individually click KPI Card 1, KPI Card 2, and KPI Card 3 to highlight all three together.
2. A context-specific **Format** tab will appear at the absolute top ribbon menu layer. Click it.
3. Click the **Align** icon button to open the sub-menu:
   * Select **Align Top** (this forces their top borders to lock to the exact same pixel elevation).
   * Click the menu again and select **Distribute Horizontally** (this forces the white-space pixel gaps between the cards to become completely uniform).
4. With all three cards still selected as a group, look at the **Visualizations Pane** -> **Format** tab -> **General** sub-tab -> expand **Properties**:
   * Change **Vertical (Y)** position to exactly `15`. This shifts the entire banner cleanly into place.
5. Save your file as `Exoplanet_Master_Controls.pbix`. 

Your control infrastructure is complete. Stand by to receive Teammate B's data visualization charts via copy-paste to finalize the layout.