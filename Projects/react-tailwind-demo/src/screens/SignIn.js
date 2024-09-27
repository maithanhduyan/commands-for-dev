import React, { useState } from 'react';

const SignIn = () => {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [rememberMe, setRememberMe] = useState(false);

  const handleSubmit = (event) => {
    event.preventDefault();
    // Handle sign-in logic here
    console.log(`Signing in with: ${email}`);
  };

  return (
    <div className="bg-white min-h-screen flex flex-col items-center justify-center p-4">
      <div className="w-full max-w-xs">
        <h1 className="text-2xl font-semibold text-center mb-6">SIGN IN</h1>
        <form onSubmit={handleSubmit} className="bg-gray-100 shadow-md rounded px-8 pt-6 pb-8 mb-4">
          <div className="mb-4">
            <input
              type="email"
              value={email}
              onChange={(e) => setEmail(e.target.value)}
              placeholder="Your Email"
              className="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
              required
            />
          </div>
          <div className="mb-6">
            <input
              type="password"
              value={password}
              onChange={(e) => setPassword(e.target.value)}
              placeholder="Password"
              className="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 mb-3 leading-tight focus:outline-none focus:shadow-outline"
              required
            />
            <div className="flex justify-between items-center text-sm">
              <label className="inline-flex items-center">
                <input
                  type="checkbox"
                  checked={rememberMe}
                  onChange={(e) => setRememberMe(e.target.checked)}
                  className="form-checkbox text-orange-500"
                />
                <span className="ml-2">Remember Me</span>
              </label>
              <a href="#" className="text-orange-500 hover:text-orange-600 hover:underline">
                Forgot password?
              </a>
            </div>
          </div>
          <div className="flex flex-col space-y-4">
            <button
              type="submit"
              className="bg-orange-500 hover:bg-orange-600 text-white font-bold py-2 px-4 rounded focus:outline-none focus:shadow-outline"
            >
              SIGN IN
            </button>
            <button
              type="button" // Change this depending on how Facebook login is handled
              className="bg-blue-500 hover:bg-blue-600 text-white font-bold py-2 px-4 rounded focus:outline-none focus:shadow-outline"
            >
              SIGN IN WITH FACEBOOK
            </button>
          </div>
          <div className="text-center text-sm mt-6">
            I don't have an account? <a href="#" className="text-orange-500 hover:underline">Sign Up</a>
          </div>
        </form>
      </div>
    </div>
  );
};

export default SignIn;
