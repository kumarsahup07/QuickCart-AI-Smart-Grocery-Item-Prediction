"""
Catalog Generator for QuickCart AI.
Generates 1,000+ distinct, authentic Indian supermarket & grocery items across:
- Snacks & Munchies
- Atta, Rice & Dals (Lunch & Dinner Staples)
- Breakfast & Instant Foods
- Dairy, Bread & Eggs
- Masalas & Spices
- Tea, Coffee & Beverages
- Sauces, Spreads & Condiments
"""

import json
from pathlib import Path

# Paths
ROOT_DIR = Path(__file__).resolve().parent.parent
ITEMS_JSON_ROOT = ROOT_DIR / "items.json"
ITEMS_JSON_SRC = ROOT_DIR / "src" / "items.json"

# Load original 24 items to preserve them exactly
with open(ITEMS_JSON_ROOT, "r", encoding="utf-8") as f:
    existing_items = json.load(f)

existing_ids = {item["id"] for item in existing_items}
all_items = list(existing_items)

print(f"Loaded {len(existing_items)} existing items.")

def add_item(item_id, name, category, price, rating, unit, badge, image_url, description, pairing_text):
    clean_id = item_id.lower().replace(" ", "_").replace("-", "_").replace("&", "and").replace("'", "").replace(".", "")
    if not clean_id.startswith("item_"):
        clean_id = f"item_{clean_id}"
    
    if clean_id in existing_ids:
        # Append unique suffix if colliding
        idx = 2
        while f"{clean_id}_{idx}" in existing_ids:
            idx += 1
        clean_id = f"{clean_id}_{idx}"
        
    existing_ids.add(clean_id)
    all_items.append({
        "id": clean_id,
        "name": name,
        "category": category,
        "price": round(float(price), 1),
        "rating": round(float(rating), 1),
        "unit": unit,
        "badge": badge,
        "image_url": image_url,
        "description": description,
        "pairing_text": pairing_text
    })

# Curated High-Res Unsplash Images by Product Type
IMG_SNACKS_CHIPS = "https://images.unsplash.com/photo-1566478989037-eec170784d0b?w=600&auto=format&fit=crop&q=80"
IMG_SNACKS_NAMKEEN = "https://images.unsplash.com/photo-1599488615731-7e5c2823ff28?w=600&auto=format&fit=crop&q=80"
IMG_SNACKS_BISCUITS = "https://images.unsplash.com/photo-1558961363-fa8fdf82db35?w=600&auto=format&fit=crop&q=80"
IMG_SNACKS_COOKIES = "https://images.unsplash.com/photo-1499636136210-6f4ee915583e?w=600&auto=format&fit=crop&q=80"
IMG_SNACKS_NUTS = "https://images.unsplash.com/photo-1508061253366-f7da158b6d46?w=600&auto=format&fit=crop&q=80"
IMG_SNACKS_CHOCOLATE = "https://images.unsplash.com/photo-1549007994-cb92caebd54b?w=600&auto=format&fit=crop&q=80"
IMG_SNACKS_SWEETS = "https://images.unsplash.com/photo-1599785209707-a456fc1337bb?w=600&auto=format&fit=crop&q=80"

IMG_RICE = "https://images.unsplash.com/photo-1586201375761-83865001e31c?w=600&auto=format&fit=crop&q=80"
IMG_DAL = "https://images.unsplash.com/photo-1546069901-ba9599a7e63c?w=600&auto=format&fit=crop&q=80"
IMG_ATTA = "https://images.unsplash.com/photo-1509440159596-0249088772ff?w=600&auto=format&fit=crop&q=80"
IMG_OIL = "https://images.unsplash.com/photo-1474979266404-7eaacbcd87c5?w=600&auto=format&fit=crop&q=80"
IMG_GHEE = "https://images.unsplash.com/photo-1631452180519-c014fe946bc7?w=600&auto=format&fit=crop&q=80"
IMG_PULSES = "https://images.unsplash.com/photo-1515543237350-b3eea1ec8082?w=600&auto=format&fit=crop&q=80"
IMG_READY_MEAL = "https://images.unsplash.com/photo-1589301760014-d929f3979dbc?w=600&auto=format&fit=crop&q=80"

IMG_NOODLES = "https://images.unsplash.com/photo-1612927601601-6638404737ce?w=600&auto=format&fit=crop&q=80"
IMG_OATS = "https://images.unsplash.com/photo-1517673132405-a56a62b18caf?w=600&auto=format&fit=crop&q=80"
IMG_BATTER = "https://images.unsplash.com/photo-1589301760014-d929f3979dbc?w=600&auto=format&fit=crop&q=80"
IMG_JAM_HONEY = "https://images.unsplash.com/photo-1584308666744-24d5c474f2ae?w=600&auto=format&fit=crop&q=80"
IMG_PASTA = "https://images.unsplash.com/photo-1551462147-ff29053bfc14?w=600&auto=format&fit=crop&q=80"

IMG_MILK = "https://images.unsplash.com/photo-1550583724-b2692b85b150?w=600&auto=format&fit=crop&q=80"
IMG_BUTTER = "https://images.unsplash.com/photo-1589985270826-4b7bb135bc9d?w=600&auto=format&fit=crop&q=80"
IMG_CHEESE = "https://images.unsplash.com/photo-1618160702438-9b02ab6515c9?w=600&auto=format&fit=crop&q=80"
IMG_PANEER = "https://images.unsplash.com/photo-1631452180519-c014fe946bc7?w=600&auto=format&fit=crop&q=80"
IMG_BREAD = "https://images.unsplash.com/photo-1509440159596-0249088772ff?w=600&auto=format&fit=crop&q=80"
IMG_EGGS = "https://images.unsplash.com/photo-1582722872445-44dc5f7e3c8f?w=600&auto=format&fit=crop&q=80"
IMG_CURD = "https://images.unsplash.com/photo-1488477181946-6428a0291777?w=600&auto=format&fit=crop&q=80"

IMG_SPICES_GROUND = "https://images.unsplash.com/photo-1596040033229-a9821ebd058d?w=600&auto=format&fit=crop&q=80"
IMG_SPICES_WHOLE = "https://images.unsplash.com/photo-1599940824399-b87987ceb72a?w=600&auto=format&fit=crop&q=80"
IMG_SALT_SUGAR = "https://images.unsplash.com/photo-1628088062854-d1870b4553da?w=600&auto=format&fit=crop&q=80"
IMG_GINGER_GARLIC = "https://images.unsplash.com/photo-1615485290382-441e4d049cb5?w=600&auto=format&fit=crop&q=80"

IMG_TEA = "https://images.unsplash.com/photo-1576092768241-dec231879fc3?w=600&auto=format&fit=crop&q=80"
IMG_COFFEE = "https://images.unsplash.com/photo-1514432324607-a09d9b4aefdd?w=600&auto=format&fit=crop&q=80"
IMG_JUICE = "https://images.unsplash.com/photo-1551024709-8f23befc6f87?w=600&auto=format&fit=crop&q=80"
IMG_COLD_DRINK = "https://images.unsplash.com/photo-1527661591475-527312dd65f5?w=600&auto=format&fit=crop&q=80"
IMG_SAUCE = "https://images.unsplash.com/photo-1589647363585-f4a7d3877b10?w=600&auto=format&fit=crop&q=80"

# =========================================================================
# 1. SNACKS & MUNCHIES (~260 items)
# =========================================================================
chips_brands = [
    ("Lay's", "Potato Chips", ["Classic Salted", "India's Magic Masala", "American Style Cream & Onion", "Spanish Tomato Tango", "Chili Limon", "Wafer Style Salt & Pepper", "Sizzling Hot", "Gourmet Vintage Cheese", "Gourmet Lime & Cracked Pepper"]),
    ("Bingo!", "Mad Angles", ["Achaari Masti", "Very Peri Peri", "Tomato Madness", "Cheese Nachos", "Chaahat Chaat", "Pizza Masti"]),
    ("Bingo!", "Tedhe Medhe", ["Masala Tadka", "Tomato Twister", "Pudina Punch", "Wakhra Style Achaari"]),
    ("Balaji", "Wafers", ["Simply Salted", "Masala Wafers", "Tomato Twist", "Cream & Onion", "Rumbles Pudina Twist", "Chaat Chaska"]),
    ("Pringles", "Potato Crisps", ["Original", "Sour Cream & Onion", "South African Style Peri Peri", "Pizza Flavor", "Hot & Spicy", "Cheddar Cheese"]),
    ("Too Yumm!", "Veggie Stix", ["Sour Cream & Onion", "Spanish Tomato", "Chilli Achaari", "Kashmiri Chilli", "Dahi Papdi Chaat", "Quinoa Puffs Cheese", "Karare Masala"])
]

for brand, product_type, flavors in chips_brands:
    for flav in flavors:
        add_item(
            item_id=f"{brand}_{product_type}_{flav}",
            name=f"{brand} {flav} {product_type}",
            category="Snacks & Munchies",
            price=20.0 if "Pringles" not in brand else 115.0,
            rating=4.7,
            unit="50g pack" if "Pringles" not in brand else "107g can",
            badge="Crispy Favorite",
            image_url=IMG_SNACKS_CHIPS,
            description=f"Crispy and flavorful {flav} {product_type} by {brand}. Perfectly seasoned for movie marathons, tea time, and party snacking.",
            pairing_text=f"Crunchy {flav} chips snack. Frequently paired with Thums Up cold drink, dip, cheese slices, and masala chai."
        )

namkeen_items = [
    ("Haldiram's", "Bhujia Sev", "Crisp gram flour sev infused with aromatic spices", 55.0, "150g pack", "Classic Namkeen"),
    ("Haldiram's", "All in One Mixture", "Signature sweet and spicy royal mixture with dry fruits", 65.0, "200g pack", "Top Rated"),
    ("Haldiram's", "Khatta Meetha Mixture", "Tangy sweet and sour extruded snack with golden sev", 55.0, "200g pack", "Sweet & Tangy"),
    ("Haldiram's", "Panchratan Mixture", "Crispy potato straws with cashews, almonds, and raisins", 85.0, "150g pack", "Dry Fruit Mix"),
    ("Haldiram's", "Moong Dal", "Salted fried yellow split moong dal lentils", 52.0, "200g pack", "Protein Rich"),
    ("Haldiram's", "Chana Choor", "Spicy pressed Bengal gram tossed in tangy amchur", 48.0, "150g pack", "Tangy Tadka"),
    ("Haldiram's", "Salted Peanuts", "Crunchy roasted peanuts sprinkled with sea salt", 42.0, "150g pack", "Tea Snack"),
    ("Haldiram's", "Boondi Plain", "Crispy fried gram flour pearls for raita and chaat", 40.0, "200g pack", "Raita Essential"),
    ("Haldiram's", "Masala Boondi", "Spiced crispy boondi seasoned with red chili and curry leaves", 45.0, "200g pack", "Chatpata"),
    ("Haldiram's", "Navratan Mixture", "Traditional 9-ingredient spicy savoury blend", 58.0, "200g pack", "Royal Blend"),
    ("Haldiram's", "Bhel Puri Kit", "Complete Mumbai bhel mix with sev, puris, and chutney sachets", 80.0, "300g pack", "Street Style"),
    ("Haldiram's", "Mathri Punjabi Style", "Flaky savory carom-infused wheat flour crisps", 60.0, "200g pack", "Tea Time Classic"),
    ("Bikaji", "Bikaneri Bhujia", "Authentic Rajasthani moth bean bhujia with spicy warmth", 60.0, "200g pack", "Authentic Bikaneri"),
    ("Bikaji", "Sub Kuch All in One", "Crunchy cornflakes, nuts, and sev mixture", 62.0, "200g pack", "Bestseller"),
    ("Bikaji", "Tana Tan Aloo Bhujia", "Crisp spicy mint and potato noodles", 55.0, "200g pack", "Fiery Tangy"),
    ("Bikaji", "Kaju Kismis Mixture", "Premium cashew and raisin enriched tea snack", 95.0, "200g pack", "Royal Treat"),
    ("Bikaji", "Ratlaami Sev", "Famous Ratlam thick spicy clove and pepper sev", 58.0, "200g pack", "Spicy Tadka"),
    ("Bikaji", "Fatafat Bhel", "Instant bhel mix for quick evening cravings", 50.0, "150g pack", "Instant Chaat"),
    ("Balaji", "Gathiya", "Soft and crumbly Gujarat special carom gathiya", 40.0, "200g pack", "Gujarat Special"),
    ("Balaji", "Chana Jor Garam", "Traditional spicy pressed black gram snack", 38.0, "150g pack", "Spicy Crunch"),
    ("Balaji", "Farali Chevdo", "Potato sticks with peanuts for fasting and snacking", 45.0, "150g pack", "Upvas Special"),
    ("Chitale Bandhu", "Bakharwadi", "Crispy spiced spiral pinwheels packed with coconut masala", 110.0, "250g pack", "Pune Special")
]

for brand, item_name, desc, price, unit, badge in namkeen_items:
    add_item(
        item_id=f"{brand}_{item_name}",
        name=f"{brand} {item_name}",
        category="Snacks & Munchies",
        price=price,
        rating=4.8,
        unit=unit,
        badge=badge,
        image_url=IMG_SNACKS_NAMKEEN,
        description=f"{desc}. Crafted with traditional spices for superior crispiness and aroma.",
        pairing_text=f"Authentic {item_name} namkeen. Frequently paired with cutting masala chai, filter coffee, sweets, and cold drinks."
    )

biscuits_list = [
    ("Britannia", "Good Day Butter Cookies", "Rich buttery melt-in-mouth cookies with smile cuts", 45.0, "250g pack", "Everyday Smile"),
    ("Britannia", "Good Day Cashew Delight", "Loaded with rich real cashew nuts and butter", 50.0, "200g pack", "Cashew Rich"),
    ("Britannia", "Good Day Choco Chip", "Golden cookies studded with luscious chocolate chips", 55.0, "200g pack", "Choco Indulgence"),
    ("Britannia", "Bourbon Chocolate Cream", "Crunchy sugar-dusted chocolate biscuits with cocoa cream", 35.0, "150g pack", "Kids Favorite"),
    ("Britannia", "Marie Gold Crisp Biscuits", "Light and wholesome tea-dipping biscuits with vitamins", 38.0, "300g pack", "Tea Companion"),
    ("Britannia", "Milk Bikis Milk Biscuits", "Wholesome goodness of milk and energy for growing kids", 32.0, "150g pack", "Milk Power"),
    ("Britannia", "50-50 Maska Chaska", "Buttery salted crackers topped with fragrant herbs", 30.0, "120g pack", "Sweet & Salty"),
    ("Britannia", "50-50 Sweet & Salty", "Dual-flavored light cracker biscuit", 28.0, "120g pack", "Classic Cracker"),
    ("Britannia", "NutriChoice Digestive Hi-Fibre", "Whole wheat dietary fibre biscuits for healthy snacking", 65.0, "250g pack", "High Fibre"),
    ("Britannia", "NutriChoice Oats & Almond Cookies", "Crunchy roasted oats cookies loaded with almonds", 75.0, "150g pack", "Healthy Choice"),
    ("Britannia", "Pure Magic Chocolush", "Crispy cookies with a molten liquid chocolate center", 60.0, "120g pack", "Choco Fills"),
    ("Parle", "Hide & Seek Chocolate Chip", "Dark cocoa biscuits filled with premium chocolate chips", 40.0, "120g pack", "Real Chocolate"),
    ("Parle", "Hide & Seek Caffe Mocha", "Infused with aromatic roasted coffee beans and chocolate", 45.0, "120g pack", "Coffee Choco"),
    ("Parle", "Monaco Classic Salted Crackers", "Light salty mini crackers ideal with cheese toppings", 25.0, "120g pack", "Salty Crunch"),
    ("Parle", "Krackjack Sweet & Salty", "Original dual-taste crisp snack cracker", 28.0, "120g pack", "Original Dual Taste"),
    ("Parle", "Magix Choco Vanilla Cream", "Dual swirl cream sandwiched between golden cookies", 20.0, "100g pack", "Cream Fun"),
    ("Parle", "Nutricrunch Honey & Oats", "Wholesome oats cookies sweetened with natural honey", 50.0, "150g pack", "High Fibre"),
    ("Sunfeast", "Dark Fantasy Choco Fills", "Decadent cookie with luxurious molten choco lava center", 70.0, "150g pack", "Pure Indulgence"),
    ("Sunfeast", "Dark Fantasy Coffee Fills", "Rich chocolate cookie with a molten coffee center", 75.0, "150g pack", "Coffee Lava"),
    ("Sunfeast", "Mom's Magic Butter & Cashew", "Nutty homestyle cookies baked with aromatic butter", 45.0, "200g pack", "Homestyle"),
    ("Sunfeast", "Bounce Tangy Orange Cream", "Crispy biscuits with zesty orange flavored cream", 20.0, "100g pack", "Tangy Cream"),
    ("Oreo", "Original Vanilla Creme", "Dark cocoa sandwich biscuits with sweet vanilla cream", 40.0, "120g pack", "Twist Lick Dunk"),
    ("Oreo", "Chocolate Creme Biscuit", "Double cocoa sandwich cookies with rich choco cream", 42.0, "120g pack", "Double Choco"),
    ("Oreo", "Strawberry Creme Biscuit", "Fruity sweet strawberry cream layered in cocoa biscuits", 40.0, "120g pack", "Berry Delight"),
    ("Unibic", "Snack Bar Choco Hazelnut", "Multi-grain nutritional snack bar with rich hazelnut", 40.0, "40g bar", "Energy On The Go"),
    ("Unibic", "Fruit & Nut Cookies", "Packed with almonds, cashews, raisins, and papaya bits", 60.0, "150g pack", "Fruit & Nut Rich"),
    ("Unibic", "Scotch Finger Shortbread", "Rich golden buttery shortbread biscuits", 55.0, "150g pack", "Buttery Crumb")
]

for brand, b_name, b_desc, b_price, b_unit, b_badge in biscuits_list:
    add_item(
        item_id=f"{brand}_{b_name}",
        name=f"{brand} {b_name}",
        category="Snacks & Munchies",
        price=b_price,
        rating=4.8,
        unit=b_unit,
        badge=b_badge,
        image_url=IMG_SNACKS_BISCUITS if "Cookie" not in b_name else IMG_SNACKS_COOKIES,
        description=f"{b_desc}. Made with premium ingredients for the ultimate tea-time dunking experience.",
        pairing_text=f"Delicious {b_name}. Frequently paired with Tata Tea Gold, hot milk, Nescafe coffee, and evening snacks."
    )

nuts_dryfruits = [
    ("Happilo", "California Premium Almonds", "Crunchy high-protein raw California badam", 240.0, "200g pack", "100% Natural"),
    ("Happilo", "Whole Cashews W320", "Creamy whole white cashew nuts rich in zinc", 260.0, "200g pack", "King Size"),
    ("Happilo", "Roasted & Salted Pistachios", "Crispy opened pistachios lightly seasoned with salt", 280.0, "200g pack", "Salted Crunch"),
    ("Happilo", "Chilean Walnut Kernels", "Omega-3 rich brain-boosting natural walnut halves", 310.0, "200g pack", "Omega-3 Boost"),
    ("Happilo", "Golden Indian Raisins (Kishmish)", "Naturally sweet sun-dried long seedless raisins", 120.0, "250g pack", "Naturally Sweet"),
    ("Happilo", "Arabian Omani Dates", "Soft and succulent naturally sweet dates", 160.0, "500g pack", "Natural Energy"),
    ("Happilo", "Royal Trail Mix", "Curated blend of dried cranberries, blueberries, and seeds", 220.0, "200g pack", "Antioxidant Rich"),
    ("Nutty Gritties", "Barbeque Almonds", "Slow roasted California almonds in smoky BBQ seasoning", 175.0, "100g pack", "Smoky Flavor"),
    ("Nutty Gritties", "Peri Peri Cashews", "Spicy whole cashews tossed in fiery African peri peri", 195.0, "100g pack", "Spicy Zest"),
    ("Farmley", "Roasted Makhana Peri Peri", "Fox nuts tossed in fiery olive oil and African peri peri", 110.0, "100g pack", "Zero Trans Fat"),
    ("Farmley", "Roasted Makhana Himalayan Salt", "Crunchy lotus seeds lightly roasted in rock salt", 105.0, "100g pack", "Diet Friendly"),
    ("Farmley", "Roasted Makhana Mint & Pudina", "Refreshing herb and mint roasted fox nuts", 110.0, "100g pack", "Cool Mint"),
    ("Farmley", "Roasted Makhana Cream & Onion", "Savory sour cream and onion flavored lotus seeds", 115.0, "100g pack", "Gourmet Snack"),
    ("True Elements", "Raw Chia Seeds", "High fiber and omega-3 superfood seeds for weight management", 160.0, "250g pack", "Superfood"),
    ("True Elements", "Raw Pumpkin Seeds", "Zinc-rich whole green pumpkin pepitas", 180.0, "250g pack", "Immunity Boost"),
    ("True Elements", "Roasted Flax Seeds", "Golden roasted alsi seeds rich in dietary fiber", 120.0, "250g pack", "Heart Healthy")
]

for brand, n_name, n_desc, n_price, n_unit, n_badge in nuts_dryfruits:
    add_item(
        item_id=f"{brand}_{n_name}",
        name=f"{brand} {n_name}",
        category="Snacks & Munchies",
        price=n_price,
        rating=4.9,
        unit=n_unit,
        badge=n_badge,
        image_url=IMG_SNACKS_NUTS,
        description=f"{n_desc}. Nitrogen flushed for farm-fresh crunch and long-lasting freshness.",
        pairing_text=f"Wholesome {n_name}. Frequently paired with warm milk, morning breakfast oats, green tea, and dessert recipes."
    )

chocolates_sweets = [
    ("Cadbury", "Dairy Milk Chocolate Bar", "Signature smooth milk chocolate bar", 45.0, "50g bar", "Bestseller"),
    ("Cadbury", "Dairy Milk Silk Classic", "Unbelievably smooth and velvety luxury milk chocolate", 85.0, "60g bar", "Silky Smooth"),
    ("Cadbury", "Dairy Milk Silk Roast Almond", "Velvety chocolate bar studded with crunchy whole roasted almonds", 95.0, "60g bar", "Nutty Silk"),
    ("Cadbury", "Dairy Milk Silk Fruit & Nut", "Loaded with sweet raisins and crunchy chopped almonds", 95.0, "60g bar", "Rich Indulgence"),
    ("Cadbury", "Dairy Milk Silk Oreo", "Crunchy vanilla Oreo cookie chunks enveloped in creamy silk", 95.0, "60g bar", "Oreo Fusion"),
    ("Nestle", "KitKat 4 Finger Chocolate", "Crispy wafer fingers covered in smooth milk chocolate", 30.0, "38g bar", "Break Time"),
    ("Nestle", "KitKat Dessert Delight Brownie", "Layered wafer bar inspired by rich chocolate fudge brownies", 60.0, "50g bar", "Gourmet Dessert"),
    ("Ferrero", "Rocher Hazelnut Chocolates", "Crisp hazelnut and milk chocolate pralines with whole roasted hazelnut", 350.0, "Pack of 8", "Celebration Pack"),
    ("Amul", "Dark Chocolate 55% Cocoa", "Rich bittersweet dark chocolate made from single-origin cocoa beans", 110.0, "150g bar", "55% Cocoa"),
    ("Amul", "Dark Chocolate 75% Bitter", "Intense gourmet bitter dark chocolate for chocolate connoisseurs", 125.0, "150g bar", "75% Bitter Dark"),
    ("Haldiram's", "Gulab Jamun Can", "Soft spongy cottage cheese balls soaked in rose-cardamom sugar syrup", 130.0, "1 kg tin", "Festive Favorite"),
    ("Haldiram's", "Rasgulla Tin", "Delicate spongy chenna dumplings floating in sweet light syrup", 130.0, "1 kg tin", "Bengali Sweet"),
    ("Haldiram's", "Soan Papdi Flaky Sweet", "Melt-in-mouth flaky gram flour confection topped with pistachios", 90.0, "250g box", "Festive Treat"),
    ("Haldiram's", "Kaju Katli Diamond Sweet", "Classic diamond-shaped cashew nut fudge silvered with edible vark", 280.0, "250g box", "Pure Cashew"),
    ("Haldiram's", "Besan Laddu", "Traditional roasted gram flour sweet laddus infused with pure ghee", 150.0, "250g box", "Pure Desi Ghee"),
    ("Haldiram's", "Motichoor Laddu", "Tiny fried gram flour droplets cooked in saffron sugar syrup", 140.0, "250g box", "Classic Laddu")
]

for brand, c_name, c_desc, c_price, c_unit, c_badge in chocolates_sweets:
    add_item(
        item_id=f"{brand}_{c_name}",
        name=f"{brand} {c_name}",
        category="Snacks & Munchies",
        price=c_price,
        rating=4.9,
        unit=c_unit,
        badge=c_badge,
        image_url=IMG_SNACKS_CHOCOLATE if "Chocolate" in c_name or "KitKat" in c_name or "Ferrero" in c_name else IMG_SNACKS_SWEETS,
        description=f"{c_desc}. Perfect for gifting, celebrations, and late-night sweet cravings.",
        pairing_text=f"Delicious {c_name}. Frequently paired with hot filter coffee, masala chai, birthday celebrations, and party snacks."
    )

# =========================================================================
# 2. ATTA, RICE & DALS (Lunch & Dinner Staples) (~260 items)
# =========================================================================
rice_varieties = [
    ("India Gate", "Classic Basmati Rice", "Extra-long aged aromatic grains", 210.0, "1 kg bag", "King of Basmati"),
    ("India Gate", "Super Basmati Rice", "Slender aromatic grains for royal biryani", 175.0, "1 kg bag", "Royal Biryani"),
    ("India Gate", "Tibar Basmati Rice", "3/4th length aged fragrant basmati rice", 125.0, "1 kg bag", "Daily Premium"),
    ("India Gate", "Dubar Basmati Rice", "Half-grain fragrant basmati for pulao and khichdi", 110.0, "1 kg bag", "Value Pack"),
    ("India Gate", "Mini Mogra Basmati Rice", "Broken fragrant basmati rice for daily dal chawal", 85.0, "1 kg bag", "Everyday Value"),
    ("Daawat", "Biryani Basmati Rice", "World's longest basmati grain expanding up to 24mm", 225.0, "1 kg bag", "Chef's Special"),
    ("Daawat", "Super Basmati Rice", "Naturally aged aromatic slender grains", 165.0, "1 kg bag", "Aged Aromatic"),
    ("Daawat", "Rozana Gold Basmati", "Medium grain flavorful basmati for daily lunches", 105.0, "1 kg bag", "Daily Rice"),
    ("Daawat", "Brown Basmati Rice", "Nutritious whole grain brown basmati with germ and bran", 155.0, "1 kg bag", "Zero Cholesterol"),
    ("Fortune", "Special Biryani Basmati Rice", "Fluffy non-sticky basmati rice for fragrant pulao", 160.0, "1 kg bag", "Non-Sticky"),
    ("Fortune", "Rozana Basmati Rice", "Pristine white long grain basmati for everyday meals", 98.0, "1 kg bag", "Everyday Choice"),
    ("Kohinoor", "Super Silver Basmati Rice", "Rich sweet aroma aged 2 years for authentic feasts", 180.0, "1 kg bag", "Aged 2 Years"),
    ("BB Royal", "Sona Masoori Raw Rice", "Lightweight aromatic staple South Indian rice", 68.0, "1 kg bag", "South Indian Staple"),
    ("BB Royal", "Sona Masoori Steam Rice", "Steamed lightweight rice easy on digestion", 72.0, "1 kg bag", "Easy Digest"),
    ("BB Royal", "Kolam Raw Rice", "Fine grain fragrant white rice popular in Western India", 75.0, "1 kg bag", "Maharashtrian Special"),
    ("BB Royal", "Idli Rice Short Grain", "Short fat parboiled rice formulated for soft fluffy idlis", 58.0, "1 kg bag", "Fluffy Idli"),
    ("BB Royal", "Gobindobhog Rice", "Short aromatic Bengali sticky rice for khichuri and payesh", 120.0, "1 kg bag", "Bengali Aroma"),
    ("BB Royal", "Ponni Boiled Rice", "Parboiled high-fiber rice widely loved in Tamil Nadu", 65.0, "1 kg bag", "Nutritious Parboiled"),
    ("Organic Tattva", "Organic Brown Rice", "Unpolished organic brown rice loaded with fiber", 140.0, "1 kg bag", "Certified Organic"),
    ("Organic Tattva", "Organic White Basmati Rice", "Pesticide-free Himalayan organic basmati rice", 195.0, "1 kg bag", "Organic Himalayan")
]

for brand, r_name, r_desc, r_price, r_unit, r_badge in rice_varieties:
    add_item(
        item_id=f"{brand}_{r_name}",
        name=f"{brand} {r_name}",
        category="Atta, Rice & Dals",
        price=r_price,
        rating=4.8,
        unit=r_unit,
        badge=r_badge,
        image_url=IMG_RICE,
        description=f"{r_desc}. Meticulously cleaned and aged for superior grain elongation and enticing aroma.",
        pairing_text=f"Aromatic {r_name}. Frequently paired with Toor Dal, Amul Pure Desi Ghee, Catch Jeera, and Everest Garam Masala."
    )

pulses_dals = [
    ("Tata Sampann", "Moong Dal Yellow Split", "Unpolished yellow moong lentils rich in clean protein", 145.0, "1 kg pack", "Easy to Digest"),
    ("Tata Sampann", "Moong Dal Chilka Green Split", "High-fiber green split moong dal with husk", 150.0, "1 kg pack", "High Fiber"),
    ("Tata Sampann", "Whole Green Moong Sabut", "Whole green gram ideal for healthy sprouts and curries", 140.0, "1 kg pack", "Sprout Essential"),
    ("Tata Sampann", "Chana Dal Bengal Gram", "Polished-free split chickpea lentils for dal and tadka", 115.0, "1 kg pack", "Protein Rich"),
    ("Tata Sampann", "Urad Dal White Split", "Skinned split black lentils for medu vada, dosa, and dal", 160.0, "1 kg pack", "Dosa Backbone"),
    ("Tata Sampann", "Urad Dal Dhuli Whole", "Whole white urad lentils for rich dal makhani and batter", 170.0, "1 kg pack", "Creamy Dal"),
    ("Tata Sampann", "Urad Dal Black Whole (Kali Urad)", "Nutrient-dense black gram for traditional Punjabi dal makhani", 155.0, "1 kg pack", "Dal Makhani Hero"),
    ("Tata Sampann", "Masoor Dal Red Split", "Quick-cooking pink coral lentils for comforting daily dal", 125.0, "1 kg pack", "Quick Cooking"),
    ("Tata Sampann", "Masoor Whole Brown (Malka)", "Earthy brown whole lentils packed with natural minerals", 120.0, "1 kg pack", "Nutrient Dense"),
    ("Tata Sampann", "Rajma Chitra Spotted", "Creamy soft-boiling Kashmiri chitra kidney beans", 185.0, "1 kg pack", "Kashmiri Chitra"),
    ("Tata Sampann", "Rajma Red Jammu", "Rich crimson kidney beans for slow-cooked thick curries", 175.0, "1 kg pack", "Jammu Special"),
    ("Tata Sampann", "Kabuli Chana Chickpeas", "Big bold creamy chickpeas for restaurant-style chhole", 170.0, "1 kg pack", "Bold Chickpeas"),
    ("Tata Sampann", "Kala Chana Brown Chickpeas", "Traditional brown desi chickpeas for morning soaked chaat", 110.0, "1 kg pack", "Desi Chana"),
    ("Tata Sampann", "Safed Vatana White Peas", "Sun-dried white peas for Mumbai ragda patties and curries", 95.0, "1 kg pack", "Ragda Special"),
    ("Tata Sampann", "Lobia Black Eyed Peas", "Tender quick-cooking cowpeas with savory nutty flavor", 130.0, "1 kg pack", "Nutty Flavor"),
    ("Fortune", "Unpolished Toor Dal", "Natural protein rich arhar dal without artificial polish", 158.0, "1 kg pack", "100% Unpolished"),
    ("Fortune", "Unpolished Moong Dal", "Clean split yellow moong for light khichdi and soups", 142.0, "1 kg pack", "Pure Healthy"),
    ("Fortune", "Special Chana Dal", "Firm texture Bengal gram lentils for puran poli and dal", 112.0, "1 kg pack", "Wholesome"),
    ("Organic Tattva", "Organic Toor Dal", "Certified organic chemical-free arhar lentils", 195.0, "1 kg pack", "Organic Certified"),
    ("Organic Tattva", "Organic Kabuli Chana", "Pesticide-free organic chickpeas for rich curries", 210.0, "1 kg pack", "Organic Pure")
]

for brand, p_name, p_desc, p_price, p_unit, p_badge in pulses_dals:
    add_item(
        item_id=f"{brand}_{p_name}",
        name=f"{brand} {p_name}",
        category="Atta, Rice & Dals",
        price=p_price,
        rating=4.8,
        unit=p_unit,
        badge=p_badge,
        image_url=IMG_DAL if "Dal" in p_name else IMG_PULSES,
        description=f"{p_desc}. Retains natural nutrient profile and cooks evenly with rich aroma.",
        pairing_text=f"Wholesome {p_name}. Frequently paired with India Gate Basmati Rice, Amul Pure Desi Ghee, Catch Jeera, and Aashirvaad Atta."
    )

atta_flours = [
    ("Aashirvaad", "Select 100% MP Sharbati Atta", "Crafted from golden heavy Sharbati wheat grains of Madhya Pradesh", 295.0, "5 kg bag", "King of Atta"),
    ("Aashirvaad", "Multigrain High-Fibre Atta", "Infused with soya, chana, oat, maize, and psyllium husk", 310.0, "5 kg bag", "High Fibre"),
    ("Aashirvaad", "Sugar Release Control Atta", "Low GI wheat flour formulation for diabetic wellness", 340.0, "5 kg bag", "Low GI Control"),
    ("Fortune", "Chakki Fresh Whole Wheat Atta", "100% whole wheat stone ground flour for soft rotis", 235.0, "5 kg bag", "Chakki Fresh"),
    ("Fortune", "Fine Besan Gram Flour", "100% pure chana dal besan for pakodas and sweets", 85.0, "1 kg pack", "Super Fine"),
    ("Tata Sampann", "Fine Chana Dal Besan", "Naturally rich in protein with no added khesari dal", 90.0, "1 kg pack", "100% Chana Dal"),
    ("Rajdhani", "Royal Besan", "Fine milled gram flour formulated for crisp bhajjis", 82.0, "1 kg pack", "Crispy Pakoda"),
    ("Rajdhani", "Fine Sooji (Rava)", "Coarse wheat semolina for crispy rava dosa and halwa", 55.0, "1 kg pack", "Golden Rava"),
    ("Rajdhani", "Premium Maida", "Finely refined wheat flour for bakery cakes, bhaturas, and samosas", 50.0, "1 kg pack", "Refined Flour"),
    ("Organic Tattva", "Organic Wheat Flour Atta", "Unadulterated pesticide-free chakki atta", 180.0, "2 kg bag", "Organic Atta"),
    ("BB Royal", "Jowar Flour (Sorghum)", "Gluten-free traditional sorghum flour for healthy bhakri", 68.0, "1 kg pack", "Gluten Free"),
    ("BB Royal", "Bajra Flour (Pearl Millet)", "Iron and mineral rich winter millet flour", 62.0, "1 kg pack", "Iron Rich"),
    ("BB Royal", "Ragi Flour (Finger Millet)", "Calcium packed red millet flour for rotis and porridge", 65.0, "1 kg pack", "Calcium Loaded"),
    ("BB Royal", "Makki Ka Atta (Maize Flour)", "Coarse yellow corn flour essential for Sarson Ka Saag meals", 70.0, "1 kg pack", "Punjab Special"),
    ("BB Royal", "Sattu Roasted Gram Flour", "Bihar special protein energy flour for sattu drink and paratha", 110.0, "1 kg pack", "Desi Superfood"),
    ("BB Royal", "Singhara Atta", "Water chestnut flour suitable for fasting and navratri meals", 95.0, "500g pack", "Vrat Special")
]

for brand, a_name, a_desc, a_price, a_unit, a_badge in atta_flours:
    add_item(
        item_id=f"{brand}_{a_name}",
        name=f"{brand} {a_name}",
        category="Atta, Rice & Dals",
        price=a_price,
        rating=4.9,
        unit=a_unit,
        badge=a_badge,
        image_url=IMG_ATTA,
        description=f"{a_desc}. Ensures soft, pliable dough and delicious nutritious homemade bread.",
        pairing_text=f"Pure {a_name}. Frequently paired with Amul Pure Desi Ghee, Toor Dal, Everest Garam Masala, and paneer curries."
    )

oils_ghee = [
    ("Mother Dairy", "Pure Cow Ghee Tin", "Golden granulated cow ghee with traditional churned aroma", 325.0, "500 ml tin", "Granulated Gold"),
    ("Aashirvaad", "Svasti Pure Cow Ghee", "Special slow cook process producing rich aroma", 335.0, "500 ml pouch", "Slow Cooked"),
    ("Gowardhan", "Pure Cow Ghee Jar", "Natural yellow pure cow ghee with rich grainy texture", 340.0, "500 ml jar", "Rich Grainy"),
    ("Patanjali", "Cow Desi Ghee", "Traditional Vedic method cow milk fat ghee", 295.0, "500 ml pouch", "Vedic Pure"),
    ("Fortune", "Sunlite Refined Sunflower Oil", "Light and healthy cooking oil enriched with vitamins A & D", 145.0, "1 Litre pouch", "Light & Healthy"),
    ("Fortune", "Soyabean Refined Cooking Oil", "Nutrient-rich versatile oil for frying and daily tadka", 135.0, "1 Litre pouch", "Daily Value"),
    ("Fortune", "Kachi Ghani Mustard Oil", "Cold pressed pungent sarson oil for robust traditional gravies", 160.0, "1 Litre bottle", "Pungent Sarson"),
    ("Saffola", "Gold Pro Healthy Lifestyle Oil", "Dual seed blend of rice bran and sunflower oil with antioxidants", 175.0, "1 Litre pouch", "Heart Shield"),
    ("Saffola", "Total Advanced Heart Care Oil", "Engineered to keep cholesterol in check with plant sterols", 210.0, "1 Litre pouch", "Advanced Care"),
    ("Dhara", "Kachi Ghani Mustard Oil", "Deeply pungent authentic mustard oil from mustard seeds", 155.0, "1 Litre pouch", "Traditional Pungent"),
    ("Gemini", "Pure Groundnut Cooking Oil", "Traditional cold-milled peanut oil with nutty aroma", 195.0, "1 Litre pouch", "Nutty Flavor"),
    ("Parachute", "100% Pure Coconut Cooking Oil", "Cold pressed pure edible coconut oil for authentic South Indian curries", 215.0, "1 Litre bottle", "100% Pure Coconut"),
    ("Figaro", "Pure Olive Oil for Cooking", "Imported Spanish olive oil suitable for frying, sautéing, and baking", 450.0, "500 ml tin", "Spanish Olive")
]

for brand, o_name, o_desc, o_price, o_unit, o_badge in oils_ghee:
    add_item(
        item_id=f"{brand}_{o_name}",
        name=f"{brand} {o_name}",
        category="Atta, Rice & Dals",
        price=o_price,
        rating=4.8,
        unit=o_unit,
        badge=o_badge,
        image_url=IMG_GHEE if "Ghee" in o_name else IMG_OIL,
        description=f"{o_desc}. Retains natural smoke point and elevates taste of curries and tadkas.",
        pairing_text=f"Premium cooking {o_name}. Frequently paired with Aashirvaad Atta, Toor Dal, Basmati Rice, and whole spices."
    )

ready_meals = [
    ("MTR", "Ready to Eat Paneer Butter Masala", "Tender paneer cubes in rich spiced cashew tomato gravy", 110.0, "300g pack", "Instant Dinner"),
    ("MTR", "Ready to Eat Dal Makhani", "Slow-cooked black lentils simmered overnight with butter and cream", 95.0, "300g pack", "Rich & Creamy"),
    ("MTR", "Ready to Eat Rajma Masala", "Red kidney beans simmered in thick onion tomato gravy", 95.0, "300g pack", "Homestyle Gravy"),
    ("MTR", "Ready to Eat Chana Masala", "Tangy and spicy chickpeas cooked in authentic Punjabi spices", 95.0, "300g pack", "Punjabi Tadka"),
    ("MTR", "Ready to Eat Palak Paneer", "Fresh spinach puree with soft paneer cubes and mild spices", 110.0, "300g pack", "Healthy Spinach"),
    ("Kitchens of India", "Dal Bukhara", "Legendary smoky slow-simmered black lentils", 140.0, "285g pack", "ITC Special"),
    ("Kitchens of India", "Chicken Chettinad Gravy", "Spicy coastal South Indian chicken gravy mix", 125.0, "100g pack", "Coastal Spicy"),
    ("Kohinoor", "Hyderabadi Biryani Kit", "Complete kit with aged basmati rice, biryani gravy, and whole spices", 160.0, "325g box", "Master Biryani"),
    ("Kohinoor", "Lucknowi Dum Biryani Kit", "Mildly spiced fragrant Awadhi biryani kit for gourmet cooking", 160.0, "325g box", "Awadhi Royal"),
    ("Nutrela", "Soya Chunks Regular", "100% vegetarian protein powerhouse expanding during cooking", 50.0, "200g pack", "52% Protein"),
    ("Nutrela", "Soya Mini Chunks", "Bite-sized soya balls perfect for pulao, curries, and stir-fry", 52.0, "200g pack", "Mini Protein"),
    ("Nutrela", "Soya Granules", "Minced soya texture for vegetarian keema and sandwich fillings", 55.0, "200g pack", "Veg Keema")
]

for brand, m_name, m_desc, m_price, m_unit, m_badge in ready_meals:
    add_item(
        item_id=f"{brand}_{m_name}",
        name=f"{brand} {m_name}",
        category="Atta, Rice & Dals",
        price=m_price,
        rating=4.7,
        unit=m_unit,
        badge=m_badge,
        image_url=IMG_READY_MEAL,
        description=f"{m_desc}. Prepared with no artificial preservatives, ready to heat and eat in 3 minutes.",
        pairing_text=f"Wholesome {m_name}. Frequently paired with India Gate Basmati Rice, Aashirvaad rotis, and fresh curd."
    )

# =========================================================================
# 3. BREAKFAST & INSTANT FOODS (~160 items)
# =========================================================================
instant_breakfast = [
    ("Maggi", "Special Masala 2-Minute Noodles", "Crafted with 20 roasted spices and herbs", 60.0, "4-pack (280g)", "Spicy Magic"),
    ("Maggi", "Atta Masala Instant Noodles", "Whole grain wheat atta noodles with crunchy veggies", 75.0, "4-pack (290g)", "Whole Wheat"),
    ("Maggi", "Oats Noodles with Veggies", "Wholesome oats noodles infused with natural dietary fiber", 80.0, "4-pack (290g)", "Oats Goodness"),
    ("Maggi", "Pazzta Cheese Macaroni", "Instant creamy cheese pasta in delicious cheesy sauce", 32.0, "70g pack", "Cheesy Mac"),
    ("Maggi", "Pazzta Masala Penne", "Tangy tomato masala durum wheat penne pasta", 30.0, "65g pack", "Desi Pasta"),
    ("Sunfeast", "Yippee! Magic Masala Noodles", "Non-sticky round block noodles with colorful vegetable flakes", 52.0, "4-pack (260g)", "Non-Sticky"),
    ("Sunfeast", "Yippee! Mood Masala Noodles", "Dual masala sachet allows customized spice level", 58.0, "4-pack (260g)", "Dual Sachet"),
    ("Top Ramen", "Curry Instant Veg Noodles", "Signature thick rich flat noodles in curry sauce", 48.0, "4-pack (280g)", "Curry Flavor"),
    ("Top Ramen", "Fiery Chili Noodles", "Intensely spicy noodles seasoned with red chili and garlic", 50.0, "4-pack (280g)", "Fiery Hot"),
    ("Wai Wai", "Ready to Eat Masala Noodles", "Pre-cooked spiced noodles ready to eat raw or boiled with soup", 45.0, "Pack of 3", "Eat Raw or Cook"),
    ("Ching's Secret", "Veg Hakka Noodles Block", "Traditional Asian flour noodles for street-style chowmein", 35.0, "150g pack", "Street Chowmein"),
    ("Ching's Secret", "Schezwan Instant Noodles", "Spicy Indo-Chinese noodles bursting with Schezwan peppers", 55.0, "4-pack (240g)", "Desi Chinese"),
    ("Barilla", "Penne Rigate Durum Wheat Pasta", "100% Italian durum wheat semolina pasta with ridges", 160.0, "500g box", "Authentic Italian"),
    ("Barilla", "Spaghetti No. 5 Pasta", "Classic long Italian durum wheat pasta", 160.0, "500g box", "Classic Spaghetti"),
    ("Disano", "Pastalicious Elbow Macaroni", "100% durum wheat semolina elbow pasta for mac & cheese", 85.0, "500g pack", "Durum Wheat"),
    ("Disano", "Pastalicious Fusilli Pasta", "Spiral pasta shapes that hold rich tomato and cream sauces", 85.0, "500g pack", "Spiral Pasta"),
    ("Kellogg's", "Corn Flakes Original", "Crispy toasted golden corn flakes with essential vitamins", 175.0, "475g box", "Morning Energy"),
    ("Kellogg's", "Corn Flakes Real Almond & Honey", "Toasted corn flakes enriched with real sliced almonds and honey", 220.0, "300g box", "Almond Honey"),
    ("Kellogg's", "Chocos Moons & Stars", "Crunchy chocolate wheat cereal that turns milk into chocolatey fun", 185.0, "375g box", "Kids Favorite"),
    ("Kellogg's", "Muesli Fruit Nut & Seeds", "Loaded with 5 nutritious grains and 21% fruits, nuts, and seeds", 310.0, "450g box", "Nutrient Loaded"),
    ("Quaker", "100% Natural Wholegrain Rolled Oats", "Nutritious soluble beta-glucan fiber for healthy heart and stamina", 145.0, "1 kg pouch", "Heart Healthy"),
    ("Saffola", "Masala Oats Classic Masala", "Spiced whole oats cooked with carrots, green peas, and onions", 175.0, "500g pouch", "Instant Comfort"),
    ("Saffola", "Masala Oats Peppy Tomato", "Tangy tomato masala oats with real vegetable crunch", 175.0, "500g pouch", "Tangy Veggie"),
    ("Saffola", "Masala Oats Veggie Twist", "Aromatic homestyle spiced oats with herbs", 175.0, "500g pouch", "Spiced Breakfast"),
    ("Bagrry's", "Crunchy Muesli Dark Choco & Almond", "Multigrain flakes blended with dark cocoa and California almonds", 280.0, "400g box", "Dark Choco"),
    ("Yoga Bar", "Super Muesli Dark Chocolate Cranberry", "No refined sugar super muesli with whole nuts and berries", 320.0, "400g box", "Clean Fuel"),
    ("MTR", "Instant Rava Idli Mix", "Traditional semolina mix seasoned with mustard, ginger, and cashews", 90.0, "500g pack", "Quick Breakfast"),
    ("MTR", "Instant Masala Dosa Mix", "Crispy golden dosa mix requiring zero fermentation time", 85.0, "500g pack", "Instant Crisp"),
    ("MTR", "Instant Khatta Meetha Poha Mix", "Tangy beaten rice breakfast mix with peanuts and curry leaves", 75.0, "200g pack", "Ready in 3 Min"),
    ("MTR", "Instant Upma Mix", "Savory roasted semolina breakfast seasoned with ginger and chilies", 75.0, "200g pack", "South Indian Style"),
    ("Gits", "Khaman Dhokla Instant Mix", "Spongy steamed savory gram flour cakes mix", 70.0, "200g pack", "Spongy Dhokla"),
    ("Gits", "Instant Gulab Jamun Mix", "Makes 40 delicate melt-in-mouth milk sweet dumplings", 110.0, "200g pack", "Festive Dessert"),
    ("Bambino", "Roasted Vermicelli (Seviyan)", "Pre-roasted wheat vermicelli for sweet kheer and savory upma", 45.0, "400g pack", "Pre-Roasted"),
    ("Kissan", "Mixed Fruit Jam", "Blend of 8 real fruits for morning butter toast and rotis", 150.0, "500g jar", "Real Fruit Jam"),
    ("Dabur", "100% Pure Honey Squeezy", "Rich golden unfiltered honey clinically tested for zero adulteration", 195.0, "400g bottle", "Immunity Booster"),
    ("Pintola", "All-Natural Crunchy Peanut Butter", "100% roasted peanuts with zero added sugar or hydrogenated oils", 160.0, "350g jar", "Pure Protein"),
    ("Pintola", "Dark Chocolate Peanut Butter", "High protein roasted peanuts blended with rich dark cocoa", 185.0, "350g jar", "Choco Protein"),
    ("Nutella", "Hazelnut Cocoa Spread", "Iconic sweet spread crafted with roasted hazelnuts and skimmed milk", 240.0, "350g jar", "Hazelnut Dream"),
    ("Knorr", "Classic Thick Tomato Soup", "Sweet and tangy tomato soup garnished with croutons", 55.0, "Pack of 4", "Classic Comfort"),
    ("Knorr", "Classic Sweet Corn Veg Soup", "Creamy sweet corn soup infused with spring onions and celery", 55.0, "Pack of 4", "Sweet Corn"),
    ("Knorr", "Hot & Sour Veg Soup", "Spicy and tangy Chinese style soup with cabbage and carrots", 55.0, "Pack of 4", "Tangy Spicy")
]

for brand, i_name, i_desc, i_price, i_unit, i_badge in instant_breakfast:
    add_item(
        item_id=f"{brand}_{i_name}",
        name=f"{brand} {i_name}",
        category="Breakfast & Instant Foods",
        price=i_price,
        rating=4.8,
        unit=i_unit,
        badge=i_badge,
        image_url=IMG_NOODLES if "Noodle" in i_name else IMG_OATS if "Oat" in i_name or "Cereal" in i_name or "Muesli" in i_name or "Flakes" in i_name else IMG_PASTA if "Pasta" in i_name or "Pazzta" in i_name else IMG_BATTER if "Mix" in i_name else IMG_JAM_HONEY,
        description=f"{i_desc}. Convenient, delicious, and easy to prepare in under 5 minutes.",
        pairing_text=f"Breakfast staple {i_name}. Frequently paired with Amul Fresh Milk, hot tea, butter toast, and fresh fruits."
    )

# =========================================================================
# 4. DAIRY, BREAD & EGGS (~150 items)
# =========================================================================
dairy_bread_items = [
    ("Amul", "Gold Full Cream Milk", "6% milk fat rich creamy milk for thick curd, tea, and desserts", 33.0, "500 ml pouch", "Full Cream 6%"),
    ("Amul", "Cow Fresh Milk", "Pure cow milk with light digestible fat and natural golden hue", 28.0, "500 ml pouch", "100% Cow Milk"),
    ("Amul", "Masti Spiced Buttermilk (Chaas)", "Refreshing churned curd drink seasoned with cumin and mint", 15.0, "200 ml carton", "Cool Chaas"),
    ("Amul", "Masti Dahi Cup", "Thick pasteurized homestyle curd with active cultures", 35.0, "400g tub", "Thick Curd"),
    ("Amul", "Fresh Malai Cream", "25% milk fat low fat fresh cream for rich gravies and fruit salads", 65.0, "250 ml pack", "Rich Gravies"),
    ("Amul", "Processed Cheese Block", "Firm cheddar style processed cheese block for grating over pizza and pasta", 130.0, "200g block", "Grater's Choice"),
    ("Amul", "Processed Cheese Cubes", "Individually wrapped creamy cheese snack cubes", 135.0, "200g pack", "Snack Cubes"),
    ("Amul", "Diced Mozzarella & Cheddar Pizza Cheese", "Pre-shredded high stretch mozzarella cheese for bubbling pizza", 190.0, "200g pack", "Super Stretch"),
    ("Amul", "Garlic & Herbs Butter", "Rich creamy table butter blended with roasted garlic and oregano", 65.0, "100g pack", "Garlic Butter"),
    ("Amul", "Unsalted White Cooking Butter", "Pure unsalted butter formulated for baking, parathas, and clarified ghee", 60.0, "100g pack", "Pure Unsalted"),
    ("Amul", "Kool Kesar Flavored Milk", "Chilled pasteurized flavored milk with natural saffron strands", 35.0, "180 ml can", "Royal Kesar"),
    ("Amul", "Kool Badam Flavored Milk", "Rich chilled milk infused with real almond slivers", 35.0, "180 ml can", "Crunchy Badam"),
    ("Mother Dairy", "Full Cream Milk", "Wholesome pasteurized cream milk for family nourishment", 33.0, "500 ml pouch", "Full Cream"),
    ("Mother Dairy", "Classic Paneer Block", "Soft and pliable paneer cubes that retain gravy moisture", 90.0, "200g pack", "Soft Paneer"),
    ("Mother Dairy", "Ultimate Dahi", "Naturally set firm dahi free of preservatives", 35.0, "400g tub", "Homestyle Dahi"),
    ("Mother Dairy", "Tadka Chach", "Spiced buttermilk tempered with mustard seeds and curry leaves", 15.0, "200 ml pouch", "Spiced Tadka"),
    ("Britannia", "Processed Cheese Slices", "Smooth processed cheese slices with real cheddar bite", 140.0, "200g pack", "Melt In Mouth"),
    ("Britannia", "Cheezza Pizza Cheese", "High melt mozzarella blend cheese for homemade pizzas", 180.0, "200g pack", "Pizza Special"),
    ("Britannia", "100% Whole Wheat Bread", "Nutritious stone ground wheat bread with natural bran", 50.0, "400g loaf", "100% Whole Wheat"),
    ("Britannia", "Multigrain Bread Loaf", "Baked with seeds of flax, sunflower, oats, and whole wheat", 55.0, "400g loaf", "Seeds & Grains"),
    ("Harvest Gold", "White Bread Regular", "Soft spongy sandwich bread slices with golden crust", 40.0, "400g loaf", "Sandwich Favorite"),
    ("Harvest Gold", "Hearty Brown Bread", "Baked with wheat flour and caramel malt for wholesome toast", 48.0, "400g loaf", "Healthy Toast"),
    ("Harvest Gold", "Burger Buns Sesame", "Soft golden round buns topped with toasted sesame seeds", 35.0, "Pack of 4", "Sesame Topped"),
    ("Harvest Gold", "Pizza Base Pair", "Pre-baked thick crust pizza bases ready for sauce and toppings", 40.0, "Pack of 2", "Quick Pizza"),
    ("English Oven", "Sub Footlong Bread", "Fresh soft submarine sandwich loaf for loaded subs", 45.0, "Pack of 2", "Sub Style"),
    ("English Oven", "Garlic Bread Loaf", "Infused with garlic butter and herbs, ready to slice and toast", 55.0, "250g loaf", "Aromatic Garlic"),
    ("Epigamia", "Greek Yogurt Natural", "High protein strained yogurt with zero added sugar", 60.0, "100g cup", "8g Protein"),
    ("Epigamia", "Greek Yogurt Blueberry", "Creamy Greek yogurt layered with real wild blueberry compote", 70.0, "100g cup", "Real Fruit"),
    ("Epigamia", "Greek Yogurt Alphonso Mango", "Rich yogurt flavored with sweet Ratnagiri Alphonso mango pulp", 70.0, "100g cup", "Alphonso Mango"),
    ("Nestle", "Everyday Dairy Whitener", "Finest dairy whitener formulated for rich, creamy, thick tea", 130.0, "200g pack", "Creamy Chai"),
    ("Nestle", "Milkmaid Sweetened Condensed Milk", "Classic caramelized milk recipe creator for kheer, fudge, and cakes", 145.0, "380g tin", "Dessert Creator"),
    ("Eggoz", "Farm Fresh White Eggs", "UV sanitized protein rich eggs with bright yellow yolk", 65.0, "Pack of 6", "UV Sanitized"),
    ("Eggoz", "Brown Country Free-Range Eggs", "Naturally laid brown eggs rich in Omega-3 and Vitamin E", 95.0, "Pack of 6", "Omega-3 Enriched"),
    ("Suguna", "Daily Fresh Protein White Eggs", "Graded hygienic farm eggs packed in protective carton", 115.0, "Pack of 12", "Pack of 12 Value")
]

for brand, d_name, d_desc, d_price, d_unit, d_badge in dairy_bread_items:
    add_item(
        item_id=f"{brand}_{d_name}",
        name=f"{brand} {d_name}",
        category="Dairy, Bread & Eggs",
        price=d_price,
        rating=4.9,
        unit=d_unit,
        badge=d_badge,
        image_url=IMG_MILK if "Milk" in d_name or "Whitener" in d_name else IMG_PANEER if "Paneer" in d_name else IMG_CHEESE if "Cheese" in d_name else IMG_BUTTER if "Butter" in d_name else IMG_CURD if "Dahi" in d_name or "Yogurt" in d_name or "Chaas" in d_name else IMG_EGGS if "Egg" in d_name else IMG_BREAD,
        description=f"{d_desc}. Farm-fresh delivery with strict cold-chain quality controls.",
        pairing_text=f"Fresh daily essential {d_name}. Frequently paired with hot breakfast chai, eggs, toast, butter, and curries."
    )

# =========================================================================
# 5. MASALAS & SPICES (~160 items)
# =========================================================================
spices_list = [
    ("Everest", "Kitchen King Masala", "The all-round curry powder for rich North Indian vegetable gravies", 78.0, "100g pack", "All-Round Curry"),
    ("Everest", "Chhole Masala", "Pungent and tangy blend for authentic Amritsari dark chhole", 80.0, "100g pack", "Amritsari Special"),
    ("Everest", "Pav Bhaji Masala", "Signature Mumbai street spice blend imparting spicy red color and aroma", 82.0, "100g pack", "Mumbai Chowpatty"),
    ("Everest", "Sambhar Masala", "Roasted lentils and aromatic spices for traditional South Indian sambar", 75.0, "100g pack", "South Indian Aroma"),
    ("Everest", "Shahi Paneer Masala", "Mughlai style aromatic spice mix for rich cashew tomato paneer", 85.0, "100g pack", "Mughlai Rich"),
    ("Everest", "Chaat Masala", "Zesty amchur and black salt blend for sprinkling over salads and snacks", 68.0, "100g pack", "Zesty Sprinkler"),
    ("Everest", "Turmeric Powder (Haldi)", "Golden yellow turmeric powder with high natural curcumin content", 38.0, "100g pack", "High Curcumin"),
    ("Everest", "Teekhalal Hot Red Chili Powder", "Vibrant spicy red chili powder providing fiery heat to dishes", 52.0, "100g pack", "Fiery Heat"),
    ("Everest", "Coriander Powder (Dhaniya)", "Aromatic green coriander powder roasted to retain essential oils", 40.0, "100g pack", "Fresh Aroma"),
    ("MDH", "Chana Masala", "Famous blend of pomegranates, dry mango, and spices for dark chana", 85.0, "100g pack", "Peshawari Chana"),
    ("MDH", "Chunky Chat Masala", "Tangy spice mix with tartness of dry mango, mint, and black salt", 72.0, "100g pack", "Chatpata Chaat"),
    ("MDH", "Kasoori Methi (Dried Fenugreek Leaves)", "Fragrant sun-dried fenugreek leaves crushed over rich curries", 45.0, "50g pack", "Restaurant Aroma"),
    ("MDH", "Dal Makhani Masala", "Simmered spice blend for restaurant-style black dal", 82.0, "100g pack", "Dhaba Style"),
    ("MDH", "Biryani Masala", "Fragrant saffron-tinted whole spice blend for dum biryani", 95.0, "100g pack", "Dum Biryani"),
    ("MDH", "T-Plus Tea Spices Masala", "Warming dry ginger, green cardamom, clove, and cinnamon chai masala", 75.0, "35g box", "Kadak Chai Mix"),
    ("Catch", "Super Garam Masala Sprinkler", "Table top sprinkler with moisture-proof cap for seasoning hot food", 65.0, "100g sprinkler", "Table Sprinkler"),
    ("Catch", "Black Pepper Powder (Kali Mirch)", "Finely ground bold black peppercorns from Malabar coast", 95.0, "100g pack", "Malabar Bold"),
    ("Catch", "Cumin Powder (Jeera Powder)", "Roasted whole cumin seeds milled into fragrant brown powder", 70.0, "100g pack", "Roasted Jeera"),
    ("Catch", "Kala Namak (Black Salt)", "Mineral rich black rock salt with volcanic sulfur aroma", 35.0, "100g pack", "Digestive Salt"),
    ("Catch", "Dry Mango Powder (Amchur)", "Sun-dried raw green mangoes ground into sour seasoning powder", 65.0, "100g pack", "Tangy Amchur"),
    ("Catch", "Black Mustard Seeds (Rai)", "Small pungent black mustard seeds for South Indian tempering", 42.0, "100g pack", "Pungent Tempering"),
    ("Catch", "Fennel Seeds (Saunf)", "Sweet fragrant Lucknowi fennel seeds for digestion and gravies", 55.0, "100g pack", "Sweet Saunf"),
    ("Catch", "Green Cardamom (Chhoti Elaichi)", "Aromatic 8mm bold green cardamom pods with intact black seeds", 185.0, "50g pack", "8mm Bold"),
    ("Catch", "Cinnamon Sticks (Dalchini)", "Sweet aromatic rolled Ceylon cinnamon barks for biryani and curries", 75.0, "50g pack", "Sweet Ceylon"),
    ("Catch", "Whole Cloves (Laung)", "Premium handpicked whole cloves rich in eugenol oil", 85.0, "50g pack", "Handpicked Cloves"),
    ("Catch", "Carom Seeds (Ajwain)", "Pungent carom seeds essential for puris, samosas, and parathas", 45.0, "100g pack", "Digestive Ajwain"),
    ("Catch", "Bay Leaves (Tej Patta)", "Sun-dried aromatic Indian bay leaves for pulao and curries", 35.0, "30g pack", "Fragrant Tej Patta"),
    ("Catch", "Fenugreek Seeds (Methi Dana)", "Golden bitter fenugreek seeds for pickles and fish curries", 35.0, "100g pack", "Bitter Methi"),
    ("Catch", "White Sesame Seeds (Safed Til)", "Clean nutty white sesame seeds for sweets, breads, and gravies", 58.0, "100g pack", "Nutty Sesame"),
    ("Tata Salt", "Vacuum Evaporated Iodized Salt", "India's trusted vacuum evaporated purity salt for everyday cooking", 28.0, "1 kg pack", "Desh Ka Namak"),
    ("Tata Salt", "Lite 15% Low Sodium Salt", "Specially formulated with 15% less sodium for blood pressure care", 45.0, "1 kg pack", "Low Sodium"),
    ("Tata Salt", "Rock Salt (Sendha Namak)", "Pure pink Himalayan rock salt rich in natural trace minerals", 65.0, "1 kg pack", "Himalayan Pink"),
    ("Madhur", "Pure & Hygienic Crystal Sugar", "Refined without harmful sulfur chemicals, 100% sparkling white", 55.0, "1 kg pack", "Sulfur Free"),
    ("24 Mantra", "Organic Jaggery Powder (Gud)", "Chemical-free unrefined cane jaggery powder for healthy sweetening", 75.0, "500g pack", "Organic Cane Jaggery"),
    ("Dabur", "Hommade Ginger Garlic Paste", "Thick concentrated blend of freshly crushed ginger and garlic", 55.0, "200g pouch", "No Added Water"),
    ("Dabur", "Hommade Tomato Puree", "Crafted from ripe red Indian tomatoes, equal to 8 whole tomatoes", 35.0, "200g pack", "100% Ripe Tomatoes"),
    ("Smith & Jones", "Ginger Garlic Paste", "Homestyle crushed ginger and garlic paste for instant curry base", 50.0, "200g pouch", "Homestyle Base")
]

for brand, s_name, s_desc, s_price, s_unit, s_badge in spices_list:
    add_item(
        item_id=f"{brand}_{s_name}",
        name=f"{brand} {s_name}",
        category="Masalas & Spices",
        price=s_price,
        rating=4.8,
        unit=s_unit,
        badge=s_badge,
        image_url=IMG_SALT_SUGAR if "Salt" in s_name or "Sugar" in s_name or "Jaggery" in s_name else IMG_GINGER_GARLIC if "Paste" in s_name or "Puree" in s_name else IMG_SPICES_WHOLE if "Seeds" in s_name or "Sticks" in s_name or "Cloves" in s_name or "Cardamom" in s_name or "Leaves" in s_name else IMG_SPICES_GROUND,
        description=f"{s_desc}. Ground at low temperatures to lock in volatile essential oils and aroma.",
        pairing_text=f"Aromatic spice {s_name}. Frequently paired with Toor Dal, India Gate Basmati Rice, Aashirvaad Atta, and Amul Paneer."
    )

# =========================================================================
# 6. TEA, COFFEE & BEVERAGES (~150 items)
# =========================================================================
beverages_list = [
    ("Tata Tea", "Premium Desh Ki Chai", "Unique blend of fine tea leaves and big strong CTC grains", 140.0, "250g pack", "Desh Ki Chai"),
    ("Tata Tea", "Agni Strong CTC Leaf Tea", "10% extra strong tea leaves formulated for high energy kadak chai", 110.0, "250g pack", "High Energy"),
    ("Tata Tea", "Elaichi Flavored Chai", "Infused with natural crushed green cardamom aroma", 155.0, "250g pack", "Natural Elaichi"),
    ("Tata Tea", "Tulsi Green Tea Bags", "Pure whole green tea leaves blended with sacred tulsi leaves", 160.0, "25 tea bags", "Antioxidant Rich"),
    ("Brooke Bond", "Red Label Strong Tea", "India's beloved tea with natural warmth and togetherness", 145.0, "250g pack", "Warmth & Care"),
    ("Brooke Bond", "Red Label Natural Care Tea", "Enhanced with 5 Ayurvedic herbs: ashwagandha, mulethi, tulsi, cardamom, ginger", 165.0, "250g pack", "5 Ayurvedic Herbs"),
    ("Brooke Bond", "Taj Mahal Classic Orange Pekoe", "Exquisite gourmet tea leaves yielding delicate aroma and golden brew", 210.0, "250g box", "Wah Taj!"),
    ("Brooke Bond", "Taaza Strong Kadak Chai", "Fresh green tea leaves picked for invigorating refreshment", 115.0, "250g pack", "Instant Refresh"),
    ("Society", "Masala Flavour Tea", "Pre-blended with dry ginger, cardamom, cinnamon, and pepper", 155.0, "250g pack", "Masala Blend"),
    ("Wagh Bakri", "Spiced Tea Masala Chai", "CTC tea infused with 7 warming traditional Indian spices", 165.0, "250g pack", "7 Spices"),
    ("Twinings", "Green Tea Lemon & Honey", "Soothing whole leaf green tea infused with tart lemon and sweet honey", 260.0, "25 tea bags", "Lemon Honey"),
    ("Twinings", "Earl Grey Black Tea", "Classic fine black tea delicately scented with bergamot citrus", 290.0, "25 tea bags", "Citrus Bergamot"),
    ("Tetley", "Pure Green Tea Bags", "100% natural green tea with 5x antioxidants to detoxify", 175.0, "25 tea bags", "Detox Daily"),
    ("Organic India", "Tulsi Sweet Rose Herbal Infusion", "Caffeine-free soothing infusion of organic tulsi and rose petals", 195.0, "25 tea bags", "Stress Relief"),
    ("Nescafé", "Gold Blend Rich & Smooth Coffee", "Crafted with golden roasted mountain Arabica beans for velvety taste", 380.0, "50g glass jar", "Crafted Arabica"),
    ("Nescafé", "Sunrise Chicory Rich Coffee", "Slow-roasted coffee beans blended with chicory for South Indian style", 140.0, "100g pouch", "South Indian Aroma"),
    ("Bru", "Instant Coffee Chicory Mix", "Rich roasted coffee beans and chicory delivering comforting warm aroma", 155.0, "100g pouch", "Rich Roasted"),
    ("Bru", "Gold 100% Pure Instant Coffee", "100% pure Robusta and Arabica granular coffee crystals", 220.0, "50g glass jar", "Pure Crystals"),
    ("Davidoff", "Rich Aroma Gourmet Instant Coffee", "Luxurious South American and East African master roasted coffee", 520.0, "100g jar", "Luxury Gourmet"),
    ("Sleepy Owl", "Cold Brew Coffee Bags Dark Roast", "Steep overnight in water for smooth, bold, low-acid cold brew", 350.0, "Pack of 5 bags", "Cold Brew Expert"),
    ("Real Fruit Power", "Mixed Fruit Juice", "Packed with 9 nutritious fruits with no added preservatives", 115.0, "1 Litre tetrapak", "9 Fruit Blend"),
    ("Real Fruit Power", "Pomegranate Anar Juice", "Antioxidant rich ruby red pomegranate juice", 130.0, "1 Litre tetrapak", "Heart Healthy"),
    ("Real Fruit Power", "Alphonso Mango Juice", "Rich nectar made from sweet pulpy Indian Alphonso mangoes", 115.0, "1 Litre tetrapak", "Alphonso Pulpy"),
    ("Real Fruit Power", "Valencia Orange Juice", "Zesty morning breakfast juice packed with Vitamin C", 115.0, "1 Litre tetrapak", "Vitamin C Boost"),
    ("Tropicana", "100% Orange Juice No Sugar Added", "Pure squeezed orange juice with natural pulp and zero added sugar", 145.0, "1 Litre tetrapak", "100% Pure Squeezed"),
    ("Paper Boat", "Aamras Mango Drink", "Authentic thick homestyle sweet mango pulp drink", 35.0, "200 ml pouch", "Homestyle Aamras"),
    ("Paper Boat", "Chilli Guava Drink", "Juicy ripe guava juice finished with a pinch of black salt and chili", 35.0, "200 ml pouch", "Spicy Sweet"),
    ("Paper Boat", "Jaljeera Tangy Drink", "Cooling cumin and mint digestive cooler with lemon zest", 35.0, "200 ml pouch", "Cooling Digest"),
    ("Frooti", "Fresh N Juicy Mango Drink", "India's beloved sweet mango nectar drink in portable pack", 20.0, "150 ml tetrapak", "Mango Magic"),
    ("Thums Up", "Charged Strong Cold Drink", "Iconic spicy fizzy cola with maximum punch and fizz", 40.0, "750 ml bottle", "Taste the Thunder"),
    ("Coca-Cola", "Original Taste Soft Drink", "Refreshing world-famous sparkling soda beverage", 40.0, "750 ml bottle", "Original Taste"),
    ("Sprite", "Lemon-Lime Flavored Soda", "Crisp, clean, thirst-quenching transparent lemon-lime soda", 40.0, "750 ml bottle", "Clear Refresh"),
    ("Limca", "Tangy Lemon Drink", "Zesty cloudy lemon soda packed with natural fizzy lime kick", 40.0, "750 ml bottle", "Zesty Cloud"),
    ("Red Bull", "Energy Drink", "Revitalizes body and mind with taurine, caffeine, and B-group vitamins", 125.0, "250 ml can", "Vitalizes Body"),
    ("Bournvita", "Pro-Health Chocolate Drink Mix", "Loaded with Vitamin D, iron, and calcium for active bone strength", 240.0, "500g jar", "Inner Strength"),
    ("Horlicks", "Classic Malt Health Drink", "Clinically proven to make kids taller, stronger, and sharper", 260.0, "500g jar", "Classic Malt"),
    ("Bisleri", "Packaged Mineral Drinking Water", "Ozonated and multi-filtered clean pure mineral drinking water", 20.0, "1 Litre bottle", "Purity Guaranteed"),
    ("Vedica", "Himalayan Spring Natural Mineral Water", "Untouched mineral water sourced directly from Himalayan springs", 60.0, "1 Litre bottle", "Himalayan Spring")
]

for brand, bev_name, bev_desc, bev_price, bev_unit, bev_badge in beverages_list:
    add_item(
        item_id=f"{brand}_{bev_name}",
        name=f"{brand} {bev_name}",
        category="Tea, Coffee & Beverages",
        price=bev_price,
        rating=4.8,
        unit=bev_unit,
        badge=bev_badge,
        image_url=IMG_TEA if "Tea" in bev_name or "Chai" in bev_name else IMG_COFFEE if "Coffee" in bev_name else IMG_JUICE if "Juice" in bev_name or "Drink" in bev_name or "Paper Boat" in brand or "Frooti" in bev_name or "Sharbat" in bev_name else IMG_COLD_DRINK,
        description=f"{bev_desc}. Quenches thirst and elevates any gathering or relaxing break.",
        pairing_text=f"Refreshing {bev_name}. Frequently paired with Parle-G biscuits, Britannia Rusk, spicy bhujia, and breakfast toast."
    )

# =========================================================================
# 7. SAUCES, CONDIMENTS & PICKLES (~60 items)
# =========================================================================
condiments_list = [
    ("Maggi", "Rich Tomato Ketchup", "Classic tangy sweet tomato sauce made from plump red tomatoes", 115.0, "500g bottle", "Classic Ketchup"),
    ("Maggi", "Hot & Sweet Tomato Chili Sauce", "Fiery red chili twist blended into sweet tomato sauce", 120.0, "500g bottle", "Hot & Sweet"),
    ("Kissan", "Fresh Tomato Ketchup Squeezy", "100% real ripe tomatoes pureed into thick kid-friendly ketchup", 110.0, "450g squeezy", "100% Real Tomatoes"),
    ("Heinz", "Tomato Ketchup Classic", "World-renowned thick slow-pouring tomato ketchup", 150.0, "500g bottle", "Thick & Rich"),
    ("Ching's Secret", "Schezwan Chutney Dip", "Fiery Sichuan pepper and garlic sauce for noodles, momos, and samosas", 85.0, "250g glass jar", "Desi Chinese Hero"),
    ("Ching's Secret", "Dark Soy Sauce", "Rich umami brewed soy sauce for authentic Asian color and taste", 55.0, "200g bottle", "Rich Umami"),
    ("Ching's Secret", "Green Chilli Sauce", "Spicy green chili dip for roll fillings, fried rice, and snacks", 50.0, "200g bottle", "Zesty Green"),
    ("Ching's Secret", "Red Chilli Sauce", "Pungent red chili dipping sauce for fries, burgers, and spring rolls", 50.0, "200g bottle", "Fiery Red"),
    ("Veeba", "Truly Tomato Ketchup No Onion No Garlic", "Jain recipe ketchup made with premium spices and vinegar", 115.0, "450g bottle", "Jain Friendly"),
    ("Veeba", "Classic Veg Mayonnaise", "Eggless creamy white mayonnaise spread for burgers and sandwiches", 85.0, "250g pouch", "100% Eggless"),
    ("Veeba", "Burger Mayonnaise Spread", "Tangy orange mayonnaise crafted specifically for homemade burgers", 90.0, "250g pouch", "Burger Special"),
    ("Veeba", "Chipotle Southwest Salad Dressing", "Smoky jalapeño and herb dressing for salads and grilled wraps", 125.0, "300g bottle", "Smoky Chipotle"),
    ("FunFoods", "Veg Mayonnaise Garlic", "Creamy eggless mayonnaise infused with roasted garlic", 95.0, "250g pouch", "Garlic Mayo"),
    ("Mother's Recipe", "Mango Pickle (Aam Ka Achaar)", "Traditional sun-ripened raw mango pickle in pure mustard oil and fenugreek", 110.0, "400g jar", "Traditional Aam"),
    ("Mother's Recipe", "Mixed Pickle", "Zesty assortment of mango, lime, carrot, and green chili pickle", 110.0, "400g jar", "Assorted Tangy"),
    ("Mother's Recipe", "Lime Sweet & Sour Pickle (Nimbu)", "Sun-cured juicy yellow lime pickle balanced with sugar and spices", 115.0, "400g jar", "Khatta Meetha"),
    ("Mother's Recipe", "Garlic Pickle (Lahsun Achaar)", "Pungent whole garlic cloves marinated in spicy mustard gravy", 125.0, "400g jar", "Garlic Punch"),
    ("Priya", "Cut Mango Pickle With Garlic", "Spicy Andhra style fiery red cut mango pickle with mustard seeds", 120.0, "300g jar", "Andhra Fiery"),
    ("Priya", "Gongura Pickle (Sorrel Leaves)", "Authentic Telugu tangy sorrel leaves pickle prepared in sesame oil", 130.0, "300g jar", "Authentic Telugu")
]

for brand, cond_name, cond_desc, cond_price, cond_unit, cond_badge in condiments_list:
    add_item(
        item_id=f"{brand}_{cond_name}",
        name=f"{brand} {cond_name}",
        category="Snacks & Munchies",
        price=cond_price,
        rating=4.8,
        unit=cond_unit,
        badge=cond_badge,
        image_url=IMG_SAUCE,
        description=f"{cond_desc}. Elevates simple meals, fast foods, and evening snacks.",
        pairing_text=f"Zesty condiment {cond_name}. Frequently paired with Maggi noodles, samosas, parathas, and rice dishes."
    )

print(f"Total curated base items: {len(all_items)}")

# =========================================================================
# 8. PROGRAMMATIC MULTI-TIER EXPANSION TO REACH 1,000+ DISTINCT ITEMS
# =========================================================================
# We systematically expand authentic product sizes, regional variants, and staple combinations
# across all six major supermarket categories until we exceed 1,050 items.

categories_distribution = [
    {
        "category": "Snacks & Munchies",
        "prefixes": [
            ("Haldiram's", ["Navratan Mixture", "Cornflakes Mixture", "Bhel Mix", "Punjabi Tadka Sev", "Kaju Dalmoth", "Diet Murmura Chivda", "Tasty Nuts Masala Peanuts", "Masala Kaju Roasted", "Salted Cashew Crunch", "Bikaneri Papad Extra Spiced", "Moong Dal Papad", "Chana Masala Roasted", "Gathiya Bhavnagri", "Chakli Murukku Spirals", "Papdi Namkeen"]),
            ("Bikaji", ["Kuch Kuch All in One", "Mastkin Corn Mixture", "Chowpati Bhel", "Ajwain Gathiya", "Methi Mathri", "Soya Sticks Masala", "Pasta Bites Chatpata", "Roasted Diet Chana", "Pudina Aloo Sev", "Pani Puri Pellets", "Jeera Papad", "Urad Dal Special Papad"]),
            ("Balaji", ["Wafers Masala Chilli", "Farali Sev", "Moong Dal Salted", "Sing Bhujia Peanuts", "Ratlami Teekha Sev", "Chaat Chaska Wheels", "Cream Onion Rings", "Tomato Sev Murmura", "Bhel Mix Quick Snacking"]),
            ("Crax", ["Corn Curls Tangy Tomato", "Corn Curls Masala Mania", "Fritts Crispy French Fry", "Natkhat Classic Wheat Puffs", "Rings Chatpata Masala"]),
            ("Britannia", ["Good Day Pista Badam Cookies", "Bourbon Rich Vanilla Cream", "Marie Gold Vita Marie", "Milk Bikis Choco Cream", "Treat Jim Jam Berry Cookies", "NutriChoice 5 Grain Digestive", "Nice Sugar Coconut Crackers", "Little Hearts Sugar Glazed"]),
            ("Parle", ["Hide & Seek Black Bourbon", "Milano Choco Delight Cookies", "Parle 20-20 Cashew Cookies", "Top Butter Cracker", "Gold Star Glucose Tea Biscuits", "Kaccha Aam Mango Candy"]),
            ("Sunfeast", ["Dark Fantasy Bourbon", "Mom's Magic Cashew & Almond", "Bounce Elaichi Delight", "All Rounder Potato Thin Biscuits", "Caker Swiss Roll Chocolate", "Caker Trinity Triple Chocolate Cake"]),
            ("Cadbury", ["Perk Double Crisp Wafer Bar", "5 Star Caramel Nougat Bar", "Fuse Peanut Chocolate Bar", "Gems Chocolate Lentils Pouch", "Dairy Milk Crispello Chocolate", "Nutties Milk Chocolate Almonds"]),
            ("Nestle", ["Munch Crunchy Wafer Bar", "BarOne Nougat Caramel Bar", "Milkybar White Chocolate Bar", "Classic Milk Chocolate Bar", "Munch Max Crisp Wafer"])
        ],
        "sizes": ["Small Pocket Pack (45g)", "Medium Sharing Pack (120g)", "Value Family Pack (250g)", "Mega Party Tub (500g)"],
        "base_price": 25.0,
        "img": IMG_SNACKS_NAMKEEN,
        "desc_template": "Crispy appetizing {name} prepared with select farm-fresh ingredients and traditional seasonings.",
        "pairing_template": "Popular tea-time munchie. Frequently paired with cutting chai, Thums Up, and afternoon snacks."
    },
    {
        "category": "Atta, Rice & Dals",
        "prefixes": [
            ("India Gate", ["Basmati Rice Everyday Rozana", "Basmati Rice Mogra Broken", "Basmati Rice Biryani Special", "Super Rozana Long Grain"]),
            ("Daawat", ["Devaaya Basmati Rice", "Traditional Long Grain Basmati", "Brown Basmati Fitness Rice", "Pulav Basmati Rice"]),
            ("Tata Sampann", ["Organic Moong Dal Yellow", "Organic Chana Dal", "Organic Kabuli Chana", "Organic Rajma Red", "Organic Urad Black Whole", "Unpolished Masoor Whole"]),
            ("24 Mantra Organic", ["Organic Sonamasuri Raw Rice", "Organic Foxtail Millet", "Organic Little Millet", "Organic Barnyard Millet", "Organic Kodo Millet", "Organic Pearl Millet Grains"]),
            ("Aashirvaad", ["Whole Wheat Atta Sharbati Select", "Fortified Chakki Atta Iron Enriched", "Organic Whole Wheat Atta", "Multigrain Fiber Rich Atta"]),
            ("Fortune", ["Super Food Khichdi Mix Dal & Rice", "Bespoke Biryani Basmati Grain", "Traditional Kachi Ghani Sarson Mustard", "Cottonseed Refined Cooking Oil", "Corn Refined Cooking Oil"]),
            ("Saffola", ["Aura Extra Virgin Olive & Flaxseed Oil", "Gold Pro Blended Cooking Oil", "Tasty Pro Heart Healthy Cooking Oil"])
        ],
        "sizes": ["1 kg pack", "2 kg economy pack", "5 kg family bag", "10 kg bulk pack"],
        "base_price": 120.0,
        "img": IMG_RICE,
        "desc_template": "Premium pantry staple {name}. Rigorously quality-screened for grain consistency, purity, and superior nutrition.",
        "pairing_template": "Essential meal foundation. Frequently paired with yellow dal tadka, desi ghee, rotis, and dry sabzi."
    },
    {
        "category": "Breakfast & Instant Foods",
        "prefixes": [
            ("Maggi", ["Nutri-licious Masala Veg Atta Noodles", "Nutri-licious Oats Masala Noodles", "Hot Heads Spicy Chili Noodles", "Fusilli Cheese Pasta", "Penne Cream Tomato Pasta"]),
            ("Ching's Secret", ["Singapore Curry Instant Noodles", "Manchurian Instant Noodles", "Hot Garlic Instant Noodles", "Egg Hakka Noodles Block", "Veg Chowmein Stir-Fry Noodles"]),
            ("Knorr", ["International Italian Mushroom Soup", "Chicken Delite Sweet Corn Soup", "Spring Vegetable Clear Soup", "Chinese Sweet Corn Hot Soup"]),
            ("Kellogg's", ["Special K Multigrain Fitness Flakes", "Oat Flakes Crunchy Honey", "Chocos Fills Chocolate Center", "Chocos Crunchy Bites Variety"]),
            ("MTR", ["Breakfast Rava Dosa Instant Mix", "Breakfast Vada Instant Mix", "Breakfast Multigrain Idli Mix", "Instant Khaman Dhokla Mix", "Instant Uttapam Breakfast Mix"]),
            ("iD Fresh", ["Ragi Dosa Natural Batter", "Multi-Millet Fermented Batter", "Whole Wheat Malabar Parotta", "Fluffy Wheat Chapati Ready to Puff"]),
            ("Pintola", ["Organic High Protein Crunchy Peanut Butter", "Wood Pressed Coconut Oil Natural Spread", "Performance High Protein Almond Butter", "Dark Chocolate Smooth Peanut Butter"])
        ],
        "sizes": ["Single Serve (75g)", "Family 4-Pack (280g)", "Jumbo Value Pack (500g)", "Mega Saver Box (1 kg)"],
        "base_price": 55.0,
        "img": IMG_NOODLES,
        "desc_template": "Quick and wholesome {name}. Delivers homestyle taste and comforting flavor in minutes.",
        "pairing_template": "Convenient breakfast choice. Frequently paired with boiled milk, eggs, hot coffee, and fruit slices."
    },
    {
        "category": "Dairy, Bread & Eggs",
        "prefixes": [
            ("Amul", ["Cow Milk Homogenised Tetra", "Masti Spiced Jeera Buttermilk", "Pure Buffalo Ghee Rich Aroma", "Garlic Butter Spread Tub", "White Cooking Butter Unsalted", "Pizza Mozzarella Shredded Cheese", "Gouda Dutch Style Cheese Block", "Emmental Swiss Cheese Slice"]),
            ("Mother Dairy", ["Cow Fresh Milk Light", "Full Cream Milk Rich Cream", "Diet Curd Low Fat", "Classic Malai Paneer Block", "Probiotic Tadka Chach Bottle", "Cow Milk Desi Ghee Tin"]),
            ("Britannia", ["Winkin Cow Vanilla Thick Shake", "Winkin Cow Strawberry Thick Shake", "Winkin Cow Chocolate Thick Shake", "Cheese Spread Classic Plain", "Cheese Spread Roasted Garlic", "Cheese Spread Mexican Chilli"]),
            ("Harvest Gold", ["Bombay Pav Jumbo Pack", "Burger Buns Whole Wheat", "Fruit Sweet Bun", "Sweet Coconut Bun", "Dinner Rolls Soft Crust", "Brown Bread Multigrain Fiber"]),
            ("English Oven", ["Ciabatta Artisan Bread", "Focaccia Herb Bread Loaf", "Multigrain Sourdough Bread", "Pita Pocket Breads", "Whole Wheat Burger Buns Sesame"]),
            ("Eggoz", ["Pasteurised Liquid Egg White", "Golden Yolk Country Brown Eggs", "Organic Omega Rich Farm Eggs", "Diet White High Protein Farm Eggs"])
        ],
        "sizes": ["Standard Pack (200g)", "Medium Tub (400g)", "Large Carton (500ml)", "Family Pack (1 Litre / 12 Eggs)"],
        "base_price": 60.0,
        "img": IMG_MILK,
        "desc_template": "Fresh and pure {name}. Farm sourced under strict sanitary conditions for clean wholesome nutrition.",
        "pairing_template": "Daily breakfast and cooking staple. Frequently paired with hot chai, eggs, toast, and lunch curries."
    },
    {
        "category": "Masalas & Spices",
        "prefixes": [
            ("Everest", ["Meat Masala", "Chicken Masala", "Fish Curry Masala", "Egg Curry Masala", "Chana Masala", "Jaljeera Powder Drink", "Pani Puri Masala Cool", "Biryani Spices Aromatic", "Dal Tadka Special Masala", "Dry Ginger Saunth Powder"]),
            ("MDH", ["Amritsari Chole Masala", "Meat Curry Masala", "Fish Masala Spiced", "Shahi Garam Masala Royal", "Kashmiri Mirch Mild Heat", "Pani Puri Masala Tangy", "Dhania Jeera Ground Powder", "Kasuri Methi Fragrant Leaf"]),
            ("Catch", ["Meat Masala", "Chicken Masala", "Garam Masala Sprinkler Can", "Sabzi Masala All In One", "Raita Masala Cumin Blend", "Kitchen King Classic Gravy", "Rock Salt Pink Grinder", "Black Pepper Grinder Bold"]),
            ("Badshah", ["Rajwadi Garam Masala", "Mumbai Bhaji Pav Masala", "Kamal Tea Masala Spiced", "Chaat Masala Tangy", "Biryani Pulav Masala Royal", "Pani Puri Masala Zingy"]),
            ("Tata Sampann", ["Dal Tadka Masala with Natural Oils", "Punjabi Chhole Masala Chef Recipe", "Kashmiri Red Chilli Powder Pure", "Coriander Powder High Aroma", "Cumin Powder Slow Ground", "Garam Masala Chef Special"])
        ],
        "sizes": ["Small Box (50g)", "Standard Box (100g)", "Economy Box (200g)", "Value Pouch (500g)"],
        "base_price": 50.0,
        "img": IMG_SPICES_GROUND,
        "desc_template": "Authentic sun-ripened {name}. Ground at controlled low temperatures to retain intense essential oils and aroma.",
        "pairing_template": "Curry and tadka essential. Frequently paired with Toor Dal, Basmati Rice, Atta rotis, and mustard oil."
    },
    {
        "category": "Tea, Coffee & Beverages",
        "prefixes": [
            ("Tata Tea", ["Gold Care 5 Natural Herbs", "Premium Elaichi Flavor", "Kanan Devan Classic High Grown", "Chakra Gold Strong Dust", "Gemini Strong CTC Leaf"]),
            ("Wagh Bakri", ["Navchetan Strong CTC Leaf", "Good Morning Premium Darjeeling", "Green Tea Honey Lemon Bags", "Green Tea Mint Tulsi Bags", "Instant Masala Tea Premix"]),
            ("Brooke Bond", ["3 Roses Natural Care CTC Tea", "Red Label Dust Strong Leaf", "Taj Mahal Darjeeling Tea", "Taaza Dust Kadak Chai"]),
            ("Nescafé", ["Roast & Ground Filter Coffee", "Latte Hazelnut Instant Premix", "Cappuccino Instant Premix", "Classic Dark Roast Jar", "Gold Origins Alta Rica"]),
            ("Bru", ["Select 100% Pure Filter Coffee", "Roast & Ground Chicory Blend", "Gold Freeze Dried Pure Coffee", "Instant Super Strong Chicory"]),
            ("Real Fruit Power", ["Cranberry Pure Nectar", "Pink Guava Nectar", "Litchi Luscious Drink", "Apple Crisp Mountain Juice", "Grape Black Sweet Juice", "Tender Coconut Water 100% Pure"]),
            ("Paper Boat", ["Alphonso Aam Panna Raw Mango", "Thandai Spiced Milk Drink", "Ginger Lemon Zesty Fizz", "Jamun Kala Khatta Fruit Drink", "Badam Thandai Festive Cooler"]),
            ("Bisleri", ["Fonzo Mango Fizz Soft Drink", "Limmonata Fizzy Lime Drink", "Spyci Jeera Masala Soda", "Vedica Himalayan Sparkling Spring Water"])
        ],
        "sizes": ["200 ml On-The-Go", "500 ml Bottle", "1 Litre Family Tetrapak", "250g Jar / 25 Bags"],
        "base_price": 65.0,
        "img": IMG_TEA,
        "desc_template": "Invigorating {name}. Refreshing taste profile crafted with quality leaves, beans, and fresh natural extracts.",
        "pairing_template": "Refreshing companion. Frequently paired with Parle-G biscuits, Britannia Rusk, and evening snacks."
    }
]

# Generate items systematically across combinations to surpass 1,050 total items
target_count = 1060

while len(all_items) < target_count:
    for cat_data in categories_distribution:
        if len(all_items) >= target_count:
            break
        category = cat_data["category"]
        img = cat_data["img"]
        
        for brand, products in cat_data["prefixes"]:
            if len(all_items) >= target_count:
                break
            for prod in products:
                if len(all_items) >= target_count:
                    break
                for size_idx, size in enumerate(cat_data["sizes"]):
                    if len(all_items) >= target_count:
                        break
                    
                    item_id = f"{brand}_{prod}_{size}".replace(" ", "_").replace("(", "").replace(")", "").replace("/", "_")
                    clean_id = f"item_{item_id.lower()}"
                    if clean_id in existing_ids:
                        continue
                    
                    price = round(cat_data["base_price"] * (1.0 + size_idx * 0.75) + ((len(prod) * 3) % 25), 1)
                    rating = round(4.3 + ((len(prod) + size_idx) % 7) * 0.1, 1)
                    if rating > 4.9:
                        rating = 4.9
                    
                    badges = ["Bestseller", "Top Pick", "Popular", "Family Size", "Value Pack", "Fresh Stock", "Chef's Choice"]
                    badge = badges[(len(prod) + size_idx) % len(badges)]
                    
                    name = f"{brand} {prod} ({size})"
                    desc = cat_data["desc_template"].format(name=f"{brand} {prod}")
                    pairing = cat_data["pairing_template"].format(name=prod)
                    
                    add_item(
                        item_id=item_id,
                        name=name,
                        category=category,
                        price=price,
                        rating=rating,
                        unit=size,
                        badge=badge,
                        image_url=img,
                        description=desc,
                        pairing_text=pairing
                    )

print(f"Successfully generated {len(all_items)} total items!")

# Save to root items.json
with open(ITEMS_JSON_ROOT, "w", encoding="utf-8") as f:
    json.dump(all_items, f, indent=2, ensure_ascii=False)
print(f"Saved {len(all_items)} items to {ITEMS_JSON_ROOT}")

# Save to src items.json
with open(ITEMS_JSON_SRC, "w", encoding="utf-8") as f:
    json.dump(all_items, f, indent=2, ensure_ascii=False)
print(f"Saved {len(all_items)} items to {ITEMS_JSON_SRC}")
