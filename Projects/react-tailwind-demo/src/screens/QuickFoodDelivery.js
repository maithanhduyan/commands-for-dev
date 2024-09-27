import React from 'react';
import Button from '../components/Button';

const QuickFoodDelivery = () => {
  return (
    <div className="bg-white h-screen flex flex-col items-center justify-center px-4">
      <div className="bg-orange-100 p-6 rounded-lg shadow-lg text-center">
        <img src="/path-to-food-image.jpg" alt="Food Delivery" className="w-64 h-64 object-cover rounded-full mx-auto" />
        <h2 className="text-xl font-semibold mt-4">Quick Food Delivery</h2>
        <p className="text-gray-600 my-2">
          Loved the class! Such beautiful and collective impact infrastructure social entrepreneur.
        </p>
        <button className="bg-orange-500 text-white py-2 px-6 rounded-full mt-4 hover:bg-orange-600 transition duration-300">
          SIGN IN WITH FACEBOOK
        </button>
        <button className="bg-orange-500 text-white py-2 px-6 rounded-full mt-2 hover:bg-orange-600 transition duration-300">
          SIGN IN
        </button>
        {/* <Button>Sign In</Button> */}
        {/* <Button variant="secondary">Sign In with Facebook</Button> */}
        <p className="mt-2">
          Or <a href="#" className="text-orange-500 hover:underline">Start to Search Now</a>
        </p>
      </div>
    </div>
  );
};

export default QuickFoodDelivery;
