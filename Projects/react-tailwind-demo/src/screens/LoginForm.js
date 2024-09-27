import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';

function LoginForm() {

    const [email, setEmail] = useState('');
    const [password, setPassword] = useState('');
    const navigate = useNavigate();
  
    const handleSubmit = (event) => {
      event.preventDefault();
      // Handle login logic
      navigate('/food-menu');  // Redirect after login
    };

    return (
        <div className="min-h-screen flex items-center justify-center bg-red-100"> {/* Giữ nguyên màu nền hoặc thay đổi nếu cần */}
            <div className="bg-white p-6 rounded-lg shadow-md w-96">
                <h2 className="text-2xl font-semibold text-center mb-6">Sign In</h2>
                <form onSubmit={handleSubmit} >
                    <div className="mb-4">
                        <label className="block text-gray-700" htmlFor="email">
                            Your Email:
                        </label>
                        <input
                            type="email"
                            id="email"
                            className="w-full px-4 py-2 border rounded-md focus:outline-none focus:ring-2 focus:ring-custom-orange"
                            placeholder="Enter your email"
                        />
                    </div>
                    <div className="mb-4">
                        <label className="block text-gray-700" htmlFor="password">
                            Password:
                        </label>
                        <input
                            type="password"
                            id="password"
                            className="w-full px-4 py-2 border rounded-md focus:outline-none focus:ring-2 focus:ring-custom-orange"
                            placeholder="Enter your password"
                        />
                    </div>
                    <button
                        type="submit"
                        className="w-full bg-custom-orange text-white px-4 py-2 rounded-md hover:bg-orange-600 transition duration-300"
                    >
                        Sign In
                    </button>
                </form>
            </div>
        </div>
    );
}


export default LoginForm;
