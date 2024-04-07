## Project Description

This is a simple project aimed at demonstrating the interaction between a frontend built with React and a backend
developed with FastAPI.

### Frontend

The frontend aspect of the project showcases various aspects of React development:

- Components: Utilizes simple yet effective components from the Ant Design library, providing a clean and modern user
  interface.
- Hooks: Employs React hooks such as useState and useEffect for managing component state and side effects, ensuring a
  responsive and interactive user experience.
- HTTP Requests: Utilizes Axios library for making asynchronous HTTP requests, facilitating smooth communication with
  the backend API.
- Styling: Implements styling using Tailwind CSS, enabling rapid prototyping and flexible customization of the user
  interface.

### Backend

The backend aspect of the project is focused on providing robust backend functionalities:

- CORS (Cross-Origin Resource Sharing) Setup: Configures CORS to allow cross-origin requests, enabling interaction with
  the frontend application hosted on a different domain.
- Caching: Implements caching mechanisms to optimize performance by reducing the load on external resources and
  improving response times for frequently accessed data.
- Asynchronous Functions: Utilizes asynchronous functions to handle tasks such as database queries, ensuring efficient
  utilization of resources and responsiveness.
- Asynchronous External API Requests: Makes asynchronous requests to external APIs, enabling the backend to retrieve and
  process data from external sources asynchronously, without blocking the main execution thread.

### External API Integration

To integrate with the external API provided by [CoinMarketCap](https://coinmarketcap.com), you need to obtain an API key from their website and insert it into the `.env` file. The API key is required to authenticate your requests and access their data. Please ensure to keep your API key secure and do not expose it publicly.
 
### Running the Project

#### Backend

To start the backend server:

1. Create a virtual environment:

```
python3 -m venv venv
```

2. Activate the virtual environment:

- On Unix/Linux:
  ```
  . venv/bin/activate
  ```
- On Windows:
  ```
  .\venv\Scripts\activate.bat
  ```

3. Install the required dependencies:
```
pip install -r requirements.txt
```
   
4. Navigate to the backend directory:
```
cd backend
```
  
5. Start the backend server using uvicorn:
```
uvicorn src.main:app --reload
```


#### Frontend

To start the frontend development server:

1. Create a new Vite project:
```
npm create vite@latest
```

2. Install dependencies:
```
npm install
```
3. Start the development server:
```
npm run dev
 ```
