import React, { useState, useEffect } from 'react';
import { FaSearch, FaShoppingCart, FaTimes } from 'react-icons/fa';
import { IoMdAdd, IoMdRemove } from 'react-icons/io';

import californiaRollImg from './assets/images/california-roll.jpg';
import salmonNigiriImg from './assets/images/salmon-nigiri.jpg';
import spicyTunaRollImg from './assets/images/spicy-tuna-roll.jpg';
import dragonRollImg from './assets/images/dragon-roll.jpg';
import vegetableTempuraRollImg from './assets/images/vegetable-tempura-roll.jpg';

const SushiShopMenu = () => {
    const [menuItems, setMenuItems] = useState([]);
    const [filteredItems, setFilteredItems] = useState([]);
    const [cart, setCart] = useState([]);
    const [searchTerm, setSearchTerm] = useState('');
    const [activeFilters, setActiveFilters] = useState([]);
    const [isCartOpen, setIsCartOpen] = useState(false);

    useEffect(() => {
        // Simulating API call to fetch menu items
        const fetchedMenuItems = [
            {
                id: 1,
                name: 'California Roll',
                description: 'Crab, avocado, and cucumber roll',
                price: 8.99,
                category: 'maki',
                image: californiaRollImg,
                tags: ['popular', 'vegetarian-option']
            },
            {
                id: 2,
                name: 'Salmon Nigiri',
                description: 'Fresh salmon over pressed rice',
                price: 6.99,
                category: 'nigiri',
                image: salmonNigiriImg,
                tags: ['gluten-free']
            },
            {
                id: 3,
                name: 'Spicy Tuna Roll',
                description: 'Spicy tuna and cucumber roll',
                price: 9.99,
                category: 'maki',
                image: spicyTunaRollImg,
                tags: ['spicy']
            },
            {
                id: 4,
                name: 'Dragon Roll',
                description: 'Eel, crab, and avocado roll topped with avocado',
                price: 14.99,
                category: 'special',
                image: dragonRollImg,
                tags: ['popular']
            },
            {
                id: 5,
                name: 'Vegetable Tempura Roll',
                description: 'Assorted vegetable tempura roll',
                price: 7.99,
                category: 'maki',
                image: vegetableTempuraRollImg,
                tags: ['vegetarian']
            }
        ];
        setMenuItems(fetchedMenuItems);
        setFilteredItems(fetchedMenuItems);
    }, []);

    useEffect(() => {
        const filtered = menuItems.filter(item =>
            item.name.toLowerCase().includes(searchTerm.toLowerCase()) &&
            (activeFilters.length === 0 || activeFilters.some(filter => item.tags.includes(filter)))
        );
        setFilteredItems(filtered);
    }, [searchTerm, activeFilters, menuItems]);

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

    const clearCart = () => {
        setCart([]);
    };

    const getTotalCost = () => {
        return cart.reduce((total, item) => total + item.price * item.quantity, 0).toFixed(2);
    };

    const toggleFilter = (filter) => {
        setActiveFilters(prevFilters =>
            prevFilters.includes(filter)
                ? prevFilters.filter(f => f !== filter)
                : [...prevFilters, filter]
        );
    };

    return (
        <div className="container mx-auto px-4 py-8">
            <h1 className="text-4xl font-bold mb-8 text-center">Meta Sushi Menu</h1>

            {/* Search and Filter */}
            <div className="mb-8">
                <div className="flex items-center mb-4">
                    <input
                        type="text"
                        placeholder="Search sushi..."
                        className="flex-grow p-2 border rounded-l"
                        value={searchTerm}
                        onChange={(e) => setSearchTerm(e.target.value)}
                        aria-label="Search sushi"
                    />
                    <button className="bg-blue-500 text-white p-2 rounded-r" aria-label="Search">
                        <FaSearch />
                    </button>
                </div>
                <div className="flex flex-wrap gap-2">
                    {['vegetarian', 'gluten-free', 'spicy', 'popular'].map(filter => (
                        <button
                            key={filter}
                            onClick={() => toggleFilter(filter)}
                            className={`px-3 py-1 rounded ${activeFilters.includes(filter) ? 'bg-blue-500 text-white' : 'bg-gray-200'}`}
                            aria-pressed={activeFilters.includes(filter)}
                        >
                            {filter}
                        </button>
                    ))}
                </div>
            </div>

            {/* Menu Items */}
            <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
                {filteredItems.map(item => (
                    <div key={item.id} className="bg-white rounded-lg shadow-md overflow-hidden transition-transform hover:scale-105">
                        <img src={item.image} alt={item.name} className="w-full h-48 object-cover" />
                        <div className="p-4">
                            <h2 className="text-xl font-semibold mb-2">{item.name}</h2>
                            <p className="text-gray-600 mb-2">{item.description}</p>
                            <div className="flex justify-between items-center">
                                <span className="text-lg font-bold">${item.price.toFixed(2)}</span>
                                <button
                                    onClick={() => addToCart(item)}
                                    className="bg-green-500 text-white px-4 py-2 rounded hover:bg-green-600 transition-colors"
                                    aria-label={`Add ${item.name} to cart`}
                                >
                                    Add to Cart
                                </button>
                            </div>
                        </div>
                    </div>
                ))}
            </div>

            {/* Cart */}
            <div className={`fixed top-0 right-0 h-full w-80 bg-white shadow-lg transform ${isCartOpen ? 'translate-x-0' : 'translate-x-full'} transition-transform duration-300 ease-in-out`}>
                <div className="p-4">
                    <div className="flex justify-between items-center mb-4">
                        <h2 className="text-2xl font-bold">Your Cart</h2>
                        <button onClick={() => setIsCartOpen(false)} className="text-gray-500 hover:text-gray-700" aria-label="Close cart">
                            <FaTimes />
                        </button>
                    </div>
                    {cart.length === 0 ? (
                        <p>Your cart is empty</p>
                    ) : (
                        <>
                            {cart.map(item => (
                                <div key={item.id} className="flex justify-between items-center mb-2">
                                    <span>{item.name}</span>
                                    <div className="flex items-center">
                                        <button onClick={() => removeFromCart(item.id)} className="text-red-500 mr-2" aria-label={`Remove ${item.name} from cart`}>
                                            <IoMdRemove />
                                        </button>
                                        <span>{item.quantity}</span>
                                        <button onClick={() => addToCart(item)} className="text-green-500 ml-2" aria-label={`Add another ${item.name} to cart`}>
                                            <IoMdAdd />
                                        </button>
                                    </div>
                                </div>
                            ))}
                            <div className="mt-4">
                                <p className="text-xl font-bold">Total: ${getTotalCost()}</p>
                                <button onClick={clearCart} className="w-full bg-red-500 text-white py-2 rounded mt-4 hover:bg-red-600 transition-colors">
                                    Clear Cart
                                </button>
                            </div>
                        </>
                    )}
                </div>
            </div>

            {/* Cart Toggle Button */}
            <button
                onClick={() => setIsCartOpen(true)}
                className="fixed bottom-4 right-4 bg-blue-500 text-white p-4 rounded-full shadow-lg hover:bg-blue-600 transition-colors"
                aria-label="Open cart"
            >
                <FaShoppingCart />
            </button>
        </div>
    );
};

export default SushiShopMenu;