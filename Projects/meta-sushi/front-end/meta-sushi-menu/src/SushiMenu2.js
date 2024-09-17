import React, { useState, useEffect } from 'react';
import { FaSearch, FaShoppingCart, FaFilter, FaSort } from 'react-icons/fa';
import { motion, AnimatePresence } from 'framer-motion';

import californiaRoll2Img from './assets/images/california_Roll2.jpg'; // https://images.unsplash.com/photo-1579871494447-9811cf80d66c
import Salmon_Nigiri_Img from './assets/images/Salmon_Nigiri.jpg'; // https://images.unsplash.com/photo-1534482421-64566f976cfa
import Spicy_Tuna_Roll_Img from './assets/images/Spicy_Tuna_Roll.jpg'; // https://images.unsplash.com/photo-1617196034796-73dfa7b1fd56
import Vegetable_Tempura_Roll_Img from './assets/images/Veggie-Tempura-Roll_ok.jpg'; // https://images.unsplash.com/photo-1620039102630-11cb2004c5c5
import Tuna_Sashimi_Img from './assets/images/california-roll.jpg'; // https://images.unsplash.com/photo-1579584425555-c3ce17fd4351

const sushiMenu = [
  { id: 1, name: 'California Roll', category: 'Maki Rolls', price: 8.99, description: 'Crab, avocado, cucumber', image: californiaRoll2Img, tags: ['popular'] },
  { id: 2, name: 'Salmon Nigiri', category: 'Nigiri', price: 6.99, description: 'Fresh salmon over rice', image: Salmon_Nigiri_Img, tags: ['gluten-free'] },
  { id: 3, name: 'Spicy Tuna Roll', category: 'Maki Rolls', price: 9.99, description: 'Spicy tuna, cucumber', image: Spicy_Tuna_Roll_Img, tags: ['spicy'] },
  { id: 4, name: 'Vegetable Tempura Roll', category: 'Special Rolls', price: 7.99, description: 'Assorted vegetables, tempura batter', image: Vegetable_Tempura_Roll_Img, tags: ['vegetarian'] },
  { id: 5, name: 'Tuna Sashimi', category: 'Sashimi', price: 12.99, description: 'Sliced raw tuna', image: Tuna_Sashimi_Img, tags: ['gluten-free'] },
];

const SushiMenu = () => {
  const [menu, setMenu] = useState(sushiMenu);
  const [searchTerm, setSearchTerm] = useState('');
  const [filter, setFilter] = useState('');
  const [sortBy, setSortBy] = useState('');
  const [cart, setCart] = useState([]);
  const [error, setError] = useState('');

  useEffect(() => {
    let filteredMenu = sushiMenu;

    if (searchTerm) {
      filteredMenu = filteredMenu.filter(item =>
        item.name.toLowerCase().includes(searchTerm.toLowerCase()) ||
        item.description.toLowerCase().includes(searchTerm.toLowerCase())
      );
    }

    if (filter) {
      filteredMenu = filteredMenu.filter(item =>
        item.tags.includes(filter) || item.category === filter
      );
    }

    if (sortBy === 'price') {
      filteredMenu.sort((a, b) => a.price - b.price);
    } else if (sortBy === 'name') {
      filteredMenu.sort((a, b) => a.name.localeCompare(b.name));
    }

    setMenu(filteredMenu);
  }, [searchTerm, filter, sortBy]);

  const addToCart = (item) => {
    setCart([...cart, item]);
    setError('');
  };

  const handleSearch = (e) => {
    setSearchTerm(e.target.value);
    setError('');
  };

  const handleFilter = (filterValue) => {
    setFilter(filterValue);
    setError('');
  };

  const handleSort = (sortValue) => {
    setSortBy(sortValue);
    setError('');
  };

  return (
    <div className="container mx-auto px-4 py-8">
      <h1 className="text-4xl font-bold text-center mb-8">Meta Sushi Menu</h1>

      <div className="flex flex-col md:flex-row justify-between items-center mb-8">
        <div className="relative w-full md:w-1/3 mb-4 md:mb-0">
          <input
            type="text"
            placeholder="Search menu..."
            value={searchTerm}
            onChange={handleSearch}
            className="w-full pl-10 pr-4 py-2 rounded-lg border border-gray-300 focus:outline-none focus:ring-2 focus:ring-blue-500"
            aria-label="Search menu"
          />
          <FaSearch className="absolute left-3 top-3 text-gray-400" />
        </div>

        <div className="flex space-x-4">
          <div className="relative">
            <select
              onChange={(e) => handleFilter(e.target.value)}
              className="appearance-none bg-white border border-gray-300 rounded-lg pl-4 pr-10 py-2 focus:outline-none focus:ring-2 focus:ring-blue-500"
              aria-label="Filter menu"
            >
              <option value="">All Items</option>
              <option value="vegetarian">Vegetarian</option>
              <option value="gluten-free">Gluten-Free</option>
              <option value="spicy">Spicy</option>
            </select>
            <FaFilter className="absolute right-3 top-3 text-gray-400 pointer-events-none" />
          </div>

          <div className="relative">
            <select
              onChange={(e) => handleSort(e.target.value)}
              className="appearance-none bg-white border border-gray-300 rounded-lg pl-4 pr-10 py-2 focus:outline-none focus:ring-2 focus:ring-blue-500"
              aria-label="Sort menu"
            >
              <option value="">Sort By</option>
              <option value="price">Price</option>
              <option value="name">Name</option>
            </select>
            <FaSort className="absolute right-3 top-3 text-gray-400 pointer-events-none" />
          </div>
        </div>
      </div>

      {error && (
        <div className="bg-red-100 border border-red-400 text-red-700 px-4 py-3 rounded relative mb-4" role="alert">
          <strong className="font-bold">Error:</strong>
          <span className="block sm:inline"> {error}</span>
        </div>
      )}

      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
        <AnimatePresence>
          {menu.map((item) => (
            <motion.div
              key={item.id}
              initial={{ opacity: 0, y: 20 }}
              animate={{ opacity: 1, y: 0 }}
              exit={{ opacity: 0, y: -20 }}
              className="bg-white rounded-lg shadow-lg overflow-hidden"
            >
              <img src={item.image} alt={item.name} className="w-full h-48 object-cover" />
              <div className="p-4">
                <h2 className="text-xl font-semibold mb-2">{item.name}</h2>
                <p className="text-gray-600 mb-2">{item.description}</p>
                <div className="flex justify-between items-center">
                  <span className="text-lg font-bold">${item.price.toFixed(2)}</span>
                  <button
                    onClick={() => addToCart(item)}
                    className="bg-blue-500 text-white px-4 py-2 rounded-lg hover:bg-blue-600 transition duration-300"
                    aria-label={`Add ${item.name} to cart`}
                  >
                    Add to Cart
                  </button>
                </div>
              </div>
            </motion.div>
          ))}
        </AnimatePresence>
      </div>

      {menu.length === 0 && (
        <p className="text-center text-gray-500 mt-8">No items found. Please try a different search or filter.</p>
      )}

      <div className="fixed bottom-4 right-4">
        <button
          className="bg-blue-500 text-white p-4 rounded-full shadow-lg hover:bg-blue-600 transition duration-300"
          aria-label="View cart"
        >
          <FaShoppingCart className="text-2xl" />
          {cart.length > 0 && (
            <span className="absolute -top-2 -right-2 bg-red-500 text-white rounded-full w-6 h-6 flex items-center justify-center text-sm">
              {cart.length}
            </span>
          )}
        </button>
      </div>
    </div>
  );
};

export default SushiMenu;