import React, { useState } from 'react';
import { FaChevronLeft, FaRegCheckCircle, FaRegClock, FaRedo } from 'react-icons/fa';

const MyOrder = () => {
    const [activeTab, setActiveTab] = useState('complete');

    const orders = {
        complete: [
            { id: 1, restaurant: "KFC", items: "Pizza, Alo Bortha, Thethul achar, Chicken tiriaky", price: 59, status: 'complete' },
            // Additional completed orders
        ],
        pending: [
            { id: 2, restaurant: "KFC", items: "Burger, Fries, Coke", price: 45, status: 'pending' },
            // Additional pending orders
        ]
    };

    return (
        <div className="bg-gray-100 min-h-screen p-4">
            <div className="bg-white py-4 px-6 mb-4 shadow-md flex justify-between items-center">
                <FaChevronLeft className="cursor-pointer text-gray-600" onClick={() => console.log('Go Back')} />
                <h1 className="text-xl font-bold">My Order</h1>
                <p></p>
            </div>
            <div className="flex justify-around bg-white p-2 shadow-md">
                <button
                    className={`flex-1 ${activeTab === 'complete' ? 'text-orange-500 font-bold' : 'text-gray-500'}`}
                    onClick={() => setActiveTab('complete')}
                >
                    Complete Order
                </button>
                <button
                    className={`flex-1 ${activeTab === 'pending' ? 'text-orange-500 font-bold' : 'text-gray-500'}`}
                    onClick={() => setActiveTab('pending')}
                >
                    Pending Order
                </button>
            </div>
            <div className="space-y-4 mt-4">
                {orders[activeTab].map(order => (
                    <div key={order.id} className="bg-white p-4 rounded-lg shadow-md flex justify-between items-center">
                        <div>
                            <h5 className="font-bold">{order.restaurant}</h5>
                            <p className="text-sm text-gray-500">{order.items}</p>
                            <p className="text-sm text-gray-500">${order.price}</p>
                        </div>
                        <button className="flex items-center text-orange-500">
                            <FaRedo className="mr-2" />
                            Order Again
                        </button>
                    </div>
                ))}
            </div>
        </div>
    );
};

export default MyOrder;
