import React from 'react';

const GPSTrackingCard = () => {
  return (
    <div className="bg-white h-screen flex flex-col items-center justify-center">
      <div className="relative">
        <img src="/path-to-dumpling-image.jpg" alt="Dumplings" className="w-64 h-64 object-cover rounded-full" />
        <div className="absolute inset-0 flex justify-center items-center">
          <div className="bg-white bg-opacity-75 w-72 h-72 rounded-full flex justify-center items-center">
            <div className="text-center px-6 py-2">
              <h2 className="text-xl font-semibold text-gray-800">GPS Tracking</h2>
              <p className="text-gray-600 mt-2">
                Loved the class! Such beautiful land and collective impact infrastructure social entrepreneur.
              </p>
            </div>
          </div>
        </div>
      </div>
      <button className="bg-orange-500 text-white py-2 px-6 mt-4 rounded-full hover:bg-orange-600 transition duration-300">
        CONTINUE
      </button>
    </div>
  );
};

export default GPSTrackingCard;
