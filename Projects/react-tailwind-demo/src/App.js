import './App.css'
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import React, { lazy, Suspense } from 'react';
import NoPage from './screens/NoPage';

// Lazy-load screens
const WelcomeFoody = lazy(() => import('./screens/WelcomeFoody'));
const Cart = lazy(() => import('./screens/Cart'));
const Checkout = lazy(() => import('./screens/Checkout'));
const Discount = lazy(() => import('./screens/Discount'));
const FoodMenu = lazy(() => import('./screens/FoodMenu'));
const ForgotPassword = lazy(() => import('./screens/ForgotPassword'));
const GPSTrackingCard = lazy(() => import('./screens/GPSTrackingCard'));
const GPSTrackingScreen = lazy(() => import('./screens/GPSTrackingScreen'));
const LoginForm = lazy(() => import('./screens/LoginForm'));
const MyOrder = lazy(() => import('./screens/MyOrder'));
const QuickFoodDelivery = lazy(() => import('./screens/QuickFoodDelivery'));
const Review = lazy(() => import('./screens/Review'));
const Sidebar = lazy(() => import('./screens/Sidebar'));
const SignIn = lazy(() => import('./screens/SignIn'));
const SignUp = lazy(() => import('./screens/SignUp'));
const WelcomeScreen = lazy(() => import('./screens/WelcomeScreen'));

function App() {
  const Loader = () => (
    <div className="flex justify-center items-center h-screen">
      <div className="spinner"></div>  {/* Custom CSS spinner */}
    </div>
  );
  return (
    <Router>
      <Suspense fallback={<Loader />}>
        <Routes>
          <Route path="/" element={<WelcomeFoody />} />
          <Route path="/cart" element={<Cart />} />
          <Route path="/checkout" element={<Checkout />} />
          <Route path="/discount" element={<Discount />} />
          <Route path="/food-menu" element={<FoodMenu />} />
          <Route path="/forgot-password" element={<ForgotPassword />} />
          <Route path="/gps-tracking-card" element={<GPSTrackingCard />} />
          <Route path="/gps-tracking-screen" element={<GPSTrackingScreen />} />
          <Route path="/login" element={<LoginForm />} />
          <Route path="/my-order" element={<MyOrder />} />
          <Route path="/quick-food-delivery" element={<QuickFoodDelivery />} />
          <Route path="/review" element={<Review />} />
          <Route path="/sidebar" element={<Sidebar />} />
          <Route path="/sign-in" element={<SignIn />} />
          <Route path="/sign-up" element={<SignUp />} />
          <Route path="/welcome" element={<WelcomeScreen />} />
          <Route path="*" element={<NoPage />} />
        </Routes>
      </Suspense>
    </Router>
  );
}

export default App;
