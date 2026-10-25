/**
 * QuickCart AI — Smart Shopping Cart & Vector Recommendation Engine
 * Frontend Logic & Real-time Embedding Interactions
 */

// API Configuration
const API_BASE = window.location.origin.startsWith('http') 
  ? window.location.origin 
  : 'http://localhost:8000';

// Global Application State
let allProducts = [];
let displayedProducts = [];
let cart = {}; // itemId -> { item, quantity }
let activeCategory = 'all';
let searchQuery = '';
let activeRecommendationSource = null;
let visibleCount = 48;

// DOM Elements
const productGrid = document.getElementById('productGrid');
const categoryTabs = document.getElementById('categoryTabs');
const searchInput = document.getElementById('searchInput');
const clearSearchBtn = document.getElementById('clearSearchBtn');
const sortSelect = document.getElementById('sortSelect');
const catalogTitle = document.getElementById('currentCategoryTitle');
const catalogCountBadge = document.getElementById('catalogCountBadge');

// Recommendation Banner Elements
const recommendationBanner = document.getElementById('recommendationBanner');
const recBannerTitle = document.getElementById('recBannerTitle');
const recBannerSubtitle = document.getElementById('recBannerSubtitle');
const recBannerCards = document.getElementById('recBannerCards');
const closeRecBannerBtn = document.getElementById('closeRecBannerBtn');

// Cart Drawer Elements
const cartDrawer = document.getElementById('cartDrawer');
const cartDrawerOverlay = document.getElementById('cartDrawerOverlay');
const cartToggleBtn = document.getElementById('cartToggleBtn');
const closeCartBtn = document.getElementById('closeCartBtn');
const cartItemsList = document.getElementById('cartItemsList');
const cartEmptyState = document.getElementById('cartEmptyState');
const cartBadgeCount = document.getElementById('cartBadgeCount');
const cartTotalHeader = document.getElementById('cartTotalHeader');
const cartItemCountHeader = document.getElementById('cartItemCountHeader');
const deliveryProgressMsg = document.getElementById('deliveryProgressMsg');
const deliveryProgressBar = document.getElementById('deliveryProgressBar');
const cartSubtotal = document.getElementById('cartSubtotal');
const cartDeliveryFee = document.getElementById('cartDeliveryFee');
const cartDiscount = document.getElementById('cartDiscount');
const cartDiscountRow = document.getElementById('cartDiscountRow');
const cartGrandTotal = document.getElementById('cartGrandTotal');
const checkoutBtn = document.getElementById('checkoutBtn');
const checkoutBtnAmount = document.getElementById('checkoutBtnAmount');
const cartRecommendationsSection = document.getElementById('cartRecommendationsSection');
const cartRecCards = document.getElementById('cartRecCards');

// Modals
const productModalOverlay = document.getElementById('productModalOverlay');
const closeModalBtn = document.getElementById('closeModalBtn');
const modalProductImg = document.getElementById('modalProductImg');
const modalProductBadge = document.getElementById('modalProductBadge');
const modalCategory = document.getElementById('modalCategory');
const modalTitle = document.getElementById('modalTitle');
const modalRating = document.getElementById('modalRating');
const modalUnit = document.getElementById('modalUnit');
const modalPrice = document.getElementById('modalPrice');
const modalDescription = document.getElementById('modalDescription');
const modalAddToCartBtn = document.getElementById('modalAddToCartBtn');
const modalPairingsList = document.getElementById('modalPairingsList');

// Order Success Modal
const orderSuccessModalOverlay = document.getElementById('orderSuccessModalOverlay');
const orderIdText = document.getElementById('orderIdText');
const orderSummaryBox = document.getElementById('orderSummaryBox');
const continueShoppingBtn = document.getElementById('continueShoppingBtn');

// Theme & Toast
const themeToggleBtn = document.getElementById('themeToggleBtn');
const toastContainer = document.getElementById('toastContainer');

// Active modal item reference
let currentModalItem = null;

// ==========================================================================
// Initialization
// ==========================================================================
document.addEventListener('DOMContentLoaded', () => {
  initTheme();
  loadCartFromStorage();
  fetchCatalog();
  attachEventListeners();
});

function initTheme() {
  const savedTheme = localStorage.getItem('quickcart_theme') || 'light';
  if (savedTheme === 'dark') {
    document.body.classList.remove('light-theme');
    document.body.classList.add('dark-theme');
    themeToggleBtn.querySelector('.theme-icon').textContent = '☀️';
  } else {
    document.body.classList.add('light-theme');
    document.body.classList.remove('dark-theme');
    themeToggleBtn.querySelector('.theme-icon').textContent = '🌙';
  }
}

function toggleTheme() {
  const isDark = document.body.classList.contains('dark-theme');
  if (isDark) {
    document.body.classList.remove('dark-theme');
    document.body.classList.add('light-theme');
    themeToggleBtn.querySelector('.theme-icon').textContent = '🌙';
    localStorage.setItem('quickcart_theme', 'light');
  } else {
    document.body.classList.remove('light-theme');
    document.body.classList.add('dark-theme');
    themeToggleBtn.querySelector('.theme-icon').textContent = '☀️';
    localStorage.setItem('quickcart_theme', 'dark');
  }
}

// ==========================================================================
// API Calls & Data Fetching
// ==========================================================================
async function fetchCatalog() {
  try {
    const res = await fetch(`${API_BASE}/api/items`);
    if (!res.ok) throw new Error(`HTTP ${res.status}`);
    allProducts = await res.json();
    const allPill = document.getElementById('allCategoryPill');
    if (allPill) allPill.textContent = `All Items (${allProducts.length})`;
    displayedProducts = [...allProducts];
    visibleCount = 48;
    renderProducts();
    updateCartUI();
  } catch (err) {
    console.error('Error fetching items catalog:', err);
    productGrid.innerHTML = `
      <div class="empty-search-state">
        <h3>Could not connect to QuickCart API</h3>
        <p>Ensure the FastAPI server is running on <code>http://localhost:8000</code></p>
      </div>
    `;
  }
}

async function fetchRecommendationsForItem(itemId) {
  try {
    const res = await fetch(`${API_BASE}/api/recommend/${itemId}?limit=4`);
    if (!res.ok) throw new Error(`HTTP ${res.status}`);
    return await res.json();
  } catch (err) {
    console.error(`Error fetching recommendations for ${itemId}:`, err);
    return [];
  }
}

async function fetchRecommendationsForCart(itemIds) {
  try {
    const res = await fetch(`${API_BASE}/api/recommend/cart`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ item_ids: itemIds, limit: 3 })
    });
    if (!res.ok) throw new Error(`HTTP ${res.status}`);
    return await res.json();
  } catch (err) {
    console.error('Error fetching cart recommendations:', err);
    return [];
  }
}

async function performSemanticSearch(query) {
  if (!query || query.trim() === '') {
    displayedProducts = [...allProducts];
    visibleCount = 48;
    renderProducts();
    return;
  }

  productGrid.innerHTML = `
    <div class="loading-state">
      <div class="spinner"></div>
      <p>Semantic Vector Search for "${query}"...</p>
    </div>
  `;

  try {
    const res = await fetch(`${API_BASE}/api/search?q=${encodeURIComponent(query)}&limit=10`);
    if (!res.ok) throw new Error(`HTTP ${res.status}`);
    const results = await res.json();
    displayedProducts = results;
    visibleCount = 48;
    catalogTitle.textContent = `Search results for "${query}"`;
    catalogCountBadge.textContent = `${results.length} found`;
    renderProducts();
  } catch (err) {
    console.error('Search error:', err);
    // Client-side fallback text filter
    displayedProducts = allProducts.filter(p => 
      p.name.toLowerCase().includes(query.toLowerCase()) || 
      p.description.toLowerCase().includes(query.toLowerCase())
    );
    renderProducts();
  }
}

// ==========================================================================
// Rendering Functions
// ==========================================================================
function renderProducts() {
  if (displayedProducts.length === 0) {
    productGrid.innerHTML = `
      <div class="empty-search-state">
        <span style="font-size: 2.5rem; display:block; margin-bottom: 10px;">🔍</span>
        <h3>No matching items found</h3>
        <p>Try searching for "bread", "snacks", "spices", or "breakfast"</p>
      </div>
    `;
    return;
  }

  const itemsToShow = displayedProducts.slice(0, visibleCount);

  const cardsHtml = itemsToShow.map(product => {
    const inCartQty = cart[product.id] ? cart[product.id].quantity : 0;
    const similarityBadge = product.similarity_percent 
      ? `<span class="rec-match-pill" style="margin-bottom: 6px;">${product.similarity_percent}% Match</span>`
      : '';

    return `
      <div class="product-card" data-id="${product.id}">
        <div class="card-img-wrapper" onclick="openProductModal('${product.id}')">
          <img 
            src="${product.image_url}" 
            alt="${product.name}" 
            class="card-img" 
            loading="lazy"
            onerror="this.src='https://images.unsplash.com/photo-1542838132-92c53300491e?w=600&auto=format&fit=crop&q=80'"
          >
          ${product.badge ? `<span class="card-badge">${product.badge}</span>` : ''}
          <button class="card-quick-view-btn" onclick="event.stopPropagation(); openProductModal('${product.id}')">
            ✨ Pairings & Info
          </button>
        </div>

        <div class="card-content">
          ${similarityBadge}
          <span class="card-category">${product.category}</span>
          <h3 class="card-title" onclick="openProductModal('${product.id}')">${product.name}</h3>
          <span class="card-unit">${product.unit || 'Standard Pack'}</span>

          <div class="card-meta-row">
            <span class="card-rating">⭐ ${product.rating || '4.8'}</span>
          </div>

          <div class="card-footer">
            <span class="card-price">₹${product.price.toFixed(2)}</span>

            ${inCartQty === 0 ? `
              <button class="add-btn" onclick="addToCart('${product.id}')">
                + Add
              </button>
            ` : `
              <div class="qty-control">
                <button class="qty-btn" onclick="updateItemQuantity('${product.id}', -1)">−</button>
                <span class="qty-val">${inCartQty}</span>
                <button class="qty-btn" onclick="updateItemQuantity('${product.id}', 1)">+</button>
              </div>
            `}
          </div>
        </div>
      </div>
    `;
  }).join('');

  const loadMoreHtml = displayedProducts.length > visibleCount ? `
    <div class="load-more-container">
      <button id="loadMoreBtn" class="load-more-btn" onclick="loadMoreProducts()">
        Load More Products (Showing ${itemsToShow.length} of ${displayedProducts.length})
      </button>
    </div>
  ` : '';

  productGrid.innerHTML = cardsHtml + loadMoreHtml;
}

window.loadMoreProducts = function() {
  visibleCount += 48;
  renderProducts();
};

// ==========================================================================
// Smart Recommendation Banner (Frequently Bought Together)
// ==========================================================================
async function triggerRecommendationForProduct(product) {
  activeRecommendationSource = product;
  const recommendations = await fetchRecommendationsForItem(product.id);
  
  if (!recommendations || recommendations.length === 0) return;

  recBannerTitle.innerHTML = `Ordered <strong>${product.name}</strong>? Frequently Bought Together:`;
  recBannerSubtitle.textContent = `AI vector embeddings recommend these complementary pairings for your order`;

  recBannerCards.innerHTML = recommendations.slice(0, 3).map(rec => `
    <div class="rec-mini-card">
      <img src="${rec.image_url}" alt="${rec.name}" class="rec-mini-img" onerror="this.src='https://images.unsplash.com/photo-1542838132-92c53300491e?w=600&auto=format&fit=crop&q=80'">
      <div class="rec-mini-info">
        <span class="rec-match-pill">${rec.similarity_percent}% Pair Match</span>
        <h4 class="rec-mini-title">${rec.name}</h4>
        <span class="rec-mini-price">₹${rec.price.toFixed(2)}</span>
      </div>
      <button class="rec-mini-add-btn" onclick="addToCart('${rec.id}')">
        + Add
      </button>
    </div>
  `).join('');

  recommendationBanner.classList.remove('hidden');
  recommendationBanner.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
}

// ==========================================================================
// Cart State & Drawer Logic
// ==========================================================================
function addToCart(itemId) {
  const item = allProducts.find(p => p.id === itemId);
  if (!item) return;

  if (cart[itemId]) {
    cart[itemId].quantity += 1;
  } else {
    cart[itemId] = { item, quantity: 1 };
  }

  saveCartToStorage();
  updateCartUI();
  renderProducts();

  // Trigger dynamic recommendation banner for this item!
  triggerRecommendationForProduct(item);

  // Show Toast
  showToast(`Added ${item.name} to cart!`);
}

function updateItemQuantity(itemId, delta) {
  if (!cart[itemId]) return;

  cart[itemId].quantity += delta;
  if (cart[itemId].quantity <= 0) {
    delete cart[itemId];
  }

  saveCartToStorage();
  updateCartUI();
  renderProducts();
}

function updateCartUI() {
  const cartEntries = Object.values(cart);
  const totalCount = cartEntries.reduce((sum, entry) => sum + entry.quantity, 0);
  const subtotal = cartEntries.reduce((sum, entry) => sum + (entry.item.price * entry.quantity), 0);

  // Header Cart Badge & Total
  cartBadgeCount.textContent = totalCount;
  cartTotalHeader.textContent = `₹${subtotal.toFixed(2)}`;
  cartItemCountHeader.textContent = `${totalCount} item${totalCount === 1 ? '' : 's'}`;

  // Free delivery progress (₹199 threshold)
  const deliveryThreshold = 199.0;
  if (subtotal >= deliveryThreshold || subtotal === 0) {
    deliveryProgressBar.style.width = '100%';
    deliveryProgressMsg.innerHTML = subtotal === 0 
      ? `Add ₹199.00 for <strong>FREE Delivery</strong>` 
      : `🎉 You unlocked <strong>FREE Delivery!</strong>`;
  } else {
    const diff = deliveryThreshold - subtotal;
    const pct = Math.min(100, Math.round((subtotal / deliveryThreshold) * 100));
    deliveryProgressBar.style.width = `${pct}%`;
    deliveryProgressMsg.innerHTML = `Add <strong>₹${diff.toFixed(2)}</strong> more for <strong>FREE Delivery</strong>`;
  }

  // Cart Empty State vs Items List
  if (totalCount === 0) {
    cartEmptyState.style.display = 'block';
    cartItemsList.innerHTML = '';
    cartRecommendationsSection.classList.add('hidden');
    checkoutBtn.disabled = true;

    cartSubtotal.textContent = '₹0.00';
    cartDeliveryFee.textContent = '₹0.00';
    cartDiscountRow.style.display = 'none';
    cartGrandTotal.textContent = '₹0.00';
    checkoutBtnAmount.textContent = '₹0.00';
    return;
  }

  cartEmptyState.style.display = 'none';
  checkoutBtn.disabled = false;

  // Render items list
  cartItemsList.innerHTML = cartEntries.map(entry => {
    const lineTotal = (entry.item.price * entry.quantity).toFixed(2);
    return `
      <div class="cart-item-row">
        <img src="${entry.item.image_url}" alt="${entry.item.name}" class="cart-item-img" onerror="this.src='https://images.unsplash.com/photo-1542838132-92c53300491e?w=600&auto=format&fit=crop&q=80'">
        <div class="cart-item-details">
          <div class="cart-item-title">${entry.item.name}</div>
          <div class="cart-item-price">₹${entry.item.price.toFixed(2)} × ${entry.quantity} = <strong>₹${lineTotal}</strong></div>
        </div>
        <div class="cart-item-qty-wrap">
          <div class="qty-control">
            <button class="qty-btn" onclick="updateItemQuantity('${entry.item.id}', -1)">−</button>
            <span class="qty-val">${entry.quantity}</span>
            <button class="qty-btn" onclick="updateItemQuantity('${entry.item.id}', 1)">+</button>
          </div>
        </div>
      </div>
    `;
  }).join('');

  // Bill Calculations
  const deliveryFee = subtotal >= deliveryThreshold ? 0.0 : 30.0;
  const discount = subtotal >= 499 ? 50.0 : 0.0;
  const grandTotal = Math.max(0, subtotal + deliveryFee - discount);

  cartSubtotal.textContent = `₹${subtotal.toFixed(2)}`;
  cartDeliveryFee.textContent = deliveryFee === 0 ? 'FREE' : `₹${deliveryFee.toFixed(2)}`;
  
  if (discount > 0) {
    cartDiscountRow.style.display = 'flex';
    cartDiscount.textContent = `-₹${discount.toFixed(2)}`;
  } else {
    cartDiscountRow.style.display = 'none';
  }

  cartGrandTotal.textContent = `₹${grandTotal.toFixed(2)}`;
  checkoutBtnAmount.textContent = `₹${grandTotal.toFixed(2)}`;

  // Update AI Basket Recommendations in Cart
  updateCartRecommendations();
}

async function updateCartRecommendations() {
  const itemIds = Object.keys(cart);
  if (itemIds.length === 0) {
    cartRecommendationsSection.classList.add('hidden');
    return;
  }

  const recs = await fetchRecommendationsForCart(itemIds);
  if (!recs || recs.length === 0) {
    cartRecommendationsSection.classList.add('hidden');
    return;
  }

  cartRecommendationsSection.classList.remove('hidden');
  cartRecCards.innerHTML = recs.map(item => `
    <div class="cart-rec-card">
      <img src="${item.image_url}" alt="${item.name}" onerror="this.src='https://images.unsplash.com/photo-1542838132-92c53300491e?w=600&auto=format&fit=crop&q=80'">
      <div class="cart-rec-card-info">
        <div class="cart-rec-card-title">${item.name}</div>
        <span class="cart-rec-card-match">${item.similarity_percent}% Basket Match • ₹${item.price.toFixed(2)}</span>
      </div>
      <button class="cart-rec-card-btn" onclick="addToCart('${item.id}')">+ Add</button>
    </div>
  `).join('');
}

function openCart() {
  cartDrawer.classList.add('open');
  cartDrawerOverlay.classList.remove('hidden');
}

function closeCart() {
  cartDrawer.classList.remove('open');
  cartDrawerOverlay.classList.add('hidden');
}

function saveCartToStorage() {
  localStorage.setItem('quickcart_items', JSON.stringify(cart));
}

function loadCartFromStorage() {
  try {
    const saved = localStorage.getItem('quickcart_items');
    if (saved) {
      cart = JSON.parse(saved);
    }
  } catch (e) {
    cart = {};
  }
}

// ==========================================================================
// Product Quick-View & Vector Similarity Modal
// ==========================================================================
async function openProductModal(itemId) {
  const product = allProducts.find(p => p.id === itemId);
  if (!product) return;

  currentModalItem = product;
  modalProductImg.src = product.image_url;
  modalProductBadge.textContent = product.badge || 'Featured';
  modalCategory.textContent = product.category;
  modalTitle.textContent = product.name;
  modalRating.textContent = `⭐ ${product.rating || '4.8'}`;
  modalUnit.textContent = product.unit || 'Standard';
  modalPrice.textContent = `₹${product.price.toFixed(2)}`;
  modalDescription.textContent = product.description;

  modalPairingsList.innerHTML = `<div class="spinner" style="margin: 20px auto;"></div>`;
  productModalOverlay.classList.remove('hidden');

  // Fetch Vector Similarity Pairings
  const recommendations = await fetchRecommendationsForItem(itemId);
  if (recommendations && recommendations.length > 0) {
    modalPairingsList.innerHTML = recommendations.map(rec => `
      <div class="modal-pairing-item">
        <img src="${rec.image_url}" alt="${rec.name}" onerror="this.src='https://images.unsplash.com/photo-1542838132-92c53300491e?w=600&auto=format&fit=crop&q=80'">
        <div class="modal-pairing-info">
          <div class="modal-pairing-name">${rec.name} (₹${rec.price.toFixed(2)})</div>
          <div class="modal-pairing-reason">💡 ${rec.recommendation_reason}</div>
        </div>
        <div class="modal-sim-bar-wrap">
          <span class="modal-sim-pct">${rec.similarity_percent}%</span>
          <div class="modal-sim-bar">
            <div class="modal-sim-fill" style="width: ${rec.similarity_percent}%"></div>
          </div>
        </div>
        <button class="rec-mini-add-btn" onclick="addToCart('${rec.id}')">+ Add</button>
      </div>
    `).join('');
  } else {
    modalPairingsList.innerHTML = `<p style="font-size: 0.85rem; color: var(--text-muted);">No pairings found.</p>`;
  }
}

function closeProductModal() {
  productModalOverlay.classList.add('hidden');
}

// ==========================================================================
// Checkout & Celebration Modal
// ==========================================================================
function handleCheckout() {
  const cartEntries = Object.values(cart);
  if (cartEntries.length === 0) return;

  closeCart();
  const randomOrderNum = Math.floor(10000 + Math.random() * 90000);
  orderIdText.textContent = `#QC-${randomOrderNum}`;

  orderSummaryBox.innerHTML = `
    <strong>Items Ordered (${cartEntries.reduce((s, e) => s + e.quantity, 0)}):</strong>
    <ul style="margin: 6px 0 0 16px; padding: 0;">
      ${cartEntries.map(e => `<li>${e.item.name} × ${e.quantity} (₹${(e.item.price * e.quantity).toFixed(2)})</li>`).join('')}
    </ul>
  `;

  orderSuccessModalOverlay.classList.remove('hidden');

  // Reset Cart
  cart = {};
  saveCartToStorage();
  updateCartUI();
  renderProducts();
}

function closeOrderModal() {
  orderSuccessModalOverlay.classList.add('hidden');
}

// ==========================================================================
// Toast Notifications
// ==========================================================================
function showToast(message) {
  const toast = document.createElement('div');
  toast.className = 'toast';
  toast.innerHTML = `<span>✨</span><span>${message}</span>`;
  toastContainer.appendChild(toast);

  setTimeout(() => {
    toast.style.opacity = '0';
    toast.style.transform = 'translateY(10px)';
    toast.style.transition = 'all 0.3s ease';
    setTimeout(() => toast.remove(), 300);
  }, 2400);
}

// ==========================================================================
// Event Listeners Setup
// ==========================================================================
function attachEventListeners() {
  // Theme Toggle
  themeToggleBtn.addEventListener('click', toggleTheme);

  // Cart Drawer
  cartToggleBtn.addEventListener('click', openCart);
  closeCartBtn.addEventListener('click', closeCart);
  cartDrawerOverlay.addEventListener('click', closeCart);
  checkoutBtn.addEventListener('click', handleCheckout);

  // Close Banner
  closeRecBannerBtn.addEventListener('click', () => {
    recommendationBanner.classList.add('hidden');
  });

  // Category Tabs Filter
  categoryTabs.addEventListener('click', (e) => {
    const pill = e.target.closest('.category-pill');
    if (!pill) return;

    document.querySelectorAll('.category-pill').forEach(p => p.classList.remove('active'));
    pill.classList.add('active');

    activeCategory = pill.dataset.category;
    filterAndSortProducts();
  });

  // Sort Dropdown
  sortSelect.addEventListener('change', () => {
    filterAndSortProducts();
  });

  // Search Input with Debounce
  let searchTimeout = null;
  searchInput.addEventListener('input', (e) => {
    const val = e.target.value.trim();
    clearSearchBtn.style.display = val.length > 0 ? 'block' : 'none';

    clearTimeout(searchTimeout);
    searchTimeout = setTimeout(() => {
      searchQuery = val;
      if (val.length >= 2) {
        performSemanticSearch(val);
      } else {
        filterAndSortProducts();
      }
    }, 350);
  });

  clearSearchBtn.addEventListener('click', () => {
    searchInput.value = '';
    searchQuery = '';
    clearSearchBtn.style.display = 'none';
    filterAndSortProducts();
  });

  // Demo Chips
  document.querySelectorAll('.demo-chip').forEach(chip => {
    chip.addEventListener('click', () => {
      const itemId = chip.dataset.item;
      const targetItem = allProducts.find(p => p.id === itemId);
      if (targetItem) {
        addToCart(itemId);
        openProductModal(itemId);
      }
    });
  });

  // Product Modal Events
  closeModalBtn.addEventListener('click', closeProductModal);
  productModalOverlay.addEventListener('click', (e) => {
    if (e.target === productModalOverlay) closeProductModal();
  });

  modalAddToCartBtn.addEventListener('click', () => {
    if (currentModalItem) {
      addToCart(currentModalItem.id);
      closeProductModal();
    }
  });

  // Order Success Modal Events
  continueShoppingBtn.addEventListener('click', closeOrderModal);
  orderSuccessModalOverlay.addEventListener('click', (e) => {
    if (e.target === orderSuccessModalOverlay) closeOrderModal();
  });
}

function filterAndSortProducts() {
  if (activeCategory === 'all') {
    displayedProducts = [...allProducts];
    catalogTitle.textContent = 'All Grocery & Supermarket Items';
  } else {
    displayedProducts = allProducts.filter(p => p.category === activeCategory);
    catalogTitle.textContent = activeCategory;
  }

  // Sort
  const sortMode = sortSelect.value;
  if (sortMode === 'price-low') {
    displayedProducts.sort((a, b) => a.price - b.price);
  } else if (sortMode === 'price-high') {
    displayedProducts.sort((a, b) => b.price - a.price);
  } else if (sortMode === 'rating') {
    displayedProducts.sort((a, b) => (b.rating || 0) - (a.rating || 0));
  }

  visibleCount = 48;
  catalogCountBadge.textContent = `${displayedProducts.length} items`;
  renderProducts();
}
