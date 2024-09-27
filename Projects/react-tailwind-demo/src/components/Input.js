// components/Input.js
const Input = ({ type, value, onChange, placeholder }) => (
    <input
      type={type}
      value={value}
      onChange={onChange}
      className="w-full px-4 py-2 border rounded-md"
      placeholder={placeholder}
    />
  );
  
  export default Input;
  