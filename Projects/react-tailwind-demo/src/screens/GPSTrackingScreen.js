import React from 'react';

const GPSTrackingScreen = () => {
  return (
    <div className="flex flex-col items-center justify-center h-screen bg-white p-4">
      <button className="absolute top-4 right-4 text-red-500 font-semibold">
        Skip 
      </button>
      <div className="relative">
        <div className="w-64 h-64 bg-gray-200 rounded-full flex items-center justify-center mb-6">
          {/* Placeholder for user image */}
          <img
            src="path_to_your_image.jpg"
            alt="User"
            className="w-full h-full object-cover rounded-full"
          />
          <div className="absolute inset-0 flex justify-center items-center">
            {/* Placeholder for circular badge */}
            <div className="absolute border-4 border-red-500 rounded-full w-full h-full"></div>
          </div>
          {/* Additional smaller badges around the user image */}
          <div className="absolute -top-4 -left-4 w-12 h-12 bg-white rounded-full flex items-center justify-center border border-gray-200">
            {/* Placeholder for small badge */}
            <span>Logo 1</span>
          </div>
          <div className="absolute -top-4 -right-4 w-12 h-12 bg-white rounded-full flex items-center justify-center border border-gray-200">
            {/* Placeholder for small badge */}
            <span>Logo 2</span>
          </div>
          <div className="absolute -bottom-4 -left-4 w-12 h-12 bg-white rounded-full flex items-center justify-center border border-gray-200">
            {/* Placeholder for small badge */}
            <span>Logo 3</span>
          </div>
          <div className="absolute -bottom-4 -right-4 w-12 h-12 bg-white rounded-full flex items-center justify-center border border-gray-200">
            {/* Placeholder for small badge */}
            <span>Logo 4</span>
          </div>
        </div>
      </div>
      <div className="text-center px-4">
        <h2 className="text-xl font-semibold mb-2">GPS Tracking</h2>
        <p className="text-gray-600">
          Loved the class! Such beautiful land and collective impact infrastructure social entrepreneur.
        </p>
      </div>
      <button className="bg-red-500 hover:bg-red-600 text-white font-semibold py-2 px-12 rounded-full mt-6 transition duration-200">
        Continue
      </button>
    </div>
  );
};

export default GPSTrackingScreen;
