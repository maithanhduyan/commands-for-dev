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
