import React from 'react';
import { FaUser, FaAddressCard, FaCreditCard, FaCog, FaQuestionCircle, FaSignOutAlt } from 'react-icons/fa';

const Sidebar = () => {
    return (
        <div className="bg-white h-screen w-64 py-5 px-4 shadow-lg">
            <div className="flex items-center space-x-4 p-2 mb-5">
                <img src="/path-to-your-profile-image.jpg" alt="Adom Shafi" className="h-14 w-14 rounded-full object-cover" />
                <div>
                    <h2 className="text-lg font-semibold">Adom Shafi</h2>
                    <p className="text-sm text-gray-600">hellobesnik@gmail.com</p>
                </div>
            </div>
            <ul className="flex flex-col space-y-4">
                <li className="flex items-center text-gray-800 text-sm p-2 hover:bg-gray-100 rounded-md cursor-pointer">
                    <FaUser className="text-lg mr-2" /> My Profile
                </li>
                <li className="flex items-center text-gray-800 text-sm p-2 hover:bg-gray-100 rounded-md cursor-pointer">
                    <FaAddressCard className="text-lg mr-2" /> My Address
                </li>
                <li className="flex items-center text-gray-800 text-sm p-2 hover:bg-gray-100 rounded-md cursor-pointer">
                    <FaCreditCard className="text-lg mr-2" /> Payment Method
                </li>
                <li className="flex items-center text-gray-800 text-sm p-2 hover:bg-gray-100 rounded-md cursor-pointer">
                    <FaCog className="text-lg mr-2" /> Settings
                </li>
                <li className="flex items-center text-gray-800 text-sm p-2 hover:bg-gray-100 rounded-md cursor-pointer">
                    <FaQuestionCircle className="text-lg mr-2" /> Help & FAQ
                </li>
            </ul>
            <button className="flex items-center justify-center text-white bg-red-500 p-3 mt-5 rounded-full">
                <FaSignOutAlt className="mr-2" /> Log Out
            </button>
        </div>
    );
};

export default Sidebar;
