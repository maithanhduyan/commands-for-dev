import React from 'react';

const WelcomeScreen = () => {
  return (
    <div className="flex flex-col items-center justify-center h-screen bg-[#fd7f5d] p-4">
      <div className="bg-white p-6 rounded-lg shadow-xl max-w-sm w-full">
        <div className="flex flex-col items-center mb-6">
          <div className="w-20 h-20 bg-gray-300 rounded-full flex items-center justify-center mb-3">
            <span className="text-xl font-semibold text-gray-500">Logo</span>
          </div>
          <h1 className="text-2xl font-semibold mb-1">Welcome!</h1>
          <p className="text-center text-gray-600 text-sm">
            Start your journey with us.
          </p>
        </div>
        <button className="bg-blue-600 hover:bg-blue-700 text-white py-3 px-12 rounded-full w-full transition duration-300">
          Continue
        </button>
      </div>
      <button className="absolute top-4 right-4 text-white text-lg font-medium">
        Skip
      </button>
    </div>
  );
};

export default WelcomeScreen;



