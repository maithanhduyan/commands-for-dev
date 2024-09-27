import React, { useState } from 'react';
import { FaChevronLeft, FaShoppingCart } from 'react-icons/fa';
import { Link } from 'react-router-dom';

// Sample data for the food items
const foodItems = [
  { id: 1, name: "Red n hot pizza", description: "Spicy chicken, beef", price: "9.50", category: "Fast food", rating: "4.5", reviews: "25" },
  { id: 2, name: "Meat Pasta", description: "Meat & Basil", price: "9.50", category: "Fast food", rating: "4.5", reviews: "20" },
  { id: 3, name: "Brushetta", description: "Toppings & tomato", price: "9.50", category: "Platter", rating: "4.5", reviews: "15" },
  { id: 4, name: "Salad", description: "Baked Salmon", price: "9.50", category: "Heavy food", rating: "4.5", reviews: "30" }
];

const categories = ["All", "Fast food", "Heavy food", "Platter"];

const FoodMenu = () => {
  const [activeCategory, setActiveCategory] = useState("All");

  const filteredItems = activeCategory === "All" ? foodItems : foodItems.filter(item => item.category === activeCategory);

  return (
    <div className="bg-white min-h-screen">
      <header className="flex justify-between items-center p-4 bg-white shadow-md">
        <Link to="/" className="text-orange-500 hover:underline ml-4"><FaChevronLeft className="text-2xl" /></Link>
        <h1 className="font-bold text-xl">Food Menu</h1>
        <Link to="/cart" className="text-orange-500 hover:underline ml-4"><FaShoppingCart /></Link>
      </header>
      <div className="flex justify-around bg-gray-100 p-2">
        {categories.map(category => (
          <button key={category}
            className={`py-2 px-4 ${activeCategory === category ? 'text-orange-500 font-bold' : 'text-gray-500'}`}
            onClick={() => setActiveCategory(category)}>
            {category}
          </button>
        ))}
      </div>
      <div className="p-4 grid grid-cols-2 gap-4">
        {filteredItems.map(item => (
          <div key={item.id} className="bg-white p-2 rounded shadow">
            <img src={`/path-to-images/${item.name.replaceAll(' ', '-').toLowerCase()}.jpg`} alt={item.name} className="w-full h-32 object-cover rounded" />
            <div className="p-2">
              <h5 className="font-bold">{item.name} - ${item.price}</h5>
              <p className="text-sm text-gray-600">{item.description}</p>
              <div className="flex justify-between items-center mt-2">
                <span className="text-gray-500">{item.rating} ⭐ ({item.reviews})</span>
                <button className="bg-orange-500 text-white px-3 py-1 rounded">Add</button>
              </div>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
};

export default FoodMenu;
