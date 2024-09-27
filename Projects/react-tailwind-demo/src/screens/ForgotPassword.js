import React, { useState } from 'react';

const ForgotPassword = () => {
  const [email, setEmail] = useState('');

  const handleEmailChange = (event) => {
    setEmail(event.target.value);
  };

  const handleSubmit = (event) => {
    event.preventDefault();
    // Implement the logic to handle password reset
    console.log(`Reset link would be sent to: ${email}`);
  };

  return (
    <div className="bg-white min-h-screen flex flex-col items-center justify-center p-4">
      <div className="w-full max-w-xs">
        <h1 className="text-center text-2xl font-semibold mb-6">FORGOT PASSWORD</h1>
        <form onSubmit={handleSubmit} className="bg-white">
          <input
            type="email"
            value={email}
            onChange={handleEmailChange}
            placeholder="Enter your email or phone"
            className="w-full p-4 border border-gray-300 rounded-lg mb-4 focus:outline-none focus:ring-2 focus:ring-orange-500"
            required
          />
          <button
            type="submit"
            className="w-full bg-orange-500 text-white p-4 rounded-lg hover:bg-orange-600 focus:outline-none focus:ring-2 focus:ring-orange-600"
          >
            SEND NOW
          </button>
        </form>
        <p className="text-center text-sm text-gray-600 mt-6">
          Having Problem? <a href="#" className="text-orange-500 hover:underline">Need Help</a>
        </p>
      </div>
    </div>
  );
};

export default ForgotPassword;
