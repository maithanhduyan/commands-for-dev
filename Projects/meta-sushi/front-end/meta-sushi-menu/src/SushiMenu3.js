import React, { useState, useEffect } from 'react';
import { FaSearch, FaHeart, FaShoppingCart, FaStar, FaTimes } from 'react-icons/fa';
import { IoMdAdd, IoMdRemove } from 'react-icons/io';
import { motion } from 'framer-motion';

import Edamame_Img from './assets/images/Steamed soybeans with sea salt.jpg';
import californiaRoll2Img from './assets/images/california_Roll2.jpg';
import Salmon_Nigiri_Img from './assets/images/Salmon_Nigiri.jpg';
import Dragon_Roll_Img from './assets/images/vegetable-tempura-roll.jpg';
import Mochi_Ice_Cream_Img from './assets/images/mochi_ice_cream.jpg';



const menuItems = [
  {
    id: 1,
    name: 'California Roll',
    description: 'Crab, avocado, and cucumber roll',
    price: 8.99,
    category: 'sushi rolls',
    tags: ['popular'],
    image: californiaRoll2Img
  },
  {
    id: 2,
    name: 'Edamame',
    description: 'Steamed soybeans with sea salt',
    price: 5.99,
    category: 'appetizers',
    tags: ['vegetarian', 'gluten-free'],
    image: Edamame_Img
  },
  {
    id: 3,
    name: 'Salmon Nigiri',
    description: 'Fresh salmon over pressed rice',
    price: 6.99,
    category: 'nigiri',
    tags: ['gluten-free'],
    image: Salmon_Nigiri_Img
  },
  {
    id: 4,
    name: 'Dragon Roll',
    description: 'Eel, crab, cucumber topped with avocado',
    price: 12.99,
    category: 'sushi rolls',
    tags: ['chef special'],
    image: Dragon_Roll_Img
  },
  {
    id: 5,
    name: 'Mochi Ice Cream',
    description: 'Assorted flavors of ice cream wrapped in mochi',
    price: 7.99,
    category: 'desserts',
    tags: ['vegetarian'],
    image: Mochi_Ice_Cream_Img
  },
];

const SushiMenu = () => {
  const [filteredItems, setFilteredItems] = useState(menuItems);
  const [activeFilter, setActiveFilter] = useState('all');
  const [searchTerm, setSearchTerm] = useState('');
  const [sortBy, setSortBy] = useState('name');
  const [cart, setCart] = useState([]);
  const [favorites, setFavorites] = useState([]);
  const [isCartOpen, setIsCartOpen] = useState(false);

  useEffect(() => {
    let result = menuItems;
    if (activeFilter !== 'all') {
      result = result.filter(item => item.tags.includes(activeFilter) || item.category === activeFilter);
    }
    if (searchTerm) {
      result = result.filter(item =>
        item.name.toLowerCase().includes(searchTerm.toLowerCase()) ||
        item.description.toLowerCase().includes(searchTerm.toLowerCase())
      );
    }
    result.sort((a, b) => {
      if (sortBy === 'price') return a.price - b.price;
      if (sortBy === 'name') return a.name.localeCompare(b.name);
      return 0;
    });
    setFilteredItems(result);
  }, [activeFilter, searchTerm, sortBy]);

  const addToCart = (item) => {
    const existingItem = cart.find(cartItem => cartItem.id === item.id);
    if (existingItem) {
      setCart(cart.map(cartItem =>
        cartItem.id === item.id ? { ...cartItem, quantity: cartItem.quantity + 1 } : cartItem
      ));
    } else {
      setCart([...cart, { ...item, quantity: 1 }]);
    }
  };

  const removeFromCart = (itemId) => {
    const updatedCart = cart.map(item =>
      item.id === itemId ? { ...item, quantity: item.quantity - 1 } : item
    ).filter(item => item.quantity > 0);
    setCart(updatedCart);
  };

  const getTotalCost = () => {
    return cart.reduce((total, item) => total + item.price * item.quantity, 0).toFixed(2);
  };

  const clearCart = () => {
    setCart([]);
  };

  const placeOrder = () => {
    alert('Your order has been placed!');
    clearCart();
    setIsCartOpen(false);
  };

  const toggleFavorite = (item) => {
    if (favorites.find(fav => fav.id === item.id)) {
      setFavorites(favorites.filter(fav => fav.id !== item.id));
    } else {
      setFavorites([...favorites, item]);
    }
  };

  return (
    <div className="container mx-auto px-4 py-8 bg-gray-100 min-h-screen">
      <h1 className="text-4xl font-bold text-center text-red-600 mb-8">Meta Sushi Menu</h1>

      <div className="flex flex-col md:flex-row justify-between items-center mb-8">
        <div className="relative w-full md:w-1/3 mb-4 md:mb-0">
          <input
            type="text"
            placeholder="Search menu..."
            className="w-full p-2 pl-10 rounded-full border-2 border-red-300 focus:outline-none focus:border-red-500"
            value={searchTerm}
            onChange={(e) => setSearchTerm(e.target.value)}
          />
          <FaSearch className="absolute left-3 top-3 text-gray-400" />
        </div>

        <div className="flex space-x-2">
          <select
            className="p-2 rounded-md border-2 border-red-300 focus:outline-none focus:border-red-500"
            value={activeFilter}
            onChange={(e) => setActiveFilter(e.target.value)}
          >
            <option value="all">All Items</option>
            <option value="appetizers">Appetizers</option>
            <option value="sushi rolls">Sushi Rolls</option>
            <option value="nigiri">Nigiri</option>
            <option value="desserts">Desserts</option>
            <option value="vegetarian">Vegetarian</option>
            <option value="gluten-free">Gluten-Free</option>
            <option value="chef special">Chef's Special</option>
          </select>

          <select
            className="p-2 rounded-md border-2 border-red-300 focus:outline-none focus:border-red-500"
            value={sortBy}
            onChange={(e) => setSortBy(e.target.value)}
          >
            <option value="name">Sort by Name</option>
            <option value="price">Sort by Price</option>
          </select>
        </div>
      </div>

      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
        {filteredItems.map((item) => (
          <motion.div
            key={item.id}
            className="bg-white rounded-lg shadow-md overflow-hidden"
            whileHover={{ scale: 1.05 }}
            transition={{ duration: 0.3 }}
          >
            <img src={item.image} alt={item.name} className="w-full h-48 object-cover" />
            <div className="p-4">
              <div className="flex justify-between items-start mb-2">
                <h2 className="text-xl font-semibold text-gray-800">{item.name}</h2>
                <span className="text-lg font-bold text-red-600">${item.price.toFixed(2)}</span>
              </div>
              <p className="text-gray-600 mb-4">{item.description}</p>
              <div className="flex justify-between items-center">
                <div className="space-x-2">
                  {item.tags.map((tag) => (
                    <span key={tag} className="inline-block bg-red-100 text-red-800 text-xs px-2 py-1 rounded-full">{tag}</span>
                  ))}
                </div>
                <div className="space-x-2">
                  <button
                    onClick={() => toggleFavorite(item)}
                    className="text-red-500 hover:text-red-700"
                    aria-label={`Add ${item.name} to favorites`}
                  >
                    <FaHeart className={favorites.find(fav => fav.id === item.id) ? 'text-red-500' : 'text-gray-400'} />
                  </button>
                  <button
                    onClick={() => addToCart(item)}
                    className="bg-red-500 text-white px-3 py-1 rounded-full hover:bg-red-600"
                    aria-label={`Add ${item.name} to cart`}
                  >
                    <FaShoppingCart />
                  </button>
                </div>
              </div>
            </div>
          </motion.div>
        ))}
      </div>

      {filteredItems.length === 0 && (
        <p className="text-center text-gray-500 mt-8">No items found. Try adjusting your search or filters.</p>
      )}

      {/* Cart and Favorites Buttons */}
      <div className="fixed bottom-4 right-4 flex space-x-4">
        <button
          onClick={() => setIsCartOpen(true)}
          className="bg-red-500 text-white p-3 rounded-full shadow-lg hover:bg-red-600 relative"
          aria-label="View cart"
        >
          <FaShoppingCart />
          {cart.length > 0 && (
            <span className="absolute -top-2 -right-2 bg-yellow-500 text-xs text-white w-5 h-5 flex items-center justify-center rounded-full">
              {cart.length}
            </span>
          )}
        </button>
        <button
          className="bg-red-500 text-white p-3 rounded-full shadow-lg hover:bg-red-600 relative"
          aria-label="View favorites"
        >
          <FaHeart />
          {favorites.length > 0 && (
            <span className="absolute -top-2 -right-2 bg-yellow-500 text-xs text-white w-5 h-5 flex items-center justify-center rounded-full">
              {favorites.length}
            </span>
          )}
        </button>
      </div>

      {/* Cart Component */}
      {isCartOpen && (
        <div className="fixed top-0 right-0 w-full sm:w-96 h-full bg-white shadow-lg z-50 overflow-y-auto">
          <div className="p-4">
            <div className="flex justify-between items-center mb-4">
              <h2 className="text-2xl font-bold">Your Cart</h2>
              <button
                onClick={() => setIsCartOpen(false)}
                className="text-gray-500 hover:text-gray-700"
                aria-label="Close cart"
              >
                <FaTimes />
              </button>
            </div>
            {cart.length === 0 ? (
              <p>Your cart is empty</p>
            ) : (
              <>
                {cart.map((item) => (
                  <div key={item.id} className="flex justify-between items-center mb-2">
                    <span>{item.name}</span>
                    <div className="flex items-center">
                      <button
                        onClick={() => removeFromCart(item.id)}
                        className="text-red-500 mr-2"
                        aria-label={`Remove ${item.name} from cart`}
                      >
                        <IoMdRemove />
                      </button>
                      <span>{item.quantity}</span>
                      <button
                        onClick={() => addToCart(item)}
                        className="text-green-500 ml-2"
                        aria-label={`Add another ${item.name} to cart`}
                      >
                        <IoMdAdd />
                      </button>
                    </div>
                  </div>
                ))}
                <div className="mt-4">
                  <p className="text-xl font-bold">Total: ${getTotalCost()}</p>
                  <button
                    onClick={placeOrder}
                    className="w-full bg-green-500 text-white py-2 rounded mt-4 hover:bg-green-600 transition-colors"
                  >
                    Place Order
                  </button>
                  <button
                    onClick={clearCart}
                    className="w-full bg-red-500 text-white py-2 rounded mt-4 hover:bg-red-600 transition-colors"
                  >
                    Clear Cart
                  </button>
                </div>
              </>
            )}
          </div>
        </div>
      )}
    </div>
  );
};

export default SushiMenu;