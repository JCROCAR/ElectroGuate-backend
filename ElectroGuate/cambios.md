# Cambios

Se realizaron cambios en:
Cambio en los endpoints

- **Antes:**
  - api/products/products/
  - api/products/brand/
  - api/products/category/
  - api/users/users/
    - Servia tanto para **GET**  y **POST**
- **Ahora:**
  - api/products/products
  - api/products/brand
  - api/products/category
  - api/users/users/
    - Solo admitirá el método **POST**
  - api/users/list
    - Solo admitirá el método **GET** que listará a los usuarios

Autenticación en los endpoints **método POST** necesita autenticación mientras que **método GET** no necesita autenticación

- api/products/products
- api/products/brand
- api/products/category
- api/users/users/
  - **No necesita autenticación**
- api/users/list
  - **Si necesita autenticación**

Mientras que los metodos **PUT, GET, DELETE**
Si se necesita autenticación

- api/products/products/{id}
- api/products/brand/{id}
- api/products/category/{id}
