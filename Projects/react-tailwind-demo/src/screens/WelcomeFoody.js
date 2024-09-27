import React, { useState } from 'react';
import { FaBars, FaSearch, FaUserCircle, FaHome, FaRegListAlt, FaUser, FaShoppingCart } from 'react-icons/fa';
import Sidebar from './Sidebar';
import { Link } from 'react-router-dom';

const WelcomeFoody = () => {
  const [sidebarOpen, setSidebarOpen] = useState(false);

  const toggleSidebar = () => {
    setSidebarOpen(!sidebarOpen);
  };

  const nearbyPlaces = [
    { name: 'Hungry Station', location: 'Jail road. Zinda Bazar, Sylhet' },
    { name: 'Artisan Coffee Shop', location: 'Mira bazar. Sylhet' },
    { name: 'KFC', location: 'Zindabazar road, Sylhet' }
  ];

  const popularRestaurants = [
    { name: 'Panshi In', reviews: '30 reviews' },
    { name: 'Food House', reviews: '47 reviews' }
  ];

  return (
    <div className="relative min-h-screen md:flex">
      {/* Sidebar */}
      <div className={`bg-white w-64 space-y-6 py-7 px-2 absolute inset-y-0 left-0 transform ${sidebarOpen ? 'translate-x-0' : '-translate-x-full'} transition duration-200 ease-in-out`}>
        <Sidebar />
      </div>

      {/* Content Area */}
      <div className="flex-1">
        <div className="bg-gray-100">
          <div className="bg-white px-4 py-4 flex justify-between items-center">
            <FaBars className="text-2xl cursor-pointer" onClick={toggleSidebar} />
            <span>Deliver to Parijat, Housing Estate</span>
            <FaUserCircle className="text-2xl" />
          </div>
          <div className="p-4">
            <h1 className="text-xl font-bold mb-2">Welcome Foody!</h1>
            <div className="flex items-center bg-gray-200 rounded">
              <FaSearch className="text-gray-500 m-2" />
              <input className="bg-transparent p-2 w-full" placeholder="Find Your Food" />
            </div>
            {/* Nearby Places */}
            <div className="mt-4">
              <div className="flex justify-between items-center">
                <h2 className="font-bold mb-2">Nearby Place</h2>
                <a href="#" className="text-orange-500">See All</a>
              </div>
              <div className="grid grid-cols-1 gap-4">
                {nearbyPlaces.map((place, index) => (
                  <div key={index} className="bg-white rounded-lg p-4 shadow">
                    <h3 className="font-semibold">{place.name}</h3>
                    <p className="text-gray-600">{place.location}</p>
                  </div>
                ))}
              </div>
            </div>
            {/* Popular Restaurants */}
            <div className="mt-4">
              <div className="flex justify-between items-center">
                <h2 className="font-bold mb-2">Popular Restaurants</h2>
                <a href="#" className="text-orange-500">See All</a>
              </div>
              <div className="grid grid-cols-1 gap-4">
                {popularRestaurants.map((restaurant, index) => (
                  <div key={index} className="bg-white rounded-lg p-4 shadow">
                    <h3 className="font-semibold">{restaurant.name}</h3>
                    <p className="text-gray-600">{restaurant.reviews}</p>
                  </div>
                ))}
              </div>
            </div>
          </div>
        </div>
      </div>
      {/* Bottom Navigation Bar */}
      <nav className="fixed bottom-0 left-0 right-0 bg-white p-3 shadow-md flex justify-around text-lg">
        <Link to="/" className="text-orange-500 hover:underline"><FaHome className="text-2xl" /></Link>
        <Link to="/" className="text-orange-500 hover:underline"><FaSearch className="text-2xl" /></Link>
        <Link to="/cart" className="text-orange-500 hover:underline"><FaShoppingCart className="text-2xl" /></Link>
        <Link to="/food-menu" className="text-orange-500 hover:underline ml-4"><FaRegListAlt className="text-2xl" /></Link>
        <Link to="/login" className="text-orange-500 hover:underline ml-4"><FaUser className="text-2xl" /></Link>
      </nav>
    </div>
  );
};

export default WelcomeFoody;
