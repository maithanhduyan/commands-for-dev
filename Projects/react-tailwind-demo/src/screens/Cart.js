import React, { useState } from 'react';
import { FaShoppingCart, FaAngleLeft, FaPlus, FaMinus, FaTrash } from 'react-icons/fa';
import{Link} from 'react-router-dom';

const Cart = () => {
    // Initial cart items
    const initialCartItems = [
        { id: 1, name: 'Red n hot pizza', description: 'Spicy chicken, beef', price: 9.50, quantity: 2, image: '/path-to-image/red-n-hot-pizza.jpg' },
        { id: 2, name: 'Spicy Pizza', description: 'Spicy chicken, beef', price: 9.50, quantity: 2, image: '/path-to-image/spicy-pizza.jpg' },
        { id: 3, name: 'Parata', description: 'Spicy chicken, beef', price: 9.50, quantity: 2, image: '/path-to-image/parata.jpg' }
    ];

    // State for cart items
    const [cartItems, setCartItems] = useState(initialCartItems);

    // Function to update the quantity of cart items
    const handleQuantityChange = (itemId, delta) => {
        setCartItems(currentItems =>
            currentItems.map(item =>
                item.id === itemId ? { ...item, quantity: Math.max(0, item.quantity + delta) } : item
            )
        );
    };

    const totalPrice = cartItems.reduce((total, item) => total + item.price * item.quantity, 0);
    const deliveryFee = 5.30;
    const grandTotal = totalPrice + deliveryFee;

    return (
        <div className="p-4 bg-gray-100 min-h-screen">
            <div className="bg-white py-4 px-6 mb-4 shadow-md flex justify-between items-center">
               <Link to="/"><FaAngleLeft className="cursor-pointer text-2xl"/></Link> 
                <h1 className="text-xl font-bold">Cart</h1>
                <FaShoppingCart className='cursor-pointer'/>
            </div>
            {cartItems.map(item => (
                <CartItem key={item.id} item={item} handleQuantityChange={handleQuantityChange} />
            ))}
            <div className="bg-white p-4 shadow-md rounded-lg mt-4">
                <div className="flex justify-between mb-2">
                    <span>Delivery Fee</span>
                    <span>${deliveryFee.toFixed(2)}</span>
                </div>
                <div className="flex justify-between mb-2 font-bold">
                    <span>Total</span>
                    <span>${grandTotal.toFixed(2)}</span>
                </div>
                <button className="w-full bg-red-500 text-white py-3 mt-4 rounded-lg">CHECKOUT</button>
            </div>
        </div>
    );
};

const CartItem = ({ item, handleQuantityChange }) => {
    return (
        <div className="flex items-center justify-between p-4 bg-white shadow-lg rounded-lg mb-4">
            <img src={item.image} alt={item.name} className="w-20 h-20 rounded-full object-cover" />
            <div>
                <h5 className="font-bold">{item.name}</h5>
                <p className="text-sm text-gray-500">{item.description}</p>
                <div className="flex items-center">
                    <FaMinus onClick={() => handleQuantityChange(item.id, -1)} className="text-red-500 cursor-pointer" />
                    <span className="mx-2">{item.quantity}</span>
                    <FaPlus onClick={() => handleQuantityChange(item.id, 1)} className="text-green-500 cursor-pointer" />
                </div>
            </div>
            <span className="text-lg font-bold">${item.price.toFixed(2)}</span>
            <FaTrash className="text-red-500 cursor-pointer" />
        </div>
    );
};

export default Cart;
