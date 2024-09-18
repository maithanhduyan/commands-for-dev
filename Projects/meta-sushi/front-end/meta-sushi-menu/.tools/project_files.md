# ../package.json

```
{
  "name": "meta-sushi-menu",
  "version": "0.1.0",
  "private": true,
  "dependencies": {
    "@testing-library/jest-dom": "^5.17.0",
    "@testing-library/react": "^13.4.0",
    "@testing-library/user-event": "^13.5.0",
    "framer-motion": "^11.5.4",
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
    "tailwindcss": "^3.4.11"
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
    extend: {},
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
// import './App.css';
import './index.css';
// import HomeMenu from './Home';
// import SushiShopMenu from './SushiShopMenu';
// import SushiShopMenu   from './SushiMenu2';
import SushiShopMenu   from './SushiMenu3';

function App() {
  return (
    <SushiShopMenu />
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

# ../src\Home.js

```
import logo from './logo.svg';
import './App.css';

const HomeMenu = () => {
    return (
        <div className="App">
            <header className="App-header">
                <img src={logo} className="App-logo" alt="logo" />
                <p>
                    Edit <code>src/App.js</code> and save to reload.
                </p>
                <a
                    className="App-link"
                    href="https://reactjs.org"
                    target="_blank"
                    rel="noopener noreferrer"
                >
                    Learn React
                </a>
            </header>
        </div>
    );
}

export default HomeMenu;
```

# ../src\index.css

```
/* src/index.css */
@tailwind base;
@tailwind components;
@tailwind utilities;

body {
  font-family: Arial, sans-serif;
  margin: 0;
  padding: 0;
}

.container {
  padding: 20px;
  max-width: 1200px;
  margin: auto;
}

h1 {
  text-align: center;
}

.search-bar {
  display: flex;
  margin-bottom: 20px;
}

.search-bar input {
  flex: 1;
  padding: 10px;
}

.search-bar button {
  padding: 10px;
}

.filters {
  margin-bottom: 20px;
}

.filters button {
  margin-right: 10px;
  padding: 10px;
}

.filters .active {
  background-color: blue;
  color: white;
}

.menu-items {
  display: flex;
  flex-wrap: wrap;
  gap: 20px;
}

.menu-item {
  width: calc(33.333% - 20px);
  border: 1px solid #ddd;
  padding: 10px;
  box-sizing: border-box;
}

.menu-item img {
  width: 100%;
  height: auto;
}

.menu-item h2 {
  margin: 10px 0;
}

.cart {
  position: fixed;
  top: 0;
  right: 0;
  width: 300px;
  height: 100%;
  background: white;
  border-left: 1px solid #ddd;
  padding: 20px;
  box-sizing: border-box;
}

.cart button {
  margin-bottom: 20px;
}

.cart-item {
  display: flex;
  justify-content: space-between;
  margin-bottom: 10px;
}

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
reportWebVitals(console.log);

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

# ../src\SushiMenu2.js

```
import React, { useState, useEffect } from 'react';
import { FaSearch, FaShoppingCart, FaFilter, FaSort } from 'react-icons/fa';
import { motion, AnimatePresence } from 'framer-motion';

import californiaRoll2Img from './assets/images/california_Roll2.jpg'; // https://images.unsplash.com/photo-1579871494447-9811cf80d66c
import Salmon_Nigiri_Img from './assets/images/Salmon_Nigiri.jpg'; // https://images.unsplash.com/photo-1534482421-64566f976cfa
import Spicy_Tuna_Roll_Img from './assets/images/Spicy_Tuna_Roll.jpg'; // https://images.unsplash.com/photo-1617196034796-73dfa7b1fd56
import Vegetable_Tempura_Roll_Img from './assets/images/Veggie-Tempura-Roll_ok.jpg'; // https://images.unsplash.com/photo-1620039102630-11cb2004c5c5
import Tuna_Sashimi_Img from './assets/images/california-roll.jpg'; // https://images.unsplash.com/photo-1579584425555-c3ce17fd4351

const sushiMenu = [
  { id: 1, name: 'California Roll', category: 'Maki Rolls', price: 8.99, description: 'Crab, avocado, cucumber', image: californiaRoll2Img, tags: ['popular'] },
  { id: 2, name: 'Salmon Nigiri', category: 'Nigiri', price: 6.99, description: 'Fresh salmon over rice', image: Salmon_Nigiri_Img, tags: ['gluten-free'] },
  { id: 3, name: 'Spicy Tuna Roll', category: 'Maki Rolls', price: 9.99, description: 'Spicy tuna, cucumber', image: Spicy_Tuna_Roll_Img, tags: ['spicy'] },
  { id: 4, name: 'Vegetable Tempura Roll', category: 'Special Rolls', price: 7.99, description: 'Assorted vegetables, tempura batter', image: Vegetable_Tempura_Roll_Img, tags: ['vegetarian'] },
  { id: 5, name: 'Tuna Sashimi', category: 'Sashimi', price: 12.99, description: 'Sliced raw tuna', image: Tuna_Sashimi_Img, tags: ['gluten-free'] },
];

const SushiMenu = () => {
  const [menu, setMenu] = useState(sushiMenu);
  const [searchTerm, setSearchTerm] = useState('');
  const [filter, setFilter] = useState('');
  const [sortBy, setSortBy] = useState('');
  const [cart, setCart] = useState([]);
  const [error, setError] = useState('');

  useEffect(() => {
    let filteredMenu = sushiMenu;

    if (searchTerm) {
      filteredMenu = filteredMenu.filter(item =>
        item.name.toLowerCase().includes(searchTerm.toLowerCase()) ||
        item.description.toLowerCase().includes(searchTerm.toLowerCase())
      );
    }

    if (filter) {
      filteredMenu = filteredMenu.filter(item =>
        item.tags.includes(filter) || item.category === filter
      );
    }

    if (sortBy === 'price') {
      filteredMenu.sort((a, b) => a.price - b.price);
    } else if (sortBy === 'name') {
      filteredMenu.sort((a, b) => a.name.localeCompare(b.name));
    }

    setMenu(filteredMenu);
  }, [searchTerm, filter, sortBy]);

  const addToCart = (item) => {
    setCart([...cart, item]);
    setError('');
  };

  const handleSearch = (e) => {
    setSearchTerm(e.target.value);
    setError('');
  };

  const handleFilter = (filterValue) => {
    setFilter(filterValue);
    setError('');
  };

  const handleSort = (sortValue) => {
    setSortBy(sortValue);
    setError('');
  };

  return (
    <div className="container mx-auto px-4 py-8">
      <h1 className="text-4xl font-bold text-center mb-8">Meta Sushi Menu</h1>

      <div className="flex flex-col md:flex-row justify-between items-center mb-8">
        <div className="relative w-full md:w-1/3 mb-4 md:mb-0">
          <input
            type="text"
            placeholder="Search menu..."
            value={searchTerm}
            onChange={handleSearch}
            className="w-full pl-10 pr-4 py-2 rounded-lg border border-gray-300 focus:outline-none focus:ring-2 focus:ring-blue-500"
            aria-label="Search menu"
          />
          <FaSearch className="absolute left-3 top-3 text-gray-400" />
        </div>

        <div className="flex space-x-4">
          <div className="relative">
            <select
              onChange={(e) => handleFilter(e.target.value)}
              className="appearance-none bg-white border border-gray-300 rounded-lg pl-4 pr-10 py-2 focus:outline-none focus:ring-2 focus:ring-blue-500"
              aria-label="Filter menu"
            >
              <option value="">All Items</option>
              <option value="vegetarian">Vegetarian</option>
              <option value="gluten-free">Gluten-Free</option>
              <option value="spicy">Spicy</option>
            </select>
            <FaFilter className="absolute right-3 top-3 text-gray-400 pointer-events-none" />
          </div>

          <div className="relative">
            <select
              onChange={(e) => handleSort(e.target.value)}
              className="appearance-none bg-white border border-gray-300 rounded-lg pl-4 pr-10 py-2 focus:outline-none focus:ring-2 focus:ring-blue-500"
              aria-label="Sort menu"
            >
              <option value="">Sort By</option>
              <option value="price">Price</option>
              <option value="name">Name</option>
            </select>
            <FaSort className="absolute right-3 top-3 text-gray-400 pointer-events-none" />
          </div>
        </div>
      </div>

      {error && (
        <div className="bg-red-100 border border-red-400 text-red-700 px-4 py-3 rounded relative mb-4" role="alert">
          <strong className="font-bold">Error:</strong>
          <span className="block sm:inline"> {error}</span>
        </div>
      )}

      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
        <AnimatePresence>
          {menu.map((item) => (
            <motion.div
              key={item.id}
              initial={{ opacity: 0, y: 20 }}
              animate={{ opacity: 1, y: 0 }}
              exit={{ opacity: 0, y: -20 }}
              className="bg-white rounded-lg shadow-lg overflow-hidden"
            >
              <img src={item.image} alt={item.name} className="w-full h-48 object-cover" />
              <div className="p-4">
                <h2 className="text-xl font-semibold mb-2">{item.name}</h2>
                <p className="text-gray-600 mb-2">{item.description}</p>
                <div className="flex justify-between items-center">
                  <span className="text-lg font-bold">${item.price.toFixed(2)}</span>
                  <button
                    onClick={() => addToCart(item)}
                    className="bg-blue-500 text-white px-4 py-2 rounded-lg hover:bg-blue-600 transition duration-300"
                    aria-label={`Add ${item.name} to cart`}
                  >
                    Add to Cart
                  </button>
                </div>
              </div>
            </motion.div>
          ))}
        </AnimatePresence>
      </div>

      {menu.length === 0 && (
        <p className="text-center text-gray-500 mt-8">No items found. Please try a different search or filter.</p>
      )}

      <div className="fixed bottom-4 right-4">
        <button
          className="bg-blue-500 text-white p-4 rounded-full shadow-lg hover:bg-blue-600 transition duration-300"
          aria-label="View cart"
        >
          <FaShoppingCart className="text-2xl" />
          {cart.length > 0 && (
            <span className="absolute -top-2 -right-2 bg-red-500 text-white rounded-full w-6 h-6 flex items-center justify-center text-sm">
              {cart.length}
            </span>
          )}
        </button>
      </div>
    </div>
  );
};

export default SushiMenu;
```

# ../src\SushiMenu3.js

```
import React, { useState, useEffect } from 'react';
import { FaSearch, FaHeart, FaShoppingCart, FaStar } from 'react-icons/fa';
import { motion } from 'framer-motion';

import Edamame_Img from './assets/images/Steamed soybeans with sea salt.jpg';
import californiaRoll2Img from './assets/images/california_Roll2.jpg';
import Salmon_Nigiri_Img from './assets/images/Salmon_Nigiri.jpg';
import Dragon_Roll_Img from './assets/images/vegetable-tempura-roll.jpg';
import Mochi_Ice_Cream_Img from './assets/images/mochi_ice_cream.jpg';



const menuItems = [
  {
    id: 1,
    name: 'California Roll',
    description: 'Crab, avocado, and cucumber roll',
    price: 8.99,
    category: 'sushi rolls',
    tags: ['popular'],
    image: californiaRoll2Img
  },
  {
    id: 2,
    name: 'Edamame',
    description: 'Steamed soybeans with sea salt',
    price: 5.99,
    category: 'appetizers',
    tags: ['vegetarian', 'gluten-free'],
    image: Edamame_Img
  },
  {
    id: 3,
    name: 'Salmon Nigiri',
    description: 'Fresh salmon over pressed rice',
    price: 6.99,
    category: 'nigiri',
    tags: ['gluten-free'],
    image: Salmon_Nigiri_Img
  },
  {
    id: 4,
    name: 'Dragon Roll',
    description: 'Eel, crab, cucumber topped with avocado',
    price: 12.99,
    category: 'sushi rolls',
    tags: ['chef special'],
    image: Dragon_Roll_Img
  },
  {
    id: 5,
    name: 'Mochi Ice Cream',
    description: 'Assorted flavors of ice cream wrapped in mochi',
    price: 7.99,
    category: 'desserts',
    tags: ['vegetarian'],
    image: Mochi_Ice_Cream_Img
  },
];

const SushiMenu = () => {
  const [filteredItems, setFilteredItems] = useState(menuItems);
  const [activeFilter, setActiveFilter] = useState('all');
  const [searchTerm, setSearchTerm] = useState('');
  const [sortBy, setSortBy] = useState('name');
  const [cart, setCart] = useState([]);
  const [favorites, setFavorites] = useState([]);

  useEffect(() => {
    let result = menuItems;
    if (activeFilter !== 'all') {
      result = result.filter(item => item.tags.includes(activeFilter) || item.category === activeFilter);
    }
    if (searchTerm) {
      result = result.filter(item =>
        item.name.toLowerCase().includes(searchTerm.toLowerCase()) ||
        item.description.toLowerCase().includes(searchTerm.toLowerCase())
      );
    }
    result.sort((a, b) => {
      if (sortBy === 'price') return a.price - b.price;
      if (sortBy === 'name') return a.name.localeCompare(b.name);
      return 0;
    });
    setFilteredItems(result);
  }, [activeFilter, searchTerm, sortBy]);

  const addToCart = (item) => {
    setCart([...cart, item]);
  };

  const toggleFavorite = (item) => {
    if (favorites.find(fav => fav.id === item.id)) {
      setFavorites(favorites.filter(fav => fav.id !== item.id));
    } else {
      setFavorites([...favorites, item]);
    }
  };

  return (
    <div className="container mx-auto px-4 py-8 bg-gray-100 min-h-screen">
      <h1 className="text-4xl font-bold text-center text-red-600 mb-8">Meta Sushi Menu</h1>
      
      <div className="flex flex-col md:flex-row justify-between items-center mb-8">
        <div className="relative w-full md:w-1/3 mb-4 md:mb-0">
          <input
            type="text"
            placeholder="Search menu..."
            className="w-full p-2 pl-10 rounded-full border-2 border-red-300 focus:outline-none focus:border-red-500"
            value={searchTerm}
            onChange={(e) => setSearchTerm(e.target.value)}
          />
          <FaSearch className="absolute left-3 top-3 text-gray-400" />
        </div>
        
        <div className="flex space-x-2">
          <select
            className="p-2 rounded-md border-2 border-red-300 focus:outline-none focus:border-red-500"
            value={activeFilter}
            onChange={(e) => setActiveFilter(e.target.value)}
          >
            <option value="all">All Items</option>
            <option value="appetizers">Appetizers</option>
            <option value="sushi rolls">Sushi Rolls</option>
            <option value="nigiri">Nigiri</option>
            <option value="desserts">Desserts</option>
            <option value="vegetarian">Vegetarian</option>
            <option value="gluten-free">Gluten-Free</option>
            <option value="chef special">Chef's Special</option>
          </select>
          
          <select
            className="p-2 rounded-md border-2 border-red-300 focus:outline-none focus:border-red-500"
            value={sortBy}
            onChange={(e) => setSortBy(e.target.value)}
          >
            <option value="name">Sort by Name</option>
            <option value="price">Sort by Price</option>
          </select>
        </div>
      </div>

      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
        {filteredItems.map((item) => (
          <motion.div
            key={item.id}
            className="bg-white rounded-lg shadow-md overflow-hidden"
            whileHover={{ scale: 1.05 }}
            transition={{ duration: 0.3 }}
          >
            <img src={item.image} alt={item.name} className="w-full h-48 object-cover" />
            <div className="p-4">
              <div className="flex justify-between items-start mb-2">
                <h2 className="text-xl font-semibold text-gray-800">{item.name}</h2>
                <span className="text-lg font-bold text-red-600">${item.price.toFixed(2)}</span>
              </div>
              <p className="text-gray-600 mb-4">{item.description}</p>
              <div className="flex justify-between items-center">
                <div className="space-x-2">
                  {item.tags.map((tag) => (
                    <span key={tag} className="inline-block bg-red-100 text-red-800 text-xs px-2 py-1 rounded-full">{tag}</span>
                  ))}
                </div>
                <div className="space-x-2">
                  <button
                    onClick={() => toggleFavorite(item)}
                    className="text-red-500 hover:text-red-700"
                    aria-label={`Add ${item.name} to favorites`}
                  >
                    <FaHeart className={favorites.find(fav => fav.id === item.id) ? 'text-red-500' : 'text-gray-400'} />
                  </button>
                  <button
                    onClick={() => addToCart(item)}
                    className="bg-red-500 text-white px-3 py-1 rounded-full hover:bg-red-600"
                    aria-label={`Add ${item.name} to cart`}
                  >
                    <FaShoppingCart />
                  </button>
                </div>
              </div>
            </div>
          </motion.div>
        ))}
      </div>

      {filteredItems.length === 0 && (
        <p className="text-center text-gray-500 mt-8">No items found. Try adjusting your search or filters.</p>
      )}

      <div className="fixed bottom-4 right-4 flex space-x-4">
        <button
          className="bg-red-500 text-white p-3 rounded-full shadow-lg hover:bg-red-600"
          aria-label="View cart"
        >
          <FaShoppingCart />
          {cart.length > 0 && (
            <span className="absolute -top-2 -right-2 bg-yellow-500 text-xs text-white w-5 h-5 flex items-center justify-center rounded-full">
              {cart.length}
            </span>
          )}
        </button>
        <button
          className="bg-red-500 text-white p-3 rounded-full shadow-lg hover:bg-red-600"
          aria-label="View favorites"
        >
          <FaHeart />
          {favorites.length > 0 && (
            <span className="absolute -top-2 -right-2 bg-yellow-500 text-xs text-white w-5 h-5 flex items-center justify-center rounded-full">
              {favorites.length}
            </span>
          )}
        </button>
      </div>
    </div>
  );
};

export default SushiMenu;
```

# ../src\SushiShopMenu.js

```
import React, { useState, useEffect } from 'react';
import { FaSearch, FaShoppingCart, FaTimes } from 'react-icons/fa';
import { IoMdAdd, IoMdRemove } from 'react-icons/io';

import californiaRollImg from './assets/images/california-roll.jpg';
import salmonNigiriImg from './assets/images/salmon-nigiri.jpg';
import spicyTunaRollImg from './assets/images/spicy-tuna-roll.jpg';
import dragonRollImg from './assets/images/dragon-roll.jpg';
import vegetableTempuraRollImg from './assets/images/vegetable-tempura-roll.jpg';

const SushiShopMenu = () => {
    const [menuItems, setMenuItems] = useState([]);
    const [filteredItems, setFilteredItems] = useState([]);
    const [cart, setCart] = useState([]);
    const [searchTerm, setSearchTerm] = useState('');
    const [activeFilters, setActiveFilters] = useState([]);
    const [isCartOpen, setIsCartOpen] = useState(false);

    useEffect(() => {
        // Simulating API call to fetch menu items
        const fetchedMenuItems = [
            {
                id: 1,
                name: 'California Roll',
                description: 'Crab, avocado, and cucumber roll',
                price: 8.99,
                category: 'maki',
                image: californiaRollImg,
                tags: ['popular', 'vegetarian-option']
            },
            {
                id: 2,
                name: 'Salmon Nigiri',
                description: 'Fresh salmon over pressed rice',
                price: 6.99,
                category: 'nigiri',
                image: salmonNigiriImg,
                tags: ['gluten-free']
            },
            {
                id: 3,
                name: 'Spicy Tuna Roll',
                description: 'Spicy tuna and cucumber roll',
                price: 9.99,
                category: 'maki',
                image: spicyTunaRollImg,
                tags: ['spicy']
            },
            {
                id: 4,
                name: 'Dragon Roll',
                description: 'Eel, crab, and avocado roll topped with avocado',
                price: 14.99,
                category: 'special',
                image: dragonRollImg,
                tags: ['popular']
            },
            {
                id: 5,
                name: 'Vegetable Tempura Roll',
                description: 'Assorted vegetable tempura roll',
                price: 7.99,
                category: 'maki',
                image: vegetableTempuraRollImg,
                tags: ['vegetarian']
            }
        ];
        setMenuItems(fetchedMenuItems);
        setFilteredItems(fetchedMenuItems);
    }, []);

    useEffect(() => {
        const filtered = menuItems.filter(item =>
            item.name.toLowerCase().includes(searchTerm.toLowerCase()) &&
            (activeFilters.length === 0 || activeFilters.some(filter => item.tags.includes(filter)))
        );
        setFilteredItems(filtered);
    }, [searchTerm, activeFilters, menuItems]);

    const addToCart = (item) => {
        const existingItem = cart.find(cartItem => cartItem.id === item.id);
        if (existingItem) {
            setCart(cart.map(cartItem =>
                cartItem.id === item.id ? { ...cartItem, quantity: cartItem.quantity + 1 } : cartItem
            ));
        } else {
            setCart([...cart, { ...item, quantity: 1 }]);
        }
    };

    const removeFromCart = (itemId) => {
        const updatedCart = cart.map(item =>
            item.id === itemId ? { ...item, quantity: item.quantity - 1 } : item
        ).filter(item => item.quantity > 0);
        setCart(updatedCart);
    };

    const clearCart = () => {
        setCart([]);
    };

    const getTotalCost = () => {
        return cart.reduce((total, item) => total + item.price * item.quantity, 0).toFixed(2);
    };

    const toggleFilter = (filter) => {
        setActiveFilters(prevFilters =>
            prevFilters.includes(filter)
                ? prevFilters.filter(f => f !== filter)
                : [...prevFilters, filter]
        );
    };

    return (
        <div className="container mx-auto px-4 py-8">
            <h1 className="text-4xl font-bold mb-8 text-center">Meta Sushi Menu</h1>

            {/* Search and Filter */}
            <div className="mb-8">
                <div className="flex items-center mb-4">
                    <input
                        type="text"
                        placeholder="Search sushi..."
                        className="flex-grow p-2 border rounded-l"
                        value={searchTerm}
                        onChange={(e) => setSearchTerm(e.target.value)}
                        aria-label="Search sushi"
                    />
                    <button className="bg-blue-500 text-white p-2 rounded-r" aria-label="Search">
                        <FaSearch />
                    </button>
                </div>
                <div className="flex flex-wrap gap-2">
                    {['vegetarian', 'gluten-free', 'spicy', 'popular'].map(filter => (
                        <button
                            key={filter}
                            onClick={() => toggleFilter(filter)}
                            className={`px-3 py-1 rounded ${activeFilters.includes(filter) ? 'bg-blue-500 text-white' : 'bg-gray-200'}`}
                            aria-pressed={activeFilters.includes(filter)}
                        >
                            {filter}
                        </button>
                    ))}
                </div>
            </div>

            {/* Menu Items */}
            <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
                {filteredItems.map(item => (
                    <div key={item.id} className="bg-white rounded-lg shadow-md overflow-hidden transition-transform hover:scale-105">
                        <img src={item.image} alt={item.name} className="w-full h-48 object-cover" />
                        <div className="p-4">
                            <h2 className="text-xl font-semibold mb-2">{item.name}</h2>
                            <p className="text-gray-600 mb-2">{item.description}</p>
                            <div className="flex justify-between items-center">
                                <span className="text-lg font-bold">${item.price.toFixed(2)}</span>
                                <button
                                    onClick={() => addToCart(item)}
                                    className="bg-green-500 text-white px-4 py-2 rounded hover:bg-green-600 transition-colors"
                                    aria-label={`Add ${item.name} to cart`}
                                >
                                    Add to Cart
                                </button>
                            </div>
                        </div>
                    </div>
                ))}
            </div>

            {/* Cart */}
            <div className={`fixed top-0 right-0 h-full w-80 bg-white shadow-lg transform ${isCartOpen ? 'translate-x-0' : 'translate-x-full'} transition-transform duration-300 ease-in-out`}>
                <div className="p-4">
                    <div className="flex justify-between items-center mb-4">
                        <h2 className="text-2xl font-bold">Your Cart</h2>
                        <button onClick={() => setIsCartOpen(false)} className="text-gray-500 hover:text-gray-700" aria-label="Close cart">
                            <FaTimes />
                        </button>
                    </div>
                    {cart.length === 0 ? (
                        <p>Your cart is empty</p>
                    ) : (
                        <>
                            {cart.map(item => (
                                <div key={item.id} className="flex justify-between items-center mb-2">
                                    <span>{item.name}</span>
                                    <div className="flex items-center">
                                        <button onClick={() => removeFromCart(item.id)} className="text-red-500 mr-2" aria-label={`Remove ${item.name} from cart`}>
                                            <IoMdRemove />
                                        </button>
                                        <span>{item.quantity}</span>
                                        <button onClick={() => addToCart(item)} className="text-green-500 ml-2" aria-label={`Add another ${item.name} to cart`}>
                                            <IoMdAdd />
                                        </button>
                                    </div>
                                </div>
                            ))}
                            <div className="mt-4">
                                <p className="text-xl font-bold">Total: ${getTotalCost()}</p>
                                <button onClick={clearCart} className="w-full bg-red-500 text-white py-2 rounded mt-4 hover:bg-red-600 transition-colors">
                                    Clear Cart
                                </button>
                            </div>
                        </>
                    )}
                </div>
            </div>

            {/* Cart Toggle Button */}
            <button
                onClick={() => setIsCartOpen(true)}
                className="fixed bottom-4 right-4 bg-blue-500 text-white p-4 rounded-full shadow-lg hover:bg-blue-600 transition-colors"
                aria-label="Open cart"
            >
                <FaShoppingCart />
            </button>
        </div>
    );
};

export default SushiShopMenu;
```

