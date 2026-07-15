# E-Commerce Backend
This project will serve REST API to the frontend of E-Commerce web Application 



## 📋 Database Models

### Category
- `name` - Category name
- `slug` - URL-friendly identifier

### Product
- `name` - Product name
- `description` - Product description
- `price` - Product price
- `image` - Product image
- `created_at` - Timestamp of creation

### UserProfile
- `user` - One-to-one relationship with Django User
- `phone` - User's phone number
- `address` - User's shipping address

### Order
- `user` - Foreign key to User
- `created_at` - Order creation timestamp
- `total_amount` - Total order amount

### OrderItem
- `order` - Foreign key to Order
- `product` - Foreign key to Product
- `quantity` - Quantity of product ordered
- `price` - Price of product at time of order