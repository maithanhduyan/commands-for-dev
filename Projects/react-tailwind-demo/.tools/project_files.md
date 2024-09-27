# ../package.json

```
{
  "name": "react-tailwind-demo",
  "version": "0.1.0",
  "private": true,
  "dependencies": {
    "@testing-library/jest-dom": "^5.17.0",
    "@testing-library/react": "^13.4.0",
    "@testing-library/user-event": "^13.5.0",
    "react": "^18.3.1",
    "react-dom": "^18.3.1",
    "react-icons": "^5.3.0",
    "react-scripts": "5.0.1",
    "web-vitals": "^2.1.4"
  },
  "scripts": {
    "start": "react-scripts start",
    "build": "react-scripts build",
    "test": "react-scripts test",
    "eject": "react-scripts eject"
  },
  "eslintConfig": {
    "extends": [
      "react-app",
      "react-app/jest"
    ]
  },
  "browserslist": {
    "production": [
      ">0.2%",
      "not dead",
      "not op_mini all"
    ],
    "development": [
      "last 1 chrome version",
      "last 1 firefox version",
      "last 1 safari version"
    ]
  },
  "devDependencies": {
    "autoprefixer": "^10.4.20",
    "postcss": "^8.4.47",
    "tailwindcss": "^3.4.12"
  }
}

```

# ../postcss.config.js

```
module.exports = {
  plugins: {
    tailwindcss: {},
    autoprefixer: {},
  },
}

```

# ../tailwind.config.js

```
/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./src/**/*.{js,jsx,ts,tsx}",
  ],
  theme: {
    extend: {
      colors: {
        'custom-orange': '#fd7f5d',
        'brand-orange': '#FF3D00',
      },
    },
  },
  plugins: [],
}


```

# ../public\index.html

```
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8" />
    <link rel="icon" href="%PUBLIC_URL%/favicon.ico" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <meta name="theme-color" content="#000000" />
    <meta
      name="description"
      content="Web site created using create-react-app"
    />
    <link rel="apple-touch-icon" href="%PUBLIC_URL%/logo192.png" />
    <!--
      manifest.json provides metadata used when your web app is installed on a
      user's mobile device or desktop. See https://developers.google.com/web/fundamentals/web-app-manifest/
    -->
    <link rel="manifest" href="%PUBLIC_URL%/manifest.json" />
    <!--
      Notice the use of %PUBLIC_URL% in the tags above.
      It will be replaced with the URL of the `public` folder during the build.
      Only files inside the `public` folder can be referenced from the HTML.

      Unlike "/favicon.ico" or "favicon.ico", "%PUBLIC_URL%/favicon.ico" will
      work correctly both with client-side routing and a non-root public URL.
      Learn how to configure a non-root public URL by running `npm run build`.
    -->
    <title>React App</title>
  </head>
  <body>
    <noscript>You need to enable JavaScript to run this app.</noscript>
    <div id="root"></div>
    <!--
      This HTML file is a template.
      If you open it directly in the browser, you will see an empty page.

      You can add webfonts, meta tags, or analytics to this file.
      The build step will place the bundled scripts into the <body> tag.

      To begin the development, run `npm start` or `yarn start`.
      To create a production bundle, use `npm run build` or `yarn build`.
    -->
  </body>
</html>

```

# ../public\manifest.json

```
{
  "short_name": "React App",
  "name": "Create React App Sample",
  "icons": [
    {
      "src": "favicon.ico",
      "sizes": "64x64 32x32 24x24 16x16",
      "type": "image/x-icon"
    },
    {
      "src": "logo192.png",
      "type": "image/png",
      "sizes": "192x192"
    },
    {
      "src": "logo512.png",
      "type": "image/png",
      "sizes": "512x512"
    }
  ],
  "start_url": ".",
  "display": "standalone",
  "theme_color": "#000000",
  "background_color": "#ffffff"
}

```

# ../src\App.css

```
.App {
  text-align: center;
}

.App-logo {
  height: 40vmin;
  pointer-events: none;
}

@media (prefers-reduced-motion: no-preference) {
  .App-logo {
    animation: App-logo-spin infinite 20s linear;
  }
}

.App-header {
  background-color: #282c34;
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  font-size: calc(10px + 2vmin);
  color: white;
}

.App-link {
  color: #61dafb;
}

@keyframes App-logo-spin {
  from {
    transform: rotate(0deg);
  }
  to {
    transform: rotate(360deg);
  }
}

```

# ../src\App.js

```
import logo from './logo.svg';
import './App.css';
import LoginForm from './screens/LoginForm';
import WelcomeScreen from './screens/WelcomeScreen';
import GPSTrackingScreen from './screens/GPSTrackingScreen';
import GPSTrackingCard from './screens/GPSTrackingCard';
import QuickFoodDelivery from './screens/QuickFoodDelivery';
import ForgotPassword from './screens/ForgotPassword';
import SignUp from './screens/SignUp';
import SignIn from './screens/SignIn';
import WelcomeFoody from './screens/WelcomeFoody';
import FoodMenu from './screens/FoodMenu';
import Cart from './screens/Cart';
import Checkout from './screens/Checkout';
import Review from './screens/Review';
import MyOrder from './screens/MyOrder';
import Discount from './screens/Discount';
import Sidebar from './screens/Sidebar';
function App() {
  return (
    <div>
      <WelcomeFoody />
    </div>
  );
}

export default App;

```

# ../src\App.test.js

```
import { render, screen } from '@testing-library/react';
import App from './App';

test('renders learn react link', () => {
  render(<App />);
  const linkElement = screen.getByText(/learn react/i);
  expect(linkElement).toBeInTheDocument();
});

```

# ../src\index.css

```
@tailwind base;
@tailwind components;
@tailwind utilities;


/* body {
  margin: 0;
  font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', 'Roboto', 'Oxygen',
    'Ubuntu', 'Cantarell', 'Fira Sans', 'Droid Sans', 'Helvetica Neue',
    sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}

code {
  font-family: source-code-pro, Menlo, Monaco, Consolas, 'Courier New',
    monospace;
} */

```

# ../src\index.js

```
import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';
import App from './App';
import reportWebVitals from './reportWebVitals';

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>
);

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();

```

# ../src\reportWebVitals.js

```
const reportWebVitals = onPerfEntry => {
  if (onPerfEntry && onPerfEntry instanceof Function) {
    import('web-vitals').then(({ getCLS, getFID, getFCP, getLCP, getTTFB }) => {
      getCLS(onPerfEntry);
      getFID(onPerfEntry);
      getFCP(onPerfEntry);
      getLCP(onPerfEntry);
      getTTFB(onPerfEntry);
    });
  }
};

export default reportWebVitals;

```

# ../src\setupTests.js

```
// jest-dom adds custom jest matchers for asserting on DOM nodes.
// allows you to do things like:
// expect(element).toHaveTextContent(/react/i)
// learn more: https://github.com/testing-library/jest-dom
import '@testing-library/jest-dom';

```

# ../src\components\Button.js

```
import React from 'react';

const Button = ({ children, onClick, variant = 'primary' }) => {
  const baseStyle = "";
  const variantStyles = {
    primary: "bg-orange-500 text-white py-2 px-6 rounded-full mt-4 hover:bg-orange-600 transition duration-300",
    secondary: "bg-orange-500 text-white py-2 px-6 rounded-full mt-2 hover:bg-orange-600 transition duration-300"
  };

  return (
    <button
      onClick={onClick}
      className={`${baseStyle} ${variantStyles[variant]}`}
    >
      {children}
    </button>
  );
};

export default Button;

```

# ../src\screens\Cart.js

```
import React, { useState } from 'react';
import { FaShoppingCart, FaAngleLeft, FaPlus, FaMinus, FaTrash } from 'react-icons/fa';

const Cart = () => {
    // Initial cart items
    const initialCartItems = [
        { id: 1, name: 'Red n hot pizza', description: 'Spicy chicken, beef', price: 9.50, quantity: 2, image: '/path-to-image/red-n-hot-pizza.jpg' },
        { id: 2, name: 'Spicy Pizza', description: 'Spicy chicken, beef', price: 9.50, quantity: 2, image: '/path-to-image/spicy-pizza.jpg' },
        { id: 3, name: 'Parata', description: 'Spicy chicken, beef', price: 9.50, quantity: 2, image: '/path-to-image/parata.jpg' }
    ];

    // State for cart items
    const [cartItems, setCartItems] = useState(initialCartItems);

    // Function to update the quantity of cart items
    const handleQuantityChange = (itemId, delta) => {
        setCartItems(currentItems =>
            currentItems.map(item =>
                item.id === itemId ? { ...item, quantity: Math.max(0, item.quantity + delta) } : item
            )
        );
    };

    const totalPrice = cartItems.reduce((total, item) => total + item.price * item.quantity, 0);
    const deliveryFee = 5.30;
    const grandTotal = totalPrice + deliveryFee;

    return (
        <div className="p-4 bg-gray-100 min-h-screen">
            <div className="bg-white py-4 px-6 mb-4 shadow-md flex justify-between items-center">
                <FaAngleLeft className="cursor-pointer"/>
                <h1 className="text-xl font-bold">Cart</h1>
                <FaShoppingCart className='cursor-pointer'/>
            </div>
            {cartItems.map(item => (
                <CartItem key={item.id} item={item} handleQuantityChange={handleQuantityChange} />
            ))}
            <div className="bg-white p-4 shadow-md rounded-lg mt-4">
                <div className="flex justify-between mb-2">
                    <span>Delivery Fee</span>
                    <span>${deliveryFee.toFixed(2)}</span>
                </div>
                <div className="flex justify-between mb-2 font-bold">
                    <span>Total</span>
                    <span>${grandTotal.toFixed(2)}</span>
                </div>
                <button className="w-full bg-red-500 text-white py-3 mt-4 rounded-lg">CHECKOUT</button>
            </div>
        </div>
    );
};

const CartItem = ({ item, handleQuantityChange }) => {
    return (
        <div className="flex items-center justify-between p-4 bg-white shadow-lg rounded-lg mb-4">
            <img src={item.image} alt={item.name} className="w-20 h-20 rounded-full object-cover" />
            <div>
                <h5 className="font-bold">{item.name}</h5>
                <p className="text-sm text-gray-500">{item.description}</p>
                <div className="flex items-center">
                    <FaMinus onClick={() => handleQuantityChange(item.id, -1)} className="text-red-500 cursor-pointer" />
                    <span className="mx-2">{item.quantity}</span>
                    <FaPlus onClick={() => handleQuantityChange(item.id, 1)} className="text-green-500 cursor-pointer" />
                </div>
            </div>
            <span className="text-lg font-bold">${item.price.toFixed(2)}</span>
            <FaTrash className="text-red-500 cursor-pointer" />
        </div>
    );
};

export default Cart;

```

# ../src\screens\Checkout.js

```
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

```

# ../src\screens\Discount.js

```
import React, { useState } from 'react';
import { FaSearch, FaChevronLeft, FaStar, FaLeaf, FaPepperHot, FaUtensils } from 'react-icons/fa';

const Discount = () => {
    const restaurants = [
        {
            id: 1,
            name: "Artisan Coffee Shop",
            recipes: 29,
            rating: 4,
            discount: 25,
            type: "Vegetarian",
            image: "/path-to-image/artisan-coffee-shop.jpg"
        },
        {
            id: 2,
            name: "KAZY ASPARAGAS",
            recipes: 29,
            rating: 4,
            discount: 25,
            type: "Vegetarian",
            image: "/path-to-image/kazy-asparagas.jpg"
        },
        { id: 3, name: "Burger Zone", recipes: 15, rating: 3, discount: 10, type: "Halal", image: "/images/burger-zone.jpg" },
        { id: 4, name: "Spicy Delight", recipes: 20, rating: 4, discount: 15, type: "Spicy", image: "/images/spicy-delight.jpg" },
        { id: 5, name: "Green Bites", recipes: 18, rating: 5, discount: 20, type: "Vegetarian", image: "/images/green-bites.jpg" },
        { id: 6, name: "Halal Feast", recipes: 22, rating: 4, discount: 18, type: "Halal", image: "/images/halal-feast.jpg" },
        { id: 7, name: "Chili House", recipes: 30, rating: 5, discount: 22, type: "Spicy", image: "/images/chili-house.jpg" },
        { id: 8, name: "Veggie Paradise", recipes: 25, rating: 3, discount: 12, type: "Vegetarian", image: "/images/veggie-paradise.jpg" },
        { id: 9, name: "Halal Corner", recipes: 28, rating: 4, discount: 10, type: "Halal", image: "/images/halal-corner.jpg" },
        { id: 10, name: "Spice Hub", recipes: 17, rating: 4, discount: 20, type: "Spicy", image: "/images/spice-hub.jpg" },
        { id: 11, name: "Pure Vegan", recipes: 20, rating: 5, discount: 30, type: "Vegetarian", image: "/images/pure-vegan.jpg" },
        { id: 12, name: "Meat Masters", recipes: 19, rating: 4, discount: 15, type: "Halal", image: "/images/meat-masters.jpg" }
    ];

    const [activeCategory, setActiveCategory] = useState('All');

    const categories = [
        { name: "All", icon: <FaUtensils className="text-blue-500" /> },
        { name: "Halal", icon: <FaUtensils className="text-yellow-500" /> },
        { name: "Spicy", icon: <FaPepperHot className="text-red-500" /> },
        { name: "Vegetarian", icon: <FaLeaf className="text-green-500" /> },
        // { name: "Pizza", icon: <FaLeaf className="text-gray-500" /> }
    ];

    const filterRestaurants = activeCategory === 'All' ? restaurants : restaurants.filter(restaurant => restaurant.type === activeCategory);

    return (
        <div className="bg-gray-100 min-h-screen p-4">
            <div className="flex items-center justify-between p-4 bg-white">
                <FaChevronLeft className="text-xl" />
                <h1 className="text-lg font-bold">Deliver to Parijat, Housing Estate</h1>
                <div></div>  {/* Placeholder for right side icon or spacing */}
            </div>
            <div className="p-4 bg-white">
                <div className="flex items-center bg-gray-200 rounded">
                    <FaSearch className="text-gray-500 m-2" />
                    <input className="bg-transparent p-2 w-full" placeholder="Find Your Restaurants" />
                </div>
                <div className="flex justify-around my-4">
                    {categories.map(category => (
                        <button key={category.name} className={`flex flex-col items-center ${activeCategory === category.name ? 'text-orange-500' : 'text-gray-500'}`} onClick={() => setActiveCategory(category.name)}>
                            {category.icon}
                            <span>{category.name}</span>
                        </button>
                    ))}
                </div>
            </div>
            <div className="space-y-4">
                {filterRestaurants.map(restaurant => (
                    <div key={restaurant.id} className="bg-white p-4 rounded-lg shadow">
                        <div className="relative">
                            <img src={restaurant.image} alt={restaurant.name} className="w-full h-40 object-cover rounded-lg" />
                            <span className="absolute top-2 right-2 bg-orange-500 text-white px-3 py-1 rounded">{restaurant.discount}% Discount</span>
                        </div>
                        <div className="mt-2 flex justify-between items-center">
                            <div>
                                <h5 className="font-bold">{restaurant.name}</h5>
                                <p className="text-sm text-gray-500">{restaurant.recipes} recipes</p>
                            </div>
                            <div className="flex items-center">
                                {[...Array(restaurant.rating)].map((_, i) => (
                                    <FaStar key={i} className="text-yellow-500" />
                                ))}
                                <span className="text-sm text-gray-500 ml-1">{restaurant.rating}</span>
                            </div>
                        </div>
                    </div>
                ))}
            </div>
        </div>
    );
};

export default Discount;

```

# ../src\screens\FoodMenu.js

```
import React, { useState } from 'react';

// Sample data for the food items
const foodItems = [
  { id: 1, name: "Red n hot pizza", description: "Spicy chicken, beef", price: "9.50", category: "Fast food", rating: "4.5", reviews: "25" },
  { id: 2, name: "Meat Pasta", description: "Meat & Basil", price: "9.50", category: "Fast food", rating: "4.5", reviews: "20" },
  { id: 3, name: "Brushetta", description: "Toppings & tomato", price: "9.50", category: "Platter", rating: "4.5", reviews: "15" },
  { id: 4, name: "Salad", description: "Baked Salmon", price: "9.50", category: "Heavy food", rating: "4.5", reviews: "30" }
];

const categories = ["All", "Fast food", "Heavy food", "Platter"];

const FoodMenu = () => {
  const [activeCategory, setActiveCategory] = useState("All");

  const filteredItems = activeCategory === "All" ? foodItems : foodItems.filter(item => item.category === activeCategory);

  return (
    <div className="bg-white min-h-screen">
      <header className="flex justify-between items-center p-4 bg-white shadow-md">
        <button>🔙</button>
        <h1 className="font-bold text-xl">Food Menu</h1>
        <button>🛒</button>
      </header>
      <div className="flex justify-around bg-gray-100 p-2">
        {categories.map(category => (
          <button key={category}
                  className={`py-2 px-4 ${activeCategory === category ? 'text-red-500 font-bold' : 'text-gray-500'}`}
                  onClick={() => setActiveCategory(category)}>
            {category}
          </button>
        ))}
      </div>
      <div className="p-4 grid grid-cols-2 gap-4">
        {filteredItems.map(item => (
          <div key={item.id} className="bg-white p-2 rounded shadow">
            <img src={`/path-to-images/${item.name.replaceAll(' ', '-').toLowerCase()}.jpg`} alt={item.name} className="w-full h-32 object-cover rounded"/>
            <div className="p-2">
              <h5 className="font-bold">{item.name} - ${item.price}</h5>
              <p className="text-sm text-gray-600">{item.description}</p>
              <div className="flex justify-between items-center mt-2">
                <span className="text-gray-500">{item.rating} ⭐ ({item.reviews})</span>
                <button className="bg-red-500 text-white px-3 py-1 rounded">Add</button>
              </div>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
};

export default FoodMenu;

```

# ../src\screens\ForgotPassword.js

```
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

```

# ../src\screens\GPSTrackingCard.js

```
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

```

# ../src\screens\GPSTrackingScreen.js

```
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

```

# ../src\screens\LoginForm.js

```
import React from 'react';

function LoginForm() {
    return (
        <div className="min-h-screen flex items-center justify-center bg-red-100"> {/* Giữ nguyên màu nền hoặc thay đổi nếu cần */}
            <div className="bg-white p-6 rounded-lg shadow-md w-96">
                <h2 className="text-2xl font-semibold text-center mb-6">Sign In</h2>
                <form>
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

```

# ../src\screens\MyOrder.js

```
import React, { useState } from 'react';
import { FaChevronLeft, FaRegCheckCircle, FaRegClock, FaRedo } from 'react-icons/fa';

const MyOrder = () => {
    const [activeTab, setActiveTab] = useState('complete');

    const orders = {
        complete: [
            { id: 1, restaurant: "KFC", items: "Pizza, Alo Bortha, Thethul achar, Chicken tiriaky", price: 59, status: 'complete' },
            // Additional completed orders
        ],
        pending: [
            { id: 2, restaurant: "KFC", items: "Burger, Fries, Coke", price: 45, status: 'pending' },
            // Additional pending orders
        ]
    };

    return (
        <div className="bg-gray-100 min-h-screen p-4">
            <div className="bg-white py-4 px-6 mb-4 shadow-md flex justify-between items-center">
                <FaChevronLeft className="cursor-pointer text-gray-600" onClick={() => console.log('Go Back')} />
                <h1 className="text-xl font-bold">My Order</h1>
                <p></p>
            </div>
            <div className="flex justify-around bg-white p-2 shadow-md">
                <button
                    className={`flex-1 ${activeTab === 'complete' ? 'text-orange-500 font-bold' : 'text-gray-500'}`}
                    onClick={() => setActiveTab('complete')}
                >
                    Complete Order
                </button>
                <button
                    className={`flex-1 ${activeTab === 'pending' ? 'text-orange-500 font-bold' : 'text-gray-500'}`}
                    onClick={() => setActiveTab('pending')}
                >
                    Pending Order
                </button>
            </div>
            <div className="space-y-4 mt-4">
                {orders[activeTab].map(order => (
                    <div key={order.id} className="bg-white p-4 rounded-lg shadow-md flex justify-between items-center">
                        <div>
                            <h5 className="font-bold">{order.restaurant}</h5>
                            <p className="text-sm text-gray-500">{order.items}</p>
                            <p className="text-sm text-gray-500">${order.price}</p>
                        </div>
                        <button className="flex items-center text-orange-500">
                            <FaRedo className="mr-2" />
                            Order Again
                        </button>
                    </div>
                ))}
            </div>
        </div>
    );
};

export default MyOrder;

```

# ../src\screens\QuickFoodDelivery.js

```
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

```

# ../src\screens\Review.js

```
import React, { useState } from 'react';
import { FaChevronLeft, FaEllipsisV } from 'react-icons/fa';

const ReviewModal = ({ isOpen, onClose, onSubmit }) => {
    const [reviewText, setReviewText] = useState('');

    if (!isOpen) return null;

    return (
        <div className="fixed inset-0 bg-gray-600 bg-opacity-50 flex justify-center items-center p-4">
            <div className="bg-white p-4 rounded-lg shadow-lg space-y-4">
                <textarea
                    className="w-full p-2 border border-gray-300 rounded"
                    value={reviewText}
                    onChange={(e) => setReviewText(e.target.value)}
                    placeholder="Write your review..."
                />
                <button
                    className="bg-blue-500 text-white p-2 rounded"
                    onClick={() => {
                        onSubmit(reviewText);
                        onClose();
                    }}
                >
                    Submit Review
                </button>
            </div>
        </div>
    );
};

const Review = () => {
    const reviews = [
        {
            id: 1,
            name: "Nathasa Malkuba",
            date: "28/02/2021",
            review: "Loved the class! Such beautiful land and collective impact infrastructure social entrepreneurship mass incarceration 👍",
            rating: 5.0
        },
        {
            id: 2,
            name: "Furinai Millabi",
            date: "01/03/2021",
            review: "Never run so well and it’s all thanks to Jordan. Silo framework overcome justice ideate, citizen-centered effective",
            rating: 4.0
        },
        {
            id: 3,
            name: "Sami Rafi",
            date: "01/03/2021",
            review: "Big up my running crew, they better not say running crew who! Commitment equal opportunity empower.",
            rating: 4.5
        }
    ];
    const [modalOpen, setModalOpen] = useState(false);

    const handleReviewSubmit = (review) => {
        console.log("Review Submitted: ", review); // Handle review submission
    };

    return (
        <div className="bg-gray-100 min-h-screen p-4">
            <div className="bg-white py-4 px-6 mb-4 shadow-md flex justify-between items-center">
                <FaChevronLeft className="cursor-pointer text-gray-600" onClick={() => console.log('Go Back')} />
                <h1 className="text-xl font-bold">Review</h1>
                <FaEllipsisV className="cursor-pointer text-gray-600" />
            </div>
            {/* Review list here */}
            <div className="space-y-4">
                {reviews.map(review => (
                    <div key={review.id} className="bg-white p-4 rounded-lg shadow-md">
                        <div className="flex justify-between items-center">
                            <div>
                                <h5 className="font-bold">{review.name}</h5>
                                <p className="text-sm text-gray-500">{review.date}</p>
                            </div>
                            <FaEllipsisV className="cursor-pointer text-gray-500" />
                        </div>
                        <p className="mt-2">{review.review}</p>
                    </div>
                ))}
            </div>
            <button
                className="mt-6 bg-blue-500 text-white p-3 rounded-lg w-full"
                onClick={() => setModalOpen(true)}
            >
                Write your review...
            </button>
            <ReviewModal
                isOpen={modalOpen}
                onClose={() => setModalOpen(false)}
                onSubmit={handleReviewSubmit}
            />
        </div>
    );
};

export default Review;

```

# ../src\screens\Sidebar.js

```
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

```

# ../src\screens\SignIn.js

```
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

```

# ../src\screens\SignUp.js

```
import React, { useState } from 'react';

const SignUp = () => {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [mobile, setMobile] = useState('');
  const [agreed, setAgreed] = useState(false);

  const handleSubmit = (event) => {
    event.preventDefault();
    // Implement the sign-up logic
    console.log(`User signed up with email: ${email}, mobile: ${mobile}`);
  };

  return (
    <div className="bg-white min-h-screen flex flex-col items-center justify-center px-4">
      <div className="w-full max-w-sm">
        <h1 className="text-2xl font-semibold text-center mb-6">SIGN UP</h1>
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
          <div className="mb-4">
            <input
              type="password"
              value={password}
              onChange={(e) => setPassword(e.target.value)}
              placeholder="Password"
              className="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 mb-3 leading-tight focus:outline-none focus:shadow-outline"
              required
            />
          </div>
          <div className="mb-4">
            <input
              type="text"
              value={mobile}
              onChange={(e) => setMobile(e.target.value)}
              placeholder="Mobile"
              className="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
              required
            />
          </div>
          <div className="mb-4 flex items-center">
            <input
              type="checkbox"
              checked={agreed}
              onChange={(e) => setAgreed(e.target.checked)}
              className="mr-2 leading-tight"
            />
            <span className="text-sm">
              I accepted all terms & conditions.
            </span>
          </div>
          <div className="flex items-center justify-between">
            <button
              type="submit"
              className="bg-orange-500 hover:bg-orange-600 text-white font-bold py-2 px-4 rounded focus:outline-none focus:shadow-outline"
            >
              SIGN UP
            </button>
          </div>
          <div className="text-center text-sm mt-4">
            I already have an account? <a href="#" className="text-orange-500 hover:underline">Sign In</a>
          </div>
        </form>
      </div>
    </div>
  );
};

export default SignUp;

```

# ../src\screens\WelcomeFoody.js

```
import React, { useState } from 'react';
import { FaBars, FaSearch, FaUserCircle, FaHome, FaRegListAlt, FaUser } from 'react-icons/fa';
import Sidebar from './Sidebar';

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
        <FaHome className="text-2xl" />
        <FaSearch className="text-2xl" />
        <FaRegListAlt className="text-2xl" />
        <FaUser className="text-2xl" />
      </nav>
    </div>
  );
};

export default WelcomeFoody;

```

# ../src\screens\WelcomeScreen.js

```
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




```

