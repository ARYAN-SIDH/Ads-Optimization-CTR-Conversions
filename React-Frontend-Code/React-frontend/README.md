## 📺 Ad Tracking Frontend (React)

This is the React frontend for the Ad Analytics and Tracking System. Users interact with movie cards and advertisements (banner and video), and the app logs user engagement, impressions, and click data. An admin dashboard is provided to visualize ad performance using tables and graphs.

---

### 🚀 Features

- 🎬 Movie browsing with clickable cards
- 📢 Banner and video advertisements with interaction tracking
- 📈 Admin dashboard showing:
  - Ad Impressions, Clicks, CTR
  - Graphs (Bar and Pie)
  - Click Logs with device/location info
- 🌐 Axios integration with Spring Boot backend

---

### 🧱 Tech Stack

- **React** (with hooks)
- **Axios** for API communication
- **Recharts** for data visualization
- **React Context API** for global state (e.g., favorites, userId)
- **CSS** for styling and layout

---

### 📁 Project Structure

```
src/
├── components/
│   ├── AdminDashboard.jsx       # Main analytics view (tables + graphs)
│   ├── MovieCard.jsx            # Movie card UI with click tracking
│   ├── NavBar.jsx               # Navigation bar
│   ├── Prac.jsx                 # (test or WIP component)
│   └── VideoAd.jsx              # Video ad player with impression/click tracking
│
├── contexts/
│   └── MovieContext.jsx         # Global user/favorite movie context
│
├── css/                         # Individual style files
│   ├── AdminDashboard.css
│   ├── App.css
│   ├── Home.css
│   ├── Favorites.css
│   ├── MovieCard.css
│   ├── Navbar.css
│   └── VideoAd.css
│
├── pages/
│   ├── Admin.jsx                # Dashboard routing component
│   ├── Favorites.jsx            # List of favorited movies
│   └── Home.jsx                 # Home page with movie feed and ads
│
├── services/                    # (Future API layer)
│
├── utils/
│   ├── adAnalyticsLogger.jsx    # Impression logging logic
│   └── trackAdClick.jsx         # Click logging logic
│
├── App.jsx                      # Main app router
├── main.jsx                     # Entry point
└── .gitignore
```

---

### 🌐 Backend API Endpoints

| Method | Endpoint                    | Purpose                          |
|--------|-----------------------------|----------------------------------|
| POST   | `/api/ads/click`            | Log an ad click (type, location) |
| GET    | `/api/analytics`            | Get ad-wise impression/click CTR |
| GET    | `/api/ads/clicks`           | Fetch full ad click logs         |

Make sure backend is running at `http://localhost:8081`.

---

### ⚙️ Setup Instructions

#### 1. Install dependencies

```bash
npm install
# or
yarn install
```

#### 2. Start the React app

```bash
npm run dev
# or for CRA users
npm start
```

#### 3. Backend should run at:

```
http://localhost:8081/
```

Make sure Spring Boot backend is running and CORS is enabled for `http://localhost:5173`.

---

### 📊 Admin Dashboard

Visit `/admin` in the browser to access:
- Ad performance table
- Bar chart of impressions vs clicks
- Pie chart of CTR share
- Scrollable click event logs

---

### 📝 To Do

- [ ] Add filtering by Ad Type in dashboard
- [ ] Add CSV export for clicks table
- [ ] Add pagination to click logs

---

### 📦 Extras

- 🧪 Postman was used to test API endpoints in bulk and inject test data.
- 🌍 GeoIP2 API is used to enrich click logs with city, state, and country data based on IP.
- 🔄 Frontend calls backend using `axios.post()` and `axios.get()` in `useEffect`.

---

### Note:
To handle the large video file in your GitHub repository without committing it (since it exceeds the 100MB limit), here’s how you can document it in your `README.md` file:

---

**Video Advertisement File**

The `video.mp4` file used in this project exceeds GitHub's 100MB file size limit and is **not included in this repository**.

📦 **Download it separately from the link below and place it in:**

```
React-Frontend-Code/public/video.mp4
```

🔗 **Download video here:**  
[Click on this if you want this video](https://tinyurl.com/44h3b6kv)

# React + Vite

This template provides a minimal setup to get React working in Vite with HMR and some ESLint rules.

Currently, two official plugins are available:

- [@vitejs/plugin-react](https://github.com/vitejs/vite-plugin-react/blob/main/packages/plugin-react/README.md) uses [Babel](https://babeljs.io/) for Fast Refresh
- [@vitejs/plugin-react-swc](https://github.com/vitejs/vite-plugin-react-swc) uses [SWC](https://swc.rs/) for Fast Refresh

## Expanding the ESLint configuration

If you are developing a production application, we recommend using TypeScript and enable type-aware lint rules. Check out the [TS template](https://github.com/vitejs/vite/tree/main/packages/create-vite/template-react-ts) to integrate TypeScript and [`typescript-eslint`](https://typescript-eslint.io) in your project.
