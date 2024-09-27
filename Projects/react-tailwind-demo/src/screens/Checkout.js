import React from 'react';
import { FaChevronLeft, FaPlus, FaApple, FaCcPaypal, FaCcMastercard, FaChevronRight } from 'react-icons/fa';

const Checkout = () => {
    // Function to handle back navigation
    const goBack = () => window.history.back();
    return (
        <div className="bg-gray-100 min-h-screen p-4">
            <div className="bg-white py-4 px-6 mb-4 shadow-md flex justify-between items-center">
                <FaChevronLeft onClick={goBack} className="cursor-pointer text-gray-600 mr-2"/>
                <h1 className="text-xl font-bold">Checkout</h1>
                <p></p>
            </div>
            <div className="bg-white items-center p-4 rounded-lg shadow-md">
                <section className="mb-6">
                    <h2 className="text-gray-800 font-semibold mb-2">Delivery Details</h2>
                    <div className="flex justify-between items-center mb-2">
                        <p className="text-gray-600">New York, Street 12, Calafony Road USA</p>
                        <FaChevronRight className="text-gray-500" />
                    </div>
                    <div className="flex justify-between items-center">
                        <p className="text-gray-600">+880-17048-3990</p>
                        <FaChevronRight className="text-gray-500" />
                    </div>
                </section>

                <section className="mb-6">
                    <h2 className="text-gray-800 font-semibold mb-2">Payment Method</h2>
                    <div className="flex space-x-4">
                        <FaPlus className="text-gray-500 bg-gray-200 p-2 rounded-full" />
                        <FaApple className="text-gray-500 bg-gray-200 p-2 rounded-full" />
                        <FaCcPaypal className="text-blue-500 bg-gray-200 p-2 rounded-full" />
                        <FaCcMastercard className="text-red-500 bg-gray-200 p-2 rounded-full" />
                    </div>
                    <div className="flex items-center mt-4">
                        <input type="checkbox" className="form-checkbox text-red-500 mr-2" />
                        <span>Use cash on delivery</span>
                    </div>
                </section>

                <section className="mb-6">
                    <div className="flex justify-between">
                        <span>Delivery Fee</span>
                        <span>$5.30</span>
                    </div>
                    <div className="flex justify-between font-bold">
                        <span>Total</span>
                        <span>$311.05</span>
                    </div>
                </section>

                <section className="mb-6">
                    <div className="flex justify-between items-center">
                        <span>Delivery Time</span>
                        <div className="flex items-center">
                            <span>28 Feb 2021 10:30 am</span>
                            <FaChevronRight className="text-gray-500" />
                        </div>
                    </div>
                </section>

                <button className="w-full bg-red-500 text-white p-3 rounded-lg">CONFIRM</button>
            </div>
        </div>
    );
};

export default Checkout;
