import React, { useState } from 'react';
import { FaSearch, FaChevronLeft, FaStar, FaLeaf, FaPepperHot, FaUtensils } from 'react-icons/fa';

const Discount = () => {
    const restaurants = [
        {
            id: 1,
            name: "Artisan Coffee Shop",
            recipes: 29,
            rating: 4,
            discount: 25,
            type: "Vegetarian",
            image: "/path-to-image/artisan-coffee-shop.jpg"
        },
        {
            id: 2,
            name: "KAZY ASPARAGAS",
            recipes: 29,
            rating: 4,
            discount: 25,
            type: "Vegetarian",
            image: "/path-to-image/kazy-asparagas.jpg"
        },
        { id: 3, name: "Burger Zone", recipes: 15, rating: 3, discount: 10, type: "Halal", image: "/images/burger-zone.jpg" },
        { id: 4, name: "Spicy Delight", recipes: 20, rating: 4, discount: 15, type: "Spicy", image: "/images/spicy-delight.jpg" },
        { id: 5, name: "Green Bites", recipes: 18, rating: 5, discount: 20, type: "Vegetarian", image: "/images/green-bites.jpg" },
        { id: 6, name: "Halal Feast", recipes: 22, rating: 4, discount: 18, type: "Halal", image: "/images/halal-feast.jpg" },
        { id: 7, name: "Chili House", recipes: 30, rating: 5, discount: 22, type: "Spicy", image: "/images/chili-house.jpg" },
        { id: 8, name: "Veggie Paradise", recipes: 25, rating: 3, discount: 12, type: "Vegetarian", image: "/images/veggie-paradise.jpg" },
        { id: 9, name: "Halal Corner", recipes: 28, rating: 4, discount: 10, type: "Halal", image: "/images/halal-corner.jpg" },
        { id: 10, name: "Spice Hub", recipes: 17, rating: 4, discount: 20, type: "Spicy", image: "/images/spice-hub.jpg" },
        { id: 11, name: "Pure Vegan", recipes: 20, rating: 5, discount: 30, type: "Vegetarian", image: "/images/pure-vegan.jpg" },
        { id: 12, name: "Meat Masters", recipes: 19, rating: 4, discount: 15, type: "Halal", image: "/images/meat-masters.jpg" }
    ];

    const [activeCategory, setActiveCategory] = useState('All');

    const categories = [
        { name: "All", icon: <FaUtensils className="text-blue-500" /> },
        { name: "Halal", icon: <FaUtensils className="text-yellow-500" /> },
        { name: "Spicy", icon: <FaPepperHot className="text-red-500" /> },
        { name: "Vegetarian", icon: <FaLeaf className="text-green-500" /> },
        // { name: "Pizza", icon: <FaLeaf className="text-gray-500" /> }
    ];

    const filterRestaurants = activeCategory === 'All' ? restaurants : restaurants.filter(restaurant => restaurant.type === activeCategory);

    return (
        <div className="bg-gray-100 min-h-screen p-4">
            <div className="flex items-center justify-between p-4 bg-white">
                <FaChevronLeft className="text-xl" />
                <h1 className="text-lg font-bold">Deliver to Parijat, Housing Estate</h1>
                <div></div>  {/* Placeholder for right side icon or spacing */}
            </div>
            <div className="p-4 bg-white">
                <div className="flex items-center bg-gray-200 rounded">
                    <FaSearch className="text-gray-500 m-2" />
                    <input className="bg-transparent p-2 w-full" placeholder="Find Your Restaurants" />
                </div>
                <div className="flex justify-around my-4">
                    {categories.map(category => (
                        <button key={category.name} className={`flex flex-col items-center ${activeCategory === category.name ? 'text-orange-500' : 'text-gray-500'}`} onClick={() => setActiveCategory(category.name)}>
                            {category.icon}
                            <span>{category.name}</span>
                        </button>
                    ))}
                </div>
            </div>
            <div className="space-y-4">
                {filterRestaurants.map(restaurant => (
                    <div key={restaurant.id} className="bg-white p-4 rounded-lg shadow">
                        <div className="relative">
                            <img src={restaurant.image} alt={restaurant.name} className="w-full h-40 object-cover rounded-lg" />
                            <span className="absolute top-2 right-2 bg-orange-500 text-white px-3 py-1 rounded">{restaurant.discount}% Discount</span>
                        </div>
                        <div className="mt-2 flex justify-between items-center">
                            <div>
                                <h5 className="font-bold">{restaurant.name}</h5>
                                <p className="text-sm text-gray-500">{restaurant.recipes} recipes</p>
                            </div>
                            <div className="flex items-center">
                                {[...Array(restaurant.rating)].map((_, i) => (
                                    <FaStar key={i} className="text-yellow-500" />
                                ))}
                                <span className="text-sm text-gray-500 ml-1">{restaurant.rating}</span>
                            </div>
                        </div>
                    </div>
                ))}
            </div>
        </div>
    );
};

export default Discount;
