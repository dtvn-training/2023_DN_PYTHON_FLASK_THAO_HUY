import React, { lazy, Suspense } from "react";
import { Routes, Route, BrowserRouter } from "react-router-dom";

const LazyLoginPage = lazy(() => import("./views/LoginPage/LoginPage"));
const LazyHomePage = lazy(() => import("./views/HomePage/HomePage"));

function App() {
  return (
    <BrowserRouter>
      <Routes>
        {
          <Route
            path="/login"
            element={
              <Suspense fallback={<div>Loading...</div>}>
                <LazyLoginPage />
              </Suspense>
            }
          />
        }
        {
          <Route
            path="/home"
            element={
              <Suspense fallback={<div>Loading...</div>}>
                <LazyHomePage />
              </Suspense>
            }
          />
        }
      </Routes>
    </BrowserRouter>
  );
}

export default App;
