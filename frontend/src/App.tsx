// src/App.tsx

import DashboardLayout from "./layouts/DashboardLayout";
import DashboardPage from "./pages/DashboardPage";

function App() {
  return (
    <div className="font-sans text-gray-900 antialiased">
      <DashboardLayout>
        <DashboardPage />
      </DashboardLayout>
    </div>
  );
}

export default App;
