import { useEffect, useState } from "react";
import axios from "axios";
import "../css/AdminDashboard.css";
import {
  BarChart, Bar, XAxis, YAxis, Tooltip, Legend,
  ResponsiveContainer, PieChart, Pie, Cell
} from "recharts";

const COLORS = ["#8884d8", "#82ca9d", "#ffc658", "#ff7f50", "#00c49f"];

function AdminDashboard() {
  const [analyticsData, setAnalyticsData] = useState([]);
  const [clickData, setClickData] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const fetchData = async () => {
      try {
        const analyticsRes = await axios.get("http://localhost:8081/api/analytics");
        setAnalyticsData(analyticsRes.data);

        const clicksRes = await axios.get("http://localhost:8081/api/ads/clicks");
        setClickData(clicksRes.data);
      } catch (error) {
        console.error("Failed to fetch dashboard data:", error);
      } finally {
        setLoading(false);
      }
    };

    fetchData();
  }, []);

  if (loading) return <div>Loading analytics...</div>;

  return (
    <div className="admin-dashboard">
      <h2>Advertisement Analytics Dashboard</h2>

      {/* Analytics Table */}
      <table className="analytics-table">
        <thead>
          <tr>
            <th>Ad ID</th>
            <th>Impressions</th>
            <th>Clicks</th>
            <th>CTR (%)</th>
            <th>Last Updated</th>
          </tr>
        </thead>
        <tbody>
          {analyticsData.map((ad, index) => (
            <tr key={index}>
              <td>{ad.adId}</td>
              <td>{ad.impressions}</td>
              <td>{ad.clicks}</td>
              <td>{ad.ctr.toFixed(2)}%</td>
              <td>{new Date(ad.timestamp).toLocaleString()}</td>
            </tr>
          ))}
        </tbody>
      </table>

      {/* Bar Chart */}
      <h3>Impressions vs Clicks</h3>
      <ResponsiveContainer width="100%" height={400}>
        <BarChart data={analyticsData}>
          <XAxis dataKey="adId" />
          <YAxis />
          <Tooltip
            contentStyle={{
              backgroundColor: "#2a2a2a",
              borderRadius: "10px",
              border: "none",
            }}
            itemStyle={{ color: "#ffffff" }}
            cursor={false}
          />
          <Legend />
          <Bar dataKey="impressions" fill="#8884d8" />
          <Bar dataKey="clicks" fill="#82ca9d" />
        </BarChart>
      </ResponsiveContainer>

      {/* Pie Chart */}
      <h3>CTR Share (%)</h3>
      <ResponsiveContainer width="100%" height={400}>
        <PieChart>
          <Pie
            data={analyticsData}
            dataKey="ctr"
            nameKey="adId"
            cx="50%"
            cy="50%"
            outerRadius={150}
            label={({ name, percent }) => `${name}: ${(percent * 100).toFixed(1)}%`}
          >
            {analyticsData.map((entry, index) => (
              <Cell key={`cell-${index}`} fill={COLORS[index % COLORS.length]} />
            ))}
          </Pie>
          <Tooltip />
        </PieChart>
      </ResponsiveContainer>

      {/* Divider */}
      <hr style={{ margin: "40px 0", borderTop: "1px solid #ccc" }} />

      {/* Clicks Table (Scrollable) */}
      <h2>Ad Click Events</h2>
      <div className="clicks-table-container">
        <table className="clicks-table">
          <thead>
            <tr>
              <th>Ad ID</th>
              <th>User ID</th>
              <th>Ad Type</th>
              <th>Device Type</th>
              <th>Browser</th>
              <th>City</th>
              <th>State</th>
              <th>Country</th>
              <th>Timestamp</th>
            </tr>
          </thead>
          <tbody>
            {clickData.map((click, index) => (
              <tr key={index}>
                <td>{click.adId}</td>
                <td>{click.userId}</td>
                <td>{click.type}</td>
                <td>{click.deviceType}</td>
                <td>{click.browser}</td>
                <td>{click.city}</td>
                <td>{click.state}</td>
                <td>{click.country}</td>
                <td>{new Date(click.timestamp).toLocaleString()}</td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  );
}

export default AdminDashboard;
